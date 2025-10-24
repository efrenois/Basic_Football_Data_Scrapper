# Basic_Sports_Data_Scrapper

This project provides a Python scraper that allows you to collect statistical data on different sport matches and players from public sources. It offers configurable scraping rules and CSV export to prepare datasets for analysis or machine learning purposes. 

## Features
- Scraping of match and player statistics from various sport websites.
- Configurable scraping rules for different websites.
- Export of collected data to CSV format for easy analysis.

## Project architecture

The project is structured as follows:

```bash
Basic_Sport_Data_Scrapper/
├── core
│   ├── exporter.py             # Export to CSV
│   ├── fetcher.py              # Downloading HTML pages
│   └── parser.py               # Parsing HTML content
├── data                        # Folder for storing data collected from scraping 
├── main.py                     # Entry point of the application  
├── README.md
├── requirements.txt            # List of dependencies
├── scraper.py                  # Scraper class coordinating the scraping process
```       
## Setup and Running 
### Running locally 
This requires Python and manual installation of dependencies on your host machine.

1. Install Python (version 3.7 or higher).
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git # Replace with your repo URL
   cd your-repo-name
2. Create virtual environment and activate it (Recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt  

## Example Usage 
1. Open `main.py` and set the URL of the page you want to scrape (line 7).
2. Open `scraper.py` and set the CSS selector for the table from which you want to extract the data. 
3. Run the script using:
   ```bash
   python main.py
4. The scraped data will be saved in the `data` folder as CSV files.

# Note
This is a basic implementation and may require adjustments based on the specific structure of the target websites.

# Contributing
Contributions are welcome! 
