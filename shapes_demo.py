# Pygame
# Canvas for your 2D objects
import pygame
from pygame.locals import *

# module for creating 2D/3D objects
# using points, lines, predefined methods 
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    # set up the canvas
    pygame.init()
    # window size
    display = (500, 500)
    # configure pygame's window
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)
    
    # change the perspective of the canvas to the window
    gluPerspective(100, display[0]/display[1], 1, 10)
    # apply translate
    glTranslate(0.0, 0.0, -5)

    # draw the objects
    # since this is a game window, it continuously listens for user input
    # and updates the screen using loops
    while True:
        # listen for events
        for event in pygame.event.get():
            # If the user clicks the close button
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Perform transforms
                if event.key == pygame.K_q:
                    glTranslatef(0, 0.5, 0)
                if event.key == pygame.K_w:
                    glScalef(1.1,1.1,0.0)
                if event.key == pygame.K_e:
                    glRotate(50, 0, 0, 1)
                if event.key == pygame.K_r:
                    gluProject(0.5, 0, 0)

        # Clears the previous drawn object
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # drawPoints()
        # drawLines()
        drawShapes()

        # update the pygame window
        pygame.display.flip()

def drawPoints():
    # 
    glColor3f(0.0,1.0,0.0)
    # size of the point
    glPointSize(5.0)

    # start the object drawing
    glBegin(GL_POINTS) # with OpenGL, you can specify what objects you create

    # Set the points you want to draw
    # 2f refers to 2 points, each with floating values
    glVertex2f(1, 1)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glVertex2f(-1, 1)

    # stop the object drawing
    glEnd()

def drawLines():
    glColor3f(0.0,0.0,1.0)
    # size of the point
    glPointSize(5.0)

    # glBegin(GL_LINES) # finds a pair of vertices and draws a line
    # glBegin(GL_LINE_STRIP) # draws line in order of the vertices
    glBegin(GL_LINE_LOOP) # draws line in order of the vertices, then connects the last and first points
    glVertex2f(1, 1)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glVertex2f(-1, 1)
    glEnd()

def drawShapes():
    glColor3f(1.0,0.0,0.0)
    # size of the point
    glPointSize(5.0)

    # glBegin(GL_TRIANGLES) # look for 3 vertices and create a closed line
    glBegin(GL_QUADS) # # look for 4 vertices and create a closed line
    glVertex2f(1, 1)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glVertex2f(-1, 1)
    glEnd()
    
# call the main function
main()