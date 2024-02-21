from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random


Width, Height = 500, 500
speed = 0.1
blink = False
freeze = False
freezeArray = []
blinkArray = []
pointsArray = []


class Point:
    
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.z = 0
        self.dx = dx
        self.dy = dy
        
        self.color = color


def convertToCoordinate(x, y):
    global Width, Height
    a = x - (Width / 2)
    b = (Height / 2) - y
    return a, b


def drawPoints(x, y, color):
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x, y)
    glEnd()


def mouseListener(button, state, x, y):
    global pointsArray, blink
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        c_x, c_y = convertToCoordinate(x, y)
        color = (random.random(), random.random(), random.random())
        # Random diagonal movement
        dx, dy = random.choice([(1, 1), (-1, 1), (-1, -1), (1, -1)])
        point_data = Point(c_x, c_y, dx, dy, color)
        pointsArray.append(point_data)
        
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # blinking effect
        blink = True
        print("Blink")
        glutPostRedisplay()


def display():
    global blink, freeze
    # clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)  # color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # load the correct matrix-- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # initialize the matrix
    glLoadIdentity()
    # now give three info
    # 1. where is the camera (viewer)?
    # 2. where is the camera looking?
    # 3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    if not freeze:
        for point in pointsArray:
            drawPoints(point.x, point.y, point.color)
            # Update point position
            point.x += point.dx
            point.y += point.dy
            # Boundary conditions
            if point.x < -180 or point.x > 180:
                point.dx = -point.dx
            if point.y < -180 or point.y > 180:
                point.dy = -point.dy

        if blink:
            for point in pointsArray:
                # If the point's color is red, transition to black; otherwise, transition to red
                if point.color == [1.0, 0.0, 0.0]:
                    point.color = [0.0, 0.0, 0.0]
                else:
                    point.color = [1.0, 0.0, 0.0]
                    
    glutSwapBuffers()




def specialKeyListener(key, x, y):
    global speed
    if key == GLUT_KEY_UP:
        speed *= 2
        print("Increase Speed")
    if key == GLUT_KEY_DOWN:
        speed /= 2
        print("Speed Decrease")
    glutPostRedisplay()


def keyboardListener(key, x, y):
    global freeze
    if key == b' ':
        freeze = not freeze
        if freeze:
            print("Points freezed")
        else:
            print("Points unfreeze")
    glutPostRedisplay()


def init():
    # clear the screen
    glClearColor(0, 0, 0, 0)
    # load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # initialize the matrix
    glLoadIdentity()

    gluPerspective(104, 1, 1, 1000.0)


glutInit()

glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(display)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()  # The main loop of OpenGL
