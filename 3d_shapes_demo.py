# Pygame
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Vertices and Edges of the Square

# has 3 parameters, x, y and z
vertices=[
    # Page 1
    (1,1,1),(1,-1,1),(-1, -1,1),(-1, 1,1),
    # Page 2
    (1,1,-1),(1,-1,-1),(-1, -1,-1),(-1, 1,-1)
]

# line that will connect the points
# the number refers to the index of the vertices
edges=[ 
    # Page 1
    (0, 1), (1, 2), (2, 3), (3, 0),
    # Page 2
    (4, 5), (5, 6), (6, 7), (7, 4),
    # Connecting two squares
    (0, 4), (1, 5), (2, 6), (3, 7),
]

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
                    glRotate(10, 1, 0, 0)
                if event.key == pygame.K_d:
                    glRotate(10, 0, 1, 0)

        # Clears the previous drawn object
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # draw3DSquare()
        drawTriangle()

        # update the pygame window
        pygame.display.flip()

def draw3DSquare():
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)

    # start the object drawing
    glBegin(GL_LINES) 

    # Define each point of the
    # glVertex3 uses 3 points/axis 
    
    # Square in the front
    # draw the lines that will make up the square
    glVertex3iv((1,1,1))
    glVertex3iv((1,-1,1))

    glVertex3iv((1,-1,1))
    glVertex3iv((-1,-1,1))

    glVertex3iv((-1,-1,1))
    glVertex3iv((-1,1,1))

    glVertex3iv((-1,1,1))
    glVertex3iv((1,1,1))

    # Square in the back
    # notice the z axis is -1
    glVertex3iv((1,1,-1))
    glVertex3iv((1,-1,-1))

    glVertex3iv((1,-1,-1))
    glVertex3iv((-1,-1,-1))

    glVertex3iv((-1,-1,-1))
    glVertex3iv((-1,1,-1))

    glVertex3iv((-1,1,-1))
    glVertex3iv((1,1,-1))

    # Create the lines that will connect the 2 squares
    glVertex3iv((1,1,1))
    glVertex3iv((1,1,-1))

    glVertex3iv((1,-1,1))
    glVertex3iv((1,-1,-1))

    glVertex3iv((-1,-1,1))
    glVertex3iv((-1,-1,-1))

    glVertex3iv((-1,1,1))
    glVertex3iv((-1,1,-1))

    # OR

    # create a for loop
    # for e in edges:
    #     for vertex in e:
    #         # use 3 params (x,y,z)
    #         glVertex3iv(vertices[vertex])

    glEnd()

def drawTriangle():
    glColor3f(1.0,1.0,0.0)
    glPointSize(5.0)

    # start the object drawing
    glBegin(GL_LINES) 

    glVertex3iv((0,2,1))
    glVertex3iv((2,0,1))

    glVertex3iv((2,0,1))
    glVertex3iv((-2,0,1))

    glVertex3iv((-2,0,1))
    glVertex3iv((0,2,1))

    # shape at the back
    glVertex3iv((0,2,-1))
    glVertex3iv((2,0,-1))

    glVertex3iv((2,0,-1))
    glVertex3iv((-2,0,-1))

    glVertex3iv((-2,0,-1))
    glVertex3iv((0,2,-1))

    # # Create the lines that will connect the 2 squares
    glVertex3iv((0,2,1))
    glVertex3iv((0,2,-1))

    glVertex3iv((2,0,1))
    glVertex3iv((2,0,-1))

    glVertex3iv((-2,0,1))
    glVertex3iv((-2,0,-1))

    glEnd()
    


# call the main function
main()