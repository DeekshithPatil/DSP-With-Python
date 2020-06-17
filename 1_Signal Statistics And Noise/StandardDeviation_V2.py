import mysignals as sig

_mean = 0
_variance = 0
_std = 0

def calc_std(sig_arr):
    global _mean
    global _variance
    global _std
    for i in sig_arr:
        _mean += i
    _mean = _mean / len(sig_arr)
    for i in sig_arr:
        _variance = _variance + (i - _mean)**2

    _variance = _variance/len(sig_arr)
    _std = _variance ** 0.5
    return(_std)


print(calc_std(sig.InputSignal_1kHz_15kHz))