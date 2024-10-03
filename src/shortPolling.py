import requests
import json
from polling2 import poll_decorator
from databaseQuery import insert_publisher, view_publishers, config

@poll_decorator(step=10, poll_forever=True)
def check():
    rows = view_publishers("*", config)
    for endpoint in rows:
        response = requests.get(endpoint[3])
        if response.status_code != 200:
            raise Exception(f"Failed to reach {endpoint[3]}")
        print("Success")
        print(json.dumps(response.json(), indent=4))

def add_publisher():
    api_key = input("Enter API Key: ")
    endpoint = input("Enter Endpoint: ")
    publisher_id = input("Enter Publisher ID: ")
    publisher_name = input("Enter Publisher Name: ")
    insert_publisher(api_key, endpoint, publisher_id, publisher_name, config)

check()