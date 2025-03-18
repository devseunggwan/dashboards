import httpx
import pandas as pd


class Reservoir:
    def __init__(self, api_key: str):
        self.headers = {"x-api-key": api_key}
        self.reservoir_networks_url_prefix = {
            "ethereum": "api",
            "polygon": "api-polygon",
            "bsc": "api-bsc",
            "arbitrum": "api-arbitrum",
            "optimism": "api-optimism",
            "base": "api-base",
            "linea": "api-linea",
            "avalanche": "api-avalanche",
        }
        self.reservoir_period = ["1d", "7d", "30d"]
        self.reservoir_ranking_url = (
            lambda x: f"https://{self.reservoir_networks_url_prefix[x]}.reservoir.tools/collections/trending/v1"
        )
        self.reservoir_collection_url = (
            lambda x: f"https://{self.reservoir_networks_url_prefix[x]}.reservoir.tools/collections/v7"
        )
        self.reservoir_nft_list_url = (
            lambda x: f"https://{self.reservoir_networks_url_prefix[x]}.reservoir.tools/tokens/v7"
        )

    def get_collection_ranking_by_network(self, network, period: str = "1d", sortby: str = "volume") -> dict:
        ranking_columns = [
            "image",
            "id",
            "name",
            "volume",
            "volumePercentChange",
            "count",
            "countPercentChange",
        ]
        params = {
            "period": period,
            "sortBy": sortby,
            "limit": 100,
        }
        __url = self.reservoir_ranking_url(network)

        ranking = httpx.get(__url, params=params, headers=self.headers).json()
        ranking = ranking["collections"]
        ranking = pd.DataFrame(data=ranking)
        ranking = ranking[ranking_columns]

        return ranking

    def get_collection_by_id(self, network: str, id: str) -> dict:
        params = {
            "id": id,
        }
        collection = httpx.get(self.reservoir_collection_url(network), params=params, headers=self.headers).json()

        return collection

    def get_nfts_by_collection_id(self, network: str, collection_id: str, limit: int = 100) -> dict:
        params = {"collection": collection_id, "sortBy": "updatedAt", "limit": limit}

        nft_list = httpx.get(self.reservoir_nft_list_url(network), params=params, headers=self.headers).json()

        return nft_list
