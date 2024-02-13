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
    x = 0
    y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: # button 4 refers to scroll up on the mouse wheel
                    glTranslatef(0, 0, 0.5)
                if event.button == 5: # button 5 refers to scroll down on the mouse wheel
                    glTranslatef(0, 0, -0.5) 

            if event.type == pygame.MOUSEMOTION:
                # MOUSEBUTTONUP triggers if the user lifts up the button after clicking
                # MOUSEBUTTON DOWN triggers if the user clicks/presses down the button
                # MOUSEMOTION tracks the position and movement of the user
                pos = pygame.mouse.get_pos()
                if (x != 0 or y != 0):
                    # set the object first to the center
                    glTranslatef((x*-1)/35, (y*-1)/35, 0)
                    # get the current position (x, y) of the mouse clicked
                    # 250 refers to the half of the screen size
                    x = int(pos[0]) - 250
                    y = 250 - int(pos[1])
                    glTranslatef(x/35, y/35, 0)
                else: 
                    x = int(pos[0]) - 250
                    y= 250-int(pos[1])
                    glTranslatef(x/35, y/35, 0) # trial and error for the value of 35
                print(x, y)
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