import sys

from core.config import Settings
from core.containers import AppContainer
from presentation.views.pages.main_page import render_main_page

container = AppContainer()
container.config.from_pydantic(Settings())

container.init_resources()
container.wire(modules=[sys.modules[__name__]])


def main():
    collection_ranking_view_model = container.view_models().collection_ranking()
    nft_curation_view_model = container.view_models().nft_curation()
    render_main_page(
        collection_ranking_view_model=collection_ranking_view_model,
        nft_curation_view_model=nft_curation_view_model,
    )


if __name__ == "__main__":
    main()
