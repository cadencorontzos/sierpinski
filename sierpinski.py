#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:14:06 2019

@author: cadecorontzos
"""
from math import cos,sin,tan,sqrt,radians
from pgl import GCompound, GPolygon, GWindow


#recursively draws a sierpinski triangle of the given order
def createSierpinskiTriangle(size, order):
    if order==0:#base case
       return drawTriangle(size)
    else:
        gc=GCompound()
        s=(size/(2*sqrt(3)))
        sx=s*cos(radians(30))
        sy=s*sin(radians(30))
        gc.add(createSierpinskiTriangle(size/2,order-1),0,-s)
        gc.add(createSierpinskiTriangle(size/2,order-1),sx,sy)
        gc.add(createSierpinskiTriangle(size/2,order-1),-sx,sy)
        return gc

#draws a triangle of the given size
def drawTriangle(size):
    t=GPolygon()
    t.addVertex(0,-(size/(2* sqrt(3))))
    t.addPolarEdge(size,300)
    t.addPolarEdge(size,180)
    return t

#makes a sierpinski triangle to the order of the input of the user
#Note that things get a bit dense for orders higher than 10, may want to adjust window size for higher orders to avoid window crashes
if __name__=="__main__":
    print("What order sierpinski triangle would you like? Please enter a positive integer.")
    order = int(input())
    gw=GWindow(500,500)
    gw.add(createSierpinskiTriangle(300, order),250,250)

    
