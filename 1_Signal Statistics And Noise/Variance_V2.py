import mysignals as sig

_mean = 0
_variance = 0

def calc_variance(sig_arr):
    global _mean
    global _variance
    for i in sig_arr:
        _mean += i
    _mean = _mean / len(sig_arr)
    for i in sig_arr:
        _variance = _variance + (i - _mean)**2

    _variance = _variance/len(sig_arr)
    return(_variance)

print(calc_variance(sig.InputSignal_1kHz_15kHz))