from pytube import YouTube
import youtube_dl
from moviepy.editor import AudioFileClip
from pydub import AudioSegment
import sys
import os

def download_mp3_from_youtube(url, outputdir, fname=None):
    yt = YouTube(url) 
    stream = yt.streams.filter(only_audio=True).first()
    f = stream.download()
    if fname is None: 
        fname = f.split('/')[-1][:-4]
    audio = AudioFileClip(f)
    # Extract audio from video
    audio.write_audiofile(outputdir + fname + '.mp3')
    os.remove(f)

def crop_mp3(path, start_time, end_time, newpath=None):
    start_time = start_time * 1000 # convert to ms
    end_time = end_time * 1000
    audio = AudioSegment.from_mp3(path)
    
    cropped_audio = audio[start_time:end_time]

    if newpath is None: 
        newpath = path
    cropped_audio.export(newpath, format="mp3")

download_mp3_from_youtube("https://www.youtube.com/watch?v=Pb-K2tXWK4w","./")

'''video_url = 


# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first() 
print(stream)
# download into working directory
stream.download()'''

# Load the mp4 file


sys.exit()

video_url = "https://www.youtube.com/watch?v=Pb-K2tXWK4w"
video = YouTube(video_url)
filename = video.streams.get_audio_only().download()
clip = AudioFileClip(filename)
clip.write_audiofile(filename[:-4] + ".mp3")
clip.close()

sys.exit(0)




ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

'''
selected_video = YouTube(video_url)

print(selected_video.streams.filter(only_audio=True))

audio = selected_video.streams.filter(only_audio=True, file_extension='mp4').first()
audio.download()'''