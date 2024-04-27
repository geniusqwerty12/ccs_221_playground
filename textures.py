# Pygame
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Crate Textures
# https://www.pinterest.ph/pin/427771664586086293/

# Declare all of the points
vertices=[
    (1,1,1),(1,-1,1),(-1, -1,1),(-1, 1,1),
    (1,1,-1),(1,-1,-1),(-1, -1,-1),(-1, 1,-1),
]

# Since we are using quadrilaterals
# we can define the faces directly
# faces, index based on the vertices given
faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (0, 3, 7, 4),
    (2, 3, 7, 6),
    (1, 2, 6, 5),
]

texture_coords = (
    # Apply the texture to the
    # whole face
    (0, 0),  # 0
    (0, 1),  # 1
    (1, 1),  # 2
    (1, 0),  # 3
)

def main():
    # set up the canvas
    pygame.init()
    # window size
    display = (500, 500)

    # configure pygame's window
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    # initalize the texture
    global texture_id
    texture_id = load_texture("assets/box-crate-1.jpg")

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
                    glTranslatef(0, 0, 1)
                if event.key == pygame.K_w:
                    glScalef(1.1,1.1,1.1)
                if event.key == pygame.K_e:
                    glRotate(-10, 1, 0, 0)
                if event.key == pygame.K_d:
                    glRotate(10, 0, 0, 1)

        # Clears the previous drawn object
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw3DSquare()

        # update the pygame window
        pygame.display.flip()

def draw3DSquare():

    # Texture Binding
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # start the object drawing
    glBegin(GL_QUADS) 

    # start from the faces
    for i, face in enumerate(faces):
        # glTexCoord2fv(texture_coords[i])
        for i, vertex in enumerate(face):
            glTexCoord2fv(texture_coords[i])
            glVertex3iv(vertices[vertex])
        

    # for index, vertex in enumerate(vertices):
    #     # Apply the texture
    #     glTexCoord2fv(texture_coords[index])
    #     # use 3 params (x,y,z)
    #     glVertex3iv(vertex)

    glEnd()
    glDisable(GL_TEXTURE_2D)
    
def load_texture(filename):
    # Load image with Pygame
    image = pygame.image.load(filename)
    image_data = pygame.image.tostring(image, 'RGBA')

    # Generate texture handle
    texture_id = glGenTextures(1)

    # Bind texture to handle
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Upload image data to GPU
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    # Set texture parameters for filtering
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id

# call the main function
main()