from pathlib import Path
from pytube import YouTube
import platform

def download_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # Set default output path to user's Downloads folder
        if platform.system() == 'Linux': # WSL
            output_path = Path(f'/mnt/c/Users/David/Downloads/')
        else:
            output_path = Path.home() / 'Downloads'

        # Download the video
        print(f"Downloading {yt.title}...")
        stream.download(output_path)
        print("Completed successfully! Check your Downloads folder!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Prompt user to input YouTube URL
    video_url = input("Enter the YouTube URL of the video you want to download: ")

    # Download the video
    download_video(video_url)
