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
        data = response.content
        print(data)
        print("Success")
        print(json.dumps(response.json(), indent=4))


check()
