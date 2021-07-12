import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import figure
import math
import mat4py
import scipy as sp
from scipy.fftpack import fft, ifft
from scipy.signal.windows import hamming

data = pd.read_csv("data.csv")
t = data["t_values"].values.tolist()
x = data["ir_values"].values.tolist()

t2 = t[13474:14037]
x2 = x[13474:14037]

w = hamming(len(x2), sym=True)

w_sig = sp.signal.convolve(x2, w)
# w_sig = w_sig[0:563]
print(len(w_sig), len(x2))
# Ts = np.mean(np.abs(np.diff(t2)))
# fs = 1000
#
# N = len(t2)
# xf = fft(x)
# mag = (2/N)*np.abs(xf)
# fm = (fs/2)*np.linspace(0, 1, int(N/2))
# mag_ = mag[0:len(fm)]

plt.plot(w_sig)
plt.show()














# data = pd.read_csv("data.csv")
# t = (data.tail(128)["t_values"].values/1000000).tolist()
# x = data.tail(128)["ir_values"].values.tolist()
#
#
# N = len(x)
# # fs = np.mean(np.abs(np.diff(t)))
# fs = 1000
# xf = fft(x)
# mag = (2/N)*np.abs(xf)
#
# fm = (fs/2)*np.linspace(0, 1, int(N/2))
# mag2 = mag[0:len(fm)]
#
# plt.plot(fm, mag2)
# plt.show()


