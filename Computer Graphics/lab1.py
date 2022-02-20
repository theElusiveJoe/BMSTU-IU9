import glfw
import random
import math

delta = 0
dx, dy, dz = 1.1,1.1,1.1
angle = 0.0
window = None
display = None

from OpenGL.GL import *


def main():
    global window

    if not glfw.init():
        return
    window = glfw.create_window(1200, 1200, "Lab1", None, None)
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
    global angle, delta, dx,dy,dz
    if action == glfw.PRESS:
        if key == glfw.KEY_A:
            delta -=1
        if key == glfw.KEY_D:
            delta +=1
        if key == glfw.KEY_W:
            dx += 0.1
            dy += 0.1
            dz +=0.1
        if key == glfw.KEY_S:
            dx -= 0.1
            dy -= 0.1
            dz -=0.1
    if action == glfw.RELEASE:
        if key == glfw.KEY_A:
            delta +=1
        if key == glfw.KEY_D:
            delta -=1

size = 0.5
vertexes = []
height = 0

def gen_poly(num):
    for i in range(1, num+1):
        len = random.uniform(0.5,0.9);
        ang = 2*math.pi * ((i+random.random())/num);
        vertexes.append([math.cos(ang)*len, math.sin(ang), (0, abs(math.cos(math.pi*(i)/num)), 0)])

    vertexes[0]= [0,0, vertexes[0][2]]

def gen_growing_poly(num):
    for i in range(0, num):
        vertexes.append({
            'angle':2*math.pi * i/num, 
            'len': random.uniform(0.5,0.9),
            'growing_speed': random.uniform(0.005,0.009), 
            # 'color':(
            #     -(2*i/num-1)**6+1, 
            #     -(2*i/num-1)**6+1, 
            #     -(2*i/num-1)**6+1, 
            # )
            'color' : (
                math.sin(i/num*math.pi),
                math.sin(((i+num/4)%num)/num*math.pi),
                math.sin(((i+num/3)%num)/num*math.pi),
            )
        })

    # vertexes[0]= [0,0, vertexes[0][2]]

def gen_dots():
    global height

    size = 30
    height = 1/size
    for i in range(size):
        row = []
        for j in range(size):
            red =math.sqrt(i*i + j*j)/size -0.1#random.uniform(0.3, 0.7)
            # red = (math.cos(j)*math.sin(2*i) + math.sin(2**i))
            green = 1
            row.append({
                'x' : ((j*height + height/2 + height/2*((i)%2))*2-1)*1.5,
                'y' : ((i*height + height/2)*2-1)*1.5,
                'x_c' : ((j*height + height/2 + height/2*((i)%2))*2-1)*1.5,
                'y_c' : ((i*height + height/2)*2-1)*1.5,
                'direction' : [random.uniform(-0.0003, 0.0003), random.uniform(-0.0003, 0.0003)],
                # 'color' : (random.uniform(0.5, 1), random.uniform(0.5, 1),random.uniform(0.5, 1))
                'color' : (red, green, 0)
            })
        vertexes.append(row)

def draw_dots():    
    global height

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0, 0, 0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    
    for i in range(len(vertexes)-1):
        for j in range(len(vertexes[0])-1):
            glBegin(GL_POLYGON)

            glColor3f(*(vertexes[i][j]['color']))
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])

            glColor3f(*(vertexes[i][j+1]['color']))
            glVertex2f(vertexes[i][j+1]['x'], vertexes[i][j+1]['y'])

            glColor3f(*(vertexes[i][j]['color']))
            glVertex2f(vertexes[i+1][j+(i%2)]['x'], vertexes[i+1][j+(i%2)]['y'])

            glEnd()

    for i in range(0, len(vertexes)-1):
        for j in range((i+1)%2, len(vertexes[0])-(i%2)):

            glBegin(GL_POLYGON)

            glColor3f(*(vertexes[i][j]['color']))
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])

            glColor3f(*(vertexes[i+1][j]['color']))
            glVertex2f(vertexes[i+1][j]['x'], vertexes[i+1][j]['y'])

            glColor3f(*(vertexes[i+1][j+(i%2)-((i+1)%2)]['color']))
            glVertex2f(vertexes[i+1][j+(i%2)-((i+1)%2)]['x'], vertexes[i+1][j+(i%2)-((i+1)%2)]['y'])

            glEnd()

            glBegin(GL_LINES)
            
            glColor3f(0,0,0)
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])
            glVertex2f(vertexes[i+1][j]['x'], vertexes[i+1][j]['y'])
            glVertex2f(vertexes[i+1][j]['x'], vertexes[i+1][j]['y'])
            glVertex2f(vertexes[i+1][j+(i%2)-((i+1)%2)]['x'], vertexes[i+1][j+(i%2)-((i+1)%2)]['y'])
            glVertex2f(vertexes[i+1][j+(i%2)-((i+1)%2)]['x'], vertexes[i+1][j+(i%2)-((i+1)%2)]['y'])
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])
            glEnd()

def draw_dots2():    
    global height, angle, delta, window, dx, dy, dz

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0, 0, 0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glScalef(dx,dy,dz)
    dx += random.uniform(-0.003, 0.003)
    dy += random.uniform(-0.003, 0.003)
    dz += random.uniform(-0.003, 0.003)
    delta += random.uniform(-0.005, 0.005)
    angle += delta

    for i in range(len(vertexes)-1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(len(vertexes[0])-1):

            glColor3f(*(vertexes[i][j]['color']))
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])

            glColor3f(*(vertexes[i][j+1]['color']))
            glVertex2f(vertexes[i][j+1]['x'], vertexes[i][j+1]['y'])

            glColor3f(*(vertexes[i][j]['color']))
            glVertex2f(vertexes[i+1][j+(i%2)]['x'], vertexes[i+1][j+(i%2)]['y'])

        glEnd()

    for i in range(0, len(vertexes)-1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range((i+1)%2, len(vertexes[0])-(i%2)):
            glColor3f(*(vertexes[i][j]['color']))
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])

            glColor3f(*(vertexes[i+1][j]['color']))
            glVertex2f(vertexes[i+1][j]['x'], vertexes[i+1][j]['y'])

            glColor3f(*(vertexes[i+1][j+(i%2)-((i+1)%2)]['color']))
            glVertex2f(vertexes[i+1][j+(i%2)-((i+1)%2)]['x'], vertexes[i+1][j+(i%2)-((i+1)%2)]['y'])

        glEnd()

    glColor3f(0,0,0)
    for i in range(0, len(vertexes)-1):
        for j in range((i+1)%2, len(vertexes[0])-(i%2)):
            glBegin(GL_LINES)
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])
            glVertex2f(vertexes[i+1][j]['x'], vertexes[i+1][j]['y'])
            glVertex2f(vertexes[i+1][j]['x'], vertexes[i+1][j]['y'])
            glVertex2f(vertexes[i+1][j+(i%2)-((i+1)%2)]['x'], vertexes[i+1][j+(i%2)-((i+1)%2)]['y'])
            glVertex2f(vertexes[i+1][j+(i%2)-((i+1)%2)]['x'], vertexes[i+1][j+(i%2)-((i+1)%2)]['y'])
            glVertex2f(vertexes[i][j]['x'], vertexes[i][j]['y'])
            glEnd()

    glBegin(GL_POINTS)
    glColor3f(0,0,0)
    for r in vertexes:
        for v in r:
            v['x'] += v['direction'][0]
            v['y'] += v['direction'][1]
            if abs(v['x'] - v['x_c']) > height : v['direction'][0] = random.uniform(0, 0.0003)*(-1)*v['direction'][0]/abs(v['direction'][0])
            if abs(v['y'] - v['y_c']) > height : v['direction'][1] = random.uniform(0, 0.0003)*(-1)*v['direction'][1]/abs(v['direction'][1])
            glVertex2f(v['x'], v['y'])
    glEnd()

   
    glPopMatrix()
    print(window)
    glfw.swap_buffers(window)
    glfw.poll_events()

def display_all():
    global angle, delta, window, vertexes
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_POLYGON)
    
    for i, v in enumerate(vertexes):
        glColor3f(*v[2])
        glVertex2f(v[0], v[1])
        v[0] = (v[0] + 0.0005)%1
        v[1] = (v[1] + 0.0005)%1
    glEnd()
    glPopMatrix()
    angle += delta
    glfw.swap_buffers(window)
    glfw.poll_events()

def display_growing_poly():
    global angle, delta
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0, 0, 0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_POLYGON)
    
    # for i, v in enumerate(vertexes):
    #     glColor3f(*v['color'])
    #     x = math.cos(v['angle']) * v['len']
    #     y = math.sin(v['angle']) * v['len']
    #     print(v)
    #     print(x,y)
    #     glVertex2f(x, y)
    #     v['len'] += v['growing_speed'] 
    #     if not 0.5 < v['len'] < 0.9:
    #         v['growing_speed'] = random.uniform(0.005,0.009)*(-1)*v['growing_speed']/abs(v['growing_speed'])
    #     # v['angle'] += 0.02
    glColor3f(1,1,1)
    glVertex2f(1,1)
    glColor3f(1,1,0)
    glVertex2f(-1,1)
    glColor3f(0,1,1)
    glVertex2f(0,0)

    glEnd()
    glPopMatrix()
    angle += delta
    glfw.swap_buffers(window)
    glfw.poll_events()

def display():
    global angle, delta
    posx = posy = size = 0
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.1, 0.1, 0.1)
    glVertex2f(posx + size + 0.5, posy + size + 0.5)
    glColor3f(0.35, 0.0, 0.89)
    glVertex2f(posx - size + -0.5, posy + size + 0.5)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(posx - size + -0.5, posy - size + -0.5)
    glColor3f(0.78, 0.23, 1.0)
    glVertex2f(posx + size + 0.5, posy - size + -0.5)
    glEnd()
    glPopMatrix()
    angle += delta
    glfw.swap_buffers(window)
    glfw.poll_events()


display = draw_dots2
gen_dots()
main()
