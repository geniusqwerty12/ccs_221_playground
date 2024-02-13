import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

print("Drawing points on Python...")

# Create the points to be drawn
points=[
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1),
    ]

def main():
    # Initialize the Game window
    pygame.init()
    display = [500, 500] # you can adjust the size
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Setting up the perspective
    gluPerspective(80, display[0]/display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)

    # Run the game indefinitely
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        drawPoints()
        pygame.display.flip()

# This function can also accept the points as a parameter
def drawPoints():
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    
    for p in points:
        glVertex2f(p[0], p[1])

    glEnd()

main()