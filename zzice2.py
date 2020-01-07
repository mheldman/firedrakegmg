from firedrake import *

a1                   = .01
a2                   = .03
R                    = a2/(a1 + a2)
p = 4.
cmesh = RectangleMesh(2, 2, 2, 2, quadrilateral=True)



def g(x, y):
  return Constant(0.0)

def f(x, y):
  r = sqrt((x - 1.)**2 + (y - 1.)**2)
  
  return conditional(r < R - 1e-12, conditional(r > 1e-12, (1./(177147.*(3. - 4.*r)**(2./3.)*r))*16.*(-3. + 3.**(2./3.)*(3. - 4.*r)**(1./3.) + 6.**(2/3)*r**(1/3))**2*(3. - 3.*3.**(2/3)*(3. - 4.*r)**(1/3)+4.*(-4. + 3.**(2/3)*(3. - 4.*r)**(1./3.))*r + 4.*6.**(2./3.)*r**(4/3))**4.*(9.*(-4*3**(2/3) + 3.*(9. - 12.*r)**(1/3) + (3. - 4.*r)**(2/3)) - 6.*2.**(2/3)*3.**(1/3)*(-9 + 3**(1/3)*(3. - 4.*r)**(2/3))*r**(1/3) + 12*(52*3**(2/3) - 29*(9 - 12*r)**(1/3) - 24*(3 - 4*r)**(2/3))*r + 12*2**(2/3)*3**(1/3)*(-55 + 17*3**(1/3)*(3 - 4*r)**(2/3))*r**(4/3) - 208*6**(1/3)*(3-4*r)**(2/3)*r**(5/3) + (-816*3**(2/3)+  416*(9-12*r)**(1/3))*r**2 + 832*2**(2/3)*3**(1/3)*r**(7/3)), 4096./81.), 0.0)

def psi(x, y):
  return Constant(0.0)

def init(x, y):
  r = sqrt((x - 1.)**2 + (y - 1.)**2)
  return sin(pi*x/2.)*sin(pi*y/2.)#sin(pi*r/R)*sin(pi*r/R)#conditional(r < R, sin(pi*r/R)*sin(pi*r/R), 0.0)

def exact(x, y):
    r = sqrt((x - 1.)**2 + (y - 1.)**2)
    return conditional( r < R, 1 - ((p - 1)/(p - 2))*((r/R)**(p/(p - 1)) - (1 - r/R)**(p/(p - 1)) + 1 - (p/(p - 1))*(r/R)), 0.0)
