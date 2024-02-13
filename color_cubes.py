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
    # Rotating the object
    glRotatef(90, 1, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # rotate continuously
        glRotatef(1, 1, 2, 1)
        # Clears the previous drawn object
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Call the function
        sq()
        # update the screen
        pygame.display.flip()
        # add timeout before updating
        pygame.time.wait(10)
# vertices for the square
# has 3 parametes
vertices=[
    # Page 1
    (1,1,1),(1,-1,1),(-1, -1,1),(-1, 1,1),
    # Page 2
    (1,1,-1),(1,-1,-1),(-1, -1,-1),(-1, 1,-1)
]

# line that will connect the points
# the number refers to the index of the vertices

# setting each edge will result in gradient on colors
# edges=[
#     (0,1), (2,3), # front
#     (4,5), (6,7), # back

#     (0,1), (5,4), # left 
#     (3,2), (6,7), # right

#     (0,3),(7,4), # top
#     (1,2),(6,5), # bottom
# ]

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

# colors = [
#     (1, 0, 1),
#     (1, 1, 0),
#     (1, 0, 1),
#     (0, 1, 1),
#     (1, 0, 0),
#     (0, 0, 1),
#     (0, 1, 0),
#     (1, 0, 1),
#     (1, 1, 0),
#     (0, 1, 1),
#     (1, 0, 0),
#     (0, 1, 0),
#     (1, 1, 1),
# ]

colors = [
    (1, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
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