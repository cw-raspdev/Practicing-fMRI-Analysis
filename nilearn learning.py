import nilearn as nil
from nilearn import masking
# help(nil)

# Section 1: Defining variables
# rawpath is the 4D data we want to convert to a mask
# imgs is where we want to store the mask and what name we'll give it
# path1 is the data we want to analyze and apply the mask to
# imgs1 is where we want to store the mask and the name we'll give it
rawpath = 'TestData/sub-01 copy/anat/sub-01_T1w.nii.gz'
imgs = 'TestData/mask storage/output.nii'
path1 = 'TestData/sub-01 copy/anat/sub-01_T1w.nii.gz'
imgs1 = 'TestData/mask storage/output1.nii'

print('start')
# Section 2: To create a 3D mask which is an average of the 4D mask
beep = masking.compute_epi_mask(rawpath, lower_cutoff=0.2, upper_cutoff=0.85, memory=imgs, verbose=0)
print(beep)
# Section 3: To apply the mask
boop = masking.apply_mask(path1, beep, dtype='f')
print('embark on a mission')
print(boop)
