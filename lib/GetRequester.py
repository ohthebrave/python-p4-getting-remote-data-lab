import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        programs = json.loads(self.get_response_body())
        for program in programs:
            print(program)
        return programs

# Example usage:
url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
requester = GetRequester(url)
json_data = requester.load_json()

# # Process the JSON data as needed
if json_data:
    print(json_data)