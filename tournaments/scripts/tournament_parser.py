from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
from ..models import Tournament


def parse_tournaments(driver, valid_city):
    url = "https://gofederation.ru/tournaments"
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find("div", {"class": 'tournament-list'})

    
    id = [row["href"].split('/')[-1] for row in table.find_all('a', {"class": ""})]
    title = [row.string for row in table.find_all('a', {"class": ""})]
    city = [row.string for row in table.find_all('div', {"class": 'location'})]
    period = [row.text for row in table.find_all('div', {"class": 'dates'})]
    date = [row.span.time["datetime"] for row in table.find_all('div', {"class": 'dates'})]
    df = pd.DataFrame({"id": id, "title": title, "city": city, "period": period, "date": date})
    df = df.set_index("id")
    df = df.dropna()
    df = df.query("city in @valid_city")
    print(df)
    return df


def run(*args):
    valid_city = ["Тюмень"]
    driver = webdriver.Chrome()

    df = parse_tournaments(driver, valid_city)
    
    already_exists = set([str((t.title, t.period)) for t in Tournament.objects.all()])
    for id, row in df.iterrows():
        if str((row["title"], row["period"])) in already_exists:
            continue

        tournament_info = {
            "title": row["title"],
            "city": row["city"],
            "period": row["period"],
            "date": row["date"],
        }
        tournament, created = Tournament.objects.update_or_create(id=id, defaults=tournament_info)
    
    driver.quit()

    
