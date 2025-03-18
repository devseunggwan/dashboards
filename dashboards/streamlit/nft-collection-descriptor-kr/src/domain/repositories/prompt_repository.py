from abc import ABC, abstractmethod
from typing import Optional

from ..entities.prompt import Completion, Prompt


class PromptReopsitory(ABC):
    @abstractmethod
    def save_prompt(self, prompt: Prompt) -> Prompt:
        pass

    @abstractmethod
    def save_completion(self, completion: Completion) -> Completion:
        pass

    @abstractmethod
    def get_history(self, limit: int = 10) -> list[tuple[Prompt, Completion]]:
        pass

    @abstractmethod
    def get_prompt_by_id(self, prompt_id: int) -> Optional[Prompt]:
        pass
