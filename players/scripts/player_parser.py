from ..models import Player
from django.apps import apps
from tqdm import tqdm
import requests
from django.utils import timezone

def fetch_and_save_players(url):
    print(f"GET {url}")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    players = data.get("Players", [])

    id_set = set()
    print("Start json deserialization")
    for player_data in tqdm(players):
        id = player_data.get("ID")
        url = player_url(id)
        name = player_data.get("Name")
        city = player_data.get("Location")
        rating = player_data.get("Rating")
        rank = player_rank(rating)
        last_game_date = player_data.get("LastUpdate")
        last_game_date = timezone.datetime.fromisoformat(last_game_date[:-1]) if last_game_date else None

        Player.objects.update_or_create(
            id=id,
            defaults={
                'name': name,
                'url': url,
                'city': city,
                'rating': rating,
                'rank': rank,
                'last_game_date': last_game_date,

            }
        )
        id_set.add(id)
    
    print("Start getting statistics")

    for id in tqdm(id_set):
        url = player_statistics_url(id)

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        stats = data.get("Statistics")
        tournaments = stats.get("Tournaments")
        games = stats.get("Games")
        Player.objects.update_or_create(
            id=id,
            defaults={
                'tournaments': tournaments,
                'games': games,
            }
        )

    print("Players updating done")
        

def player_statistics_url(id):
    return f"https://sputnik-go.com/api/v1/profile/{id}"


def player_url(id):
    return f"https://sputnik-go.com/players/{id}"


def get_valid_city():
    City = apps.get_model('main', 'City')
    return City.objects.filter(deleted=False).values_list("name", flat=True)


def player_rank(rating):
    rank = ""
    if rating < 600:
        rank = f"{30 - rating//60} кю"
    elif rating < 2100:
        rank = f"{20 - (rating-600)//75} кю"
    elif rating < 3000:
        rank = f"{(rating - 2000)//100} дан"
    return rank


def run():
    valid_city = get_valid_city()
    url = "https://sputnik-go.com/api/v1/players?loc=155&sort=rating"
    fetch_and_save_players(url)