import requests
from bs4 import BeautifulSoup

content = requests.get('http://www.xinshipu.com/zuofadaquan/622/').content;
soup = BeautifulSoup(content, 'html.parser');

for div in soup.find_all('div', {'class': 'content'}):
    print(div.text.strip());
print('zhe')
