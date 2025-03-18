from data.repositories.nft_repository import Reservoir
from data.repositories.sqlite_prompt_repository import SqlitePromptRepository
from data.services.llm_service import OpenAIService
from domain.use_cases.collection_description import CollectionDescriptionUseCase, CollectionTitleUseCase
from domain.use_cases.load_nft_data import LoadCollectionRankingUseCase, LoadCollectionUseCase, LoadNftUseCase
from presentation.viewmodels.collection_ranking_viewmodel import CollectionRankingViewModel
from presentation.viewmodels.nft_curation_viewmodel import NftCurationViewModel

from core.prompt_templates import prompt_curation_description, prompt_curation_tag, prompt_curation_title


class Container:
    def __init__(self, config):
        self.prompt_repository = SqlitePromptRepository(db_path=config.db_path)
        self.nft_repository = Reservoir(api_key=config.reservoir_api_key)
        self.llm_service = OpenAIService(api_key=config.openai_api_key)

        self.collection_description_use_case = CollectionDescriptionUseCase(
            prompt_repository=self.prompt_repository,
            llm_service=self.llm_service,
            prompt_template=prompt_curation_description,
        )
        self.collection_tags_use_case = CollectionDescriptionUseCase(
            prompt_repository=self.prompt_repository, llm_service=self.llm_service, prompt_template=prompt_curation_tag
        )
        self.collection_title_use_case = CollectionTitleUseCase(
            prompt_repository=self.prompt_repository,
            llm_service=self.llm_service,
            prompt_template=prompt_curation_title,
        )
        self.load_collection_ranking_use_case = LoadCollectionRankingUseCase(nft_repository=self.nft_repository)
        self.load_collection_use_case = LoadCollectionUseCase(nft_repository=self.nft_repository)
        self.load_nft_use_case = LoadNftUseCase(nft_repository=self.nft_repository)

        self.collection_ranking_view_model = CollectionRankingViewModel(
            collection_ranking_use_case=self.load_collection_ranking_use_case
        )
        self.nft_curation_view_model = NftCurationViewModel(
            collection_description_use_case=self.collection_description_use_case,
            collection_tags_use_case=self.collection_tags_use_case,
            collection_title_use_case=self.collection_title_use_case,
            load_collection_use_case=self.load_collection_use_case,
            load_nft_use_case=self.load_nft_use_case,
        )
