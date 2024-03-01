from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def plot_circle_points(xc, yc, x, y):
    glBegin(GL_POINTS)
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)

    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)
    glEnd()


def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    plot_circle_points(xc, yc, x, y)

    while y > x:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        plot_circle_points(xc, yc, x, y)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    midpoint_circle(250, 250, 50)  # Draw a circle with center at (250, 250) and radius 100
    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set clear color to black
    gluOrtho2D(0, 500, 0, 500)  # Set the coordinate system


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Midpoint Circle Drawing")
    init()
    glutDisplayFunc(display)
    glutMainLoop()


# Example usage:
main()
