#s24009
#沖縄県の推計人口のページより最新情報をスクレイビングするpythonコード
#view-source:https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

url = "https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html"
html = requests.get(url)

html.encoding = 'Shift_JIS'

#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.find('title').string)

table = soup.find("table", class_="table1 font2 gyo5")
print(table.find_all("td"))
