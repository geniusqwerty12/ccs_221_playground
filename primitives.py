# Primitives are basic shapes
# easy to draw

# glBegin
# glEnd

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(80, display[0]/display[1], 1, 10)
    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw()
        pygame.display.flip()

def draw():
    # set the primitive you want to draw
    # glBegin(GL_POINTS) # Draw points on the window
    # glBegin(GL_LINES) # Pair two points and draw a line for each pair
    # glBegin(GL_LINE_STRIP) # Connect all of the points in one line
    # glBegin(GL_LINE_LOOP) # Connect all of the lines, also connecting the start and end
    # glBegin(GL_TRIANGLES) # Group 3 points to make a triangle
    # glBegin(GL_TRIANGLE_STRIP)
    # glBegin(GL_TRIANGLE_FAN)
    # glBegin(GL_QUADS) # Draw 4 sided shapes
    # glBegin(GL_QUAD_STRIP)
    glBegin(GL_POLYGON)

    # Add color to the shape
    # Red, Green, Blue
    glColor3f(1, 1, 0)

    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # set the vertices here
    # 2 params or 2D (x,y) float
    glVertex2f(-3, 2)
    glVertex2f(-1, 4)
    glVertex2f(0, 2)
    glVertex2f(-2, 0)
    glVertex2f(-1, 0)
    glColor3f(1, 0, 0) # adds contrast
    glVertex2f(1, 2)
    glVertex2f(2, 1)
    glVertex2f(0, -2)
    glVertex2f(1, -2)
    glVertex2f(3, 0)
    glColor4f(1, 0, 1, 0.5)
    glVertex2f(4, -2)
    glVertex2f(2, -4)
    glEnd()

main()