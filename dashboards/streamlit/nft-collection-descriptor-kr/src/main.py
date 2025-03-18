from core.config import Config
from core.container import Container
from presentation.views.pages.main_page import render_main_page

if __name__ == "__main__":
    

    config = Config()
    container = Container(config=config)

    render_main_page(
        collection_ranking_view_model=container.collection_ranking_view_model,
        nft_curation_view_model=container.nft_curation_view_model,
    )
