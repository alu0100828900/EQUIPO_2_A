#!/usr/bin/python
#!encoding: UTF-8

from math import e

x = [ ]
for i in range (0,5):
  if i == 0:
    xi = 0.00
  else:
    xi = xi + 1/4.0
  x += [xi]
  
print 'Lista con los valores de x:'  
print x # Imprime las x
print '            '

fx = [ ]
for i in range (0,5):
    fxi = e**x[i]
    fx += [fxi]

print 'Lista con los valores de f(x):'
print fx # Imprime las fx
print '            '

d = [ ]
for i in range (0,5):
  if i == 0:
    di = fx[i]
  else:
    di = (fx[i] - fx[i-1])/(x[i] - x[i-1])
  d += [di]


a = [d[0], d[1], (d[2]-d[1])/(x[2]-x[0]), (d[3]-d[2]+d[1]-d[2])/(x[3]-x[0]), (d[4]-d[3]+d[2]-d[3]+d[2]-d[3]+d[2]-d[1])/(x[4]-x[0])]

print 'Lista con los coeficientes:'
print a # Imprime los coeficientes del polinomio
print '            '

y = 0
l = [ ]
valorx = 0.43
for i in range (0,5):
  li = 1
  if i == 0:
    li = 1
  else:
    for j in range (0,i):
      li = li*(valorx-x[j])
      j+=1
  l = l + [li]

print 'Lista con la parte literal:'  
print l #Imprime la parte literal del polinomio con el valor de x predeterminado
print '            '

valorpol = 0

for i in range (0,5):
  valorpol += a[i] * l[i]
  
print 'Valor del polinomio en x = 0.43: %.35f' %valorpol # Imprime el valor del polinomio con la x que le hemos dado
print '        '  
real = e**valorx
print 'Valor de f(0.43) = e^(0.43) : %.35f' %real # Imprime el valor real de la función con el valor de x
print '        ' 
print 'Error cometido en la aproximación del polinomio: %.35f' %(abs(valorpol-real)) 
# Imprime el valor absoluto del error cometido con el polinomio
print '        ' 
