from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def findZone(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx > dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 <= dy:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        elif dx > 0 and dy < 0:
            return 6
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy <= 0:
            return 7

def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake, must be initialized before glBegin
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # must be called before any other drawing
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # call the draw methods here
    draw_points(250, 250)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
