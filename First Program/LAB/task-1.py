from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# def draw_points(x, y):
#     glPointSize(5)      #pixel size. by default 1 thake, must be initialized before glBegin
#     glBegin(GL_POINTS)
#     glVertex2f(x,y) #jekhane show korbe pixel
#     glEnd()

BG_COLOR = (0, 0, 0)
LINE_COLOR = (1, 1, 1)


def draw_house():
    c1, c2, c3 = LINE_COLOR
    glBegin(GL_LINES)
    glColor3f(c1, c2, c3)

    glVertex2f(200, 100)
    glVertex2f(500, 100)

    glVertex2f(500, 100)
    glVertex2f(500, 300)

    glVertex2f(500, 300)
    glVertex2f(200, 300)

    glVertex2f(200, 300)
    glVertex2f(200, 100)

    # # triangle
    glVertex2f(350, 400)
    glVertex2f(190, 292)

    glVertex2f(350, 400)
    glVertex2f(510, 292)

    # window
    glVertex2f(388, 170)
    glVertex2f(388, 250)

    glVertex2f(388, 250)
    glVertex2f(465, 250)

    glVertex2f(465, 250)
    glVertex2f(465, 170)

    glVertex2f(465, 170)
    glVertex2f(388, 170)

    # vertical line
    glVertex2f(425, 170)
    glVertex2f(425, 250)

    glVertex2f(430, 170)
    glVertex2f(430, 250)

    glVertex2f(425, 210)
    glVertex2f(430, 210)

    # Door
    glVertex2f(225, 100)
    glVertex2f(225, 250)

    glVertex2f(325, 100)
    glVertex2f(325, 250)

    glVertex2f(225, 250)
    glVertex2f(325, 250)

    # Door line
    glVertex2f(275, 100)
    glVertex2f(275, 200)

    glVertex2f(275, 200)
    glVertex2f(225, 250)

    glVertex2f(275, 200)
    glVertex2f(325, 250)

    glEnd()


def drawRainLine(x1, y1, x2, y2):
    c1, c2, c3 = LINE_COLOR
    glBegin(GL_LINES)
    glColor3f(c1, c2, c3)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glEnd()


rain_shifting = "default"


def rain():
    global rain_shifting
    for x in range(0, 800, 40):
        y = 600
        y1 = 600 - random.randint(20, 70)
        rain_gap = 20  # vertical rain to rain gap

        shift = 0

        while y1 > 325:
            y1 -= rain_gap
            # if y1 < 300:
            #     break
            temp = y1 - random.randint(10, 30)

            if rain_shifting == "right":
                shift = y1 - temp
            elif rain_shifting == "left":
                shift = -(y1 - temp)

            if temp < 325:
                drawRainLine(x, y1, x + shift, temp)
            else:
                drawRainLine(x, y1, x + shift, temp)
                y1 = temp


def specialKeyListener(key, x, y):
    global rain_shifting

    if key == GLUT_KEY_RIGHT:
        rain_shifting = 'right'
    elif key == GLUT_KEY_LEFT:
        rain_shifting = 'left'
    elif key == GLUT_KEY_UP:
        rain_shifting = 'default'

    glutPostRedisplay()


def keyboardListener(key, x, y):
    global BG_COLOR, LINE_COLOR

    if key == b'n':
        BG_COLOR = (0, 0, 0)
        LINE_COLOR = (1, 1, 1)
        print("Night Mode On")
    if key == b'l':
        BG_COLOR = (1, 1, 1)
        LINE_COLOR = (1, 0, 1)
        print("Light Mode On")

    glutPostRedisplay()


def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:  # // 2 times?? in ONE click? -- solution is checking DOWN or UP
            print(x, y)

    glutPostRedisplay()


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
    # draw_points(250, 250)

    rain()
    draw_house()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

# special Functions
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)

glutMainLoop()
