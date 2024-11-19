import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_nba_data():
    url = "https://www.nba.com/stats/players/traditional"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to fetch data from NBA.com")

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")

    data = []
    for row in rows[1:]:  # Skip header row
        columns = row.find_all("td")
        data.append([col.text.strip() for col in columns])

    columns = [col.text.strip() for col in rows[0].find_all("th")]
    df = pd.DataFrame(data, columns=columns)
    return df
