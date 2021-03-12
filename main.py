from bs4 import BeautifulSoup as bs
import requests
import time

while True:
    wst = requests.get("https://livescores.worldsnookerdata.com/").text
    soup = bs(wst, "lxml")
    nav_bar = soup.find("a", string="Live Scores")
    live_scores_url = "https://livescores.worldsnookerdata.com" + nav_bar.get("href")
    live_scores = requests.get(live_scores_url).text
    soup = bs(live_scores, "lxml")
    live_matches = soup.find_all("div", class_="live-match-item")
    players = []
    scores = []
    name1 = "Unknown"
    name2 = "Unknown"
    names1 = []
    names2 = []
    player1 = soup.findAll("span", {"class":"live-match-item-val-player1"}, text=True)
    for playerX in player1:
        name1 = playerX.text
        names1.append(name1)
        
    player2 = soup.findAll("span", {"class":"live-match-item-val-player2"}, text=True)
    for playerY in player2:
        name2 = playerY.text
        names2.append(name2)
    l = 0
    while l < len(names1):
        players.append(names1[l])
        players.append(names2[l])
        l += 1

    scoring = soup.findAll("td", class_="col-lg-3 col-md-3 col-sm-3 col-xs-3")
    for scoreX in scoring:
        score = scoreX.text
        scores.append(score)
    p1 = 0
    sc1 = 0
    #print(players)
    while sc1 < len(players):
        print(players[sc1] + " " + scores[sc1] + " vs "  + scores[sc1 + 1] + " " + players[sc1 + 1])
        p1 += 1
        sc1 += 2
    print ("-----------------")
    time.sleep(30)
