import nilearn as nil
from nilearn import masking
# help(nil)

# Change the file path to your path
path = 'TestData/sub-01 copy/anat/sub-01_T1w.nii.gz'
imgs = 'TestData/joblib/nilearn/image/image/_compute_mean/1963a433b8dda4c04d2d5bc58733f27e/output.nii'
masking.apply_mask(imgs, path, dtype='f', ensure_finite=True)

