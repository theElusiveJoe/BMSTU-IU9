# govnokod by E-Matveev©
import random
import time
from OpenGL.GL import *
import glfw
import numpy as np
from scipy.spatial.transform import Rotation as R


window = None

quad_strip_levels = None

turn = 0

flag_spin = True
flag_textured = True
flag_move = True
flag_ranom = False

sphere_cut_a = 10
sphere_cut_b = 10
cur_pos = np.array([0.5, 0.5, 0.5])
move_direction = [-0.4, 0.5, 0.7] / np.linalg.norm([1, -1, 0.7])

start = 0


def cmp_surfaces(s1):
    return min(list([quad_strip_levels[v][0] ** 2 + quad_strip_levels[v][1] ** 2 + (quad_strip_levels[v][2] - 10) ** 2 for v in s1]))


def turn_sphere(fi):
    r1 = R.from_rotvec([0, fi, 0])
    r2 = R.from_rotvec([0.3, 0, 0])
    return np.matmul(np.matmul(quad_strip_levels, r1.as_matrix()), r2.as_matrix())


#MAIN
def main():
    global window, start

    if not glfw.init():
        return

    window = glfw.create_window(700, 700, "lab", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    init_display_list_2()
    glCallList(2)

    glEnableClientState(GL_VERTEX_ARRAY)
    init_display_list_1()
    
    start = time.monotonic()
    for _ in range(200):
    # while not glfw.window_should_close(window):
        display()

    glfw.destroy_window(window)
    glfw.terminate()


#DISPLAY
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # масштабируем для нашлядности
    glScalef(0.2, 0.2, 0.2)

    # тут считаем движение и вызываем дисплейный список
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
        if cur_pos[0]**2 + cur_pos[1]**2 + cur_pos[2]**2 >= 10:
            b = cur_pos
            a = cur_pos-move_direction
            t_vec = cur_pos/np.linalg.norm(cur_pos)
            fi = np.arccos(np.clip(np.dot(-t_vec, -move_direction), -1.0, 1.0))
            len_t = np.linalg.norm(move_direction) * np.cos(fi)
            d = cur_pos - t_vec*len_t
            move_direction = a - b + 2*(d-a)
            move_direction = move_direction / np.linalg.norm(move_direction)

    # двигаем
    glTranslatef(*cur_pos)

    # вызываем display-list
    glCallList(1)

    glPopMatrix()


#GEN
def gen_sphere():
    global quad_strip_levels, def_colors


    half_circle = np.array([[np.sin(tao), np.cos(tao), 0]
                           for tao in np.linspace(0, np.pi, sphere_cut_a)])

    half_circles = [] # список списков точек на полуокружностях без повторений
    for fi in np.linspace(0, 2 * np.pi, sphere_cut_b, endpoint=False):
        # матрица поворота
        rot_mat = R.from_rotvec([0,fi,0]).as_matrix()
        half_circles.append( np.matmul(rot_mat, half_circle.T).T.tolist())
    
    quad_strip_levels = [[] for _ in range(sphere_cut_a-1)]
    for i, half_circle in enumerate(half_circles):
        for qs_level, top_left in enumerate(half_circle[:-1]):
            quad_strip_levels[qs_level].append(top_left)
            quad_strip_levels[qs_level].append(half_circle[qs_level+1])

    for i, qs_level in enumerate(quad_strip_levels):
        quad_strip_levels[i] = qs_level + qs_level[:2] 
    
#INIT_LISTS
def init_display_list_1():
    glNewList(1, GL_COMPILE)

    # рисуем
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1, 0, 1, 1])
    

    for qs in quad_strip_levels:
         # добавляем в список вершин то, что нагенерировали
        glVertexPointer(3, GL_FLOAT, 0, qs)
        glDrawArrays(GL_QUAD_STRIP, 0, len(qs))

    glEndList()


def init_display_list_2():
    # список для света
    glNewList(2, GL_COMPILE)
    glEnable(GL_LIGHTING)

    glDisable(GL_NORMALIZE)

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
start = time.monotonic()
main()
stop = time.monotonic()
print('fast:', stop-start)