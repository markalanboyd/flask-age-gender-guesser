import requests

from country_codes import COUNTRIES


class Guesser:
    def __init__(self):
        self.age_endpoint = "https://api.agify.io?name="
        self.gender_endpoint = "https://api.genderize.io?name="
        self.nationality_endpoint = "https://api.nationalize.io?name="

    def __get(self, name, endpoint):
        response = requests.get(endpoint + name)
        if response.status_code != 200:
            print(f"Failed to get data: {response.status_code}")
            return None
        return response.json()

    def __country_code_to_emoji(self, country_code):
        return "".join(chr(ord(c) + 127397) for c in country_code.upper())

    def age(self, name):
        return self.__get(name, self.age_endpoint)["age"]

    def gender(self, name):
        return self.__get(name, self.gender_endpoint)["gender"]

    def nationality(self, name):
        data = self.__get(name, self.nationality_endpoint)
        if data["count"] == 0:
            return None
        id = data["country"][0]["country_id"]
        return COUNTRIES[id] + " " + self.__country_code_to_emoji(id)
