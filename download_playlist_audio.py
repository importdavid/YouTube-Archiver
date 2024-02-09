"""Creates a folder in my Windows Music folder in which to download the
highest bitrate audio file for each track in a given playlist."""

from pytube import Playlist
from pathlib import Path
import platform

# Function to create directory based on artist and playlist title
def create_directory(playlist):
    first_video = playlist.videos[0]
    artist, playlist_title = first_video.author, playlist.title
    folder_name = f"{artist} - {playlist_title}"

    # My Music folder
    if platform.system() == 'Linux': # WSL
        music_folder = Path(f'/mnt/c/Users/David/Music/')
    else:
        music_folder = Path.home() / 'Music'
    output_folder = music_folder / folder_name

    # Create the folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    return output_folder

# Function to download audio with the highest bitrate
def download_highest_bitrate_audio(video, track, output_folder):
    audio_streams = video.streams.filter(only_audio=True)

    # Check if there are audio streams available
    if audio_streams:
        # Sort streams by bitrate in descending order
        audio_streams = sorted(audio_streams, key=lambda x: x.abr, reverse=True)

        # Choose the stream with the highest bitrate
        audio_stream = audio_streams[0]
    
        print(f"Downloading: {video.title}")
        audio_stream.download(
            output_path=output_folder, 
            filename_prefix=f"{str(track).zfill(2)} "
            )
    else:
        print(f"No audio streams available for: {video.title}")


if __name__ == '__main__':
    # Prompt user to input YouTube URL
    playlist_url = input("Enter the YouTube URL of the playlist you want to download: ")
    playlist = Playlist(playlist_url)

    # Create directory based on artist and playlist title
    output_folder = create_directory(playlist)

    # Iterate through videos in the playlist
    for track, video in enumerate(playlist.videos):
        download_highest_bitrate_audio(video, track, output_folder)

    print("Download complete.")