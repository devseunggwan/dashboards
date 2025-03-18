import os

import streamlit as st
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv(override=True)

        self.db_path = "sample.db"
        self.reservoir_api_key = os.getenv("RESERVOIR_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        st.session_state.reservoir = {
            "networks": {
                "ethereum": "api",
                "polygon": "api-polygon",
                "bsc": "api-bsc",
                "arbitrum": "api-arbitrum",
                "optimism": "api-optimism",
                "base": "api-base",
                "linea": "api-linea",
                "avalanche": "api-avalanche",
            },
            "periods": ["1d", "7d", "30d"],
            "sort_by": ["volume", "sales"],
        }

        st.session_state.llm_models = ["gpt-4o", "gpt-4-turbo", "gpt-o3-mini"]
