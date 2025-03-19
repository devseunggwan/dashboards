from data.repositories.nft_repository import Reservoir
from data.repositories.sqlite_prompt_repository import SqlitePromptRepository
from data.services.llm_service import GemeniService
from dependency_injector import containers, providers
from domain.use_cases.collection_description import CollectionDescriptionUseCase, CollectionTitleUseCase
from domain.use_cases.load_nft_data import LoadCollectionRankingUseCase, LoadCollectionUseCase, LoadNftUseCase
from presentation.viewmodels.collection_ranking_viewmodel import CollectionRankingViewModel
from presentation.viewmodels.nft_curation_viewmodel import NftCurationViewModel

from core.prompt_templates import prompt_curation_description, prompt_curation_tag, prompt_curation_title


class Repositories(containers.DeclarativeContainer):
    config = providers.Configuration()

    prompt_repository = providers.Singleton(SqlitePromptRepository, db_path=config.db_path)
    nft_repository = providers.Singleton(Reservoir, api_key=config.reservoir.api_key)


class Services(containers.DeclarativeContainer):
    config = providers.Configuration()

    # llm_service = providers.Singleton(OpenAIService)
    llm_service = providers.Singleton(GemeniService)


class UseCases(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    services = providers.DependenciesContainer()

    collection_description = providers.Factory(
        CollectionDescriptionUseCase,
        prompt_repository=repositories.prompt_repository,
        llm_service=services.llm_service,
        prompt_template=prompt_curation_description,
    )
    collection_tags = providers.Factory(
        CollectionDescriptionUseCase,
        prompt_repository=repositories.prompt_repository,
        llm_service=services.llm_service,
        prompt_template=prompt_curation_tag,
    )
    collection_title = providers.Factory(
        CollectionTitleUseCase,
        prompt_repository=repositories.prompt_repository,
        llm_service=services.llm_service,
        prompt_template=prompt_curation_title,
    )

    collection_ranking = providers.Factory(LoadCollectionRankingUseCase, nft_repository=repositories.nft_repository)
    collection = providers.Factory(LoadCollectionUseCase, nft_repository=repositories.nft_repository)
    nfts = providers.Factory(LoadNftUseCase, nft_repository=repositories.nft_repository)


class ViewModels(containers.DeclarativeContainer):
    use_cases = providers.DependenciesContainer()

    collection_ranking = providers.Factory(
        CollectionRankingViewModel, collection_ranking_use_case=use_cases.collection_ranking
    )
    nft_curation = providers.Factory(
        NftCurationViewModel,
        collection_description_use_case=use_cases.collection_description,
        collection_tags_use_case=use_cases.collection_tags,
        collection_title_use_case=use_cases.collection_title,
        load_collection_use_case=use_cases.collection,
        load_nft_use_case=use_cases.nfts,
    )


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    repositories = providers.Container(Repositories, config=config)
    services = providers.Container(Services, config=config)
    use_cases = providers.Container(UseCases, repositories=repositories, services=services)
    view_models = providers.Container(ViewModels, use_cases=use_cases)
