from sites.fbref import FBrefScraper

def main():
    print("⚽️ Football Data Scraper")
    print("------------------------")

    url = "https://fbref.com/en/comps/12/La-Liga-Stats" # URL de la page à scrapper
    FBrefScraper().scrape_tables(url)

if __name__ == "__main__":
    main()

