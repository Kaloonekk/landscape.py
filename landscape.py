
import pygame
import time

pygame.init()

WIDTH = 660
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200
cloudX = 100
cloudY = 100
sunX = 0
sunY = 0
cloudMoving = True
moonX = 900
moonY = 0
r=135
g=206
b=235
ticks = 0
zOffset = 0
tickMultiples = 0
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Pausing the Sun, Moon and Clouds
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if cloudMoving == True:
               cloudMoving = False
            else:
               cloudMoving = True

#The Backround
    r = 135 - sunY/4
    g = 206 - sunY/3
    b = 255 - sunY/2

    if r<0:
        r=0
    if g<0:
        g=0
    if b<0:
        b=0
    screen.fill((r, g, b))  # always the first drawing command

#The Sun
    pygame.draw.circle(screen, (245,239,71), (sunX, sunY), 40)
#The Moon
    pygame.draw.circle(screen, (245,245,245), (moonX, moonY), 40)
    pygame.draw.circle(screen, (212,212,212), (moonX+12, moonY+12), 15)
    pygame.draw.circle(screen, (212,212,212), (moonX-12, moonY-12), 10)

#The clouds
    pygame.draw.circle(screen, (245, 245, 245), (cloudX - 50, 85), 35)
    pygame.draw.circle(screen, (245, 245, 245), (cloudX - 26, 43), 30)
    pygame.draw.circle(screen, (245, 245, 245), (cloudX + 15, 71), 35)

    pygame.draw.circle(screen, (255, 255, 255), (cloudY - 50, 115), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloudY - 26, 83), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloudY + 15, 101), 35)

#The Ground
    pygame.draw.rect(screen, (120, 191,69), pygame.Rect(0, 380, 660, 100))      

#The Dog house
    pygame.draw.rect(screen, (199, 26, 26), pygame.Rect(280, 260, 140, 120))
    pygame.draw.polygon(screen, (79, 59, 39), ((280, 260), (420,260), (350, 180)))
    pygame.draw.circle(screen, (33,33,33), (350, 300), 25)
    pygame.draw.rect(screen, (33,33,33), pygame.Rect(325, 300, 50, 80))
    pygame.draw.circle(screen, (153,124,81), (350, 230), 20)
    pygame.draw.circle(screen, (184,170,130), (350, 235), 9)
    pygame.draw.circle(screen, (184,170,130), (350, 220), 5)
    pygame.draw.circle(screen, (184,170,130), (360, 225), 5)
    pygame.draw.circle(screen, (184,170,130), (340, 225), 5)

#The Tree
    pygame.draw.rect(screen, (112, 87, 39), pygame.Rect(70, 200 , 70, 180))
    pygame.draw.circle(screen, (49, 91, 31), (60, 180), 45)
    pygame.draw.circle(screen, (49, 91, 31), (100, 150), 50)
    pygame.draw.circle(screen, (49, 91, 31), (140, 180), 45)

#The Dog
    pygame.draw.circle(screen, (122,99,72), (448, 363), 30)
    pygame.draw.ellipse(screen, (122,99,72), (465, 351, 130, 65), 60)
    pygame.draw.circle(screen, (122,99,72), (422, 355), 12)
    pygame.draw.circle(screen, (122,99,72), (462, 340), 12)
    pygame.draw.rect(screen, (5, 5, 5), pygame.Rect(428, 354, 12, 4))
    pygame.draw.rect(screen, (5, 5, 5), pygame.Rect(448, 354, 12, 4))
    pygame.draw.ellipse(screen, (5,5,5), (436, 361, 20, 10), 10)
    pygame.draw.rect(screen, (5, 5, 5), pygame.Rect(441, 376, 24, 4))
    pygame.draw.circle(screen, (212,102,136), (459, 383), 4)
    pygame.draw.rect(screen, (212, 102, 136), pygame.Rect(454, 379, 8, 6))
    pygame.draw.rect(screen, (122, 99, 72), pygame.Rect(440, 393, 175, 8))
    pygame.draw.rect(screen, (122, 99, 72), pygame.Rect(455, 405, 175, 8))
    pygame.draw.aalines(screen, (122,99,72), False, [(592,383), (619,386), (631,395)])
    pygame.draw.aalines(screen, (122,99,72), False, [(592,382), (619,385), (631,394)])
    pygame.draw.aalines(screen, (122,99,72), False, [(592,381), (619,384), (631,393)])
    pygame.draw.aalines(screen, (122,99,72), False, [(592,380), (619,383), (631,392)])
    pygame.draw.aalines(screen, (122,99,72), False, [(592,379), (619,382), (631,391)])
    pygame.draw.aalines(screen, (122,99,72), False, [(592,378), (619,381), (631,390)])

#Snore
   # Snore1 = pygame.draw.aalines(screen, (5,5,5), False, [(448,288), (475,282), (450,318),(478,307)])
   # Snore2 = pygame.draw.aalines(screen, (5,5,5), False, [(480,225), (511,227), (483,257),(505,257)])
   # Snore3 = pygame.draw.aalines(screen, (5,5,5), False, [(531,179), (556,180), (525,205),(548,206)])

#The Fence
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(0, 420, 640, 20)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(0, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(40, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(80, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(120, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(160, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(200, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(240, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(280, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(320, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(360, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(400, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(440, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(480, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(520, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(560, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(600, 400, 20, 100)) 
    pygame.draw.rect(screen, (255, 255,255), pygame.Rect(640, 400, 20, 100)) 

    snores = ticks // 5 % 4
    for x in range(snores):
        if ticks >= snores and cloudMoving == True:
            pygame.draw.aalines(screen, (5,5,5), False, [(448+zOffset,288-zOffset), (475+zOffset,282-zOffset), (450+zOffset,318-zOffset),(478+zOffset,307-zOffset)])
        zOffset+=40
    zOffset=0 

    ticks += 1
#Cloud and Sun movement
    if cloudMoving == True:
        cloudX+=3
        cloudY+=4
        sunX +=3.5
        f=sunX - 300
        sunY = 1/900*f*f
        moonX +=3.5
        f=moonX - 300
        moonY = 1/900*f*f


#Repositioning the Cloud, Sun and Moon
    if cloudX > 750:
        cloudX = -100
    if cloudY > 750:
        cloudY = -100
    if sunX > 1200:
        sunX = -600
    if sunY > 700:
        suny = -30
    if moonX > 1200:
        moonX = -600
    if moonY > 700:
        moony = -30



    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)

    #---------------------------