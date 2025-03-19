import streamlit as st


def page_config_main():
    st.set_page_config(page_title="NFT Curation", layout="wide", initial_sidebar_state="expanded")

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
