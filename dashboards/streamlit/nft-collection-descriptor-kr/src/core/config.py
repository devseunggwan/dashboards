import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv(override=True)

        self.db_path = "sample.db"
        self.reservoir_api_key = os.getenv("RESERVOIR_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
