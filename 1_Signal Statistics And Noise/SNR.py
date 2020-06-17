import numpy as np
import mysignals as sigs

signal_std = np.std(sigs.InputSignal_1kHz_15kHz)
signal_mean = np.mean(sigs.InputSignal_1kHz_15kHz)
SNR = signal_mean / signal_std
print(SNR)