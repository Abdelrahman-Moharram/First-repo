import requests
from bs4 import BeautifulSoup


url = "http://www.fabpedigree.com/james/mathmen.htm"


res = requests.get(url).content

data = BeautifulSoup(res,'html.parser')

for li in data.findAll('li'):
    print(li.text)