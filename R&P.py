import random, vlc, os

path = 'D:/MP3random'  #<<Insert you Directory here
make_selection = random.choice(os.listdir(path))
#print(make_selection)
selection_path= f'{path}/{make_selection}'
#print(selection_path)
plyr = vlc.MediaPlayer(selection_path)
plyr.play()
while True:
    pass