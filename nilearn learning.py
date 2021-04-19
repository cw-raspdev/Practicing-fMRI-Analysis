from nilearn import masking

# Section 1: Defining variables
# ToBeComputed is the 4D data we want to convert to a mask
# TempMaskStorage is where we want to store the mask and what name we'll give it
#           --> you should add a folder to the /gitignore to save masks in
# ToAnalyze is the data we want to analyze and apply the mask to
# Analyzed is where we want to store the masked data and the name we'll give it
ToBeComputed = 'sub-01_task-Digit_run-01_bold.nii.gz'
MaskStorage = 'TestData/mask storage/' + input('What would you like to name your mask?') + '.nii'
ToAnalyze = 'sub-01_task-Digit_run-01_bold.nii.gz'
print('start')
# Section 2: To create a 3D mask which is an average of the 4D mask
MakeMask = masking.compute_epi_mask(ToBeComputed, lower_cutoff=0.2, upper_cutoff=0.85, memory=MaskStorage, verbose=0)
print('Saving mask now :D')

# Section 3: To apply the mask
maskedData = masking.apply_mask(ToAnalyze, MakeMask, dtype='f')
print('Applying mask now :D')

# Section 4: Plot voxels with given mask --> This bit comes from plot.py and is mostly Mehak's work :)
print('Here is a graph of Voxel Intensity over Time')
from matplotlib import pyplot as plt

voxel_id = 100

f, ax = plt.subplots(1, 1, figsize=(14, 5))
ax.plot(maskedData[:, voxel_id])

ax.set_title('Voxel time series, voxel id = %d' % voxel_id)
ax.set_xlabel('TR')
ax.set_ylabel('Voxel Intensity')
plt.show()
