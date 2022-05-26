import random

from OpenGL.GL import *
import glfw
import numpy as np
from scipy.spatial.transform import Rotation as R

window = None

surfaces = None

def_verticies = None
cur_verticies = None

turn = 0

flag_spin = True
flag_textured = True
flag_move = True
flag_ranom = False

sphere_cut_a = 10
sphere_cut_b = 10
cur_pos = np.array([0.5, 0.5, 0.5])
move_direction = [-0.4, 1, 1] / np.linalg.norm([-0.4, 1, 1])


def set_light():
    glEnable(GL_LIGHTING)
    # нулевой светит белым диффузным
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 0, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])

    # параметры глобальной модели
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.7, 0.7, 0.7, 1])
    glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, [1, 0, 0])
    glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, 0)


def key_callback(window, key, scancode, action, mods):
    global flag_spin, flag_textured, flag_ranom, flag_move
    if action == glfw.PRESS:
        if key == glfw.KEY_S:
            flag_spin = not flag_spin
        elif key == glfw.KEY_T:
            flag_textured = not flag_textured
        elif key == glfw.KEY_M:
            flag_move = not flag_move
        elif key == glfw.KEY_R:
            flag_random = not flag_ranom
        elif key == glfw.KEY_Z:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        elif key == glfw.KEY_C:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def cmp_surfaces(s1):
    return min(list([def_verticies[v][0] ** 2 + def_verticies[v][1] ** 2 + (def_verticies[v][2] - 10) ** 2 for v in s1]))


def gen_diffuse(surface):
    x, y, z = def_verticies[surface[0]]
    red = z/2+0.5
    green = x/2+0.5
    blue = y/2+0.5
    return [red, green, blue, np.sqrt(x**2+y**2)]


def turn_sphere(fi):
    r1 = R.from_rotvec([0, fi, 0])
    r2 = R.from_rotvec([0.3, 0, 0])
    return np.matmul(np.matmul(def_verticies, r1.as_matrix()), r2.as_matrix())


#MAIN
def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(700, 700, "lab", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    # init_display_lists()
    glEnable(GL_LIGHTING)
    # нулевой светит белым диффузным
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 0, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])

    # параметры глобальной модели
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.7, 0.7, 0.7, 1])
    glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, [1, 0, 0])
    glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, 0)

    glEnableClientState(GL_VERTEX_ARRAY)

    while not glfw.window_should_close(window):
        display()

    glfw.destroy_window(window)
    glfw.terminate()


#DISPLAY
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glVertexPointer(3, GL_FLOAT, 0, def_verticies)
    init_display_lists()

    # тест vertexlist
    # glVertexPointer(2, GL_FLOAT, 0, [0,0,0,1,1,10,1,0])
    # glPushMatrix()
    # glEnableClientState(GL_VERTEX_ARRAY)
    # glDrawArrays(GL_QUADS, 0, 4)
    # glPopMatrix()

    # масштабируем для нашлядности
    glScalef(0.2, 0.2, 0.2)

    draw_sphere()

    glfw.swap_buffers(window)
    glfw.poll_events()


#DRAW
def draw_sphere():
    global turn, cur_verticies, cur_pos, move_direction

    glPushMatrix()

    # придаем движение
    if flag_move:
        cur_pos += move_direction/10
        # print(cur_pos, move_direction)
        if cur_pos[0]**2 + cur_pos[1]**2 + cur_pos[2]**2 >= 10:
            b = cur_pos
            a = cur_pos-move_direction
            t_vec = cur_pos/np.linalg.norm(cur_pos)
            fi = np.arccos(np.clip(np.dot(-t_vec, -move_direction), -1.0, 1.0))
            len_t = np.linalg.norm(move_direction) * np.cos(fi)
            d = cur_pos - t_vec*len_t
            move_direction = a - b + 2*(d-a)
            # if flag_ranom:
            # move_direction += np.array([random.uniform(0, 0.05) for _ in range(3)])
            move_direction = move_direction / np.linalg.norm(move_direction)


    # двигаем
    glTranslatef(*cur_pos)

    # вызываем display-list
    glCallList(1)

    glPopMatrix()


#GEN
def gen_sphere():
    global def_verticies, surfaces
    r = 1

    def_verticies = []

    # полуокружность
    circle = np.array([[np.sin(tao), np.cos(tao), 0]
                       for tao in np.linspace(0, np.pi, sphere_cut_a)])
    for fi in np.linspace(0, 2 * np.pi, sphere_cut_b):
        # матрица поворота
        turn = np.array([np.cos(fi), 0, np.sin(fi),
                         0, 1, 0,
                         -np.sin(fi), 0, np.cos(fi)]).reshape(3, 3)
        def_verticies.extend((np.matmul(turn, circle.T).T.round(5).tolist()))

    print(np.linspace(0, 2 * np.pi, sphere_cut_b))

    surfaces = []
    for circle_i in range(sphere_cut_a-1):
        for point_i in range(sphere_cut_b-1):
            surfaces.append([
                sphere_cut_a*circle_i + point_i,
                sphere_cut_a*circle_i + ((point_i+1) % len(circle)),
                sphere_cut_a*((circle_i+1) % len(circle)) +
                ((point_i+1) % len(circle)),
                sphere_cut_a*((circle_i+1) % len(circle)) + point_i
            ])

    newarr = []
    for x, surface in enumerate(sorted(surfaces, key=lambda x: cmp_surfaces(x))):
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 0, 0] + [1])
        # print('ADDING POLYGON #', x)
        if flag_textured:
            glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, gen_diffuse(surface))
        for i, vertex in enumerate(surface):
            v = list(def_verticies[vertex])
            for x in v:
                # print('appending', x)
                newarr.append(x)
    
    def_verticies = newarr


#INIT_LISTS
def init_display_lists():
    global turn, cur_verticies, cur_pos, move_direction
    glNewList(1, GL_COMPILE)

    # рисуем
    if not flag_textured:
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0, 0, 0, 0])

    # glBegin(GL_QUADS)
    # for x, surface in  enumerate(sorted(surfaces, key = lambda x: cmp_surfaces(x))):
    #     glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,0,0] + [1])
    #     if flag_textured : glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, gen_diffuse(surface))
    #     for i, vertex in enumerate(surface):
    #         v = list(def_verticies[vertex])
    #         glVertex3fv(v)
    # glEnd()
    
    glDrawArrays(GL_QUADS, 0, len(def_verticies))

    glEndList()

    # список для света
    glNewList(2, GL_COMPILE)
    glEnable(GL_LIGHTING)
    # нулевой светит белым диффузным
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 0, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    # параметры глобальной модели
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.7, 0.7, 0.7, 1])
    glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, [1, 0, 0])
    glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, 0)
    glEndList()


gen_sphere()
init_display_lists()
main()
