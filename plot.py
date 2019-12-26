#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt  
import os
import sys

file_path = sys.argv[1]
step = 20

def calc_moving_average(Loss_list):
  MA_list = []
  MA_value = 0

  for j in range(step):
    MA_value = MA_value + Loss_list[j]

  for i in range(len(Loss_list)-step):
    MA_list.append(MA_value/step)
    MA_value = MA_value - Loss_list[i] + Loss_list[i+step]
  
  for k in range(len(Loss_list)-int(step), len(Loss_list)):
    MA_list.append(Loss_list[k])

  return MA_list


def main():
  # Read file
  file = open(file_path, 'r')
  Iter_list = []
  Loss_list = []
  cnt = 0
  ep = 0.0001
  for line in file:
    cnt = cnt + 1
    if cnt==1:
      continue
    else:
      tmpstr = line.split()
      if(float(tmpstr[2])<ep):
        continue
      else:
        Iter_list.append(int(tmpstr[0]))
        Loss_list.append(float(tmpstr[2]))

  # Calc
  ma_list = calc_moving_average(Loss_list)
  
  # Plot
  l1=plt.plot(Iter_list,Loss_list,'r-',label='Loss',alpha=0.3)
  l2=plt.plot(Iter_list,ma_list,'r-',label='Loss_MA', alpha=0.8)
  # plt.plot(Iter_list,Loss_list,'ro-')
  plt.title('Iteration-Loss Graph')
  plt.xlabel('Iteration')
  plt.ylabel('Loss')
  plt.grid()
  plt.legend()
  plt.show()

if __name__ == '__main__':
  main()
