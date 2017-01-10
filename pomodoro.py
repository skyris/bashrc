#!/usr/bin/env python
#!/usr/bin/env python
"""
Pomodoro timer

Created on Sun Sep 11 13:30:00
@author: Victor Klimov
"""
import pygame
import random
import time


tracks = [
('Depeche_Mode_-_Everything_Counts_Reprise_.ogg', .8, 17.25)
]

minutes = .1
seconds = minutes * 60
print "Timer is set: %s" % time.asctime()
time.sleep(seconds)

track = random.choice(tracks)

pygame.init()
song = pygame.mixer.Sound(track[0])
song.set_volume(track[1])
song.play()
time.sleep(track[2])
pygame.quit()
