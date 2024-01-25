from pytube import Playlist
from pathlib import Path

# Bo Burnham's Inside Example
playlist_url = 'https://www.youtube.com/playlist?list=PLLPzo5hOm16VQrTv7lk0POyv6RiFDqgqn'

# My Music folder
music_folder = Path(f'/mnt/c/Users/David/Music/')

# Function to create directory based on artist and playlist title
def create_directory(playlist):
    first_video = playlist.videos[0]
    artist, playlist_title = first_video.author, playlist.title
    folder_name = f"{artist} - {playlist_title}"
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
    # Create a Playlist object
    playlist = Playlist(playlist_url)

    # Create directory based on artist and playlist title
    output_folder = create_directory(playlist)

    # Iterate through videos in the playlist
    for track, video in enumerate(playlist.videos):
        download_highest_bitrate_audio(video, track, output_folder)

    print("Download complete.")
