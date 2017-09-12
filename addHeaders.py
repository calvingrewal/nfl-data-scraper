import requests
from bs4 import BeautifulSoup
import csv

teams = ['nwe', 'mia', 'nyj', 'buf', 'rav', 'pit', 'cle', 'cin', 'clt', 'jax', 'htx', 'oti', 'sdg', 'rai', 'kan', 'den','dal', 'nyg', 'was', 'phi', 'gnb', 'det', 'min', 'chi', 'atl', 'tam', 'nor', 'car', 'sea', 'crd', 'ram', 'sfo']

def add_headers():
    headers = []
    with open('sample.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)

    for team in teams:
        arr = []
        with open(team + '.csv', 'r') as f:
            reader = csv.reader(f)

            # arr = list(reader)[25:]
            arr = list(reader)
            arr.insert(0, headers)

        with open(team + '.csv', 'w') as f:
            csvfile = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvfile.writerows(arr)

add_headers()

