import os
import pygame


xmult = (1280 / 8)
ymult = (720 / 5)


def setup(screen, etc) :
    pass


def draw(screen, etc) :
    global xmult, ymult
    
    for i in range(0, 7) :
        xoffset = int(etc.knob1 * xmult)
        yoffset = int(etc.knob2 * ymult)
         
        for j in range(0, 10) :
            x = j * xmult - xmult
            y = i * ymult - ymult
            
            rad = abs(etc.audio_in[j-i] * 0.01)
            width = int(40 + rad)
            color = etc.color_picker()
            if (i%2) == 1 : 
                x = j * xmult - xmult + xoffset
            if (j%2) == 1 : 
                y = i * ymult - ymult + yoffset

            pygame.draw.circle(screen, color, (int(x), int(y)), width, 1) 
            
#TRAILS
    veil = pygame.Surface((1280,720))  
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0)) # (0,0) = starts at top left 
   
    
    