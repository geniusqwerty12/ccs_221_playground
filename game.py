import pygame as pg
from OpenGL.GL import *

import numpy as np

class App:

    def __init__(self):
        # initialize pygame
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL|pg.DOUBLEBUF)
        # create a clock for monitoring
        self.clock = pg.time.Clock()
        # initialize opengl
        glClearColor(0.1, 0.2, 0.2, 1) # RGBA
        self.mainLoop()

    def mainLoop(self):

        running = True
        while(running):
            # check events
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    running  = False

            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            # timing
            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()


# 

# Creating a triangle
class Triangle:

    def __init__ (self):
        # x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, # red
            0.5, -0.5, 0.0, 1.0, 0.0, # green
            0.0, -0.5, 0.0, 0.0, 1.0, # blue
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 1

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

if __name__ == "__main__":
    myApp = App()