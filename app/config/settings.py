import os
from dotenv import load_dotenv


load_dotenv()


class Settings:

    CHECKINPRO_URL = os.getenv(
        "CHECKINPRO_URL"
    )

    CHECKINPRO_USERNAME = os.getenv(
        "CHECKINPRO_USERNAME"
    )

    CHECKINPRO_PASSWORD = os.getenv(
        "CHECKINPRO_PASSWORD"
    )

    CHECKINPRO_COMPANY_EMAIL = os.getenv(
        "CHECKINPRO_COMPANY_EMAIL"
    )


settings = Settings()