from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from ..models import Player


def parse_players_id(driver, valid_city):
    url = "https://gofederation.ru/players"
    select_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div[1]/select'
    table_xpath = '/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/table'
    driver.get(url)
    select_element = Select(driver.find_element(By.XPATH, select_xpath))
    
    players_id = set()
    if "За всё время" in [o.text for o in select_element.options]:
        select_element.select_by_visible_text("За всё время")
        
        WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, table_xpath)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        with open('test.html', "w", encoding='utf-8') as f:
            f.write(driver.page_source)
            f.close()
        table = soup.find("tbody")
        rows = table.find_all('tr')
        
        for row in rows:
            cells = row.find_all('td')
            id = cells[1].find('a', {"class": ""})["href"].split('/')[-1]
            city = cells[2].text
            if city in valid_city:
                players_id.add(id)
    return players_id


def get_player_url(id):
    return f"https://gofederation.ru/players/{id}"


def get_player_info(driver, url):    
    try:
        driver.get(url)
        info = {
            "name": driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[1]").text,
            "city": driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[1]/span").text,
            "rating": driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]").text,
            "rank": driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[2]").text,
            "tournaments": driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[3]/div[2]").text,
            "games": driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[4]/div[2]").text,
            "last_game_date": driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td[1]/span/time[1]").get_attribute("datetime"),
        }
        if info["name"].find('_') > 0:
            info["name"] = info["name"][:info["name"].find('_')]
        if info["name"].find('(') > 0:
            info["name"] = info["name"][:info["name"].find(' (')]
        info["city"] = info["city"].replace('(', '').replace(')', '')
        info["rank"] = info["rank"].replace('d', ' дан').replace('k', ' кю')
    except:
        info = None
    return info


def update_player(driver, id, valid_city, new_player):
    url = get_player_url(id)
    player_info = get_player_info(driver, url)
    if player_info is not None:
        if new_player and (not player_info["city"] in valid_city):
            return False
        else:
            player, created = Player.objects.update_or_create(id=id, defaults=player_info)
            return created
        

def run(*args):
    valid_city = ["Тюмень"]
    driver = webdriver.Chrome()

    new_players_set = parse_players_id(driver, valid_city)
    old_players_set = set(Player.objects.values_list('id', flat=True))
    id_set = new_players_set.union(old_players_set)

    for id in id_set:
        new_player = (id in new_players_set) and not (id in old_players_set)
        update_player(driver, id, valid_city, new_player)
    
    driver.quit()
