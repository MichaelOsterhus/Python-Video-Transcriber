# Python-Video-Transcriber
A simple Python app with GUI that transcribes speech to text from YouTube video URL or local video file

## First download or clone the repository

## To run, you will need Python installed as well as the Python libraries
+ pytube - for downloading videos from YouTube
+ moviepy - for getting audio file from video
+ whisper - for transcribing audio to text

You can install these in a terminal, in the repository, using 

```pip install pytube moviepy whisper```

## To run the app
in the terminal, in the repository, type

```python gui.py```
    
The app is very simple.  It has no progress bar and you will not know it's working
until you receive an alert, but you can check the folder of the repository
as you will receive in this order:

1. 'video.mp4'
2. 'audio.mp3'
3. 'transcription.txt'