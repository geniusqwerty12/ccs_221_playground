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
    gluPerspective(40, display[0]/display[1], 1, 150)
    # float value
    glTranslate(0.0, 0.0, -15)
    # Rotating the object
    # glRotatef(90, 1, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.KEYDOWN:
            #     # Can also be changed to WASD
            #     # K_w, K_a, K_s, K_d
            #     if event.key == pygame.K_DOWN:
            #          glTranslatef(0, 0.5, 0) # add 0.5 to the y axis
            #     if event.key == pygame.K_DOWN:
            #         glTranslatef(0, -0.5, 0)
            #     if event.key == pygame.K_LEFT:
            #          glTranslatef(-0.5, 0, 0) # add 0.5 to the y axis
            #     if event.key == pygame.K_RIGHT:
            #         glTranslatef(0.5, 0, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glTranslatef(0, 0, 0.5)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, 0, -0.5) 
            keys = pygame.key.get_pressed() # retrieve the button input form the user
            if keys[K_w]:
                glTranslatef(0, 0.5, 0)
            if keys[K_s]:
                glTranslatef(0, -0.5, 0)
            if keys[K_a]:
                glTranslatef(-0.5, 0, 0)
            if keys[K_d]:
                glTranslatef(0.5, 0, 0)
        # rotate continuously
        # glRotatef(1, 1, 2, 1)
        # Clears the previous drawn object
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Call the function
        sq()
        # update the screen
        pygame.display.flip()
        # add timeout before updating
        # pygame.time.wait(10)
        
# vertices for the square
# has 3 parametes
vertices=[
    # Page 1
    (1,1,1),(1,-1,1),(-1, -1,1),(-1, 1,1),
    # Page 2
    (1,1,-1),(1,-1,-1),(-1, -1,-1),(-1, 1,-1)
]

# combining the edges will make 6 faces, one for each 
# side of the cube
edges=[
    (0,1,2,3), # front
    (4,5,6,7), # back
    (0,1,5,4), # left 
    (3,2,6,7), # right
    (0,3,7,4), # top
    (1,2,6,5), # bottom
]

colors = [
    (1, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
]

# Create a square
def sq():
    glBegin(GL_QUADS)
    # for color
    x=0
    for e in edges:
        x = x + 1
        glColor3fv(colors[x])
        for vertex in e:
            # use 3 params (x,y,z)
            glVertex3iv(vertices[vertex])
    glEnd()
    
# call the main function
main()