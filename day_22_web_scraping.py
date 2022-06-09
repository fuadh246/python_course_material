'''
What is Web Scrapping
The internet is full of huge amount of data which can be used for different purposes. To collect this data we need to know how to scrape data from a website.

Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

In this section, we will use beautifulsoup and requests package to scrape data. The package version we are using is beautifulsoup 4.

To start scraping websites you need requests, beautifoulSoup4 and a website.

pip install requests
pip install beautifulsoup4

'''

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
status = response.status_code
print(status)
content = response.content
soup = BeautifulSoup(content,'html.parser')
print(soup.title)
print(soup.title.get_text())
# print(soup.body)
# print(soup)

tables = soup.find_all('table',{'cellpadding':'3'})
table = tables[0]
for td in table.find('tr').find_all('td'):
    #print(td.text)
    pass

print()
print()
print()

import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
status = response.status_code
print(status)
content = response.content
soup = BeautifulSoup(content,'html.parser')
print(soup.title)
print(soup.title.get_text())


with open('web_scraping.json', 'w', encoding='utf-8') as file:
    lists = soup.findAll("li", {"class": "list-item"})
    # print(lists)
    for list in lists:
        # print(list.text)
        line = list.text.splitlines()
        m_line = f'{line[1]}\n{line[2]}'
        #json.dump(m_line.splitlines(), file, ensure_ascii=False, indent=4)

# with open('web_scraping.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# print(data)