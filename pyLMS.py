import numpy as np
import matplotlib.pyplot as plt
import pdb
import traceback
import sys

def lms(u, d, num_taps, mu):
    """A simple LMS equaliser:
    Inputs:
    u - input signal
    d - desired signal
    num_taps - filter length
    mu - step size

    Outputs:
    y - filtered signal
    e - estimation error
    w - final filter coeffiecents

    """

    "init"
    N = len(u)-num_taps+1
    y = np.zeros(N)
    weights = np.zeros(num_taps)
    e = np.zeros(N)
    
    "do eq"
    for n in xrange(N):
        x = np.flipud(u[n:n+num_taps])
        y[n] = np.dot(x, weights)
        e[n] = d[n+num_taps-1] - y[n]
        weights = w + mu*x*e[n] 
        y[n] = np.dot(x, weights)
    return y, e, w

try:
    np.random.seed(1337)
    ulen    = 2000
    coeff   = np.concatenate(([1], np.zeros(10), [-0.9], np.zeros(7), [0.1]))
    u       = np.random.randn(ulen)
    d       = np.convolve(u, coeff)
    num_taps       = 20 # No. of taps
    step    = 0.003 # Step size
    y, e, w = lms(u, d, num_taps, step)
    print np.allclose(w, coeff)


    plt.figure()
    plt.subplot(1,1,1)
    plt.plot(np.abs(e))
    
    plt.show()
except:
    type, value, tb = sys.exc_info()
    traceback.print_exc()
    pdb.post_mortem(tb)

