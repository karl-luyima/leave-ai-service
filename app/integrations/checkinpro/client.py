import requests

from app.config.settings import settings



class CheckinProClient:


    def __init__(self):

        self.base_url = settings.CHECKINPRO_URL

        self.api_key = settings.CHECKINPRO_API_KEY



    def get(
        self,
        endpoint
    ):

        headers = {

            "Authorization":
                f"Bearer {self.api_key}",

            "Accept":
                "application/json"

        }


        response = requests.get(

            self.base_url + endpoint,

            headers=headers

        )


        response.raise_for_status()


        return response.json()