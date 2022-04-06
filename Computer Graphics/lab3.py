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
    


# def cube():
#     global angle

#     glPushMatrix()

#     glScalef(msh, msh, msh)
#     glScalef(1, 0.5, 1)
#     glRotatef(angle, 0, 0, 1)
#     glMultMatrixd(m)
#     # angle += delta

#     glBegin(GL_QUADS)
#     for x, surface in enumerate(surfaces):
#         glColor3fv(colors[x])
#         for i, vertex in enumerate(surface):
#             glVertex3fv(verticies[vertex])

#     glEnd()

#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glColor3fv((1.0, 0.0, 0.0))
#             glVertex3fv(verticies[vertex])

#     glEnd()
#     glPopMatrix()

def gen_sphere():
    global points, ppl, circles
    r = 1

    d_fi = np.linspace(0, 2*math.pi, 50)
    d_fi = np.linspace(0, 2*math.pi, 50)
    # d_tao = np.linspace(-math.pi/2, math.pi/2, 50) 

    # points = []
    circles = []
    for fi in np.linspace(0, 2*math.pi, 10):
        turn = np.array([np.cos(fi), 0, np.sin(fi),
                        0,1,0,
                        -np.sin(fi), 0, np.cos(fi)]).reshape(3,3)
        print(turn, turn.shape)
        circle = np.array([[math.cos(tao),math.sin(tao),0] for tao in np.linspace(0, 2*math.pi, 2202020202mmm020)])
        print(circle, circle.shape)
        circles.append(np.matmul(turn, circle.T).T.round(3))
    
    # circles = circles.around(3)
    print(circles[:2])
    # for fi in np.linspace(0, 2*math.pi, 50):
    #     for tao in np.linspace(-math.pi/2, math.pi/2, 50):
    #         points.append((r*math.cos(tao)*math.cos(fi), 
    #                 r*math.cos(tao)*math.sin(fi), 
    #                 r*math.sin(tao)))

    # ppl = 100 # polygons per level
    # # print('arange:', np.linspace(-0.
    # # 5,0.5,30))
    # delta = 0
    # for z in np.linspace(-1,1,30):
    #     points.append([])
    #     r = 1-z*z
    #     delta = 0 if delta > 0 else 0.1
    #     for fi in np.linspace(0+delta, 2*math.pi+delta, ppl):
    #         points[-1].append((r*math.cos(fi), r*math.sin(fi), z))
    # print(points[:5])

def sphere():
    global circles
    glPushMatrix()
    glRotatef(angle1, 0, 0, 1)
    glRotatef(angle2, 0, 1, 0)
    glRotatef(angle3, 1, 0, 0)

    # glScalef(msh, msh, msh)
    # glScalef(1, 0.5, 1)
    # glRotatef(90, 1, 0, 0)
    # glMultMatrixd(m)
    # angle += delta
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    for circle_i, circle in enumerate(circles[:-1]):
        for point_i, point in enumerate(circle):
            # print(*(circles[circle_i][point_i]))
            glVertex3f(*(circles[circle_i][point_i]))
            glVertex3f(*(circles[circle_i][(point_i+1)%len(circle)]))
            glVertex3f(*(circles[(circle_i+1)%len(circle)][point_i]))
            glVertex3f(*(circles[(circle_i+1)%len(circle)][(point_i+1)%len(circle)]))
    # for ilvl, lvl in enumerate(points[:-1]):
    #     # glColor3fv(colors[x])
    #     for i, point in enumerate(lvl):
    #         # print(point[0], point[1], point[2])
    #         a = point
    #         b = (points[(ilvl+1)%len(points)][i])
    #         c = (lvl[(i+1)%len(lvl)])
    #         print(a, *a)
    #         glVertex3f(*a)
    #         glVertex3f(*b)
    #         glVertex3f(*b)
    #         glVertex3f(*c)
    #         glVertex3f(*c)
    #         glVertex3f(*a)
            # glVertex3f(*point)
            # glVertex3f(*(points[(ilvl+1)%len(points)][i]))
            # glVertex3f(*(lvl[(i+1)%len(lvl)]))
    # for ilvl, lvl in enumerate(reversed(points[1:])):
    #     # glColor3fv(colors[x])
    #     for i, point in enumerate(lvl):
    #         # print(point[0], point[1], point[2])
    #         a = point
    #         b = (points[(ilvl+1)%len(points)][i])
    #         c = (lvl[(i+1)%len(lvl)])
    #         print(a, *a)
    #         glVertex3f(*a)
    #         glVertex3f(*b)
    #         glVertex3f(*b)
    #         glVertex3f(*c)
    #         glVertex3f(*c)
    #         glVertex3f(*a)
    glEnd()


    # glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glColor3fv((1.0, 0.0, 0.0))
    #         glVertex3fv(verticies[vertex])

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
