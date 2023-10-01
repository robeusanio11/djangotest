from django.shortcuts import render, HttpResponse
from nbatest.models import Teams, Roster
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(req):
    # teams = Teams.objects.all()
    # idCount = 0
    teams = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
    # for team in teams:
        # teamObject = Teams(id=idCount, abbr=team)
        # teamObject.save()
        # html_text = requests.get(f"https://www.basketball-reference.com/teams/{team}/2024.html").text;
        # soup = BeautifulSoup(html_text, 'lxml');
        # player_cards = soup.find_all('td', attrs={"data-stat": "player"});
        # html_text = requests.get(f"https://www.basketball-reference.com/teams/{team}/2024.html").text
    return render(req, "teams.html", {"teams": teams})
