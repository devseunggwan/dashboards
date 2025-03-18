import pandas as pd
from domain.use_cases.load_nft_data import LoadCollectionRankingUseCase


class CollectionRankingViewModel:
    def __init__(self, collection_ranking_use_case: LoadCollectionRankingUseCase):
        self.collection_ranking_use_case = collection_ranking_use_case
        self.ranking: pd.DataFrame = pd.DataFrame()

    def load_collection_ranking(self, network: str, period: str, sortby: str) -> None:
        self.ranking = self.collection_ranking_use_case.execute(network=network, period=period, sortby=sortby)
