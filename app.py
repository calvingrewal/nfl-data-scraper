import requests
from bs4 import BeautifulSoup
import csv

afcTeams = ['nwe', 'mia', 'nyj', 'buf', 'rav', 'pit', 'cle', 'cin', 'clt', 'jax', 'htx', 'oti', 'sdg', 'rai', 'kan', 'den']

nfcTeams = ['dal', 'nyg', 'was', 'phi', 'gnb', 'det', 'min', 'chi', 'atl', 'tam', 'nor', 'car', 'sea', 'crd', 'ram', 'sfo']

for team in nfcTeams:
    weeks = []
    for i in range(2000, 2017):
        print('%s %s' %(team, i))
        url = "https://www.pro-football-reference.com/teams/%s/%s.htm" % (team, i)
        page = requests.get(url)
        contents = page.content

        soup = BeautifulSoup(contents, 'html.parser')
        table = soup.select('#all_games table')
        if len(table) > 0:
            rows = table[0].find('tbody').find_all('tr')

            for row in rows:
                week = []
                for stat in row:
                    week.append(stat.text)
                weeks.append(week)


    with open(team+'.csv', 'w') as f:
        csvfile = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvfile.writerows(weeks)
