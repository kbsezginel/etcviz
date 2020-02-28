"""
One line rotation and fade.
* Use with Auto Clear Toggle OFF

Knob 1: Rotation speed # BPM????
Knob 2: Radius
Knob 3: Alpha
"""
import pygame
import random
import math

count = 0
thick = 3

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count, thick
    speed = etc.knob1*20
    count = int(count + speed)
    color = etc.color_picker()
    
    peak = 0
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
        
    R = 4 * etc.knob2 * peak / 128
    x = R * math.cos((count /  1000.) * 6.28) + 640
    y = R * math.sin((count /  1000.) * 6.28) + 360
    pygame.draw.line(screen, color, [640, 360], [x, y], thick)
   
   
#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 150)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
   

