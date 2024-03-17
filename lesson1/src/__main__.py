import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# r = requests.get( 'https://www.canadacomputers.com/index.php?cPath=710&language=en' )
r = requests.get( 'https://www.canadacomputers.com/index.php?cPath=710&language=en&ajax=true&page=2' )
soup = BeautifulSoup(r.text, 'html.parser')
a_list = soup.find_all('a')
data = []
for a_item in a_list:
    if a_item.get('href') is None:
        continue
    href = a_item.get('href')
    if 'item_name' in ('%s' % a_item):
        a_item_parent = a_item.parent
        a_item_parent_2 = a_item_parent.parent
        name = str(a_item).split('item_name:')[-1].split('price:=')[0].strip()[1:]
        regex = r'<span class="text-danger.*?>\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        print(name)
        print('______________________________________________________')
        print('______________________________________________________')
        matches = re.findall(regex, str(a_item_parent_2))
        if len(matches) != 1:
            continue
        # print('______________________________________________________')
        # print('______________________________________________________')
        price = float(matches[0].split('$')[-1].replace(',', ''))
        # print(name)
        print(price)
        # print(href)
        data.append([name, price, href])
print(data)
df = pd.DataFrame(data, columns=['name', 'price', 'url'])
df.to_csv('data_%s.csv' % pd.Timestamp.today().strftime('%Y_%m_%d'))


