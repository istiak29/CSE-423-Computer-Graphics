from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd

balls = []
speed = 0.05
freezeChk = False
blinkchk = False
temp = None  # for freezing speed


# time = 0
# t = 0
# state = False
def drawPoints():
    global balls

    for ball in balls:
        x, y, color, dirx, diry = ball

        time = glutGet(GLUT_ELAPSED_TIME)
        delt = time % 500
        if not freezeChk and blinkchk and delt <= 250:
            r, g, b = (0, 0, 0)
        else:
            r, g, b = color
        glPointSize(10)
        glBegin(GL_POINTS)
        glColor3f(r, g, b)
        glVertex2f(x, y)
        glEnd()


def keyb(key, x, y):
    global speed, freezeChk, temp

    if key == b' ':
        if not freezeChk:
            temp = speed
            speed = 0
            freezeChk = True
        else:
            speed = temp
            freezeChk = False

    glutPostRedisplay()


def arrows(key, x, y):
    global speed

    if key == GLUT_KEY_UP:
        speed += 0.01
        print("Speed increased")
    if key == GLUT_KEY_DOWN:
        if (speed - 0.01) > 0:
            speed -= 0.01
            print("Speed decreased")
        else:
            speed = 0

    glutPostRedisplay()


# def blink(x):
#     global balls, colors, state 

#     for idx, ball in enumerate(balls):
#         x,y, color, dirx, diry = ball
#         colors.append(color) 

#         color = (1,1,1)

#         ball = x,y, color, dirx, diry
#         balls[idx] = ball

#     state = True
#     print("y")
#     glutPostRedisplay()
#     glutTimerFunc(1000, blink, 0)

# for idx, ball in enumerate(balls):
#     x,y, color, dirx, diry = ball

#     color= colors[idx]

#     ball = x,y, color, dirx, diry
#     balls[idx] = ball
# glutPostRedisplay()


def mouse(button, state, x, y):
    global balls, blinkchk

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN and not freezeChk:
            if not blinkchk:
                blinkchk = True
                # glutTimerFunc(1000, blink, 0)
            else:
                blinkchk = False

    if button == GLUT_RIGHT_BUTTON:  # spawns points
        if state == GLUT_DOWN and not freezeChk:
            print(x, y)
            dirx = rd.choice([-1, 1])
            diry = rd.choice([-1, 1])
            color = (rd.random(), rd.random(), rd.random())
            balls.append((x, 500 - y, color, dirx, diry))


def animate():
    glutPostRedisplay()
    global balls, speed

    for idx, ball in enumerate(balls):
        x, y, color, dirx, diry = ball

        x = (x + speed * dirx)
        y = (y + speed * diry)

        if y > 500:
            diry = -1
            y -= speed
        elif y < 0:
            diry = 1
            y += speed
        elif x > 1000:
            dirx = -1
            x -= speed
        elif x < 0:
            dirx = 1
            x += speed

        ball = x, y, color, dirx, diry
        balls[idx] = ball


def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1000, 0, 500, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(0, 0, 0)  # box border color
    glLineWidth(2)  # box
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(1000, 0)

    glVertex2f(1000, 0)
    glVertex2f(1000, 500)

    glVertex2f(1000, 500)
    glVertex2f(0, 500)

    glVertex2f(0, 500)
    glVertex2f(0, 0)
    glEnd()

    drawPoints()  # points

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)  # window size
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutMouseFunc(mouse)
glutKeyboardFunc(keyb)
glutSpecialFunc(arrows)
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutMainLoop()
