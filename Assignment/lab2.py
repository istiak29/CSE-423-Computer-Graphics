from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

catcher_X = 250
catcher_Y = 30
diamond_X = random.randint(50, 350)
diamond_Y = 600

diamond_stop = False
back_button = False
play_button = False
cross_button = False

score = 0
falling_speed = 1

diamond_color = (1, 1, 1)


# mid point line algorithm
def MidPointLine(zone, x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    x = x1
    y = y1

    dInitial = 2 * dy - dx

    Del_E = 2 * dy
    Del_NE = 2 * (dy - dx)

    while x <= x2:
        a, b = ConvertToOriginal(zone, x, y)
        DrawPoints(a, b)

        if dInitial <= 0:
            x = x + 1
            dInitial = dInitial + Del_E
        else:
            x = x + 1
            y = y + 1
            dInitial = dInitial + Del_NE


def FindZone(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 < dy:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6


def ConvertToZoneZero(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def ConvertToOriginal(zone, x, y):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def DrawLine(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZoneZero(zone, x1, y1)
    x2, y2 = ConvertToZoneZero(zone, x2, y2)
    MidPointLine(zone, x1, y1, x2, y2)


def catcher():
    DrawLine(catcher_X, catcher_Y, catcher_X + 100, catcher_Y)
    DrawLine(catcher_X + 20, catcher_Y - 20, catcher_X + 80, catcher_Y - 20)

    DrawLine(catcher_X, catcher_Y, catcher_X + 20, catcher_Y - 20)
    DrawLine(catcher_X + 80, catcher_Y - 20, catcher_X + 100, catcher_Y)


def diamond():
    global diamond_X, diamond_Y, catcher_X, catcher_Y
    global falling_speed, score, diamond_stop, diamond_color

    r, g, b = diamond_color

    glColor3f(r, g, b)

    DrawLine(diamond_X, diamond_Y, diamond_X + 8, diamond_Y - 10)
    DrawLine(diamond_X, diamond_Y, diamond_X - 8, diamond_Y - 10)

    DrawLine(diamond_X - 8, diamond_Y - 10, diamond_X, diamond_Y - 20)
    DrawLine(diamond_X, diamond_Y - 20, diamond_X + 8, diamond_Y - 10)

    diamond_Y = (diamond_Y - falling_speed)  # decrease Speed by speed

    if diamond_Y - 20 < catcher_Y and catcher_X <= diamond_X <= catcher_X + 100:  # Collision Part

        diamond_X = random.randint(50, 350)
        diamond_Y = 600
        score = score + 1
        falling_speed += 0.6

        diamond_color = (random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1))

        print(f"Score: {score}")

    elif diamond_Y - 20 < 0:
        falling_speed = 0
        diamond_Y = 20
        totalScore = score
        score = 0

        diamond_color = (1, 0, 0)

        diamond_stop = not diamond_stop

        print(f"Game Over! Score: {totalScore}")


def PlayButton():
    if play_button:
        DrawLine(200, 580, 240, 560)
        DrawLine(200, 540, 240, 560)
        DrawLine(200, 580, 200, 540)

    else:

        DrawLine(200, 580, 200, 540)
        DrawLine(220, 580, 220, 540)


def BackButton():
    DrawLine(10, 570, 50, 570)
    DrawLine(10, 570, 30, 580)
    DrawLine(10, 570, 30, 560)


def CrossButton():
    DrawLine(390, 580, 350, 540)
    DrawLine(350, 580, 390, 540)


def specialKeyboardListener(key, x, y):
    global catcher_X, play_button

    if play_button == False and diamond_stop == False:

        if key == GLUT_KEY_LEFT:
            catcher_X = catcher_X - 20
        elif key == GLUT_KEY_RIGHT:
            catcher_X = catcher_X + 20

        catcher_X = max(0, min(300, catcher_X))  # Window boundary for catcher


def mouseListener(button, state, x, y):
    global back_button, cross_button, play_button, diamond_stop, score

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= x <= 30 and (600 - 580) <= y <= (600 - 560):
            back_button = not back_button
        elif 370 <= x <= 390 and (600 - 580) <= y <= (600 - 560):
            cross_button = not cross_button
        elif 200 <= x <= 220 and (600 - 580) <= y <= (600 - 560):
            play_button = not play_button


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

    glutPostRedisplay()


def DrawPoints(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 400, 600)
    glOrtho(0.0, 400, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    global diamond_stop
    if diamond_stop:
        glColor3f(1, 0, 0)
        catcher()
    else:
        diamond()
        glColor3f(0.4, 0.7, 1)  # if there is a mistake
        catcher()

    global diamond_Y, score, falling_speed
    if back_button:

        # print("Starting Over!")
        glColor3f(0, 0, 1)
        BackButton()
        diamond_Y = 600
        score = 0
        fallingSpeed = 1
        diamond_Y = (diamond_Y - fallingSpeed)
        # diamond()
    else:
        glColor3f(0, 0, 1)
        BackButton()

    if cross_button:
        CrossButton()
        glutLeaveMainLoop()

    else:
        glColor3f(1, 0, 0)
        CrossButton()

    glColor3f(0, 1, 0)

    global play_button
    if play_button:
        PlayButton()
        falling_speed = 0
    else:
        PlayButton()
        temp_speed = falling_speed
        falling_speed = temp_speed

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

glutInitWindowSize(400, 600)
glutInitWindowPosition(400, 100)

wind = glutCreateWindow(b"Catch The Diamonds")
glutTimerFunc(0, timer, 0)

glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyboardListener)
glutDisplayFunc(display)

glutMainLoop()
