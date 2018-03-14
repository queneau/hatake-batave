import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

html =  urllib.request.urlopen("http://npb.jp/bis/players/31235113.html")
soup = BeautifulSoup(html, "html.parser")
td = soup.find_all("td", class_ = "year")

batave = []

for record in td:
    alice = record.find_all("td")
    batave.append(float(alice[19].string))

plt.plot(batave)
plt.show()