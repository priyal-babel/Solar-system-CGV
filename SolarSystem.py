from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import random
import decimal
start_time = time.time()

year = 0
day = 0
x_dist = []
y_dist = []
size = []

for i in range(300):
      x_dist.append(random.uniform(-9,9))
      y_dist.append(random.uniform(-8,9))
      size.append(random.uniform(0,3))

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)

def random_point():
    glBegin(GL_POINTS)
    for i in range(0,1000):
        x = random.randrange(0,1000)
        y = random.randrange(0,800)
        glVertex2i(x,y)
    glEnd()
    glFlush()

def orbit(radius, x, y, z):
      glBegin(GL_LINES)
      glColor3f (1,1,1)
      angle = 0
      while angle < (2 * math.pi):
            x1 = x + math.cos(angle) * radius
            y1 = y
            z1 = z + math.sin(angle) * radius;
            glVertex3f(x1, y1, z1)
            angle = angle + 0.01
      glEnd()

def mercury(t):
   glPopMatrix()
   glPushMatrix()
   year_period = 2.5
   year = (t / year_period)
   day = 88 * year

   glRotatef(year*360.0, 0, 1.0, 0.0)     # Mercury rotation around the sun 
   orbit(1.25,0, -0.25, 0.0) 

   glTranslatef(1.25, -0.25, 0.0)              # Mercury location
   glPushMatrix()                           # push venus system 
   glPushMatrix()                           # push Mercury system 
   glRotatef(day*360, 0.0, 0.5, 0.0)      # Mercury spinn
   glRotatef(90, 1.0, 3.0, 0.0)           # Mercury axis
   glColor3f (1,0.9,0.6)                      
   glutSolidSphere(0.05, 10, 8)               # Mercury
   glPopMatrix() 
   glPopMatrix()  

def earth_system(t):
   year_period = 4                # 5 seconds for simulating one year 
   year = (t / year_period)
   day = 365 * year
   moon_sid = (365 / 27.3) * year   
   glRotatef(year*360.0, 0,1,0)     # earth rotation around the sun 
   orbit(1.9, 0, -0.25, 0.0) 
   glTranslatef(1.9, -0.25, 0.0)              # earth location
   glPushMatrix()                           # push earth system
   glPushMatrix()
   glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
   glRotatef(90-23.4, 1.0, 1.0, 0.0)        # earth axis
   glColor3f (0, 0, 1)    
   glutSolidSphere(0.15, 10, 8)               # earth
   glPopMatrix()
   glPushMatrix()
   glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) # moon sidereal
   glTranslatef(0.5, 0.0, 0.0)              # distance moon to earth
   glRotatef(90, 1.0, 1.0, 0.0)
   glColor4f (0.4, 0.5, 0.6, 1)                         
   glutSolidSphere(0.05, 10, 8)               # moon
   glPopMatrix()
   glPopMatrix()    

def venus(t):
   glPopMatrix()
   glPushMatrix()
   year_period1 = 3                 # 5 seconds for simulating one year 
   year1  = (t / year_period1)
   day1  = 224.7 * year1
   glRotatef(year1*360.0, 0,1,0)     # venus rotation around the sun 
   orbit(1.5, 0, -0.25, 0.0)                  # blue
   glTranslatef(1.5, -0.25, 0.0)              # venus location
   glPushMatrix()                               # push venus system 
   glPushMatrix()
   glRotatef(day1*360, 0.0, 1.0, 0.0)      # venus spinn
   glRotatef(90, 3.0, 2.0, 0.0) 
   glColor3f (1,0.6,0)   
   glutSolidSphere(0.1, 10, 8)               # venus
   glPopMatrix()
   glPopMatrix() 

def uranus(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 16              # 5 seconds for simulating one year 
      year1 = (t / year_period1)
      day1 = 687 * year1
      glRotatef(year1*360.0, 0,1,0)     # uranus rotation around the sun 
      orbit(3.5,0, -0.25, 0.0) 
      glTranslatef(3.5, -0.25, 0.0)              # uranus location
      glPushMatrix()                           # push uranus system 
      glPushMatrix()
      glRotatef(day1*360, 0.0, 1.0, 0.0)      # uranus spinn
      glRotatef(50,1, 2.0, 1)        # uranus axis
      glColor3f (0.5,1,0.8)                      
      glutSolidSphere(0.2, 10, 8)               # uranus
      glPopMatrix()
      glPopMatrix()

def neptune(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 22              # 5 seconds for simulating one year 
      year1 = (t / year_period1)
      day1 = 687 * year1
      glRotatef(year1*360.0, 0,1,0)     # neptune rotation around the sun 
      orbit(3.9,0, -0.25, 0.0)      
      glTranslatef(3.9, -0.25, 0.0)              # neptune location
      glPushMatrix()                           # push neptune system 
      glPushMatrix()
      glRotatef(day1*360, 0.0, 1.0, 0.0)      # neptune spinn
      glRotatef(70,1, 2.0, 1)        # neptune axis
      glColor3f (0.5,0.7,1)                      
      glutSolidSphere(0.2, 10, 8)               # neptune
      glPopMatrix()
      glPopMatrix()

def saturn(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 11                 # 5 seconds for simulating one year 
      year1 = (t / year_period1)
      day1 = 687 * year1
      glRotatef(year1*360.0, 0,1,0)    # saturn rotation around the sun 
      orbit(3,0, -0.25, 0.0) 
      glTranslatef(3, -0.25, 0.0)              # saturn location
      glPushMatrix()                           # push saturn system 
      glPushMatrix()
      glRotatef(170, 1.0, 2.0, 4.0)        # saturn axis
      glColor3f (1,1,0.9)  
      gluDisk(gluNewQuadric(), 0.4, 0.5, 60,4)      
      glutSolidSphere(0.25, 10, 8)               # saturn
      glPopMatrix()
      glPopMatrix()

def jupiter(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 9                # 5 seconds for simulating one year 
      year1 = (t / year_period1)
      day1 = 4329 * year1
      glRotatef(year1*360.0, 0,1,0)     # jupiter rotation around the sun 
      orbit(2.5,0, -0.25, 0.0) 
      glTranslatef(2.5, -0.25, 0.0)              # jupiter location
      glPushMatrix()                           # push jupiter system 
      glPushMatrix()
      glRotatef(day1*360, 0.0, 1.0, 0.0)      # jupiter spinn
      glRotatef(75,3.0, 2.0, 0.0)        # jupiter axis
      glColor3f (1,0.9,0.7)                      
      glutSolidSphere(0.3, 10, 8)               # jupiter
      glPopMatrix()
      glPopMatrix()  

def mars(t):
      glPopMatrix()
      glPushMatrix()
      year_period1 = 5                # 5 seconds for simulating one year 
      year1 = (t / year_period1)
      day1 = 687 * year1
      glRotatef(year1*360.0, 0,1,0)     # mars rotation around the sun 
      orbit(2.2,0, -0.25, 0.0) 
      glTranslatef(2.2, -0.25, 0.0)              # mars location
      glPushMatrix()                           # push mars system 
      glPushMatrix()
      glRotatef(day1*360, 0.0, 1.0, 0.0)      # mars spinn
      glRotatef(75,3.0, 2.0, 1.0)        # mars axis
      glColor3f (1,0.2,0.3)                      
      glutSolidSphere(0.15, 10, 8)               # mars
      glPopMatrix()
      glPopMatrix()   

def stars():
      glEnable(GL_POINT_SMOOTH)
      for i in range(300):
            glPointSize(size[i])

            glBegin(GL_POINTS)
            glColor3d(1, 1, 1)
            glVertex3d(x_dist[i], y_dist[i], 0)
            glEnd()

def display():
      glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
      glEnable( GL_DEPTH_TEST )
      t = time.time() - start_time 
      stars()  
      glColor4f (1.0, 1.0, 0, 1)
      glPushMatrix()
      random_point()
      glutSolidSphere(1, 28, 16) 
      earth_system(t)
      venus(t)
      mars(t)
      mercury(t)
      jupiter(t)
      saturn(t)
      uranus(t)
      neptune(t)
      glPopMatrix()   
      glutSwapBuffers()

def reshape(w, h):
   glViewport (0, 0, w,h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(80.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 2.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1000, 600)
glutInitWindowPosition (50, 0)
glutCreateWindow("Solar system")
init()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
