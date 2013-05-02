#!/usr/bin/python

import sys, time, random
from math import *
from modulo_error import error

def getElapsedTime(expr, A, B, n):
  # Initial time 
  e0 = time.time()
  # Evals the expression n times
  i = 0
  while (i < n):
    a = random.uniform(A, B)
    b = random.uniform(A, B)
    eval(expr)
    i += 1
  # Finish time
  elapsed_time = time.time() - e0
  return elapsed_time

def getCPUTime(expr, A, B, n):
  # Initial time 
  c0 = time.clock()
  # Evals the expression n times
  i = 0
  while (i < n):
    a = random.uniform(A, B)
    b = random.uniform(A, B)
    eval(expr)
    i += 1
  # Finish time
  cpu_time = time.clock() - c0
  return cpu_time
  
if __name__ == '__main__':
  if (len(sys.argv) != 6):
    print 'Correct usage: {0} expr1 expr2 A B iterations'.format(sys.argv[0])
  else:
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    A = float(sys.argv[3])
    B = float(sys.argv[4])
    iterations = int(sys.argv[5])
    print 'CPU time invested in evaluating the expression {0} for {1} iterations: {2} seconds'.format(expr1, iterations, getCPUTime(expr1, A, B, iterations))
    print 'Elapsed time invested in evaluating the expression {0} for {1} iterations: {2} seconds'.format(expr1, iterations, getElapsedTime(expr1, A, B, iterations))
    print 'CPU time invested in evaluating the expression {0} for {1} iterations: {2} seconds'.format(expr2, iterations, getCPUTime(expr2, A, B, iterations))
    print 'Elapsed time invested in evaluating the expression {0} for {1} iterations: {2} seconds'.format(expr2, iterations, getElapsedTime(expr2, A, B, iterations))
