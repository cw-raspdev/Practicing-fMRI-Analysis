import nibabel as nib
import matplotlib.pyplot as plt

# Change the file path to your path -- or run it as-is, using the example file.
path = 'sub-01_task-Digit_run-01_bold.nii.gz'
my_img = nib.load(path)
nii_data = my_img.get_fdata()
nii_aff = my_img.affine
nii_hdr = my_img.header
sections = nii_data.shape[2]  # this is how many cross-sections there are

print(nii_data.shape)

viewtype = input('--------\n'
                 'Welcome. Please input the corresponding # if you would like to:\n'
                 ' 1) View one cross section for a specific range of time\n'
                 ' 2) View a specific range of cross sections for one point in time\n'
                 'Enter Input Here:')
if viewtype == '1':
    usersection1 = input('Which cross section? Please input an integer between 0 and '+str(nii_data.shape[2]-1)+':\n')
    usersection1 = int(usersection1)
    if len(nii_data.shape) == 3:
        print('Thank you. Now analyzing NIFTI file. Beep boop beep')
        plt.imshow(nii_data[:, :, usersection1])
        plt.show()
    elif len(nii_data.shape) == 4:
        usertime1 = input('What is initial time in range? Please input an integer between 0 and '+str(nii_data.shape[3]-1)+':\n')
        usertime2 = input('What is final time in range? Please input an integer between 0 and '+str(nii_data.shape[3]-1)+':\n')
        usertime1, usertime2 = int(usertime1), int(usertime2)
        print('Thank you. Now analyzing NIFTI file. Beep boop beep')
        for frame in range(usertime1, usertime2):
            plt.imshow(nii_data[:, :, usersection1, frame])
            plt.show()
elif viewtype == '2':
    usersection1 = input('What is initial section in range? Please input an integer between 0 and '+str(nii_data.shape[2]-1)+':\n')
    usersection2 = input('What is final section in range? Please input an integer between 0 and '+str(nii_data.shape[2]-1)+':\n')
    usersection1, usersection2 = int(usersection1), int(usersection2)
    if len(nii_data.shape) == 3:
        print('Thank you. Now analyzing NIFTI file. Boop beep boop')
        for frame in range(usersection1, usersection2):
            plt.imshow(nii_data[:, :, frame])
            plt.show()
    elif len(nii_data.shape) == 4:
        usertime1 = input('Which point in time? Please input an integer:\n')
        usertime1 = int(usertime1)
        print('Thank you. Now analyzing NIFTI file. Boop beep boop')
        for frame in range(usersection1, usersection2):
            plt.imshow(nii_data[:, :, frame, usertime1])
            plt.show()
else:
    print('Sorry, your input was not recognized. Please try again.')
