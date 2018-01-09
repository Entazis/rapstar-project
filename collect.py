
import requests
from bs4 import BeautifulSoup
import random
import csv
import io
import time

start_time = time.time()

urls = []
io.open('output.txt', 'w', encoding="utf-8").close()
with open('artists.csv', 'r') as f:
  artists = list(csv.reader(f))

for artist in artists:
    name = artist[0]
    songs = artist[1]

    page = requests.get(songs)
    bs = BeautifulSoup(page.text, 'html.parser')
    possible_links = bs.find_all('a')
    for link in possible_links:
        if link.has_attr('href') and 'dalszoveg/' in link.attrs['href'] and '/'+name+'/' in link.attrs['href'] and '.html' in link.attrs['href']:
            urls.append('http://www.zeneszoveg.hu/' + link.attrs['href'])
    print("Links have been collected from: ", name)

print(len(urls), " links have been collected!")
random.shuffle(urls)
for url in urls:
    print(url)
    page = requests.get(url)
    print(page.status_code)
    print(page.encoding)

    soup = BeautifulSoup(page.text, 'html.parser')
    lyrics = soup.find('div', attrs={'class':'lyrics-plain-text'}).text
    if len(lyrics) > 50 and lyrics is not None:
        file_output = io.open('output.txt', 'a', encoding="utf-8")
        file_output.write(lyrics)
        file_output.close()

print("Altogether ", len(urls), " songs have been collected!")
elapsed_time = time.time() - start_time
print("collecting time was: ", elapsed_time)
