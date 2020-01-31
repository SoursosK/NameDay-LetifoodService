import requests
from bs4 import BeautifulSoup
from re import compile, match
from time import sleep
from greek_stemmer import GreekStemmer
from greek_accentuation.characters import *

URL = ''
for i in range(1,2): # will be 1,24
    # sleep(4)
    URL = 'https://www.eortologio.net/giortes/'+ str(i) +'/index.php'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

results = [a.get('href') for a in soup.find_all('a')]

p = compile('/pote_giortazei/')
stemmer = GreekStemmer()

for i in range(40,594):
    if p.match(results[i]):
        parts = results[i].split('/')
        newstr = ''
        for j in range(0, len(parts[2])):
            newstr += base(parts[2][j])

        print(stemmer.stem(newstr.upper()).lower())



