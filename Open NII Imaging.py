import nibabel as nib
import matplotlib.pyplot as plt

# Change the path to your path
path = 'sub-01 copy/func/sub-01_task-Digit_run-01_bold.nii'
my_img = nib.load(path)
nii_data = my_img.get_fdata()
nii_aff = my_img.affine
nii_hdr = my_img.header
sections = nii_data.shape[2]  # this is how many cross-sections there are
time = nii_data.shape[3] # this is how many seconds(?) passed while subject was doing the task
print(nii_aff, '\n', nii_hdr)
print(nii_data.shape)

viewtype = input('---------------------------------------------------------------------\n'
                 'Welcome. Please input the corresponding # if you would like to:\n'
                 ' 1) View one cross section for a specific range of time\n'
                 ' 2) View a specific range of cross sections for one point in time\n'
                 'Enter Input Here:')
if viewtype == '1':
    usersection1 = input('Which cross section? Please input an integer:\n')
    usertime1 = input('What is initial time in range? Please input an integer:\n')
    usertime2 = input('What is final time in range? Please input an integer:\n')
    usersection1, usertime1, usertime2 = int(usersection1), int(usertime1), int(usertime2)
    print('Thank you. Now analyzing NIFTI file. Beep boop beep')
    for frame in range(usertime1, usertime2):
        plt.imshow(nii_data[:, :, usersection1, frame])
        plt.show()
elif viewtype == '2':
    usertime1 = input('Which point in time? Please input an integer:\n')
    usersection1 = input('What is initial section in range? Please input an integer:\n')
    usersection2 = input('What is final section in range? Please input an integer:\n')
    usertime1, usersection1, usersection2 = int(usertime1), int(usersection1), int(usersection2)
    print('Thank you. Now analyzing NIFTI file. Boop beep boop')
    for frame in range(usersection1, usersection2):
        plt.imshow(nii_data[:, :, frame, usertime1])
        plt.show()
else:
    print('Sorry, your input was not recognized. Please try again.')

# if userdata == 'all':
# #   if len(nii_data.shape) == 3:
# #       for slice_Number in range(nii_data.shape[2]):
# #           plt.imshow(nii_data[:, :, slice_Number])
# #           plt.show()
#     if len(nii_data.shape) == 4:
#         for frame in range(nii_data.shape[3]):
#             for slice_Number in range(nii_data.shape[2]):
#                 if sections > 0:
#                     plt.imshow(nii_data[:, :, slice_Number, frame])
#                     plt.show()
#                     sections = sections - 1
# else:
#     userdata = int(userdata)
# #   if len(nii_data.shape) == 3:
# #       for slice_Number in range(nii_data.shape[2]):
# #           plt.imshow(nii_data[:, :, slice_Number])
# #           plt.show()
#     if len(nii_data.shape) == 4:
#         for frame in range(nii_data.shape[3]):
#             plt.imshow(nii_data[:, :, userdata, frame])
#             plt.show()
#             sections = sections - 1



