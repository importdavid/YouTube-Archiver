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

    SOURCES = {
        'youtube': 'https://www.youtube.com'
    }

    def __init__(self, title, author, urls, source='youtube'):
        self.title = title
        self.author = author
        self.urls = []
        self.source = source
        self.destination = f"{self.author} - {self.title}/"

        for url in urls:
            self.urls.append(self.SOURCES[source] + url)

    def __str__(self):
        return f"{self.author}: {self.title}"

    def download(self):
        for url in self.urls:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(self.destination)


def make_playlist(playlist_url):
    """Takes a YouTube playlist URL and returns a Playlist instance with Title, Author, and Individual track URLs."""

    r = requests.get(playlist_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find(class_="pl-header-title").text.strip('\n').strip()
    author = soup.find(class_="pl-header-details").find('a').text
    playlist = soup.find(id='pl-video-list')
    rows = playlist.find_all('tr')

    urls = []
    for row in rows:
        urls.append(row.find('a').get('href'))

    return Playlist(title, author, urls)


if __name__ == "__main__":
    url = input("Enter Playlist URL: ")
    p = make_playlist(url)
    p.download()