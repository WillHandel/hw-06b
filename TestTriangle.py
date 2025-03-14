# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(10,15,20),'Scalene','10,15,30 should be scalene')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(10,10,15),'Isoceles','10,10,15 should be isoceles')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 should not be a triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','201,1,1 should be invalid input')
    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0,1,1 should be invalid input')
    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(1.1,1,1),'InvalidInput','1.1,1,1 should be invalid input')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

