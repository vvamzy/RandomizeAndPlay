import random, vlc, os, time, pathlib

path = 'D:/MP3random'
sourse = random.choice(os.listdir(path))
print(sourse)
abs_sourse= f'{path}/{sourse}'
print(abs_sourse)
plyr = vlc.MediaPlayer(abs_sourse)
plyr.play()
while True:
    pass