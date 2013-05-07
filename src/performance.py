#! /usr/bin/python
import math, timeit

#constantes
lista_identidades = [ ('(a*b)**3', '(a**3)*(b**3)'), 
                      ('a/b','1/(b/a)'), 
                      ('exp(a+b)','exp(a)*exp(b)'),
                      ('log(a**b)','b*log(a)'),
                      ('a-b','-(b-a)'),
                      ('(a*b)**4','(a**4)*(b**4)'),
                      ('(a+b)**2','(a**2)+2*a*b+(b**2)'),
                      ('(a+b)*(a-b)','(a**2)-(b**2)'),
                      ('log(a*b)','log(a)+log(b)'),
                      ('a*b','exp(log(a)+log(b))'),
                      ('1/((1/a)+(1/b))','a*b/(a+b)'), 
                      ('a*(sin(b)**2+cos(b)**2)','a'), 
                      ('sinh(a+b)','(exp(a)*exp(b)-exp(-a)*exp(-b))/2'), 
                      ('tan(a+b)','sin(a+b)/cos(a+b)'), 
                      ('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)') 
										]

numero_ejecuciones = 1000000 

if __name__ == '__main__':
  st = 'import random; from math import sinh, sin, tan, cos, exp, log; A=0; B=100; a=random.uniform(A,B); b=random.uniform(A,B)'
  for l in lista_identidades:
		t0 = timeit.Timer(l[0], setup=st)
		r0 = t0.timeit(numero_ejecuciones)
		t1 = timeit.Timer(l[1], setup=st)
		r1 = t1.timeit(numero_ejecuciones)
		print l[0], r0
		print l[1], r1
