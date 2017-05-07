import urllib.request as scrape
import re

base_url = 'http://www.dictionary.com/browse/'
word = input("Enter a word to define: ")
base_url += word

html = scrape.urlopen(base_url)
html = str(html.read())

regex = '<meta name=\"description\" content=\"(.+?)\"'
pattern = re.compile(regex)

for exp in re.findall(pattern, html):
    print(exp)

