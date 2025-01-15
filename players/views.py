from django.conf import settings
import csv
from django.shortcuts import render


def index_players(request):
    csv_file_path = settings.MEDIA_ROOT / 'csv' / 'tyumen_players.csv'
    with open(csv_file_path, 'r',  encoding="utf-8") as file:
        data = [{k: str(v) for k, v in row.items()} \
        for row in csv.DictReader(file, skipinitialspace=True)]

    return render(request, 'players/players.html', {'data': data})