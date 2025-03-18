import streamlit as st


def sidebar():
    with st.sidebar:
        st.header("NFT Curation Bot")

        st.selectbox("Selected Network", st.session_state.reservoir_networks, key="selected_network")
        st.text_input("Collection ID", key="input_collection_id")

        with st.expander("LLM Model Options"):
            st.selectbox("Selected Model", st.session_state.models, key="selected_model")
            st.slider("NFT Images", 1, 20, 10, 1, key="nft_images")
            st.slider("Max Tokens", 50, 1000, 500, 50, key="max_tokens")
            st.slider("Question Count", 1, 3, 1, 1, key="question_count")

        st.button("Run", key="run_prompt")
