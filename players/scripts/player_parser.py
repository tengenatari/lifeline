from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
from ..models import Player


def get_players_df(driver, valid_city):
    url = "https://gofederation.ru/players"
    select_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div[1]/select'
    table_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/table'

    driver.get(url)

    select_element = Select(driver.find_element(By.XPATH, select_xpath))
    
    if "За всё время" in [o.text for o in select_element.options]:
        select_element.select_by_visible_text("За всё время")
        
        WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, table_xpath)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        with open('test.html', "w", encoding='utf-8') as f:
            f.write(driver.page_source)
            f.close()
        table = soup.find("tbody")
        rows = table.find_all('tr')
        
        df = pd.DataFrame({"name": [], "city": []})
        for row in rows:
            cells = row.find_all('td')
            id = cells[1].find('a', {"class": ""})["href"].split('/')[-1]
            name = cells[1].find('a', {"class": ""}).text
            city = cells[2].text
            if name == "Raimberdiev Baytik":
                print(row)
            df.loc[id] = [name, city]
        
        df.to_csv('test.csv')
        df["name"] = df["name"].apply(lambda s: s[:(s.find("_") if s.find("_")>0 else len(s))])
        
        df = df.query('city in @valid_city')
        return df 

    return None


def get_player_info(driver, url):    
    try:
        driver.get(url)
        raiting = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]").text
        rank = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[2]").text
        tournaments = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[3]/div[2]").text
        games = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[4]/div[2]").text

        rank = rank.replace('d', ' дан').replace('k', ' кю')
    except:
        raiting = None
        rank = None
        tournaments = None
        games = None
    return raiting, rank, tournaments, games


def get_player_url(id):
    return f"https://gofederation.ru/players/{id}"


def run(*args):
    valid_city = ["Тюмень"]
    driver = webdriver.Chrome()
    df = get_players_df(driver, valid_city)
    if df is None:
        return
    
    df = df.dropna()
    #df.to_csv('test.csv')
    # for id, row in df.iterrows():
    #     url = get_player_url(id)
    #     raiting, rank, tournaments, games = get_player_info(driver, url)
    #     df.loc[id, "raiting"] = raiting
    #     df.loc[id, "rank"] = rank
    #     df.loc[id, "tournaments"] = tournaments
    #     df.loc[id, "games"] = games

    #     if raiting is not None:
    #         update_dict = {"name": row["name"], 
    #                        "city": row["city"], 
    #                        "rank": rank, 
    #                        "tournaments": tournaments, 
    #                        "games": games,
    #                        "raiting": raiting}
            
    #         player, created = Player.objects.update_or_create(id=id,  defaults=update_dict)
            
    driver.quit()  
    print(df)


# if __name__ == '__main__':
#     main()