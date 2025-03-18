from datetime import datetime
from time import time

import streamlit as st
from presentation.viewmodels.nft_curation_viewmodel import NftCurationViewModel
from streamlit_image_select import image_select


def render_curation_display(viewmodel: NftCurationViewModel):
    start_time = time()

    with st.status(
        f"⏳ Generating NFT Curation ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})",
        expanded=True,
    ):
        viewmodel.set_network(network=st.session_state.selected_network)
        viewmodel.set_collection_id(collection_id=st.session_state.input_collection_id)
        viewmodel.set_image_count(image_count=st.session_state.image_count)

        viewmodel.load_nft_data()
        viewmodel.generate_description()
        viewmodel.generate_tags()
        viewmodel.generate_title()

        st.markdown(f"##### {viewmodel.completion_title}")

        st.write("##### description")
        st.write(viewmodel.completion_description)

        st.write("##### tags")
        st.text(viewmodel.completion_tags)

        elapsed_time = time() - start_time
        st.write(f"⏱️ Elapsed Time: {elapsed_time:.2f} sec")

        if viewmodel.image_urls:
            image_select(label="Source NFT Images", images=viewmodel.image_urls, use_container_width=True)

    st.toast("Curation has been generated!", icon="✅")
