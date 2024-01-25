"""A script to examine the beautiful soup returned from a YouTube Playlist."""
# IN PROGRESS

import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from pathlib import Path

# Bo Burnham's Inside
url = 'https://www.youtube.com/watch?v=9Tnux7K3MOQ&list=PLLPzo5hOm16VQrTv7lk0POyv6RiFDqgqn'

path = Path('soup.txt')

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
path.write_text(soup.text)
# title = soup.find(class_="pl-header-title").text.strip('\n').strip()
# author = soup.find(class_="pl-header-details").find('a').text
# playlist = soup.find(id='pl-video-list')
# rows = playlist.find_all('tr')