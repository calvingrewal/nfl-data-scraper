import requests
from bs4 import BeautifulSoup
import csv
weeks = []
for i in range(2000, 2017):

    url = "https://www.pro-football-reference.com/teams/nwe/%s.htm" % (i)
    page = requests.get(url)
    contents = page.content

    soup = BeautifulSoup(contents, 'html.parser')
    table = soup.select('#all_games table')
    rows = table[0].find('tbody').find_all('tr')

    for row in rows:
        week = []
        for stat in row:
            week.append(stat.text)
        weeks.append(week)

with open('nwe.csv', 'w') as f:
    csvfile = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvfile.writerows(weeks)
