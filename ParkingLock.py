#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:16:17 2018

@author: Pierrem
"""
from scipy.optimize import minimize
import numpy as npy
import matplotlib.pyplot as plt

import volmdlr as vm

class Pawl:
    """
    point_a : centre de rotation du doigt
    alpha0 : angle entre x et le plan du plateau
    """
    def __init__(self, point_a, ab, alpha_ab, at, alpha_at, ar, alpha_ar, 
                 alpha0, alpha1, alpha2):
        self.point_a = point_a
        self.ab = ab
        self.alpha_ab = alpha_ab
        self.at = at
        self.alpha_at = alpha_at
        self.ar = ar
        self.alpha_ar = alpha_ar
        self.alpha0 = alpha0
        self.alpha1 = alpha1
        self.alpha2 = alpha2
    def Geometry(self):
        pointA = vm.Point2D(self.point_a)
        pointB = vm.Point2D((self.ab*npy.cos(self.alpha_ab), self.ab*npy.sin(self.alpha_ab)))
        pointB.Translation(pointA)
        print(pointB)
        
#    def Plot(self):
#        # A faire
        

    
class Gear:
    def __init__(self, teeth_number, pitch_diameter, point_o, external_diameter, internal_diameter):
        self.teeth_number = teeth_number
        self.pitch_diameter = pitch_diameter
        self.point_o = point_o
        
    def Geometry(self):
        pointO = vm.Point2D(self.point_o)
        
class ParlinkLock:
    def __init__(self, pawl, point_a, alpha, gear, point_o, betha):
        self.pawl = pawl
        
P1 = Pawl(point_a = [1, 1], ab = 0.2, alpha_ab = 0.05, at = 0.15, alpha_at = 0.01,
          ar = 0.17, alpha_ar = 0.011, alpha0 = -0.06, alpha1 = -0.5, alpha2 = 0.5)
G1 = Gear(teeth_number = 12, pitch_diameter = 0.07, point_o = [0, 0], 
          external_diameter = 0.08, internal_diameter = 0.06)
P1.Geometry()

PL1 = ParlinkLock(pawl = P1, point_a = [0, 1], alpha = 0.2, gear = G1, point_o = [0, 0], betha = 0)