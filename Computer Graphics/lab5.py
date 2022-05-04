from OpenGL.GL import *
import glfw
import math
import numpy as np
import random

delta = 0
angle1, angle2, angle3 = 10, 10, 10
window = None
display = None
msh = 0.2

ta, tb = 0, 1

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

verticies =np.array([
    [0.5, -0.5, -0.5],
    [0.5, 0.5, -0.5],
    [-0.5, 0.5, -0.5],
    [-0.5, -0.5, -0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, 0.5],
    [-0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5]
])

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

to_cut = np.array([
    [-1, 0, 0.7],
    [1, 0, -0.7]
])

def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(1000, 1000, "Lab2", None, None)
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
    global angle1, angle2, angle3, to_cut
    if action == glfw.PRESS:
        if key == glfw.KEY_A:
            angle1 -= 10
        elif key == glfw.KEY_D:
            angle1 += 10
        elif key == glfw.KEY_W:
            angle2 -= 10
        elif key == glfw.KEY_S:
            angle2 += 10
        elif key == glfw.KEY_Q:
            angle3 -= 10
        elif key == glfw.KEY_E:
            angle3 += 10
        elif key == glfw.KEY_1:
            to_cut = np.array([
                [-1, 0, 0.7],
                [1, 0, -0.7]
            ])
        elif key == glfw.KEY_2:
            to_cut = np.array([
                [0, 0, 0],
                [1, 0, -0.7]
            ])
        elif key == glfw.KEY_3:
            to_cut = np.array([
                [1, 0, -0.7],
                [0, 0, 0]
            ])
        elif key == glfw.KEY_4:
            to_cut = np.array([
                [0.5, 0.5, 1],
                [0.5, 0.5, -1]
            ])
        elif key == glfw.KEY_5:
            to_cut = np.array([
                [0, 0.7, 0],
                [0.7, 0, 0]
            ])



def cube():
    

    glPushMatrix()

    glScalef(msh, msh, msh)
    glRotatef(angle1, 0, 0, 1)
    glRotatef(angle2, 0, 1, 0)
    glRotatef(angle3, 1, 0, 0)

    glColor3fv((1.0, 0.0, 0.0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    glColor3fv((0.0, 1.0, 0.0))
    glBegin(GL_LINES)
    for point in to_cut:
        glVertex3fv(point)
    glEnd()

    glColor3fv((0.0, 0.0, 1.0))
    glBegin(GL_LINES)
    glVertex3fv(to_cut[0] + (to_cut[1] - to_cut[0])*ta)
    glVertex3fv(to_cut[0] + (to_cut[1] - to_cut[0])*tb)
    glEnd()

    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    find_intersection()
    cube()

    glfw.swap_buffers(window)
    glfw.poll_events()


def find_intersection():
    global ta, tb
    ta, tb = 0, 1
    to_cut_vec = to_cut[1] - to_cut[0]
    a = to_cut[0]
    b = to_cut[1]
    for surface_num, surface in enumerate(surfaces):
        d1, d2, d3 = verticies[surface[0]], verticies[surface[1]], verticies[surface[2]]
        v1, v2 = d2-d1, d3-d1 # посчитали направляющие векторы для плоскости
        norm = np.cross(v1, v2) # нашли нормаль

        if norm@to_cut_vec == 0:
            continue

        # найдем вершину многоугольника, не лежащую в плоскости текущей грани
        another_point = d1 
        while np.dot(another_point - d1, norm):
            another_point = random.choice(verticies)

        # повернем норму внутрь
        if np.dot(another_point - d1, norm) < 0:
            norm = -norm

        for t in np.linspace(0, 1, 100):
            cur_coords = a + to_cut_vec*t
            connect = cur_coords - d1
            if abs(np.dot(connect, norm)) < 0.01:
                if norm@(to_cut_vec) > 0:
                    ta = max(ta, t)
                else: 
                    tb = min(tb, t)

main()