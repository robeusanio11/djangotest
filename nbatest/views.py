from django.shortcuts import render, HttpResponse
from nbatest.models import Teams, Roster
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(req):
    # teams = Teams.objects.all()
    # idCount = 0
    teamAbbrs = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
    # for team in teams:
        # teamObject = Teams(id=idCount, abbr=team)
        # teamObject.save()
    teams = []
    for team in teamAbbrs:
        teamObj = {
            "name": team,
            "players": [],
        }
        html_text = requests.get(f"https://www.basketball-reference.com/teams/{team}/2024.html").text
        soup = BeautifulSoup(html_text, 'lxml')
        player_cards = soup.find_all('td', attrs={"data-stat": "player"})
        playerList = []
        for player in player_cards:
            print(player)
            playerList.append(player.find('a').text)
        # print(playerList)
        teamObj["players"] = playerList
        # print(teamObj)
        teams.append(teamObj)
    return render(req, "teams.html", {"teams":teams})
