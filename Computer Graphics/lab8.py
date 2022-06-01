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


turn = 0

flag_spin = True
flag_textured = True
flag_move = True
flag_ranom = False

# настройки

sphere_cut_a = 100
sphere_cut_b = 100
cur_pos = np.array([0.5, 0.5, 0.5])
move_direction = [-0.4, 0.5, 0.7] / np.linalg.norm([1, -1, 0.7])

vertex_shader_str = """
varying vec4 vertex_color;

void main(){
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    vertex_color = vec4(gl_Vertex[0]/2, gl_Vertex[1]/2, gl_Vertex[2], 
                sqrt(gl_Vertex[0]*gl_Vertex[0] + gl_Vertex[1]*gl_Vertex[1])) + vec4(0.5,0.5,0.5,0);
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

    window = glfw.create_window(300, 300, "lab", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

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


def gen_sphere():
    global def_verticies, surfaces, verticies_buf_source

    half_circle = np.array([[np.sin(tao), np.cos(tao), 0]
                           for tao in np.linspace(0, np.pi, sphere_cut_a)])
    half_circles = []
    for fi in np.linspace(0, 2 * np.pi, sphere_cut_b, endpoint=False):
        rot_mat = R.from_rotvec([0,fi,0]).as_matrix()
        half_circles.append( np.matmul(rot_mat, half_circle.T).T.tolist())

    # новая часть для шейдеров
    for i, half_circle in enumerate(half_circles):
        for qs_level, top_left in enumerate(half_circle[:-1]):
            verticies_buf_source.extend([
                *half_circles[i][qs_level],
                *half_circles[i][qs_level+1],
                *half_circles[(i+1)%len(half_circles)][qs_level+1],
                *half_circles[(i+1)%len(half_circles)][qs_level]
            ])


def display():
    global turn, cur_verticies, cur_pos, move_direction
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glTranslatef(*(np.array(cur_pos)/10).tolist())

    if flag_move :
        cur_pos += move_direction
        if cur_pos[0]**2 + cur_pos[1]**2 + cur_pos[2]**2 >= 20:
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

    glVertexPointer(3, GL_FLOAT, 0, verticies_buf_source)

    glDrawArrays(GL_QUADS, 0, len(verticies_buf_source)//3)

    glDisableClientState(GL_VERTEX_ARRAY)

    glfw.swap_buffers(window)
    glfw.poll_events()


def create_shaders():
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_str)
    glCompileShader(vertex_shader)

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_str)
    glCompileShader(fragment_shader)

    return vertex_shader, fragment_shader


gen_sphere()
main()
