import json

from domain.entities.nft import Collection, Nft
from domain.use_cases.collection_description import CollectionDescriptionUseCase, CollectionTitleUseCase
from domain.use_cases.load_nft_data import LoadCollectionUseCase, LoadNftUseCase


class NftCurationViewModel:
    def __init__(
        self,
        collection_description_use_case: CollectionDescriptionUseCase,
        collection_tags_use_case: CollectionDescriptionUseCase,
        collection_title_use_case: CollectionTitleUseCase,
        load_collection_use_case: LoadCollectionUseCase,
        load_nft_use_case: LoadNftUseCase,
    ):
        self.collection_description_use_case = collection_description_use_case
        self.collection_tags_use_case = collection_tags_use_case
        self.collection_title_use_case = collection_title_use_case
        self.load_collection_use_case = load_collection_use_case
        self.load_nft_use_case = load_nft_use_case

        self.network: str = ""
        self.collection_id: str = ""
        self.collection: Collection | None = None
        self.nfts: Nft | None = None
        self.image_urls: list[str] = []
        self.model_name: str = ""

        self.completion_description: str = ""
        self.completion_tags: list[str] = []
        self.completion_title: str = ""

    def set_network(self, network: str) -> None:
        self.network = network

    def set_collection_id(self, collection_id: str) -> None:
        self.collection_id = collection_id

    def set_model(self, model_name: str) -> None:
        self.model_name = model_name

    def load_nft_data(self):
        self.collection = self.load_collection_use_case.execute(network=self.network, id=self.collection_id)
        self.nfts = self.load_nft_use_case.execute(network=self.network, id=self.collection_id)

        self.image_urls = [nft.image_url for nft in self.nfts]

    def generate_description(self) -> None:
        _, __completion = self.collection_description_use_case.execute(
            name=self.collection.name, description=self.collection.description, image_urls=self.image_urls
        )

        self.completion_description = __completion.content

    def generate_tags(self) -> None:
        _, __completion = self.collection_tags_use_case.execute(
            name=self.collection.name, description=self.collection.description, image_urls=self.image_urls
        )

        self.completion_tags = json.loads(__completion.content)

    def generate_title(self) -> None:
        _, __completion = self.collection_title_use_case.execute(self.completion_description)

        self.completion_title = __completion.content
