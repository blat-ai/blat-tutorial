import os
from pathlib import Path
import requests

from dotenv import load_dotenv

load_dotenv()


def get_content(path: Path = Path("./get_blat/documents/content.html")):
    if path.exists():
        return path.read_text()
    else:
        raise FileNotFoundError(f"{path=}")

if __name__ == "__main__":
    BLAT_API_KEY = os.getenv("BLAT_API_KEY")
    try:
        response = requests.post(
            "https://api.blat.ai/harvest",
            headers={"X-API-KEY": BLAT_API_KEY},
            json={
                "id": "books-toscrape-com-c0d3c582",
                "mode": "parse",
                "params": {
                    "content": get_content(Path("./parse/documents/content.html"))
                }
            },
        )
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(f"{err}")
