from __future__ import unicode_literals
import youtube_dl
m4a = '140'  # audio only
mp4_144p = '160'
mp4_240p = '133'
mp4_360p = '134'
mp4_480p = '135'
mp4_720p = '136'
mp4_1080p = '137'
gp3_176_144 = '17'  # 3gp: 176*144
gp3_320_240 = '36'
flv = '5'
webm = '43'
mp4_640_360 = '18'  # 640 * 360
mp4_1280_720 = '22'
ydl_opts = {
    'postprocessors': [{
        'preferredcodec': 'mp4',
    }],
}
url = input('url: ')
format = int(input("""Choose file type:
[1]  m4a audio only
[2]  flv
[3]  webm
[4]  gp3 176x144
[5]  gp3 320x240
[6]  mp4 144p
[7]  mp4 240p
[8]  mp4 360p
[9]  mp4 480p
[10] mp4 720p
[11] mp4 1080p
[12] mp4 640x360
[13] mp4 1280x720
[14] mp3
choice: """))
formats = ['',m4a,flv,webm,gp3_176_144,gp3_320_240,mp4_144p,mp4_240p,mp4_360p,mp4_480p,mp4_720p,mp4_1080p,mp4_640_360,mp4_1280_720]
if format == 14:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
else:
    format = formats[format]
    with youtube_dl.YoutubeDL({'format':format}) as ydl:
        ydl.download([url])
