from scraper import Scraper

def main():
    print(" Sport Data Scraper")
    print("------------------------")

    url = "..." # URL de la page à scraper
    Scraper().scrape_tables(url)

if __name__ == "__main__":
    main()

