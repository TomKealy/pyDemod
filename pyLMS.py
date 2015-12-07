import numpy as np
import matplotlib.pyplot as plt
import traceback
import sys

class LMS:
    def __init__(self, input_signal, desired_signal, num_taps, learning_rate):
        self.u = input_signal
        self.d = desired_signal
        self.num_taps = num_taps
        self.mu = learning_rate
        self.num_points = len(self.u)
        self.weights = np.zeros(num_taps)
        self.y = np.zeros(self.num_points)
        self.e = np.zeros(self.num_points)
    
    def equalize(self):
        for n in xrange(self.num_taps, self.num_points):
            x = self.u[n:n-num_taps:-1]
            self.y[n] = np.dot(x, self.weights)
            self.e[n]= self.d[n] - self.y[n]
            self.weights = self.weights + self.mu*x*self.e[n] 

try:
    np.random.seed(1337)
    ulen    = 20000
    coeff   = np.concatenate(([1], np.zeros(10), [-0.9], np.zeros(7), [0.1]))
    u       = np.random.randn(ulen)
    d       = np.convolve(u, coeff)
    num_taps = 20 
    step = 0.01 

    eq = LMS(u, d, num_taps, step)
    eq.equalize()
    plt.figure()
    plt.semilogy()
    plt.subplot(1,1,1)
    plt.plot(np.abs(eq.e))
    plt.show()
except:
    type, value, tb = sys.exc_info()
    traceback.print_exc()
    pdb.post_mortem(tb)

