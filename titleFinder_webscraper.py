import urllib.request as scrape
import re

urls = ["https://google.com", "https://bing.com", "https://facebook.com", "https://youtube.com"]
titles = []
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

for url in urls:
    html = scrape.urlopen(url)
    html = str(html.read())
    titles.append(re.findall(pattern, html))

for title in titles:
    print(title)




'''
html = scrape.urlopen("https://google.com")
html = str(html.read())

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

titles = re.findall(pattern, html)

print(titles)
'''