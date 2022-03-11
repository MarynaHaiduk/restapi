import requests


class NameData(object):
    def __init__(self, name: str, age: int, count: int):
        self.name = name
        self.age = age
        self.count = count

    def __str__(self):
        return f"{self.name}'s average age is {self.age} with {self.count} occurences"


class AgifyAPIClient(object):
    base_url = "https://api.agify.io/"

    @staticmethod
    def fetch(name: str) -> NameData:
        response = requests.get(AgifyAPIClient.base_url, params={"name": name})
        response.raise_for_status()
        data = response.json()
        return NameData(**data)
