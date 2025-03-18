import streamlit as st
from presentation.viewmodels.collection_ranking_viewmodel import CollectionRankingViewModel


def render_collection_ranking_input(viewmodel: CollectionRankingViewModel):
    st.header("Collection Ranking")

    col_network, col_period, col_sortby = st.columns(3)

    with col_network:
        network = st.selectbox("Select Network", st.session_state.reservoir["networks"])
    with col_period:
        period = st.selectbox("Period", st.session_state.reservoir["ranking_period"])
    with col_sortby:
        sortby = st.selectbox("Sort By", st.session_state.reservoir["sort_by"])

    viewmodel.load_collection_ranking(network, period, sortby)


def render_collection_ranking_display(viewmodel: CollectionRankingViewModel):
    st.dataframe(
        viewmodel.ranking,
        height=1000,
        use_container_width=True,
        hide_index=True,
        column_config={"image": st.column_config.ImageColumn("icon")},
    )
