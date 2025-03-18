from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Collection:
    id: str
    network: str
    name: str
    description: str
    created_at: datetime = datetime.now()


@dataclass
class Nft:
    id: str
    network: str
    collection_id: str
    image_url: str
    created_at: datetime = datetime.now()
