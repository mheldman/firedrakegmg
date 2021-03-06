# python test.py -d zzice.py -o ./testresultspfas/ncp/pbueler --mgtype pfas --fmg true --fmgc 2 --numlevels 8 --rtol 1e-12 --eps 0.0 --maxiters 10000 --preiters 1 --postiters 1 --cycle FV

#python test.py -d zzice.py -o ./testresultsrsp/ncp/pbueler --mgtype gmg --fmg true --fmgc 2 --numlevels 8 --rtol 1e-12 --eps 0.0 --maxiters 10000 --preiters 1 --postiters 1 --cycle FV --constrain true --smoother rsgs

#python test.py -d zzice.py -o ./testresultsgmg/ncp/pbueler --mgtype gmg --fmg true --fmgc 2 --numlevels 8 --rtol 1e-12 --eps 0.0 --maxiters 10000 --preiters 1 --postiters 1 --cycle FV

from firedrake import *

a1                   = .01
a2                   = .03
R                    = a2/(a1 + a2)
p = 4.
eps = 0.0
cmesh = RectangleMesh(5, 5, 2, 2, quadrilateral=True)

def g(x, y):
  return Constant(0.0)

def f(x, y):
  r = sqrt((x - 1.)**2 + (y - 1.)**2)
  return conditional(r < R - 1e-12, conditional(r > 1e-12, (512.*(-3. + 3.**(2./3.)*(3. - 4.*r)**(1./3.) + 6.**(2./3.)*r**(1./3.))**2.*(3.*3.**(2./3.) -
   3.*(3. - 4.*r)**(2./3.) + 2.*6.**(2./3.)*(3. - 4.*r)**(2./3.)*r**(1./3.) -
   8.*3.**(2./3.)*r))/(729.*(3. - 4.*r)**(2/3)*r), 4096./81.), -4096./81.)

def psi(x, y):
  return Constant(0.0)

def init(x, y):
  return Max(f(x,y), 0.0)

def exact(x, y):
    r = sqrt((x - 1.)**2 + (y - 1.)**2)
    return conditional( r < R, 1 - ((p - 1)/(p - 2))*((r/R)**(p/(p - 1)) - (1 - r/R)**(p/(p - 1)) + 1 - (p/(p - 1))*(r/R)), 0.0)

def form(u, v):
  return (inner(grad(u), grad(u)) + eps**2)**((p - 2.)/2.)*inner(grad(u), grad(v))*dx

def transform(u):
  return u**(3/8)
