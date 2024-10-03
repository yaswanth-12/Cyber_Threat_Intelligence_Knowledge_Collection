import mysql.connector
from mysql.connector import errorcode

# Implement methods to handle SQLi (SQL Injection)

def insert_publisher(api_key, endpoint, publisher_id, publisher_name, config):
    try:
        # Establish the database connection
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        insert_query = """
        INSERT INTO publishers (API_KEY, endpoint, publisherID, publisherName)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (api_key, endpoint, publisher_id, publisher_name))
        cnx.commit()

        print("Record inserted successfully")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        elif isinstance(err, mysql.connector.errors.InterfaceError):
            print("Failed to connect to the MySQL server. Is it running?")
        else:
            print(err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()

def view_publishers(publisher_id, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        if publisher_id == "*":
            search_query = f'''
            SELECT * FROM publishers
            '''
        else:
            search_query = f'''
            SELECT * FROM publishers WHERE publisherID = {publisher_id}
            '''
        cursor.execute(search_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        return results
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        elif isinstance(err, mysql.connector.errors.InterfaceError):
            print("Failed to connect to the MySQL server. Is it running?")
        else:
            print(err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'webhook'
}

# view_publishers(2, config)
view_publishers("*", config)
# insert_publisher('59a820f2109d444d9a5172836242909', 'http://api.weatherapi.com/v1/current.json?key=59a820f2109d444d9a5172836242909&q=London', 1, 'weatherapi', config)