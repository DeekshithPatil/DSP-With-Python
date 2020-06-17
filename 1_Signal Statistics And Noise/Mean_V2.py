import mysignals as sig

_mean = 0

def calc_mean(sig_arr):
    global _mean
    for i in sig_arr:
        _mean += i
    _mean = _mean / len(sig_arr)
    return(_mean)

print(calc_mean(sig.InputSignal_1kHz_15kHz))