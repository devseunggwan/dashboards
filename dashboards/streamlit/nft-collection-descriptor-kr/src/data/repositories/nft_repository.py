import httpx
import pandas as pd
from domain.entities.nft import Collection, Nft


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

    def get_collection_ranking_by_network(self, network, period: str = "1d", sortby: str = "volume") -> pd.DataFrame:
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

    def get_collection_by_id(self, network: str, id: str) -> Collection:
        params = {
            "id": id,
        }
        __resp = httpx.get(self.reservoir_collection_url(network), params=params, headers=self.headers).json()
        collection = Collection(
            id=id,
            network=network,
            name=__resp["collections"][0]["name"],
            description=__resp["collections"][0]["description"],
        )

        return collection

    def get_nfts_by_collection_id(self, network: str, collection_id: str, limit: int = 100) -> list[Nft]:
        params = {"collection": collection_id, "sortBy": "updatedAt", "limit": limit}

        __resp = httpx.get(self.reservoir_nft_list_url(network), params=params, headers=self.headers).json()

        nfts = [
            Nft(
                id=item["token"]["tokenId"],
                network=network,
                collection_id=collection_id,
                image_url=item["token"]["imageSmall"],
            )
            for item in __resp["tokens"]
        ]

        return nfts
