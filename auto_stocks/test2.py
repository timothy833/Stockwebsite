import requests

STOCK_ID='0050'
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
res = requests.get('https://www.moneydj.com/ETF/X/Basic/Basic0007B.xdjhtm?etfid={0}.TW'.format(STOCK_ID))
res.encoding = 'utf-8'
print(res.status_code)
print(res.text)

from bs4 import BeautifulSoup
bs = BeautifulSoup(res.text, 'html.parser')

data = bs.select_one('table.datalist')
# print(data)

import pandas

print('------------------------------------------')
df = pandas.read_html(data.prettify())
print(df[0])
print(df[0].to_dict('records'))
#########################################################
data_time = bs.select('div.eTitle > div')
print(data_time)
print(data_time[0].contents)