import requests

from app.config.settings import settings


class CheckinProClient:


    def __init__(self):

        self.base_url = settings.CHECKINPRO_URL

        self.username = settings.CHECKINPRO_USERNAME

        self.password = settings.CHECKINPRO_PASSWORD

        self.company_email = settings.CHECKINPRO_COMPANY_EMAIL



    def post(
        self,
        endpoint,
        payload
    ):

        headers = {

            "Accept": "application/json",

            "Content-Type": "application/json"

        }


        response = requests.post(

            self.base_url + endpoint,

            json=payload,

            headers=headers,

            timeout=30

        )


        response.raise_for_status()


        return response.json()



    def get(
        self,
        endpoint
    ):

        headers = {

            "Accept": "application/json"

        }


        response = requests.get(

            self.base_url + endpoint,

            headers=headers,

            timeout=30

        )


        response.raise_for_status()


        return response.json()