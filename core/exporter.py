import pandas as pd
from pathlib import Path

class Exporter:
    def __init__(self, base_path="data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)

    def to_csv(self, data, filename):
        df = pd.DataFrame(data)
        output_path = self.base_path / filename
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"✅ Données sauvegardées dans {output_path}")