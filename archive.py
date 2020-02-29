import requests
from bs4 import BeautifulSoup
from pytube import YouTube


class Playlist():

    # For future compatibility with other video hosting sites.
    SOURCES = {
        'youtube': 'https://www.youtube.com',
    }

    def __init__(self, url, audio_only=True, source='youtube'):
        self.url = url
        self.source = source
        self.audio_only = audio_only
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
        total_tracks = len(self.urls)
        for index, url in enumerate(self.urls):
            yt = YouTube(url)
            if self.audio_only:
                stream = yt.streams.get_audio_only()
            else:
                stream = yt.streams.get_highest_resolution()

            stream.download(self.destination)
            print(f'Downloaded track {index + 1} of {total_tracks}.')

        print('Playlist Download Complete.')


if __name__ == "__main__":
    url = input("Enter Playlist URL: ")
    audio_only = input("Download audio only? (True/False): ")

    if audio_only.lower() == 'false':
        p = Playlist(url, audio_only=False)
    else:
        p = Playlist(url)

    p.download()