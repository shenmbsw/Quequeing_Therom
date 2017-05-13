# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:59:59 2017

@author: lenovo
"""
import numpy as np
import random
import matplotlib.pyplot as plt


end_time = 100
sample_rate = 0.005
x = np.arange(0, end_time, sample_rate);
y = np.zeros(np.shape(x))
arr_time = 0

insert_ind = int(random.random() * end_time // sample_rate)
c = np.zeros(np.shape(x))
c[insert_ind] = 1

arr_list = [0]
count = 0
while 1:
    arr_time = arr_time + np.random.exponential(10)
    arr_ind = int(arr_time//sample_rate)
    arr_list.append(arr_ind)
    if arr_time < end_time:
        y[arr_ind] = 1
        if arr_list[count] < insert_ind and arr_list[count+1] > insert_ind:
            b = (insert_ind - arr_list[count]) * sample_rate
            a =  (arr_list[count+1] - insert_ind) * sample_rate
        count+=1
    else:
        break

#print(b,a)
plt.plot(x,y)
plt.plot(x,c)

bl = []
al = []
tl = []
ave = []

for i in range(1000):
    x = np.arange(0, end_time, sample_rate);
    y = np.zeros(np.shape(x))
    arr_time = 0
    
    insert_ind = int(random.random() * end_time // sample_rate)
    c = np.zeros(np.shape(x))
    c[insert_ind] = 1
    
    arr_list = [0]
    count = 0
    while 1:
        arr_time = arr_time + np.random.exponential(10)
        arr_ind = int(arr_time//sample_rate)
        arr_list.append(arr_ind)
        if arr_time < end_time:
            y[arr_ind] = 1
            if arr_list[count] < insert_ind and arr_list[count+1] > insert_ind:
                b = (insert_ind - arr_list[count]) * sample_rate
                a = (arr_list[count+1] - insert_ind) * sample_rate
                t = (arr_list[count+1] - arr_list[count]) *sample_rate  
            count+=1
        else:
            break

    bl.append(b)
    al.append(a)
    tl.append(t)
    ave.append(arr_list[1]*sample_rate)

#print(bl)
print(sum(bl)/len(bl))

#print(al)
print(sum(al)/len(al))

print(sum(tl)/len(tl))

print(sum(ave)/len(ave))