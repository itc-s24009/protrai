# s24009
# 沖縄県の推計人口のページより最新情報をスクレイピングするpythonコード
# https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

url = ' https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(url)
html.encoding = 'Shift_JIS'

print(html.text)

soup = BeautifulSoup(html.text, "html.parser")
print(soup.find("title").string)

table = soup.find("table", class_="table font2 gyo5")
print(table)

a = []

a.append(1400000)
a.append(700000)
a.append(700000)

print(f"仮出力")
print(f"総人口:{a[0]}人")
print(f"男:{a[1]}人")
print(f"女:{a[2]}人")
