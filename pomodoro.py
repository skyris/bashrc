#!/usr/bin/env python
"""
Pomodoro timer

Created on Sun Sep 11 13:30:00
@author: Victor Klimov
"""
import sys
import time
import pygame
# try:
#     minutes = float(sys.argv[1])
# except:
minutes = 10.0
seconds = minutes * 60
print "Timer is set: %s" % time.asctime()
# start = time.time()
time.sleep(seconds)
pygame.init()
# print(pygame.mixer_music.get_volume())
pygame.mixer_music.load("/opt/my_pomodoro/ingame_07.ogg")  # "/usr/share/gnome-pomodoro/sounds/birds.ogg"
pygame.mixer_music.set_volume(0.5)
pygame.mixer_music.play()
# print "Take a rest, dear Victor ;)"
# time.sleep(60)
time.sleep(11.155)
