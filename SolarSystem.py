from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

start_time = time.time()

year = 0
day = 0

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)


def display():
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )

    t = time.time() - start_time
    year_period = 10.0                  # 5 seconds for simulating one year 
    year     = (t / year_period)
    day      = 365 * year
    moon_sid = (365 / 27.3) * year

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )

    glColor4f (1.0, 1.0, 0, 1)
    glPushMatrix()
    glutSolidSphere(0.5, 30, 16)             # sun

    glRotatef(year*360.0, 0.0, 1.0, 0.0)     # earth rotation around the sun 
    glTranslatef(3.0, 0.0, 0.0)              # earth location

    glPushMatrix()                           # push earth system 

    glPushMatrix()
    glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
    glRotatef(90-23.4, 1.0, 0.0, 0.0)        # earth axis
    glColor3f (0, 0, 1)                      # blue
    glutWireSphere(0.2, 10, 8)               # earth
    glPopMatrix()


    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) # moon sidereal
    glTranslatef(0.5, 0.0, 0.0)              # distance moon to earth
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor4f (0.4, 0.5, 0.6, 1)                         
    glutWireSphere(0.05, 10, 8)               # moon
    glPopMatrix()

    glPopMatrix()                            # pop earth system 

     # Venus
    glRotatef(year*360.0, 1.0, 1.0, 0.0)     # earth rotation around the sun 
    glTranslatef(1.0, 0.0, 0.0)              # earth location

    glPushMatrix()                           # push earth system 

    glPushMatrix()
    glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
    glRotatef(90, 1.0, 0.0, 0.0)        # venus axis
    glColor3f (0, 1, 1)                      
    glutWireSphere(0.1, 10, 8)               # venus
    glPopMatrix()
    glPopMatrix() 
    glPopMatrix()

    
    glutSwapBuffers()

def reshape(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(70.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1000, 800)
glutInitWindowPosition (100, 100)
glutCreateWindow("Solar system")
init()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
