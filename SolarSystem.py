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

def earth_system(t):
   year_period = 5.0                  # 5 seconds for simulating one year 
   year     = (t / year_period)
   day      = 365 * year
   moon_sid = (365 / 27.3) * year   
   glRotatef(year*360.0, 0.0, 1.0, 0.0)     # earth rotation around the sun 
   glTranslatef(1.5, 0.0, 0.0)              # earth location
   glPushMatrix()                           # push earth system
   glPushMatrix()
   glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
   glRotatef(90-23.4, 1.0, 0.0, 0.0)        # earth axis
   glColor3f (0, 0, 1)                      # blue
   glutSolidSphere(0.15, 10, 8)               # earth
   glPopMatrix()
   glPushMatrix()
   glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) # moon sidereal
   glTranslatef(0.5, 0.0, 0.0)              # distance moon to earth
   glRotatef(90, 1.0, 0.0, 0.0)
   glColor4f (0.4, 0.5, 0.6, 1)                         
   glutSolidSphere(0.05, 10, 8)               # moon
   glPopMatrix()
   glPopMatrix()    

def venus(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 5                 # 5 seconds for simulating one year 
      year1  = (t / year_period1)
      day1  = 224.7 * year1
      glRotatef(year1*360.0, 0.5, 2.0, 0.0)     # venus rotation around the sun 
      glTranslatef(1, -0.25, 0.0)              # venus location
      glPushMatrix()                           # push venus system 
      glPushMatrix()
      glRotatef(day1*360, 0.0, 1.0, 0.0)      # venus spinn
      glRotatef(90, 3.0, 2.0, 0.0)        # venus axis
      glColor3f (0.1, 0.1, 0.1)                      
      glutSolidSphere(0.1, 10, 8)               # venus
      glPopMatrix()
      glPopMatrix() 

def mars(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 7                 # 5 seconds for simulating one year 
      year1 = (t / year_period1)
      day1 = 687 * year1
      glRotatef(year1*360.0, 0.5, 3.0, 1.0)     # venus rotation around the sun 
      glTranslatef(2.0, -0.25, 0.0)              # venus location
      glPushMatrix()                           # push venus system 
      glPushMatrix()
      glRotatef(day1*360, 0.0, 1.0, 0.0)      # venus spinn
      glRotatef(75,3.0, 2.0, 0.0)        # venus axis
      glColor3f (1, 0, 0)                      
      glutSolidSphere(0.15, 10, 8)               # venus
      glPopMatrix()
      glPopMatrix()   

def display():
      glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
      glEnable( GL_DEPTH_TEST )

      glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
      glEnable( GL_DEPTH_TEST )
      t = time.time() - start_time   
      glColor4f (1.0, 1.0, 0, 1)
      glPushMatrix()
      glutSolidSphere(0.5, 30, 16)             # sun
      earth_system(t)
      venus(t)
      mars(t)
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
