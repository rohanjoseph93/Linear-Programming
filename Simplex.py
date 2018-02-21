# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:36:29 2017

@author: ROHAN
"""

#Simplex Minimization

#Objective function
c = [6, 5]
#Constraints (LHS)
A = [[-1, -1], [-3, -2]]
#Constraints (RHS)
b = [-5, -12]

#Bounds are none when there is no bound in that direction
x0_bounds = (None, None)
x1_bounds = (None, None)

#import linear programming library
from scipy.optimize import linprog

#Solve LP using simplex
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
              options={"disp": True})

