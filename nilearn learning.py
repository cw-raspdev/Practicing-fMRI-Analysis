# import nilearn as nil
# from nilearn import plotting
# plotting.show()
# # help(nil)
#
# # Change the file path to your path
# path = 'TestData/sub-01 copy/func/sub-01_task-Feature_run-01_bold.nii.gz'
# imgs = 'TestData/joblib/nilearn/image/image/_compute_mean/1963a433b8dda4c04d2d5bc58733f27e/output.pkl'
# nil.masking.apply_mask(imgs, path, dtype='f', ensure_finite=True)

import nibabel as nib
import matplotlib.pyplot as plt
path = 'TestData/sub-01 copy/anat/sub-01_T1w.nii.gz'
my_img = nib.load(path)
nii_data = my_img.get_fdata()
nii_aff = my_img.affine
nii_hdr = my_img.header
sections = nii_data.shape[2]  # this is how many cross-sections there are
if len(nii_data.shape) == 3:
    for slice_Number in range(nii_data.shape[2]):
        plt.imshow(nii_data[:, :, slice_Number])
        plt.show()
