from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Prompt:
    content: str
    created_at: datetime = datetime.now()
    id: Optional[int] = None


@dataclass
class Completion:
    prompt_id: int
    content: str
    created_at: datetime = datetime.now()
    id: Optional[int] = None
    model_used: str = "default_model"
