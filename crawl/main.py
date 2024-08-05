import os
import requests

from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    BLAT_API_KEY = os.getenv("BLAT_API_KEY")
    try:
        response = requests.post(
            "https://api.blat.ai/harvest",
            headers={"X-API-KEY": BLAT_API_KEY},
            json={
                "id": "books-toscrape-com-c0d3c582",
                "mode": "crawl",
                "params": {
                    "start_url": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
                }
            },
        )
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(f"{err}")
