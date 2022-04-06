from OpenGL.GL import *
import glfw
import math
import numpy

display = None
window = None
resolution = 500

delta = 0.1
angle = 0.0
msh = 0.2
d_x, d_z = 30, 0

rectangle = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0.5, 0.5],
    [0.5, 0.5, 1, 1],
    [1, 1, 1, 0]
]

pixels = [1.0 for i in range(resolution*resolution*3)]


def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(resolution, resolution, "Lab2", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        display()

    glfw.destroy_window(window)
    glfw.terminate()


def key_callback(window, key, scancode, action, mods):
    global angle, delta, dx, dy, dz
    if action == glfw.PRESS:
        if key == glfw.KEY_A:
            angle -= 10
        if key == glfw.KEY_D:
            angle += 10
        if key == glfw.KEY_Q:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        if key == glfw.KEY_E:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def lines():
    global pixels
    for edge in rectangle:
        x0, y0, x1, y1 = edge[0], edge[1], edge[2], edge[3]
        if x0 == x1:
            for i in range(y0, y1+1):
                pixels[i][x0] == 1
        elif y0 == y1:
            for i in range(x0, x1+1):
                pixels[y0][i] == 1
        else:
            pass

pixels2 = [1 for i in range(16)]
def draw():
    # global angle
    # glPushMatrix()
    # glColor3f(1,1,1)
    # glBegin(GL_LINES)
    # for edge in rectangle:
    #     x0,y0,x1,y1 = edge[0]*100, edge[1]*100, edge[2], edge[3]
    #     glVertex2f(x0,y0)
    #     glVertex2f(x1,y1)
    # glEnd()

    glDrawPixels(resolution, resolution, GL_RGB, GL_FLOAT, *pixels)

    # glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    draw()

    glfw.swap_buffers(window)
    glfw.poll_events()


# lines()
main()
