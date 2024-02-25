from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd
# 1,1,1 - white; 0,0,0- black
#glclear er age glclear related stuff set korte hoy


color = (0,0,0)
bgcolor = (1,1,1)

chk = "strt"

def quads(x,y,x1,y1,x2,y2,x3,y3, clr):
    a,b,c = clr
    glColor3f(float(a), float(b), float(c))

    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

def tri(x,y,x1,y1,x2,y2, clr):
    a,b,c = clr
    glColor3f(float(a), float(b), float(c))

    glBegin(GL_TRIANGLES)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()



def lines(x,y,x1,y1):
    global color
    a,b,c =color
    glColor3f(a, b, c)
    glLineWidth(2)

    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glEnd()

def rain():
    global chk

    for x in range(0,1200,30):
        y= 800
        y1= 800 - rd.randint(25,50)
        gap = 20

        delY = 0

        # if chk=='right':
        #     delY = (y-y1)
        # elif chk=='left':
        #     delY = -1*(y-y1)
        
        # lines(x,y, x+delY ,y1)

        while y1>400:
            y1-=gap
            if y1<400:
                break
            temp = y1 - rd.randint(25,75)
            
            if chk=='right':
                delY = (y1-temp)
            elif chk=='left':
                delY = -1*(y1-temp)


            if temp<400:
                lines(x,y1, x+delY,temp)
                break
            else:
                lines(x,y1, x+delY,temp)
                y1 = temp
            


        
def keyb(key,x,y):
    global color, bgcolor
    
    if key==b'n':
        bgcolor = (0,0,0)
        color = (1,1,1)
        print("Night time")
    elif key==b'd':
        bgcolor = (1,1,1)
        color = (0,0,0)
        print("Day time")

    glutPostRedisplay()

def specialKey(key, x, y):
    global chk

    if key==GLUT_KEY_RIGHT:
        chk = 'right'                   
    elif key==GLUT_KEY_LEFT:
        chk = 'left'
    elif key==GLUT_KEY_UP:
        chk = 'strt'
    
    glutPostRedisplay()


def iterate():
    glViewport(0, 0, 1200, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 800, 0.0, 1.0)                  #left, right, bottom, top, near, far
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global bgcolor, color

    a,b,c = bgcolor
    x,y,z = color

    glClearColor(a,b,c,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    # draw_points(250, 250)



    rain()
    quads(350,200,850,200, 850,500, 350,500, (x,y,z))
    quads(360, 210, 840, 210, 840, 490, 360, 490, (a,b,c))
    tri(330,500, 870,500, 600, 650, (x,y,z) )
    tri(360,502, 840,502, 600, 635, (a,b,c) )


    lines(400,210, 400,380)         #door
    lines(400,380, 500,380)
    lines(500,380, 500,210)

    quads(470,295,475,295,475,300,470,300, (x,y,z))         #doorknob
    
    lines(650,350, 750,350)         #window
    lines(750,350, 750,450)
    lines(750,450, 650,450)
    lines(650,450, 650,350)

    lines(700,350, 700,450)         #axes
    lines(650,400, 750,400)


    lines(650,400, 750,400)



    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1200, 800) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name

glutKeyboardFunc(keyb)
glutSpecialFunc(specialKey)
glutDisplayFunc(showScreen)

glutMainLoop()