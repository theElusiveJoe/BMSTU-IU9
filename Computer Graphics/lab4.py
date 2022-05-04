from OpenGL.GL import *
import glfw
import math
import numpy
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

display = None
window = None
resx, resy = 500, 500

delta = 0.1
angle = 0.0
msh = 0.2
d_x, d_z = 30, 0


# vertexes = [[50, 50], [490, 300], [100, 400]]
# vertexes = [[100, 100],[120, 115], [100, 120], [90, 117]]
# vertexes = [[100,100], [105,104], [100, 110], [95, 107]]
# vertexes = [[100, 100], [200, 130], [210, 250], [150, 150], [110, 240]]
# vertexes = [[100,100], [150, 100], [150, 150], [200, 150], [200, 100], [250, 100], [250, 300], [100, 300]]
vertexes = []
bg_color = [1, 1, 1]
edge_color = [0, 0, 0]
fill_color = [0, 1, 0]

pixels = [[bg_color for i in range(resx)] for k in range(resy)]


def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(resx, resy, "Lab2", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, mouse_callback)
    while not glfw.window_should_close(window):
        display()

    glfw.destroy_window(window)
    glfw.terminate()


def mouse_callback(window, button, action, mods):
    global vertexes
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        x, y = glfw.get_cursor_pos(window)
        y = 1080 - y
        print(x, y)
        vertexes.append([int(x), int(y)])


def key_callback(window, key, scancode, action, mods):
    global vertexes
    if action == glfw.PRESS:
        if key == glfw.KEY_0:
            vertexes = []
        elif key == glfw.KEY_1:
            vertexes = [[50, 50], [490, 300], [100, 400]]
        elif key == glfw.KEY_2:
            vertexes = [[100, 100], [120, 115], [100, 120], [90, 117]]
        elif key == glfw.KEY_3:
            vertexes = [[100, 100], [105, 104], [100, 110], [95, 107]]
        elif key == glfw.KEY_4:
            vertexes = [[100, 100], [200, 130], [
                210, 250], [150, 150], [110, 240]]
        elif key == glfw.KEY_5:
            vertexes = [[100, 100], [150, 100], [150, 150], [200, 150], [
                200, 100], [250, 100], [250, 300], [100, 300], [120, 250], [120, 150]]
        elif key == glfw.KEY_W:
            print('W')
            if resy <= 550:
                print('inc')
                resize(resx, resy+50)
        elif key == glfw.KEY_S:
            if resy >= 150:
                resize(resx, resy-50)
        elif key == glfw.KEY_D:
            if resx <= 750:
                resize(resx+50, resy)
        elif key == glfw.KEY_A:
            if resx >= 250:
                resize(resx-50, resy)

def lines():
    global pixels

    pixels = [[[1.0, 1.0, 1.0] for i in range(resx)] for k in range(resy)]
    to_fill = []

    for i, vertex in enumerate(vertexes[:]):
        # print('START DRAWING EDGE')
        x1, y1, x2, y2 = vertex[0], vertex[1], vertexes[(
            i+1) % len(vertexes)][0], vertexes[(i+1) % len(vertexes)][1]
        if x1 == x2:  # вертикальные
            for j in range(min(y1, y2), max(y1, y2)+2):
                pixels[j][x1] = edge_color
                if 255 > j > 245:
                    print((x1, j), 'appended')
                to_fill.append([x1, j])
        elif y1 == y2:  # горизонтальные
            for j in range(min(x1, x2), max(x1, x2)+1):
                pixels[y1][j] = edge_color
        else:
            dx = x2 - x1
            dy = y2 - y1
            sign_x = 1 if dx > 0 else -1
            sign_y = 1 if dy > 0 else -1
            dx = abs(dx)
            dy = abs(dy)
            if dx > dy: # если тангенс меньше 1
                pdx, pdy = sign_x, 0 # сдвигаемся по x
                es, el = dy, dx
            else:
                pdx, pdy = 0, sign_y
                es, el = dx, dy

            x, y = x1, y1
            error = el/2

            tg = dy/dx
            if tg > 1: tg = 1/tg
            t = 0
            while t < el:
                error -= es
                if error < 0:
                    to_fill.append([x, y])
                    if 255 > y > 245:
                        print((x, y), 'appended')
                    error += el
                    x += sign_x
                    y += sign_y
                else:
                    if pdy != 0:
                        to_fill.append([x, y])
                        if 255 > y > 245:
                            print((x, y), 'appended')
                    x += pdx
                    y += pdy
                t += 1
                color = (1 - error/el - tg/2)
                pixels[y][x] = [color, color, color]
    
    edge_num = -1
    for i, xy in enumerate(to_fill):
        x, y = xy[0], xy[1]
        if (to_fill[(i+1) % len(to_fill)][1] - y) * (y - to_fill[(i-1) % len(to_fill)][1]) < 0:
            continue
        for i in range(x, resx):
            if pixels[y][i] == bg_color:
                pixels[y][i] = fill_color
            elif pixels[y][i] == fill_color:
                pixels[y][i] = bg_color


def draw():
    lines()
    glDrawPixels(resx, resy, GL_RGB, GL_FLOAT, pixels)


def resize(newx, newy):
    global resx, resy, vertexlist, pixels
    kx, ky = newx/resx, newy/resy
    print(kx, ky)
    for i, _ in enumerate(vertexes):
        vertexes[i][0], vertexes[i][1] = int(vertexes[i][0]*kx), int(vertexes[i][1]*ky) 
    
    pixels = [[bg_color for i in range(newx)] for k in range(newy)]
    resx, resy = newx, newy



def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    draw()

    glfw.swap_buffers(window)
    glfw.poll_events()


# lines()
main()
