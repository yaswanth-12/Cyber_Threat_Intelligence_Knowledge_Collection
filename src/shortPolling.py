import requests
import json
from polling2 import poll_decorator

endPoints = ['http://api.weatherapi.com/v1/current.json?key=59a820f2109d444d9a5172836242909&q=London']

@poll_decorator(step=10, poll_forever=True)
def check():
    for endpoint in endPoints:
        response = requests.get(endpoint)
        if response.status_code != 200:
            raise Exception(f"Failed to reach {endpoint}")
        print("Success")
        print(json.dumps(response.json(), indent=4))

check()