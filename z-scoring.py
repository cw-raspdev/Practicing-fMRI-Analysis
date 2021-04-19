from nilearn import masking

# Section 1: Defining variables
# ToBeComputed is the 4D data we want to convert to a mask
# TempMaskStorage is where we want to store the mask and what name we'll give it
# ToAnalyze is the data we want to analyze and apply the mask to
# Analyzed is where we want to store the masked data and the name we'll give it
ToBeComputed = 'TestData/sub-02 copy/func/sub-02_task-Grammatical_run-01_bold.nii.gz'
MaskStorage = 'TestData/mask storage/' + input('What would you like to name your mask?') + '.nii'
ToAnalyze = 'TestData/sub-02 copy/func/sub-02_task-Grammatical_run-01_bold.nii.gz'
print('start')
# Section 2: To create a 3D mask which is an average of the 4D mask
MakeMask = masking.compute_epi_mask(ToBeComputed, lower_cutoff=0.2, upper_cutoff=0.85, memory=MaskStorage, verbose=0)
print('Saving mask now :D')

# Section 3: To apply the mask
maskedData = masking.apply_mask(ToAnalyze, MakeMask, dtype='f')
print('Applying mask now :D')

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
