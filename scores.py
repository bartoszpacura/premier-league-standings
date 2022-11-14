from bs4 import BeautifulSoup
from requests import get


URL = 'https://www.premierleague.com/tables'

page = get(URL)
page_data = BeautifulSoup(page.content, features="html.parser")

table = []

for club_data in page_data.find_all(name='tr', attrs={"data-compseason": "489"}):
    club_name = club_data.find("span", class_="long").get_text()
    club_standing = club_data.find("span", class_="resultHighlight").get_text()
    club_points = club_data.find("td", class_="points").get_text()
    club_standing = int(club_standing)

    table.append([club_standing, club_name, club_points])

table.sort()

stats = {}

for x in range(len(table)):
    stats[f"position {table[x][0]}."] = {"club" : table[x][1], "points" : table[x][2]}
