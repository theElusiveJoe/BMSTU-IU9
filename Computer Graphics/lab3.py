from OpenGL.GL import *
import glfw
import math
import numpy as np

delta = 0.1
angle = 0.0
window = None
display = None
msh = 0.2
ppl = 0

points = []
circles = []

angle1, angle2, angle3 = 0, 0, 0


def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(400, 400, "Lab2", None, None)
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
    global angle1, angle2, angle3, delta, dx, dy, dz
    if action == glfw.PRESS:
        if key == glfw.KEY_A:
            angle1 -= 10
        if key == glfw.KEY_D:
            angle1 += 10
        if key == glfw.KEY_W:
            angle2 -= 10
        if key == glfw.KEY_S:
            angle2 += 10
        if key == glfw.KEY_Q:
            angle3 -= 10
        if key == glfw.KEY_E:
            angle3 += 10
        if key == glfw.KEY_Z:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        if key == glfw.KEY_C:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def gen_sphere():
    global points, ppl, circles
    r = 1

    circles = []
    # полуокружность
    circle = np.array([[math.sin(tao), math.cos(tao), 0]
                       for tao in np.linspace(0, math.pi, 30)])
    for fi in np.linspace(0, 2*math.pi, 30):
        # матрица поворота
        turn = np.array([np.cos(fi), 0, np.sin(fi),
                        0, 1, 0,
                        -np.sin(fi), 0, np.cos(fi)]).reshape(3, 3)
        circles.append(np.matmul(turn, circle.T).T.round(3))


def sphere():
    global circles
    glPushMatrix()
    glRotatef(angle1, 0, 0, 1)
    glRotatef(angle2, 0, 1, 0)
    glRotatef(angle3, 1, 0, 0)

    glBegin(GL_QUADS)
    for circle_i, circle in enumerate(circles[:-1]):
        for point_i, point in enumerate(circle[:-1]):
            if circle_i % 2 == 0:
                glColor3f(1, 0, 0)
            else:
                glColor3f(0, 1, 0)
            glVertex3f(*(circles[circle_i][point_i]))
            glVertex3f(*(circles[circle_i][(point_i+1) % len(circle)]))
            glVertex3f(*(circles[(circle_i+1) % len(circle)]
                       [(point_i+1) % len(circle)]))
            glVertex3f(*(circles[(circle_i+1) % len(circle)][point_i]))
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    for circle_i, circle in enumerate(circles[:-1]):
        for point_i, point in enumerate(circle[:]):
            glVertex3f(*(circles[circle_i][point_i]))
            glVertex3f(*(circles[circle_i][(point_i+1) % len(circle)]))
            glVertex3f(*(circles[circle_i][(point_i+1) % len(circle)]))
            glVertex3f(*(circles[(circle_i+1) % len(circle)]
                       [(point_i+1) % len(circle)]))
            glVertex3f(*(circles[(circle_i+1) % len(circle)]
                       [(point_i+1) % len(circle)]))
            glVertex3f(*(circles[(circle_i+1) % len(circle)][point_i]))
            glVertex3f(*(circles[circle_i][point_i]))
            glVertex3f(*(circles[(circle_i+1) % len(circle)][point_i]))
    glEnd()
    glPopMatrix()


def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    sphere()

    glfw.swap_buffers(window)
    glfw.poll_events()


gen_sphere()
main()
