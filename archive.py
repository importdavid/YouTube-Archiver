"""
TODO:
add boolean audio_only default=False for purely music playlists, otherwise download video as well
add functionality to be run as command line utility and takes playlist URL as arg
"""
import requests
from bs4 import BeautifulSoup
from pytube import YouTube


# Jacob Collier - Djesse Vol. 1 Playlist for testing
DJESSE = 'https://www.youtube.com/playlist?list=OLAK5uy_nhzGQeVePsahNKbIK1U6qLRYkSvHwDTtw'


class Playlist():

    # For future compatibility with other video hosting sites.
    SOURCES = {
        'youtube': 'https://www.youtube.com',
    }

    def __init__(self, url, source='youtube'):
        self.url = url
        self.source = source
        self.scrape_info()
        self.destination = f"{self.author} - {self.title}/"

    def __str__(self):
        return f"{self.author}: {self.title}"

    def scrape_info(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.title = soup.find(class_="pl-header-title").text.strip('\n').strip()
        self.author = soup.find(class_="pl-header-details").find('a').text
        playlist = soup.find(id='pl-video-list')
        rows = playlist.find_all('tr')

        urls = []
        for row in rows:
            # Combine scrape urls for tracks with BASE YouTube URL
            url = row.find('a').get('href')
            url = self.SOURCES[self.source] + url
            urls.append(url)

        self.urls = urls

    def download(self):
        for url in self.urls:
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()
            stream.download(self.destination)


if __name__ == "__main__":
    url = input("Enter Playlist URL: ")
    p = Playlist(url)
    p.download()