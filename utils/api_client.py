import requests

class APIClient:
    BASE_URL = "https://reqres.in/api"

    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'reqres_1a8ccb2f49ee422cb1cfadba34b1e21f'
        }

    def get_user(self, user_id):
        return self.session.get(
            f"{self.BASE_URL}/users/{user_id}",
            headers=self.headers
        )

    def create_user(self, name, job):
        payload = {"name": name, "job": job}

        return self.session.post(
            f"{self.BASE_URL}/users",
            json=payload,
            headers=self.headers
        )