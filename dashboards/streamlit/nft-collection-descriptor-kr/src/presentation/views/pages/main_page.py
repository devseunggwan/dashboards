import streamlit as st
from presentation.viewmodels.collection_ranking_viewmodel import CollectionRankingViewModel
from presentation.viewmodels.nft_curation_viewmodel import NftCurationViewModel
from presentation.views.components.nft_collection_ranking import (
    render_collection_ranking_display,
    render_collection_ranking_input,
)
from presentation.views.components.nft_curation import render_curation_display
from presentation.views.components.page_config import page_config_main
from presentation.views.components.sidebar import sidebar


def render_main_page(
    collection_ranking_view_model: CollectionRankingViewModel, nft_curation_view_model: NftCurationViewModel
):
    page_config_main()
    sidebar()

    col1, col2 = st.columns(2)

    with col1.container(border=True):
        render_collection_ranking_input(collection_ranking_view_model)
        render_collection_ranking_display(collection_ranking_view_model)

    with col2.container(border=True):
        if st.session_state.run_prompt:
            for _ in range(st.session_state.question_count):
                render_curation_display(nft_curation_view_model)
