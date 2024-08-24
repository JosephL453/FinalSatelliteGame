import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600




satellites = []
lines = []
next_satellite = 0
start_time = 0
end_time = 0
total_time = 0
satellite_num = 8

def create_satellite():
    global start_time
    for i in range (satellite_num):
        satellite = Actor("satellite.png")
        satellite.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40)
        satellites.append(satellite)
    start_time = time()


def draw():
    global start_time
    global total_time
    screen.blit("starbackground.png", (0,0))
    number = 1
    for i in satellites:
        i.draw()
        screen.draw.text(str(number), (i.pos[0], i.pos[1] + 20), fontsize = 25, color = "white")
        number += 1
    
    for i in lines:
        screen.draw.line(i[0],i[1], (255,255,255))
    
    if next_satellite < 8:
        total_time = time() - start_time
        screen.draw.text(total_time, (10,10), fontsize = 30, color = "White")
    else:
        screen.draw.text(total_time, (10,10), fontsize = 30, color = "White")



def update():
    pass

def on_mouse_down(pos):
    global next_satellite, lines
    if satellites[next_satellite].collidepoint(pos):
        if next_satellite:
            lines.append((satellites[next_satellite - 1].pos, satellites[next_satellite].pos))
        next_satellite += 1
    else: 
        lines = []
        next_satellite = 0




create_satellite()
pgzrun.go()
