import json
from pprint import pprint
import math

def time_converter(s_time):
    if(s_time < 60):
        return f"{s_time:.3f}"
    minutes = 0
    while s_time >= 60:
        minutes += 1
        s_time -= 60
    s_time_flat = math.floor(s_time)
    ms_time = f"{(s_time-s_time_flat):.3f}"
    return f"{minutes}:{s_time_flat:0>2d}{ms_time[-4:]}"

data = {}
with open("track_data.json", "r") as f:
    data = json.load(f)

diamond_medal_leaderboard = {
    "sodasoker": 36,
    "Makkuusen": 36,
    "Lapis_Lettuce": 36,
    "F4n14sy": 36,
    "5h1zuy4": 36,
    "EvilScientist": 36,
    "NidoThe1st": 36,
    "Pigalala": 36,
    "Rocket_Raze": 36,
    "CaptainNoah07": 36,
    "JP77_": 36,
    "The_Lasersloth": 36,
    "AlesandroDeMoor": 36,
    "ElSacoDePapas": 35,
    "crispy_photo": 34,
    "Comfy_Vibes": 33,
    "ZeqroW": 31,
    "purple_toki": 29,
    "oinkd": 27,
    "JollyTheDuck": 25,
    "Mariana52": 23,
    "TechnoGustav": 22,
    "0x26e": 17,
    "_Ozon3_": 16,
    "Renokas1": 13,
    "Herag0n": 12,
    "captain_craftyz": 10,
    "GregSaysNo": 9,
    "fr0styguy": 8,
    "NUKll": 8,
    "Dylqn": 8,
    "sab2003": 7,
    "Bluleader64": 7,
    "SirFeederKid": 6,
    "Makknerfed": 5,
    "Criscero": 5,
    "Jmody13": 5,
    "Pana_64": 5,
    "AdamsApples": 4,
    "TheReaper____": 4,
    "Xerveus": 4,
    "Wackymaxitaxi": 4,
    "mistergreenjeans": 3,
    "__R0gue__": 3,
    "OnsHuts": 3,
    "StinkySoxx": 2,
    "Scriixer": 2,
    "FplaysYT": 2,
    "_Beertje": 2,
    "Allttro": 2,
    "LegendaryA7": 2,
    "MeatBagFranks": 2,
    "Mirkec3": 2,
    "NAIRB7002": 2,
    "kcylnFC1": 2,
    "skipsnuf": 2,
    "silverrruns": 2,
}

players = {}
validated_players = []
check_track = "BCC"
validated_times = []

for ign, medals in diamond_medal_leaderboard.items():
    players[ign] = {
        "times": 0,
        "medals": medals,
    }

for track, records in data.items():
    for ign, time in records.items():
        if(ign in players):
            players[ign]["times"] += 1

for ign in players:
    # print(f"{ign:^18} | {players[ign]['medals']:<2} / {players[ign]['times']:<2}")
    if(players[ign]["medals"] == players[ign]["times"]):
        validated_players.append(ign)

for ign, time in data[check_track].items():
    if(ign in validated_players):
        validated_times.append(time)

validated_times.sort()

print(f"Estimated diamond medal time on {check_track} is {time_converter(validated_times[-1])} from {len(validated_times)} players")
# pprint(validated_times)

pprint(len(validated_players))
# pprint(data)