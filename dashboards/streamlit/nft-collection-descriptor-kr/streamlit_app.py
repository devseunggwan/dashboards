from dotenv import load_dotenv
from src.service import NftCurationLLM
from src.view import NftCurationUI

if __name__ == "__main__":
    load_dotenv(override=True)

    llm = NftCurationLLM()
    ui = NftCurationUI(llm)
    ui.run()
