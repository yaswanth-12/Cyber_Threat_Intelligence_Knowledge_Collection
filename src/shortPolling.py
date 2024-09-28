import requests, polling

polling.poll(
    lambda: requests.get('https://www.google.com').status_code == 200,
    step=60, # steps are in seconds
    poll_forever=True
)

endPoints = ['https://api.website/v1/endpoints', 'https://api.website2/v1/endpoints']

polling.poll(
    lambda: requests.get(endPoints).content == '',
)
