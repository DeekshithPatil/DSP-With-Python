from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sig

style.use('ggplot')
style.use('dark_background')

f,pltr_arr = plt.subplots(3, sharex=True)
f.suptitle('Multiplot')

pltr_arr[0].plot(sig.InputSignal_1kHz_15kHz, color='magenta')
pltr_arr[0].set_title('Subplot1', color = 'magenta')
pltr_arr[1].plot(sig.InputSignal_1kHz_15kHz, color='white')
pltr_arr[1].set_title('Subplot2', color = 'white')
pltr_arr[2].plot(sig.InputSignal_1kHz_15kHz, color='yellow')
pltr_arr[2].set_title('Subplot3', color = 'yellow')

plt.show()
