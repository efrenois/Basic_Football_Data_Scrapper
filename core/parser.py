from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_table(self, table_selector):
        """Extrait un tableau HTML sous forme de liste de listes."""
        table = self.soup.select_one(table_selector)
        if not table:
            print("Tableau introuvable !")
            return []

        data = []
        for row in table.select("tbody tr"):
            if "thead" in row.get("class", []):
                continue
            cols = [c.text.strip() for c in row.select("th, td")]
            if any(cols):
                data.append(cols)
        return data