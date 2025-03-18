from abc import ABC, abstractmethod

import pandas as pd

from ..entities.nft import Collection, Nft


class NftRepository(ABC):
    @abstractmethod
    def get_collections_by_network(self, network: str, period: str, sortby: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_collection(self, network: str, id: str) -> Collection:
        pass

    @abstractmethod
    def get_nfts_by_collection(self, network: str, id: str, limit: int) -> list[Nft]:
        pass
