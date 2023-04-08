import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def getTrackData(track_id):
    global data
    page = requests.get(f"https://boatlabs.net/track/{track_id}")
    soup = BeautifulSoup(page.content, "html.parser")

    track_name = ' '.join(soup.find(id="title").text.split(' ')[2:])
    data[track_name] = {}

    for el in soup.find(id="toplist").find("ol").find_all("li"):
        ign, time = str(el)[4:-5].split(' - ')
        data[track_name][ign] = float(time)
    
    return

data = {}
tracks = {
    "Newbie": "1",
    "Makkuusen Raceway": "4",
    "FC1 Gumball 3000": "5",
    "Galaxy": "6",
    "Duck Park Raceway": "10",
    "The Backjard": "12",
    "Crow Valley": "19",
    "WMS": "23",
    "Greasy Circuit": "24",

    "Candyland": "25",
    "Greasy Arena": "30",
    "Spooktacular": "32",
    "Grease Puddle": "35",
    "Mariana Valley": "42",
    "Crumble": "47",
    "Latium GP": "48",
    "Cardalina": "49",
    "Yoshi Circuit": "50",

    "Silverstone": "60",
    "Waterworld": "62",
    "Atomic Dust": "67",
    "Capybara Circuit": "68",
    "Trial Tent": "71",
    "Canyon Relay": "72",
    "Duck Pond Raceway": "74",
    "Cardalina V2": "76",
    "Bloedel Oink": "77",

    "The Hedge": "78",
    "Historica": "80",
    "Neon Circuit": "84",
    "BCC": "86",
    "Sour Drive": "89",
    "Fishy Business": "90",
    "LC Track": "95",
    "Death Road": "98",
    "CGP OS2": "105",
}

for track, track_id in tracks.items():
    print(f"Adding data for {track}")
    getTrackData(track_id)


# pprint(data)

with open("track_data.json", "w") as f:
    f.write(json.dumps(data, indent=4))