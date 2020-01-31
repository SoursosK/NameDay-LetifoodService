import requests
from bs4 import BeautifulSoup
from re import compile, match
from nltk.stem import PorterStemmer
from time import sleep
from nltk.tokenize import sent_tokenize, word_tokenize
from greeklish.converter import Converter

URL = ''
for i in range(1,2): # will be 1,24
    # sleep(4)
    URL = 'https://www.eortologio.net/giortes/'+ str(i) +'/index.php'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

results = [a.get('href') for a in soup.find_all('a')]

p = compile('/pote_giortazei/')
myconverter = Converter(max_expansions=20)

for i in range(40,594):
    if p.match(results[i]):
        parts = results[i].split('/')

        print(myconverter.convert(parts[2]))






# ps = PorterStemmer()





