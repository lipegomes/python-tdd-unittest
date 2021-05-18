import requests


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.obtained_data = False

    def response_obtained_data_success_ok(self):
        response = requests.get("https://api.filipegomes.dev")

        if response.ok:
            self.obtained_data = True
            return "Connected"
        else:
            self.obtained_data = False
            return "Bad Request (400)"
