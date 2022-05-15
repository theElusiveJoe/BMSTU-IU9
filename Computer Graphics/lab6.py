from OpenGL.GL import *
import glfw
import numpy as np
from scipy.spatial.transform import Rotation as R

window = None

colors = [
    [1, 1, 1],
    [0, 1, 0.2],
    [0.2, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

surfaces = [
    [0, 1, 2, 3],
    [3, 2, 7, 6],
    [6, 7, 5, 4],
    [4, 5, 1, 0],
    [1, 5, 7, 2],
    [4, 0, 3, 6]
]

def_verticies = np.array([
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
])
cur_verticies = np.zeros_like((8,3))

turn = 0

# edges = (
#     (0, 1),
#     (0, 3),
#     (0, 4),
#     (2, 1),
#     (2, 3),
#     (2, 7),
#     (6, 3),
#     (6, 4),
#     (6, 7),
#     (5, 1),
#     (5, 4),
#     (5, 7)
# )


def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(400, 400, "lab", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    # glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        display()

    glfw.destroy_window(window)
    glfw.terminate()


# def key_callback(window, key, scancode, action, mods):
#     global angle1, angle2, angle3, delta, dx, dy, dz
#     if action == glfw.PRESS:
#         if key == glfw.KEY_A:
#             angle1 -= 10
#         if key == glfw.KEY_D:
#             angle1 += 10
#         if key == glfw.KEY_W:
#             angle2 -= 10
#         if key == glfw.KEY_S:
#             angle2 += 10
#         if key == glfw.KEY_Q:
#             angle3 -= 10
#         if key == glfw.KEY_E:
#             angle3 += 10
#         if key == glfw.KEY_Z:
#             glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
#         if key == glfw.KEY_C:
#             glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def cmp_surfaces(s1):
    return min(list([cur_verticies[v][0] ** 2 + cur_verticies[v][1] ** 2 + (cur_verticies[v][2] - 10) ** 2 for v in s1]))


def draw_cube():
    global turn, cur_verticies

    glPushMatrix()

    glScalef(0.2,0.2,0.2)

    turn += 0.003
    cur_verticies = turn_cube(turn)

    glBegin(GL_QUADS)
    for x, surface in enumerate(sorted(surfaces, key = lambda x: cmp_surfaces(x))):
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,0,0] + [1])
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0, 1, 0] + [1])
        # glColor3fv(colors[surfaces.index(surface)])
        for i, vertex in enumerate(surface):
            v = list(cur_verticies[vertex])
            glVertex3fv(v)

    glEnd()

    glPopMatrix()


def turn_cube(fi):
    r1 = R.from_rotvec([0,fi,0])
    r2 = R.from_rotvec([0.3,0,0])
    return np.matmul(np.matmul(def_verticies, r1.as_matrix()), r2.as_matrix())


def display():
    glEnable(GL_LIGHTING)

    # нулевой светит белым диффузным
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 0, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0,0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])

    # первый светит белым направленным
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0,10,0.1,1])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0, 0, 0, 0])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1, 1, 1, 1])

    # параметры глобальной модели
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.7,0.7,0.7,0])
    glLightModeliv(GL_LIGHT_MODEL_LOCAL_VIEWER, [1,0,0])
    glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, 0)

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    draw_cube()

    glfw.swap_buffers(window)
    glfw.poll_events()


main()
