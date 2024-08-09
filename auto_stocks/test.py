import requests
import context
import html

# a = requests.post('https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=0050')
# print(a.content.decode())

STOCK_ID='0050'

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
res = requests.get('https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID={0}'.format(STOCK_ID), headers = headers)
res.encoding = 'utf-8'
# print(res.text)


from bs4 import BeautifulSoup
bs = BeautifulSoup(res.text, 'html.parser')
data = bs.select_one('#tblDetail')

# print('------------------------------------------------------------------------')



import pandas
dfs = pandas.read_html(data.prettify())
print(dfs)
print('------------------------------------------------------------------------')

node = dfs[0]
print(node.head(5))
# node.columns1 = node.columns.get_level_values(1)
# node.columns2 = node.columns.get_level_values(2)
# node.columns3 = node.columns.get_level_values(3)
# print(node.columns1)
# print(node.columns2)
# print(node.columns3)
node.columns = node.columns.get_level_values(3)
print(node.columns)
node = node[['股利  發放  年度', '股利  合計', '最高', '最低']]
# node = node.head()
print(node)
print('------------------------------------------------------------------------')
# print(node[0:1])
# print(node.iloc[0])


# mask1 = node['股利  發放  年度'] != ' ∟'
# mask2 = node['股利  發放  年度'] > '2015'
# node1 = node[mask1]
# node2 = node1[mask2]
# # print(node1)
# # print(node2)
# node_dict = node2.to_dict('records')
# print(node_dict)

node1 =node[node['股利  發放  年度'] != ' ∟']
node_dict = node1.to_dict('records')
print(node_dict)
