import csv
import numpy as np
from matplotlib import pyplot as plt
import glob
# ====================================================================================================
# pathfile = "C:/Users/Katelin Folder/Pathlib/FilePath.txt"  Must be hardcoded in Python
#
#  The filepath for the data file must be specified in the FilePath.txt file on the Pathlib Folder
#      the filepath found in the file will be used to indentify the location of the following files

#  1. Input HRF Data .txt file
#  2. Input Stimulas .txt file
#
#  You can use as may file as you like
# ====================================================================================================
# HRF data plotted Signal over Time
# ====================================================================================================
def plot_hrf_figure(hrf):
    plt.rcParams.update({'font.size': 14})
    # set the length of the hrf array and set the time_vector range
    hrf_len = len(hrf)  # each = 1 second
    time_vector = range(0, hrf_len)
    # =================================================================================================
    plt.figure(figsize=(10, 5))
    plt.plot(time_vector, hrf, 'o-')  # can use x- for plotting with x
    plt.xlabel('Time (seconds)')
    plt.ylabel('fMRI signal')
    plt.title('The HRF data plotted Signal over Time')
    plt.grid(color='k', linestyle=':')  # Dotted-line grid on top of the plot/Color k=black

# ====================================================================================================
# Plot
#   1 Time-series of stim
#   2 Stimulus time-series convolved with HRF
#     can use 1 or stim stimuli time series
# ====================================================================================================
def plot_hrf_2_figure(hrf, stim1 ,stim2):
    plt.rcParams.update({'font.size': 14})
    stim_count = 0
    if len(stim1) > 0:
        stim_count = 1
    if len(stim2) == len(stim1):
        stim_count = 2

    if stim_count == 1:
        all_stim = stim1
    elif stim_count == 2:
        all_stim = stim1 + stim2

    hrf_convolved_with_stim_time_series = np.convolve(all_stim,hrf)

    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    plt.stem(all_stim, label='1 Time-series of stim')
    plt.grid(color='k', linestyle=':')
    plt.legend()
    plt.axis([0, 60, 0, 1.5])
    plt.xlabel('Time (seconds)')
    plt.ylabel('Stimulus present / absent')
    plt.title('HRF Stimulus time-series')

    #===========================================================================================

    plt.subplot(3, 1, 3)  # Draw in the second subplot
    plt.plot(hrf_convolved_with_stim_time_series, 'rx-', \
             label='Stimulus time-series convolved with HRF')
    plt.legend()
    plt.axis([0, 60, -3, 25])
    plt.xlabel('Time (seconds)')
    plt.ylabel('fMRI signal')
    plt.grid(color='k', linestyle=':')

# ====================================================================================================
# 1 Time-series of stim
# 2 Stimulus time-series convolved with HRF
# 3 HRF from 3 stimuli
#   3.1 HRF from first stimulas 1
#   3.2 HRF from second stimulas 2
#   3.3 HRF from third stimulas 3
# ====================================================================================================
def plot_hrf_3_figure(hrf, stim1, stim2, stim3):
    plt.rcParams.update({'font.size': 14})
    stim_count = 0
    if len(stim1) > 0:
        stim_count = stim_count + 1
        if len(stim2) > 0:
            stim_count = stim_count + 1
            if len(stim3) > 0:
                stim_count = stim_count + 1

    if stim_count < 2:
        print('plot_hrf_2_figure needs at lest 2 stim only found ', stim_count)
        return []

    if stim_count == 2:
        all_stim = stim1 + stim2
        hrf_convolved = np.convolve(all_stim,hrf)
        hrf_from_stim1 = np.convolve(stim1,hrf)
        hrf_from_stim2 = np.convolve(stim2,hrf)
    else:
        all_stim = stim1 + stim2 + stim3
        hrf_convolved = np.convolve(all_stim,hrf)
        hrf_from_stim1 = np.convolve(stim1,hrf)
        hrf_from_stim2 = np.convolve(stim2,hrf)
        hrf_from_stim3 = np.convolve(stim3,hrf)

    plt.figure(figsize=(10, 15))
    plt.subplot(3,1,1)
    plt.stem(all_stim,label='1 Time-series of stim')
    plt.legend()
    plt.axis([0, 60, 0, 1.2])
    plt.xlabel('Time (seconds)')
    plt.ylabel('Stimulus present / absent')
    plt.grid(color='k',linestyle=':')
    plt.title('Time-series of Stimulus  + Convolved HRF + HRF')

    #=================================================================================================

    plt.subplot(3,1,2)
    plt.plot(hrf_convolved,'rx-', \
             label='Stimulus time-series convolved with HRF')

    plt.legend()
    plt.axis([0, 60, -2, 30])
    plt.xlabel('Time (seconds)')
    plt.ylabel('fMRI signal')
    plt.grid(color='k',linestyle=':')

    #=================================================================================================

    plt.subplot(3, 1, 3)
    plt.plot(hrf_from_stim1,'b-',label='HRF from first stim')
    plt.plot(hrf_from_stim2,'m--',label='HRF from second stim')
    if stim_count == 3:
        plt.plot(hrf_from_stim3,'g-',label='HRF from third stim')

    plt.legend()
    plt.axis([0, 60, -2, 20])
    plt.xlabel('Time (seconds)')
    plt.ylabel('fMRI signal')
    plt.grid(color='k',linestyle=':')

# ====================================================================================================
# Read text file as CSV Function
# ====================================================================================================
def readHRFlist(HRFfile):
    # Read CSV file that contains the HRF Data to plot
    with open(HRFfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        hpf_file1 = []
        for row in csv_reader:
            hpf_file1 = row
            line_count += 1

    # convert input data from file to a numeric array
    # example: [1, 2, 3]
    hpf_file2 = []
    for i in range(1, len(hpf_file1)):
        x1 = float(hpf_file1[i])
        hpf_file2.append(x1)

    return hpf_file2

# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

plt.rcParams.update({'font.size': 14})

# ====================================================================================================
# Set File Path for all input files
# Set input file names
# ====================================================================================================
# pathfile = open(r"C:/Users/Rachel/Documents/Katelin Folder/Pathlib/FilePath.txt","r")
# filepath = pathfile.readline()
# pathfile.close()
# ====================================================================================================

# ====================================================================================================
# Change here to run program with your files
# ====================================================================================================
filepath = '/Users/katelinferreira/Desktop/DataFolder'
#filepath = 'DataFolder/'
HRF_file_name   = '/InputHRFData.txt'
Stim1_file_name = '/Inputstim1.txt'
Stim2_file_name = '/Inputstim2.txt'
Stim3_file_name = '/Inputstim3.txt'
# ====================================================================================================

input_file_fullpath = filepath[0:len(filepath)] + HRF_file_name
stim1_file_fullpath = filepath[0:len(filepath)] + Stim1_file_name
stim2_file_fullpath = filepath[0:len(filepath)] + Stim2_file_name
stim3_file_fullpath = filepath[0:len(filepath)] + Stim3_file_name

# ====================================================================================================
# Set the Fullpath file names
# ====================================================================================================

print('\nInput Filepath List\n')
print('Filepath1:', input_file_fullpath)
print('Filepath2:', stim1_file_fullpath)
print('Filepath3:', stim2_file_fullpath)
print('Filepath4:', stim3_file_fullpath)

# ====================================================================================================
# Read the file data
# ====================================================================================================

hrf   = np.array(readHRFlist(input_file_fullpath))
stim1 = np.array(readHRFlist(stim1_file_fullpath))
stim2 = np.array(readHRFlist(stim2_file_fullpath))
stim3 = np.array(readHRFlist(stim3_file_fullpath))

# ====================================================================================================
# Print the input HRF and stimulas data
# ====================================================================================================

#print('\nInput File Data\n')
#print('hrf:',hrf)
#print('stim1:',stim1)
#print('stim2:',stim2)
#print('stim3:',stim3)

# ===================================================================================================================
# Create the Plots
# ===================================================================================================================

plot_hrf_figure(hrf)

plot_hrf_2_figure(hrf, stim1, [])
plot_hrf_2_figure(hrf, stim1, stim2)

plot_hrf_3_figure(hrf, stim1, stim2, [])
plot_hrf_3_figure(hrf, stim1, stim2, stim3)
plt.show()
#Created by Katelin Ferreira, 30 hrs 
