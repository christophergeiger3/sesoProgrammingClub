import urllib.request as scrape
import re

base_url = 'https://www.youtube.com/results?search_query='
word = input("Enter a search term to find the first resulting title: ")
base_url += word

html = scrape.urlopen(base_url)
html = str(html.read())

regex = '<a.+?title=\"(.+?)\"'
pattern = re.compile(regex)

i = 1
for exp in re.findall(pattern, html):
    if i == 45:
        print(exp)
    i+=1
