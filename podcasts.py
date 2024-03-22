from pytube import Playlist

PODCASTS = {
    'Lex Fridman Podcast': 'https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4',
    'The Dr. Jordan B. Peterson Podcast': 'https://www.youtube.com/playlist?list=PL22J3VaeABQAbEeT04p5VmAOBmqw2kmxj',
    'Huberman Lab': 'https://www.youtube.com/playlist?list=PLPNW_gerXa4Pc8S2qoUQc5e8Ir97RLuVW',
}

PODCASTS_LIST = [
    # Lex Fridman Podcast
    'https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4',
    # The Dr. Jordan B. Peterson Podcast
    'https://www.youtube.com/playlist?list=PL22J3VaeABQAbEeT04p5VmAOBmqw2kmxj',
    # Huberman Lab
    'https://www.youtube.com/playlist?list=PLPNW_gerXa4Pc8S2qoUQc5e8Ir97RLuVW',
]

class Podcast:
    def __init__(self, title, link) -> None:
        self.title = title
        self.link = link

for podcast, link in PODCASTS.items():
    print(podcast, link)