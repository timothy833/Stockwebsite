import requests

STOCK_ID='00878'

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
res = requests.get(f'https://goodinfo.tw/tw/StockDividendSchedule.asp?STOCK_ID={STOCK_ID}', headers = headers)
res.encoding = 'utf-8'
# print(res.text)

from bs4 import BeautifulSoup
bs = BeautifulSoup(res.text, 'html.parser')
data = bs.select_one('#tblDetail')

import pandas
dfs = pandas.read_html(data.prettify())
print(dfs)
print('------------------------------------------------------------------------')


node = dfs[0]
print(node.head(5))


# node.columns = node.columns.get_level_values(2)
# print(node.columns)
# print('------------------------------------------------------------------------')
# node = node[['股利  發放  年度', '股利所屬  盈餘期間', '除息  交易日', '除息  參考  價','盈餘']]
# print(node)

# node = node[('除息日程','除息  交易日')]
# node.columns = node.columns.get_level_values(1)
# node = node[['除息  交易日']]

# 除息日程
# print('-'*10+'除息日程' + '-'*10)
# ex_dividends_date_node = node['除息日程']
# print(ex_dividends_date_node)
# print(ex_dividends_date_node.columns)
# ex_dividends_date_node.columns = ex_dividends_date_node.columns.get_level_values(1)
# print(ex_dividends_date_node)
# ex_dividends_date_node_dict = ex_dividends_date_node.to_dict('records')
# print(ex_dividends_date_node_dict)

# 股利發放年度
# print('-'*10+'股利發放年度' + '-'*10)
# payment_year_node = node[['股利  發放  年度','股利所屬  盈餘期間']]
# payment_year_node.columns = payment_year_node.columns.get_level_values(2)
# print(payment_year_node.to_dict('records'))

# 現金股利
print('-'*10+'現金股利' + '-'*10)
node = node.rename(columns=lambda x: x.replace(' ', '').replace('\xa0',''))
print(node.columns)
shareholders_dividend_node = node['股東股利(元/股)']
print(shareholders_dividend_node)
print(shareholders_dividend_node.columns)

a = shareholders_dividend_node['現金股利']
print(a.to_dict('records'))
b = shareholders_dividend_node['股票股利']
print(b.to_dict('records'))


# print(node.columns)
# node.columns = node.columns.get_level_values(1)
# shareholders_dividend_node = node[['現金股利']]
# print(shareholders_dividend_node.columns)
# print(shareholders_dividend_node)
# shareholders_dividend_node.columns = shareholders_dividend_node.columns.get_level_values(2)





