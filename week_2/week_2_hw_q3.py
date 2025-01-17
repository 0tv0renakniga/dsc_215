'''
A class has 20 students who receive the following grades on an exam with 200 points:
194  71  31  42 175  10 100  68  11 125 156 106  90 186  95  89 142  26  89  89
Please find these statistics:
    (a) mean
    (b) median and quartiles
    (c) range and IQR

Mean: 94.75
Median: 89.5
1st Quartile (Q1): 61.5
3rd Quartile (Q3): 129.25
Range: 184
IQR: 67.75
'''

import numpy as np

data = [194,71,31,42,175,10,100,68,11,125,156,106,90,186,95,89,142,26,89,89]  # Example list of numbers

mean = np.mean(data)
median = np.median(data)
quartiles = np.percentile(data, [25, 50, 75])
range_ = np.ptp(data)  # Peak-to-Peak (Range)
iqr = quartiles[2] - quartiles[0]  # Interquartile Range

print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'1st Quartile (Q1): {quartiles[0]}')
print(f'3rd Quartile (Q3): {quartiles[2]}')
print(f'Range: {range_}')
print(f'IQR: {iqr}')

