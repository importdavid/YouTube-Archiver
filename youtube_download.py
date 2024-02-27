"""
Prompts the user for a YouTube url and whether audio_only is desired.
If playlist, creates output_folder and downloads playlist to it.
If not playlist, or entire playlist undesired, downloads single YouTube file.

Todo: Possible functionality to auto-sort downloads into home folders.
"""

from pytube import YouTube, Playlist
from pathlib import Path

# Function to create directory based on artist and playlist title
def create_directory(playlist):
    """
    Creates a directory derived from YouTube playlist details.
    folder_name = f"{playlist.artist} - {playlist.title}"
    """

    first_video = playlist.videos[0]
    artist, playlist_title = first_video.author, playlist.title
    folder_name = f"{artist} - {playlist_title}"
    output_folder = Path(folder_name)

    # Create the folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    return output_folder

def download(video, output_folder=None, track=None, audio_only=False):
    """
    Downloads a single YouTube file. audio_only=False by default.
    If video is one of playlist, names file with prefix 'track #' (e.g. '001 ').
    """

    if audio_only:
        audio_streams = video.streams.filter(only_audio=True)

        # Check if there are audio streams available
        if audio_streams:
            # Sort streams by bitrate in descending order
            audio_streams = sorted(audio_streams, key=lambda x: x.abr, reverse=True)

            # Choose the stream with the highest bitrate
            stream = audio_streams[0]
        else:
            print(f"No audio streams available for: {video.title}")
    else:
        stream = video.streams.get_highest_resolution()
    
    print(f"Downloading: {video.title}")
    if output_folder:
        stream.download(
            output_path=output_folder, 
            filename_prefix=f"{str(track).zfill(2)} "
        )
    else:
        stream.download()

if __name__ == '__main__':
    # Prompt user for url.
    url = input("Enter YouTube URL: ")

    # Prompt for whether audio_only is desired.
    audio_only = input("Audio only? ('y' or 'n') ")
    if audio_only.lower().strip() == 'y':
        audio_only = True
    else:
        audio_only = False

    # Try and verify downloading as a playlist, otherwise as a single file.
    try:
        playlist = Playlist(url)

        # Check whether user intent was to download entire playlist.
        download_list = input("Download entire playlist? ('y' or 'n') ")
        if download_list.lower().strip() != 'y':
            raise KeyError
        
        # Create folder for playlist tracks
        output_folder = create_directory(playlist)
   
        # Iterate through videos in the playlist
        for track, video in enumerate(playlist.videos):
            download(video, output_folder, track, audio_only)

    except KeyError:
        print('Not a playlist...Downloading single file...')
        yt = YouTube(url)
        download(yt, audio_only=audio_only)

    print('Program finished')