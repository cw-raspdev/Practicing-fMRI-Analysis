import numpy as np
from matplotlib import pyplot as plt
from sklearn import preprocessing

#this will normalize the response within voxels over time
scaler = preprocessing.StandardScaler().fit(maskedData) #returns as a fitted model
maskedData_zscore = scaler.transform(maskedData) #returns the transformed data

#check the z-scoring by printing out the mean and standard deviation of individual voxels
voxel_mean = np.mean(maskedData_zscore, axis=0)
voxel_std = np.std(maskedData_zscore, axis=0)
print('The number of voxels in the mask is %d' % len(voxel_mean));
print('The mean of the first few voxels:\n', voxel_mean[0:4])
print('The std of the first few voxels:\n', voxel_std[0:4])

#plot the distribution of values for a z-scored voxel as a histogram
n, bins, patches = plt.hist(x=maskedData_zscore, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Voxel Means')
plt.ylabel('Frequency')
plt.title('Z-scored Data for Voxels')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
