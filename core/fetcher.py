import requests
from requests.exceptions import RequestException
import time
import random

class Fetcher:
    def __init__(self, headers=None):
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (compatible; FootballScraper/1.0)"
        }

    def get_html(self, url, retries=3):
        """Télécharge le HTML d'une page, avec gestion d’erreurs."""
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.text
            except RequestException as e:
                print(f"Erreur sur {url} : {e}. Nouvelle tentative...")
                time.sleep(random.uniform(1, 3))
        return None