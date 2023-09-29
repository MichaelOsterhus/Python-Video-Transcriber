#pip install moviepy openai-whisper

from pytube import YouTube
from moviepy.editor import VideoFileClip
import whisper

def transcribe_file(file):

    # CONVERT VIDEO TO AUDIO AND SAVE AS MP3
    video = VideoFileClip(file)
    audio = video.audio
    audio_mp3_path = "audio.mp3"

    try:
        audio.write_audiofile(audio_mp3_path, codec="mp3")
        print('Audio saved as MP3.')

    except Exception as e:
        print(f'Audio conversion error: {str(e)}')

    # CONVERT AUDIO MP3 TO TEXT
    model = whisper.load_model("base")

    result = model.transcribe(audio_mp3_path)
    with open('transcription.txt', "w") as f:
        f.write(result['text'])

    print('Audio converted to text.')

    # Clean up resources
    video.close()


def transcribe_url(url):
#DOWNLOAD VIDEO
    local_video_path = "video.mp4"

    def download(link, filename):
        try:
            ytobject = YouTube(link)
            res = ytobject.streams.get_lowest_resolution()
            res.download(filename=filename)

        except:
            print('Error Occurred.')

        print('Download complete.')

    download(url, local_video_path)

    # CONVERT VIDEO TO AUDIO AND SAVE AS MP3
    transcribe_file(local_video_path)
