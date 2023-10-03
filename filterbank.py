from scipy import signal
import numpy as np

def filterbank(eeg_data,fs,filt_idx):
    fs = fs/2
    
    passband = [6, 14, 22, 30, 38, 46, 54, 62, 70, 78]
    stopband = [4, 10, 16, 24, 32, 40, 48, 56, 64, 72]
    Wp = [passband[filt_idx]/fs, 90/fs]
    Ws = [stopband[filt_idx]/fs, 100/fs]
    N, Wn = signal.cheb1ord(Wp, Ws, 3, 40)
    B, A = signal.cheby1(N, 0.5, Wn,'bandpass')
    
    y = signal.filtfilt(B, A, eeg_data, axis=1, padlen=3*(max(len(B),len(A))-1))
    return y