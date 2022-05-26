import random

from OpenGL.GL import *
import glfw
import numpy as np
from scipy.spatial.transform import Rotation as R

window = None

surfaces = None

def_verticies = None
cur_verticies = None

verticies_buf_source = []
colors_buf_source = []

vbo = None
vao = None

turn = 0

flag_spin = True
flag_textured = True
flag_move = True
flag_ranom = False

# настройки

sphere_cut_a = 20
sphere_cut_b = 20
cur_pos = np.array([0.5, 0.5, 0.5])
move_direction = [-0.4, 0.5, 0.7] / np.linalg.norm([1, -1, 0.7])


vertex_shader_str = """
varying vec4 vertex_color;


void main(){
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    vertex_color = gl_Color;
}
"""

fragment_shader_str = """
varying vec4 vertex_color;

void main() {
    gl_FragColor = vertex_color;
}
"""


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

    program = glCreateProgram()
    vs, fs = create_shaders()
    glAttachShader(program, vs)
    glAttachShader(program, fs)
    glLinkProgram(program)
    glUseProgram(program)

    glScalef(0.2, 0.2, 0.2)

    while not glfw.window_should_close(window):
        display()

    glfw.destroy_window(window)
    glfw.terminate()


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
    return min(list([cur_verticies[v][0] ** 2 + cur_verticies[v][1] ** 2 + (cur_verticies[v][2] - 10) ** 2 for v in s1]))


def draw_cube():
    # gen_buffers()

    # program = build()
    # link_all(program)

    glDrawArrays(GL_TRIANGLES, 0, 3*len(verticies_buf_source))

    global turn, cur_verticies, cur_pos, move_direction

    # glPushMatrix()

    # # масштабируем для нашлядности
    # glScalef(0.2,0.2,0.2)

    # # поворачиваем сферу
    # if flag_spin:
    #     turn += 0.05
    #     cur_verticies = turn_cube(turn)

    # # придаем движение
    # if flag_move :
    #     cur_pos += move_direction/20
    #     if cur_pos[0]**2 + cur_pos[1]**2 + cur_pos[2]**2 >= 3:
    #         b = cur_pos
    #         a = cur_pos-move_direction
    #         t_vec = cur_pos/np.linalg.norm(cur_pos)
    #         fi = np.arccos(np.clip(np.dot(-t_vec, -move_direction), -1.0, 1.0))
    #         len_t = np.linalg.norm(move_direction) * np.cos(fi)
    #         d = cur_pos - t_vec*len_t
    #         move_direction = a - b + 2*(d-a)
    #         if flag_ranom:
    #             move_direction += np.array([random.uniform(0, 0.05) for _ in range(3)])
    #         move_direction = move_direction / np.linalg.norm(move_direction)

    # рисуем
    # if not flag_textured: glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0,0])
    # glBegin(GL_QUADS)
    # for x, surface in enumerate(sorted(surfaces, key = lambda x: cmp_surfaces(x))):
    #     glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,0,0] + [1])
    #     if flag_textured : glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, gen_diffuse(surface))
    #     # glColor3fv(colors[surfaces.index(surface)])
    #     for i, vertex in enumerate(surface):
    #         v = list(cur_verticies[vertex]) + cur_pos
    #         glVertex3fv(v)

    # glEnd()

    # glBegin(GL_LINES)
    # # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0,0])
    # glColor3f(1, 1, 1)
    # for surface in surfaces:
    #     for i in range(len(surface)):
    #         glVertex3f(*3*np.array(cur_verticies[surface[i]]))
    #     glVertex3f(*3 * np.array(cur_verticies[surface[0]]))
    # glEnd()

    # glPopMatrix()


def turn_cube(fi):
    r1 = R.from_rotvec([0, fi, 0])
    r2 = R.from_rotvec([0.3, 0, 0])
    return np.matmul(np.matmul(def_verticies, r1.as_matrix()), r2.as_matrix())


def gen_sphere():
    global def_verticies, surfaces, verticies_buf_source
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

    # surfaces = []
    # for circle_i in range(sphere_cut_a):
    #     for point_i in range(sphere_cut_b):
    #         surfaces.append([
    #                 sphere_cut_a*circle_i + point_i,
    #                 sphere_cut_a*circle_i + ((point_i+1) % len(circle)),
    #                 sphere_cut_a*((circle_i+1) % len(circle)) + ((point_i+1) % len(circle)),
    #                 sphere_cut_a*((circle_i+1) % len(circle)) + point_i
    #             ])

    # новая часть для шейдеров
    for circle_i in range(sphere_cut_a):
        for point_i in range(sphere_cut_b):
            verticies_buf_source.extend([
                *def_verticies[sphere_cut_a*circle_i + point_i],
                *def_verticies[sphere_cut_a*circle_i +
                               ((point_i+1) % len(circle))],
                *def_verticies[sphere_cut_a*((circle_i+1) %
                                             len(circle)) + ((point_i+1) % len(circle))],
                *def_verticies[sphere_cut_a*((circle_i+1) % len(circle)) + point_i]
            ])
            colors_buf_source.extend([
                gen_color(*def_verticies[sphere_cut_a*circle_i + point_i],),
                gen_color(*def_verticies[sphere_cut_a*circle_i +
                                         ((point_i+1) % len(circle))],),
                gen_color(*def_verticies[sphere_cut_a*((circle_i+1) %
                                                       len(circle)) + ((point_i+1) % len(circle))],),
                gen_color(*def_verticies[sphere_cut_a *
                          ((circle_i+1) % len(circle)) + point_i])
            ])


def display():
    global turn, cur_verticies, cur_pos, move_direction
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(10, 0, 1, 1)
    cp = (np.array(cur_pos)/7).tolist()
    glTranslatef(*cp)
   

    if flag_move :
        cur_pos += move_direction/10
        if cur_pos[0]**2 + cur_pos[1]**2 + cur_pos[2]**2 >= 3:
            b = cur_pos
            a = cur_pos-move_direction
            t_vec = cur_pos/np.linalg.norm(cur_pos)
            fi = np.arccos(np.clip(np.dot(-t_vec, -move_direction), -1.0, 1.0))
            len_t = np.linalg.norm(move_direction) * np.cos(fi)
            d = cur_pos - t_vec*len_t
            move_direction = a - b + 2*(d-a)
            if flag_ranom:
                move_direction += np.array([random.uniform(0, 0.05) for _ in range(3)])
            move_direction = move_direction / np.linalg.norm(move_direction)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, verticies_buf_source)
    glColorPointer(4, GL_FLOAT, 0, colors_buf_source)
    glDrawArrays(GL_QUADS, 0, len(verticies_buf_source)//3)
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)
    glfw.swap_buffers(window)
    glfw.poll_events()

    # glEnable(GL_LIGHTING)

    # # нулевой светит белым диффузным
    # glEnable(GL_LIGHT0)
    # glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 0, 1])
    # glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0, 0])
    # glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])

    # # первый светит белым направленным
    # # glEnable(GL_LIGHT1)
    # # glLightfv(GL_LIGHT1, GL_POSITION, [0,10,0.1,1])
    # # glLightfv(GL_LIGHT1, GL_DIFFUSE, [0, 0, 0, 0])
    # # glLightfv(GL_LIGHT1, GL_SPECULAR, [1, 1, 1, 1])

    # # параметры глобальной модели
    # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.7, 0.7, 0.7, 0])
    # glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, [1, 0, 0])
    # glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    # glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, 0)

    # glClear(GL_COLOR_BUFFER_BIT)
    # glLoadIdentity()
    # glClearColor(0.0, 0.0, 0.0, 0.0)

    # draw_cube()

    # glfw.swap_buffers(window)
    # glfw.poll_events()


def gen_diffuse(surface):
    x, y, z = def_verticies[surface[0]]
    red = z/2+0.5
    green = x/2+0.5
    blue = y/2+0.5
    return [red, green, blue, np.sqrt(x**2+y**2)]


def gen_color(x, y, z):
    red = z/2+0.5
    green = x/2+0.5
    blue = y/2+0.5
    return [red, green, blue, np.sqrt(x**2+y**2)]


def create_shaders():
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_str)
    glCompileShader(vertex_shader)

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_str)
    glCompileShader(fragment_shader)

    return vertex_shader, fragment_shader


def gen_buffers():
    glGenBuffers(1, verticies_buf_source)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_shader_str)
    glBufferData(GL_ARRAY_BUFFER, len(verticies_buf_source),
                 verticies_buf_source, GL_STREAM_DRAW)


def build():
    shader_program = glCreateProgram()

    vs, fs = create_shaders()
    glAttachShader(shader_program, vs)
    glAttachShader(shader_program, fs)

    glLinkProgram(shader_program)
    glUseProgram(shader_program)

    return shader_program


def link_all(shader_program):
    glGenVertexArrays(1, vao)
    glBindVertexArray(vao)

    pos_attrib = glGetAttribLocation(shader_program, "position")
    glVertexAttribPointer(pos_attrib, 3, GL_FLOAT, GL_FALSE, 0, 0)
    glEnableVertexAttribArray(pos_attrib)


gen_sphere()
main()
