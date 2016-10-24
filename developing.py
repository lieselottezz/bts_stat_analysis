"""Testing import csv file and plot graph"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_file = pd.read_csv('sukhumvit58.csv')
time = data_file['January']
sensors = data_file.ix[:,'January':'December']
avg = np.mean(sensors)
print(avg)
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],avg)
plt.show()
