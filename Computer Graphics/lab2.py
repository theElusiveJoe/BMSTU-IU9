from OpenGL.GL import *
import glfw
import math

delta = 0.1
angle1, angle2, angle3 = 0, 0, 0
window = None
display = None
msh = 0.2
m = []

d_x, d_z = 30, 0

colors = (
    (0, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0, 1, 0.5),
    (1, 0.7, 0)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

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


def genmatrix():
    global m
    fx, fy, fz = 0.94, 0.47, 0.94

    fi, tao = math.asin(fz/math.sqrt(2-fz**2)), math.asin(fz/math.sqrt(2))
    sf, cf, st, ct = math.sin(fi), math.cos(fi), math.sin(tao), math.cos(tao)
    m = [cf, 0, sf, 0,
         sf*st, ct, -cf*st, 0,
         sf*ct, -sf, -cf*ct, 0,
         0, 0, 0, 1]


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


def cube_default(x_shift=4):
    glPushMatrix()
    glRotatef(70, 1, 0, 0)
    glScalef(msh, msh, msh)

    glRotatef(d_x, 0, 0, 1)
    glRotatef(d_z, 0, 0, 1)
    glBegin(GL_QUADS)
    for x, surface in enumerate(surfaces):
        glColor3fv(colors[x])
        for i, vertex in enumerate(surface):
            v = list(verticies[vertex])
            v[0] += x_shift
            glVertex3fv(v)

    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1.0, 0.0, 0.0))
            v = list(verticies[vertex])
            v[0] += x_shift
            glVertex3fv(v)
    glEnd()

    glPopMatrix()


def cube():
    global angle1, angle2, angle3

    glPushMatrix()

    glScalef(msh, msh, msh)
    glScalef(1, 0.5, 1)
    glRotatef(angle1, 0, 0, 1)
    glRotatef(angle2, 0, 1, 0)
    glRotatef(angle3, 1, 0, 0)
    glMultMatrixd(m)

    glBegin(GL_QUADS)
    for x, surface in enumerate(surfaces):
        glColor3fv(colors[x])
        for i, vertex in enumerate(surface):
            glVertex3fv(verticies[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1.0, 0.0, 0.0))
            glVertex3fv(verticies[vertex])

    glEnd()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)

    cube()
    cube_default()

    glfw.swap_buffers(window)
    glfw.poll_events()


genmatrix()
main()
