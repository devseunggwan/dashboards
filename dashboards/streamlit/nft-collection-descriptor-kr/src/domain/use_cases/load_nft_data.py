import pandas as pd

from ..entities.nft import Collection, Nft
from ..repositories.nft_repository import NftRepository


class LoadCollectionRankingUseCase:
    def __init__(self, nft_repository: NftRepository):
        self.nft_repository = nft_repository

    def execute(self, network: str, period: str, sortby: str) -> pd.DataFrame:
        collections = self.nft_repository.get_collection_ranking_by_network(
            network=network, period=period, sortby=sortby
        )

        return collections


class LoadCollectionUseCase:
    def __init__(self, nft_repository: NftRepository):
        self.nft_repository = nft_repository

    def execute(self, network: str, id: str) -> Collection:
        collection = self.nft_repository.get_collection_by_id(network=network, id=id)

        return collection


class LoadNftUseCase:
    def __init__(self, nft_repository: NftRepository):
        self.nft_repository = nft_repository

    def execute(self, network: str, id: str, limit: int = 100) -> list[Nft]:
        nfts = self.nft_repository.get_nfts_by_collection_id(network=network, collection_id=id, limit=limit)

        return nfts
