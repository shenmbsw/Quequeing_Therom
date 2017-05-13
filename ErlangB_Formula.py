# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt


end_time = 1000
sample_rate = 0.005
x = np.arange(0, end_time, sample_rate);
y = np.zeros(np.shape(x))

res = np.zeros((10))
arr_time = 0
block = 0
enter = 0

while 1:
    arr_time = arr_time + np.random.exponential(0.1)
    handel_time = np.random.exponential(1)
    if arr_time < end_time:
        arr_ind = int(arr_time//sample_rate)
        han_ind = int(handel_time//sample_rate)
        if y[arr_ind] < 10:
            y[arr_ind:arr_ind+han_ind] += 1
        else:
            block += 1
        enter += 1
    else:
        break

plt.plot(x,y)

block_fre = 0
for i in y:
    if i == 10:
        block_fre += 1
block_arr_rate = block/enter
block_time_rate = block_fre/len(y)

print ("block_arr_rate:", block_arr_rate )
print ("block_time_rate:",  block_time_rate)

m = 0
for k in range(0,11):
    m += (10**k)/math.factorial(k)
    
Erlang = ((10**10)/math.factorial(10))/m

print("Erlang:",Erlang)