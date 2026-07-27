import os

from dotenv import load_dotenv


load_dotenv()



class Settings:


    DATA_PROVIDER = os.getenv(
        "DATA_PROVIDER",
        "database"
    )


    CHECKINPRO_URL = os.getenv(
        "CHECKINPRO_URL",
        "http://localhost:9000"
    )


    CHECKINPRO_API_KEY = os.getenv(
        "CHECKINPRO_API_KEY",
        "dummy_key"
    )


    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "none"
    )



settings = Settings()