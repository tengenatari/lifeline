from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
from ..models import Tournament


def parse_tournaments(driver):
    url = "https://gofederation.ru/tournaments/"
    select_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/select'
    table_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div[5]/div/div'

    driver.get(url)

    select_element = Select(driver.find_element(By.XPATH, select_xpath))
    options = select_element.options

    df = pd.DataFrame({"id": [], "title": [], "city": [], "period": [], "date": []})
    for option in options:
        select_element.select_by_visible_text(option.text)
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, table_xpath)))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        table = soup.find("div", {"class": 'tournament-list'})

        id = [row["href"].split('/')[-1] for row in table.find_all('a', {"class": ""})]
        title = [row.string for row in table.find_all('a', {"class": ""})]
        city = [row.string for row in table.find_all('div', {"class": 'location'})]
        period = [row.text for row in table.find_all('div', {"class": 'dates'})]
        date = [row.span.time["datetime"] for row in table.find_all('div', {"class": 'dates'})]
        df_year = pd.DataFrame({"id": id, "title": title, "city": city, "period": period, "date": date})
        df = pd.concat([df.reset_index(drop=True), df_year[df_year["city"] == "Тюмень"].reset_index(drop=True)], axis=0)

    df = df.set_index("id")
    return df


def run(*args):
    driver = webdriver.Chrome()

    df = parse_tournaments(driver)
    
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

    
