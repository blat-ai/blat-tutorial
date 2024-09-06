import json
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
    # HARVESTER_ID = "books-toscrape-com-c0d3c582"
    # HARVESTER_ID = "shop-google-com-109a0fdf"
    HARVESTER_ID = "shop-sponsored-google-com-7c3bde33"
    try:
        content_file = Path(f"./parse/documents/content-{HARVESTER_ID}.html")
        response = requests.post(
            "https://api.blat.ai/harvest",
            headers={"X-API-KEY": BLAT_API_KEY},
            json={
                "id": HARVESTER_ID,
                "mode": "parse",
                "params": {"content": get_content(content_file)},
            },
        )
        response.raise_for_status()
        print(json.dumps(response.json(), indent=4))
    except requests.exceptions.HTTPError as err:
        print(f"{err}")
