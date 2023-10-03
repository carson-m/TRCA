from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

fs = 125
filt_idx = 8
   
passband = [6, 14, 22, 30, 38, 46, 54, 62, 70, 78]
stopband = [4, 10, 16, 24, 32, 40, 48, 56, 64, 72]
Wp = [passband[filt_idx]/fs, 90/fs]
Ws = [stopband[filt_idx]/fs, 100/fs]
N, Wn = signal.cheb1ord(Wp, Ws, 3, 40)
B, A = signal.cheby1(N, 0.5, Wn,'bandpass')
w, h = signal.freqz(B, A)
plt.semilogx(w / np.pi, 20 * np.log10(abs(h)))
plt.title('Chebyshev I lowpass filter fit to constraints')
plt.xlabel('Normalized frequency')
plt.ylabel('Amplitude [dB]')
plt.show()