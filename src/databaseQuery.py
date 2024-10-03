import mysql.connector
from mysql.connector import errorcode

def insert_publisher(api_key, endpoint, publisher_id, publisher_name, config):
    try:
        # Establish the database connection
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Define the insert query
        insert_query = """
        INSERT INTO publishers (API_KEY, endpoint, publisherID, publisherName)
        VALUES (%s, %s, %s, %s)
        """

        # Execute the insert query
        cursor.execute(insert_query, (api_key, endpoint, publisher_id, publisher_name))

        # Commit the transaction
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
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()

# Example usage
config = {
    'user': 'yourusername',
    'password': 'yourpassword',
    'host': 'yourhost',
    'database': 'yourdatabase'
}

insert_publisher('59a820f2109d444d9a5172836242909', 'http://api.weatherapi.com/v1/current.json?key=59a820f2109d444d9a5172836242909&q=London', 'PUB-WEATHER-INFO', 'weatherapi', config)