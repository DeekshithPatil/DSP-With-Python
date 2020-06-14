import numpy as np
import mysignals as sigs

signal_std = np.std(sigs.InputSignal_1kHz_15kHz)
print(signal_std)