import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.eortologio.net/giortes/1/index.php'
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

results = [a.get('href') for a in soup.find_all('a')]
# all_hrefs = [a.get('href') for a in soup.find_all(href=re.compile("/month"))]

for i in range(40,594):
    print(results[i])


# results = soup.find_all(href=re.compile("/month"))

# for result in results:
#     print(str(result))


# results = soup.find_all('a')

# for result in results:
#     print(result.get('href'))




