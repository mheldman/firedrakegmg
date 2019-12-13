# python setup.py build_ext -i

cimport numpy as np
def gauss_seidel(np.ndarray[int, ndim=1] Ap, np.ndarray[int, ndim=1] Aj, np.ndarray[double, ndim=1] Ax, np.ndarray[double, ndim=1] x, np.ndarray[double, ndim=1] b):
    cdef unsigned int i, j, jj, start, end
    cdef double rsum, diag

    for i in xrange(0,x.shape[0]):
       start = Ap[i]
       end   = Ap[i + 1]
       rsum = 0.0
       for jj in xrange(start, end):
            diag, j = 0.0, Aj[jj]
            if i == j:
              diag = Ax[jj]
            else:
              rsum += Ax[jj]*x[j]
       if diag > 0.0:
            x[i] = (b[i] - rsum)/diag
       else:
            x[i] = b[i]

def projected_gauss_seidel(np.ndarray[int, ndim=1] Ap, np.ndarray[int, ndim=1] Aj, np.ndarray[double, ndim=1] Ax, np.ndarray[int, ndim=1] Bp, np.ndarray[int, ndim=1] Bj, np.ndarray[double, ndim=1] Bx, np.ndarray[double, ndim=1] x, np.ndarray[double, ndim=1] b, np.ndarray[double, ndim=1] c, np.ndarray[int, ndim=1] indices):
    cdef unsigned int i, j, jj, start, end
    cdef double rsum, diag, val

    for i in indices:

       start = Ap[i]
       end   = Ap[i + 1]
       rsum, diag = 0.0, 0.0
       for jj in xrange(start, end):
            j = Aj[jj]
            if i == j:
              diag  = Ax[jj]
            else:
              rsum += Ax[jj]*x[j]
       if diag > 0.0:
          x[i] = (b[i] - rsum)/diag

       start = Bp[i]
       end   = Bp[i + 1]
       rsum, diag = 0.0, 0.0
       for jj in xrange(start, end):
          j = Bj[jj]
          if i == j:
            diag  = Bx[jj]
          else:
            rsum += Bx[jj]*x[j]
       if diag > 0.0:
          val = (c[i] - rsum)/diag

       x[i] = max(val, x[i])

def symmetric_pgs(np.ndarray[int, ndim=1] Ap, np.ndarray[int, ndim=1] Aj, np.ndarray[double, ndim=1] Ax, np.ndarray[int, ndim=1] Bp, np.ndarray[int, ndim=1] Bj, np.ndarray[double, ndim=1] Bx, np.ndarray[double, ndim=1] x, np.ndarray[double, ndim=1] b, np.ndarray[double, ndim=1] c, np.ndarray[int, ndim=1] indices):


    projected_gauss_seidel(Ap, Aj, Ax, Bp, Bj, Bx, x, b, c, indices)
    projected_gauss_seidel(Ap, Aj, Ax, Bp, Bj, Bx, x, b, c, indices[len(indices) - 1:-1:-1])

    #doesn't seem to work

