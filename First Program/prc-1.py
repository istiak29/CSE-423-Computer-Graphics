from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(15)  # pixel size. by default 1 thake, must be initialized before glBegin

    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def draw_triangles():
    glBegin(GL_TRIANGLES)

    glColor3f(0, 1, 1)
    glVertex2f(500, 100)

    glColor3f(0, 1, 0)
    glVertex2f(700, 100)

    glColor3f(1, 1, 0)
    glVertex2f(700, 200)
    glEnd()


def draw_Quads():
    glBegin(GL_QUADS)

    glColor3f(1, 0, 1)

    glVertex2f(150, 100)
    glVertex2f(300, 100)
    glVertex2f(300, 200)
    glVertex2f(150, 200)

    glEnd()


def draw_with_Line():
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)

    glVertex2f(300, 500)
    glVertex2f(600, 500)
    # glEnd()

    # glBegin(GL_LINES)
    glVertex2f(300, 500)
    glVertex2f(300, 300)

    glVertex2f(300, 300)
    glVertex2f(600, 300)

    glVertex2f(600, 300)
    glVertex2f(600, 500)

    glEnd()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # must be called before any other drawing
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)

    # call the draw methods here
    draw_points(0, 0)
    draw_triangles()
    draw_Quads()

    draw_with_Line()

    glutSwapBuffers()  # must be call after all methods are called


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
