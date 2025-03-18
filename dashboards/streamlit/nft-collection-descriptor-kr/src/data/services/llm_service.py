import os
from typing import Optional

import openai


class OpenAI:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_completion(
        self,
        prompt: str,
        model_name: str = "gpt-4o",
        max_tokens: int = 1000,
        image_urls: list[str] = [],
        timeout: int = 60,
    ) -> str:
        __message = [{"role": "user", "content": []}]
        __message["content"].append({"role": "text", "text": prompt})

        if image_urls:
            __message.extend([{"type": "image_url", "image_url": {"url": image_url}} for image_url in image_urls])

        try:
            response = openai.ChatCompletion.create(
                model=model_name, message=__message, max_tokens=max_tokens, timeout=timeout
            )

            return response.choices[0].message.content.strip()
        except Exception as e:
            print(e)
            return e
