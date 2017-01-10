#!/usr/bin/env python
#!/usr/bin/env python
"""
Pomodoro timer

Created on Sun Sep 11 13:30:00
@author: Victor Klimov
"""
import notify2
import pygame
import random
import time


tracks = [
('Depeche_Mode_-_Everything_Counts_Reprise_.ogg', .8, 17.25)
]

minutes = 25.0
seconds = minutes * 60
print "Timer is set: %s" % time.asctime()
time.sleep(seconds)

track = random.choice(tracks)

notify2.init("markup")
n = notify2.Notification("Rest",
  '''
  <b>Take a rest dear <i>Victor</i>!</b>
  '''
)

pygame.init()
song = pygame.mixer.Sound(track[0])
song.set_volume(track[1])
song.play()
n.show()

time.sleep(track[2])
pygame.quit()




