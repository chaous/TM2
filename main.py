import pygame
import pygame.gfxdraw as gfx
import sympy as sp
from sympy.abc import v, t
from math import cos, sin, pi, asin
import numpy as np

WIDTH, HEIGHT = 1000, 900
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Second lab")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (30, 255, 30)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
FPS = 60


gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))


def point_on_circle(center, angle, radius):
    '''
        Finding the x,y coordinates on circle, based on given angle
    '''

    #center of circle, angle in degree and radius of circle
    #center = [0,0]
    #angle = pi / 2
    #radius = 100
    x = center[0] + (radius * cos(angle))
    y = center[1] + (radius * sin(angle))

    return x,y



def draw_box(x, y, size, t):
    try:
        x = int(x)
    except OverflowError:
        print(x)

    lines = [[x, y], [x, y + size], [x + size, y + size], [x + size, y]]
    pygame.draw.lines(WIN, GREEN, False, lines, 2)
    #pygame.draw.arc(WIN, GREEN, (x, y - size / 5, x + size, y - size / 5), 3.14, 0, 4)
    gfx.arc(WIN, (x + x + size) // 2, (y + y) // 2 , size // 2, 0, 180, RED)
    t = asin(sin(t)) + pi / 2
    weel_loc_x, weel_loc_y = point_on_circle([(x + x + size) // 2, (y + y) // 2 ], t, size // 2)
    pygame.draw.circle(WIN, MAGENTA, [weel_loc_x, weel_loc_y], 50, 3)
    pygame.draw.line(WIN, CYAN, [weel_loc_x, weel_loc_y], [(x + x + size) // 2, (y + y) // 2], 5)


def draw(background, t, cordinates, counter):
    gameDisplay.blit(background, (0, 0))
    draw_box(cordinates[counter], 370, 500, t)
    pygame.display.update()





def main():
    background = pygame.image.load('background.png')
    run = True
    clock = pygame.time.Clock()
    t_from_t = sp.simplify(input("equation for angle changing (variable t)"))
    plot1 = sp.plot(t_from_t, show=False)
    plot2 = sp.plot(sp.diff(t_from_t, t), show=False)
    t_from_t = np.vectorize(sp.lambdify(t, t_from_t))
    time = t_from_t(np.linspace(1, 500, 2000)) / 10
    counter = 0
    r_from_t = sp.simplify(input("equation for speed_x (varible v)"))
    plot3 = sp.plot(r_from_t, show=False)
    plot4 = sp.plot(sp.diff(r_from_t, t), show=False)
    r_from_t = np.vectorize(sp.lambdify(v, r_from_t))
    cordinates = np.linspace(1, 500, 1000)
    cordinates2 = np.linspace(500, 1, 1000)
    cordinates = r_from_t(np.concatenate((cordinates, cordinates2)))
    #print(cordinates)
    plot1.save("velocity_t.png")
    plot2.save("acceleration_t.png")
    plot3.save("velocity_x.png")
    plot4.save("acceleration_x.png")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(background, time[counter], cordinates, counter)
        clock.tick(60)
        #time += 0.04
        counter += 1
        if counter >= 2000:
            counter = 0



if __name__ == '__main__':
    main()
