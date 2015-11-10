import numpy as np
import pdb

def FFT(x):
    "Naive Recursive implementation of the Cooley-Tukey FFT"
    x = np.asarray(x, dtype = float)
    N = x.shape[0]

    if N <= 1:
        return x
    else:
        X_even = FFT(x[::2]) #slice even part of x
        X_odd = FFT(x[1::2]) #slice odd part of x
        twiddle = np.exp(-2j*np.pi*np.arange(N)/N) 
        return np.concatenate([X_even + twiddle[:N/2]*X_odd, X_even + twiddle[N/2:]*X_odd])

def test():
    import matplotlib.pyplot as plt
    
    fs = 256.0
    ts = 1/fs
    t = np.arange(0, 1, ts)

    sig_freq = 5
    sig = np.sin(2*np.pi*sig_freq*t)

    S = FFT(sig)
    
    N = sig.shape[0]
    k = np.arange(N)
    T = N/fs
    freq = k/T

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t, sig)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(freq,abs(S),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')
    fig.show()
