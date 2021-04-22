# boolean-fishes-proj2

README:

This project runs on Python 3.9 and requires python packages nibabel, nilearn, and matplotlib. The majority of the project is about reading single-file NIfTI-1 data, which is stored in the .nii file format. Most of our coding was done in PyCharm and then synced to Github. 

The code HRF Plot Function plots HRF data in signal vs. time graph. It also graphs the number of stimulus added to the patient, makes a graph of the stimulus time series convolved with HRF and plots the HRF data for each stimulus. To run the program you need to download InputHRFData, Inputstim1, Inputstim2, Inputstim3, and change the file path in line 187 variable to be equal to the location where the data files are in your respective computer. The data used is test data, as HRF data could not be extracted from this particular data set, but any data in the format of the test files should produce the same graphs and analysis. 

The script ‘Open NII Imaging’ visualizes nii data - the nii data format holds transverse cross sections of a scanned brain in an array of dimensions (x, y, z, t) where each plane parallel with the xy plane is an image, the z axis counts the number of images, and the t dimension represents the number of times the brain was scanned. For testing purposes, the script can be run as-is, or a different file path can be used. 
Run the script by pressing play (no command required) at which point it will output the dimensions (x, y, z, t). Then follow on-screen instructions because you will be inputting settings for visualization. 
A couple tips: 
1) Viewing a range of the cross-sections of the brain at one point in time is more fun than viewing one cross-section at a range of times. This is because the one cross-section will shift but the time intervals are so small that the shifts are small.

2) please be sure to stay within the threshold for z and t (stay between 0 and z-1, as well as stay between 0 and t-1.) After all inputs are done you should get output of a cross section of a brain. Delete one slide to access the next (there is unfortunately no way to navigate backwards).

The ‘nilearn learning’ script is to mask the data and plot voxel-time graphs of different subsets of data. 
In this, the 4D data from the study (‘ToBeComputed’) is converted to a mask (a subset of voxels we want to analyse). The mask itself is stored as TempMaskStorage, while ToAnalyze contains the data that we want to apply the mask to. The second part creates a 3D mask, which is an average of the 4D mask. The next part then uses the 3D mask (now in an array with numeric data of voxels and time) to plot a voxel-time graph. Run the script by pressing play, and as per the instruction shown, name the mask anything you’d like and press enter for the code to run. 

The ‘z-scoring’ script is a statistical analysis of the masked section of the data. It normalizes the data using the preprocessing package from sklearn. 
After the z-scoring, the next part of the code tests the result by printing the mean and standard deviation of individual voxels. The mean values may not equal exactly zero and the standard deviation may not be exactly 1, but this happens because of rounding and precision limitations. The values are considered equivalent, however, due to how close they are to 0 and 1 respectively. 
The last part of the code will create a histogram of the frequency of the selected voxel means. Since there are over 40,000 datasets, the histogram won’t work for the entire dataset, so we can choose a range within the code. 
