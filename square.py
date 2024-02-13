# Introduction to OpenGL

import pygame
from pygame.locals import *;

from OpenGL.GL import *
from OpenGL.GLU import *

# Create window to display
def main():
    # Initialize the display
    pygame.init()
    display = (500,500) # window size
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    # Point of view of the display
    # first param sets the distance of the camera
    # 2nd is the ratio
    gluPerspective(40, display[0]/display[1], 1, 10)
    # float value
    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Call the function
        sq()
        # update the screen
        pygame.display.flip()

# vertices for the square
vertices=[
    (1,1),
    (1,-1),
    (-1, -1),
    (-1, 1)
]

# line that will connect the points
# the number refers to the index of the vertices
edges=[
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
]

# Create a square
def sq():
    glBegin(GL_LINES)
    for e in edges:
        for vertex in e:
            glVertex2iv(vertices[vertex])
    glEnd()
    
# call the main function
main()