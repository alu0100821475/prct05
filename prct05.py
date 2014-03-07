#! /usr/bin/python

PI = 3.14159265358979323846264338327950288
n = int(raw_input('Introduce el valor de n: '))

if (n!=0):
  suma = 0
  for i in range(1,n+1):
    a = float(i-1)/n
    b = float(i)/n
    xi = (i-0.5)/n
    fxi = 4.0/(1.0+xi*xi)
    print a, b, xi, fxi
    suma += fxi
  pi = float (suma)/n
  print 'El valor aproximado de PI es: ', pi
  print "El valor de PI con 35 cifras decimales es: %1.35f" % PI