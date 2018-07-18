# Guide
## Installation
* Installed on Windows 10
* Make sure CMake, OpenCV, and MS Visual Studios are installed
* OpenCV should be set-up in the Environment Variables
* CMake may require a direct pointer to Eigen3 and to OpenCV in its interface
* The windows version can be downloaded using git from the following command:
```
 git clone https://github.com/Phylliida/orbslam-windows
```
The README file will have a more detailed installation guide <br />
The original code can be found at https://github.com/raulmur/ORB_SLAM2

## Usage
* Make sure to run from the terminal
* For all executions, make sure to navigate to the orbslam-windows directory in the terminal

*Note that the only difference between TUM and EuRoC formats that I could find was in how ORB-SLAM interpretted the inputs

Path for TUM format:
```
.\Examples\Monocular\Release\mon_tum.exe Vocabulary\ORBvoc.txt PATH_TO_SETTINGS_FILE PATH_TO_VIDEO_DIRECTORY
```
Path for EuRoC format:
```
.\Examples\Monocular\Release\mono_euroc.exe Vocabulary\ORBvoc.txt PATH_TO_SETTINGS_FILE PATH_TO_VIDEO_DIRECTORY PATH_TO_TIMESTAMP_FILE
```
Path for webcam:
```
.\Examples\Monocular\Release\mono_webcam.exe Vocabulary\ORBvoc.txt PATH_TO_SETTINGS_FILE
```
Other formats can be found [here](https://github.com/raulmur/ORB_SLAM2)

## Settings File
* The settings file should be in the .yaml file format
* An example settings file has been included in this repository that works for the TUM, EuRoC, and webcam formats
* More examples for each format specifically can be found in the Examples folder of the orbslam-windows directory
* For the framerate setting, I found that 25 worked best for TUM and 20 worked best for EuRoC and webcam in general although this would change based on the video and webcam
* The fx, fy, cx, cy, k1, k2, p1, p2, and k3 values can be found using OpenCV <br />

The code for calibration can be found at the following directory:
```
PATH_TO_OPENCV_DIRETORY\sources\samples\cpp\tutorial_code\calib3d\camera_calibration
```
Copy this code into a blank c++ file in a new project in Visual Studios. The compiler should be set to DEBUG mode and x64. To run the compiler, make sure to set up the properties:
1. Right click on the solution for the project and select "Properties"
2. Click on C/C++ and edit "Additional Include Directories"
3. Add the following path:
``` PATH_TO_OPENCV_DIRETORY\build\include ```
4. Click on Linker and edit "Additional Libarary Directories"
5. Add the following path: 
``` PATH_TO_OPENCV_DIRETORY\build\x64\vc15\lib ``` <br />
*Note that vc15 may change based on the version of visual studios installed*
6. Click on Linker > Input and edit "Additional Dependencies"
7. Add the following: opencv_world341d.lib <br />
*Note that this is not a file directory but rather the name of a file being directly referenced*

From the OpenCV camera_calibration directory copy the "in_VID5.xml" and "out_camera_data.yml" files and place them in the folder that contains the .vcxproj files of the visual studios calibration project. Rename the "in_VID5.xml" file to "default.xml". For calibration, a checkerboard pattern should be used where each tile should be a square. Here is the one provided by OpenCV: https://docs.opencv.org/3.1.0/pattern.png. Open "default.xml" and change the width and height to the number of internal corners visible on the checkerboard. The squareSize should be the actual size of one of the square's sides in millimeters. Input should be the path to the video file of the checkerboard. Make sure the checkerboard remains rigid while filming. The file works best in .avi format. The desired values will be outputted to the "out_camera_data.yml". The values will be given as:
```
[fx, 0, cx, 0, fy, cy, 0, 0, 1]
[k1, k2, p1, p2, k3]
```

## Video Directories
Only the TUM and EuRoC formats require video directories. The webcam will take its input from the connected webcam and this can most likely be editted in the "mono_webcam.cc" file by changing the webcam ID although I did not get a chance to test this. <br />

For both TUM and EuRoC the video needs to be converted into individual frames and a timestamp file needs to be created. To turn it into individual frames, I used VLC although any method will work. With VLC, navigate to ```C:\Program Files (x86)\VideoLAN\VLC``` or wherever the vlc.exe file is located in the command line. Then run the following command:
```
vlc.exe "PATH_TO_VIDEO" --video-filter=scene --scene-ratio=1 --scene-path="PATH_TO_OUTPUT_FOLDER" vlc://quit
```
To create the timestampfile, run either "tum_time.py" or "euroc_time.py" to generate the file. Make sure to open the code before running it and set the "direc" variable to the location of the images and the "increment" variable to the total length of the video divided by the number of images to 6 decimal places. The original image files will be renamed to a format that can be read by ORB-SLAM. <br />
*Note that this will rename the files so a copy should be made of the original images first*

 ### For TUM Format
 Rename the folder with the renamed images to "rgb". The timestamp file should automatically be named "rgb.txt" but if it is not, change it. Place both of these in a folder. The name of this folder will be the PATH_TO_VIDEO_DIRECTORY
 
 ### FOR EuRoC Format
 Rename the folder with the renamed images to "data". This is the PATH_TO_VIDEO_DIRECTORY.
