from core.fetcher import Fetcher
from core.parser import Parser
from core.exporter import Exporter

class FBrefScraper:
    def __init__(self):
        self.fetcher = Fetcher()
        self.exporter = Exporter(base_path="data")

    def scrape_tables(self, url):
        html = self.fetcher.get_html(url)
        parser = Parser(html)
        data = parser.extract_table("#all_stats_squads_standard") # Choisir le sélecteur CSS pour le tableau que l'on souhaite scrapper 
        self.exporter.to_csv(data, "fbref_results.csv")