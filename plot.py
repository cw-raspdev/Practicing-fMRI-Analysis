#After masking, the fMRI dataset at this stage is in the format rows=time, columns=voxels (no. of voxels in mask)
#Now we can plot a voxel value (in this it is voxel 100) through time
from matplotlib import pyplot as plt
voxel_id = 100

f, ax = plt.subplots(1, 1, figsize=(14, 5))
ax.plot(maskedData[:, voxel_id])

ax.set_title('Voxel time series, voxel id = %d' % voxel_id)
ax.set_xlabel('TR')
ax.set_ylabel('Voxel Intensity');

