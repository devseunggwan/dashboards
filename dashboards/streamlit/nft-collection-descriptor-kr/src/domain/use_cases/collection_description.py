from ..entities.prompt import Completion, Prompt
from ..repositories.prompt_repository import PromptReopsitory


class CollectionDescriptionUseCase:
    def __init__(self, prompt_repository: PromptReopsitory, llm_service, prompt_template):
        self.prompt_repository = prompt_repository
        self.llm_service = llm_service
        self.prompt_template = prompt_template

    def execute(self, name: str, description: str, max_tokens: int = 1000, image_urls: list[str] = []):
        prompt = Prompt(
            self.prompt_template.format(
                collection_name=name, collection_description=description, max_korean_token_length=max_tokens
            )
        )
        prompt = self.prompt_repository.save_prompt(prompt=prompt)

        completion = self.llm_service.generate_completion(prompt=prompt.content, image_urls=image_urls)
        completion = Completion(prompt_id=1, content=completion)
        completion = self.prompt_repository.save_completion(completion=completion)

        return prompt, completion


class CollectionTitleUseCase:
    def __init__(self, prompt_repository: PromptReopsitory, llm_service, prompt_template):
        self.prompt_repository = prompt_repository
        self.llm_service = llm_service
        self.prompt_template = prompt_template

    def execute(self, curation: str):
        prompt = Prompt(self.prompt_template.format(curation=curation))
        prompt = self.prompt_repository.save_prompt(prompt=prompt)

        completion = self.llm_service.generate_completion(prompt=prompt.content)
        completion = Completion(prompt_id=1, content=completion)
        completion = self.prompt_repository.save_completion(completion=completion)

        return prompt, completion
