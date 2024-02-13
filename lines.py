import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

print("Drawing points on Python...")

# Create the vertices of the line to be drawn
vertices=[
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1),
    ]

# Create the edges that will connect the verticles
edges=[
    (0, 1),
    (1, 2),
    (2, 3),
    (0, 3),
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

        drawLines()
        pygame.display.flip()

# This function can also accept the points as a parameter
def drawLines():
    glColor3f(0.0,1.0,0.0) 
    glPointSize(5.0)
    glBegin(GL_LINES)
    
    for e in edges:
        # get the index of the points on each edge
        for v in e:
            # Here we are giving a tuple (x,y)
            # The order of the vertex connection
            glVertex2iv(vertices[v])

    glEnd()

main()