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
vertexes = [] #[[100,100], [150, 100], [150, 150], [200, 150], [200, 100], [250, 100], [250, 300], [100, 300]]
bg_color = [1, 1, 1]
edge_color = [1, 0, 0]
vertex_color = [0, 0, 1]
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
            vertexes = [[100, 100],[120, 115], [100, 120], [90, 117]]
        elif key == glfw.KEY_3:
            vertexes = [[100,100], [105,104], [100, 110], [95, 107]]
        elif key == glfw.KEY_4:
            vertexes = [[100, 100], [200, 130], [210, 250], [150, 150], [110, 240]] 
        elif key == glfw.KEY_5:
            vertexes = [[100,100], [150, 100], [150, 150], [200, 150], [200, 100], [250, 100], [250, 300], [100, 300]]


def lines():
    global pixels

    pixels = [[[1.0, 1.0, 1.0] for i in range(resx)] for k in range(resy)]
    to_fill = []

    for i, vertex in enumerate(vertexes):
        # print('START DRAWING EDGE')
        x1, y1, x2, y2 = vertex[0], vertex[1], vertexes[(
            i+1) % len(vertexes)][0], vertexes[(i+1) % len(vertexes)][1]
        if x1 == x2: # вертикальные 
            for j in range(min(y1, y2), max(y1,y2)+1):
                pixels[j][x1] = edge_color
                # print('color', x1, j)
                to_fill.append([x1, j])
        elif y1 == y2: # горизонтальные 
            print('YYYYY = ', y1)
            for j in range(min(x1, x2), max(x1, x2)+1):
                pixels[y1][j] = edge_color
                # print('color', j, y1) 
            # to_fill.append([y1, x1])
            # to_fill.append([y1, x1]) 
        else:
            dx = x2 - x1
            dy = y2 - y1
            sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
            sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
            if dx < 0:
                dx = -dx
            if dy < 0:
                dy = -dy
            if dx > dy:
                pdx, pdy = sign_x, 0
                es, el = dy, dx
                flag = False
            else:
                pdx, pdy = 0, sign_y
                es, el = dx, dy
                flag = True
            x, y = x1, y1
            error, t = el/2, 0

            # to_fill.append([x, y])
            # for i in range(x, resx):
            #     if pixels[y][i] == bg_color:
            #         pixels[y][i] = fill_color
            #     elif pixels[y][i] == fill_color:
            #         pixels[y][i] = bg_color
            # pixels[y][x] = edge_color
            # to_fill.append([x, y])
            # print('color', x, y)
            while t < el:
                error -= es
                if error < 0:
                    to_fill.append([x, y])
                    # for i in range(x, resx):
                    #     if pixels[y][i] == bg_color:
                    #         pixels[y][i] = fill_color
                    #     elif pixels[y][i] == fill_color:
                    #         pixels[y][i] = bg_color
                    error += el
                    x += sign_x
                    y += sign_y
                else:
                    if pdy != 0:
                        to_fill.append([x, y])
                        # for i in range(x, resx):
                        #     if pixels[y][i] == bg_color:
                        #         pixels[y][i] = fill_color
                        #     elif pixels[y][i] == fill_color:
                        #         pixels[y][i] = bg_color
                    x += pdx
                    y += pdy 
                t += 1
                pixels[y][x] = edge_color
                # print('color', x, y)
        # print('END DRAWING EDGE')

    # counter = defaultdict(int)
    # for elem in to_fill:
    #     counter[elem[1]] += 1
    # to_check = [k for k in counter.keys() if counter[k]%2 == 1]
    # print(to_check)
    # vertX = []
    # for xy in vertexes:
    #     vertX.append(object)
    # to_fill.sort(key=itemgetter(1))
    # print('\n\n', [[y, [x[0] for x in xys]] for y, xys in groupby(to_fill, key=itemgetter(1))])
    # to_fill = [[y, [x[0] for x in xys]] for y, xys in groupby(to_fill, key=itemgetter(1))]
    # for i, pair in enumerate(to_fill):
    #     if len(pair[1])%2 != 0:

    # print(to_fill)
    edge_num = -1
    # print('\n\n', vertexes)
    for i, xy in enumerate(to_fill):
        x, y = xy[0], xy[1]
        # if xy in vertexes:
        #     edge_num += 1
        #     print('FOUND VERTEX:', x, y)
        #     print('Y dir changes:', (vertexes[(edge_num+1)%len(vertexes)][1] - y) * (y - vertexes[(edge_num-1)%len(vertexes)][1]) < 0)
        #     if (vertexes[(edge_num+1)%len(vertexes)][1] - y) * (y - vertexes[(edge_num-1)%len(vertexes)][1]) < 0:
        #         continue
        if (to_fill[(i+1)%len(to_fill)][1] - y) * (y - to_fill[(i-1)%len(to_fill)][1]) < 0:
            # print('FOUND VERTEX:', x, y)
            continue
        for i in range(x, resx):
            if pixels[y][i] == bg_color:
                pixels[y][i] = fill_color
            elif pixels[y][i] == fill_color:
                pixels[y][i] = bg_color


def draw():
    # global angle
    lines()
    glDrawPixels(resx, resy, GL_RGB, GL_FLOAT, pixels)

    # glPushMatrix()
    # glColor3f(1,0,1)
    # glPointSize(5)
    # glBegin(GL_POINTS)
    # glVertex2f(0,0)
    # glVertex2f(1,1)
    # glVertex2f(1,-1)
    # glVertex2f(-1,1)
    # glVertex2f(-1,-1)
    # glEnd()

    # glColor3f(1,0,0)
    # glBegin(GL_LINES)
    # if len(vertexes) >= 3:
    #     for vertex in vertexes:
    #         print(2*vertex[0]/resx-1, 2*vertex[1]/resy-1)
    #         glVertex2f(vertex[0]/resx-1/2, vertex[1]/resy-0.5)
    # glEnd()
    # glPopMatrix()


def draw_lines_in_pixels():
    global pixels
    for edge in rectangle:
        x0, y0, x1, y1 = edge[0], edge[1], edge[2], edge[3]


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    draw()

    glfw.swap_buffers(window)
    glfw.poll_events()


# lines()
main()
