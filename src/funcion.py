#! /usr/bin/python
#! encoding: UTF-8

import matplotlib.pyplot as pl
import numpy as np
from math import e

def f(x):
  return e**x 

pl.figure(figsize=(10,10), dpi=80)

#pl.rc('text', usetex=True)
#pl.rc('font', family='courier')

pl.subplot(1,1,1)

X = np.linspace(-10, 10, 256, endpoint=True)
Y = f(X)

pl.plot(X,Y, color="black", linewidth=2.5, linestyle="-", label=r'$e^x$')

pl.legend(loc='upper left')

pl.xlim(-10,10)
pl.ylim(0,10)

pl.xticks([-10, -5, 0, 5, 10],[r'$-10$',r'$-5$',r'$0$',r'$5$',r'$10$'])

#pl.ylim(Y.min()*1.1,Y.max()*1.1)

#pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.yticks([0, 5, 10, 15, 20, 25],[r'$0$', r'$5$', r'$10$', r'$15$', r'$20$', r'$25$' ])

pl.title(r'Representacion de $f(x)=e ^ x$')

pl.savefig("funcion.png", dpi=72)

pl.show()