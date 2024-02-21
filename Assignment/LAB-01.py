from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

rain_angle = 0.0
r_arr = []
background = (0, 0, 0, 0)

dayChangeColor = (1, 0, 1)

def draw_house():
    global dayChangeColor
    x, y, z = dayChangeColor
    
    glLineWidth(5)
    glBegin(GL_LINES)
    
    glColor3f(x, y, z)

    glVertex2f(150, 90)
    glVertex2f(150, -90)
    glVertex2f(150, -90)
    glVertex2f(-150, -90)
    glVertex2f(-150, -90)
    glVertex2f(-150, 90)
    
    # door
    # glColor3f(1, 0, 1)
    glVertex2f(-30, -90)
    glVertex2f(-30, 30)
    glVertex2f(-30, 30)
    glVertex2f(-100, 30)
    glVertex2f(-100, 30)
    glVertex2f(-100, -90)
    
    # window
    # glColor3f(1, 0, 1)
    glVertex2f(30, 30)
    glVertex2f(100, 30)
    glVertex2f(100, 30)
    glVertex2f(100, -40)
    glVertex2f(100, -40)
    glVertex2f(30, -40)
    glVertex2f(30, -40)
    glVertex2f(30, 30)
    glVertex(100, 1)
    glVertex(30, 1)
    glVertex(65, 30)
    glVertex(65, 0)
    glVertex(65, 0)
    glVertex(65, -40)
    glEnd()


def draw_roof():
    global dayChangeColor

    x, y, z = dayChangeColor
    glBegin(GL_TRIANGLES)
    # glColor3f(1, 0, 1)
    glVertex2f(-180, 90)
    glVertex2f(0, 150)
    glVertex2f(180, 90)
    glEnd()


def raindrop(x, y):
    glColor3f(0, 0, 1)
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def rain_drops():
    global rain_angle
    for i in range(0, len(r_arr)):
        update_x, update_y = r_arr[i]
        # Update the raindrop coordinate wrt angle
        update_x += rain_angle
        update_y -= 1
        # resetting position
        if update_x < -250 or update_y < -90:
            update_x = random.uniform(-150 + rain_angle, 150 + rain_angle)
            update_y = random.uniform(-90, 250)
            r_arr[i] = (update_x, update_y)


def specialKeyListener(key, x, y):
    global rain_angle
    if key == GLUT_KEY_RIGHT:
        rain_angle += 0.5
        print("Rain bending to the right")
    if key == GLUT_KEY_LEFT:
        rain_angle -= 0.5
        print("Rain bending to the left")
    glutPostRedisplay()


def keyboardListener(key, x, y):
    
    global background, dayChangeColor
    if key == b'n':
        dayChangeColor = (1, 1, 1)
        background = (0.0, 0.0, 0.0, 0.0)
        print("It's night time")
    if key == b'd':
        dayChangeColor = (1, 0, 1)
        background = (1.0, 1.0, 1.0, 1.0)
        print("It's DAY time!")
    glutPostRedisplay()


def animation():
    rain_drops()
    glutPostRedisplay()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250.0, 250.0, -250.0, 250.0, -250.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClearColor(*background)  # setting the background to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()
    draw_roof()
    # call the raindrop function
    for k in r_arr:
        raindrop(k[0], k[1])  # 2D
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") # window name
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
# glutMouseFunc(mouseListener)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
# random raindrop coordinate


for j in range(150):
    x2 = random.uniform(-250,250) 
    y2 = random.uniform(-100, 250) 
    r_arr.append((x2, y2))
    
glutMainLoop()
