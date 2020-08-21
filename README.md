# darknet-yolo
Darknet for YOLOv3 with screenshot and beep function as well as GPS Overlay

## Contents
1. Description
2. Architecture of Solution
2. Setup and Explanation
3. Results
4. Built with:
5. Credits and Contact

## 1. Description
YOLO, “You Look Only Once”, is an algorithm capable of detecting what is in an image and where stuff is, in one pass. It gives the bounding boxes around the detected objects, and it can detect multiple objects at a time. It is able to process up to 45 frames per second with a slight drop in accuracy. Thus making it a very good choice when real-time detection needed, without loss of too much accuracy. It uses darknet as a training frame for custom detection.

To be able to further push the limits, darknet is being compiled with CUDA, cuDNN and OpenCV to allow for GPU usage. This decreases the training time and increase detection speed and frames.

## 2. Architecture of Solution
Not applicable

## 3. Setup and Explanation
#### Main
Refer to my documentation link  

#### Add ons

###### Auto screenshot upon detection
Navigate to this directory: darknet/src and open ‘image.c’. Scroll down to line 308. This line of code is responsible for performing a screenshot upon detection and drawing of boundary boxes. 

- system is a C programming command to activate terminal on Ubuntu
- scrot translate to screenshot, self explanatory
- ~/darknet/screenshots/%b%d::%H%M%S.jpeg -q100 sets the directory to store the image as date and time with minimal compression

###### Beeping sound upon detection
Navigate to this directory: darknet/src and open ‘image.c’. Scroll down to line 309. This line of code is responsible for beeping upon detection and drawing of boundary boxes.

- fprintf(stdout, "\aBeep!\n" ) outputs a beeping sound and print ‘Beep’ on the terminal

###### GPS data overlay on detection frame
Navigate to this directory: darknet/src and open ‘image_opencv.cpp Scroll down to line 6 and 8.

- #include "iostream" and using namespace std; are just declarations

Further scroll down to line 106 to 109.

- std::string GPS; is to declare GPS variable as string
- ifstream FileGPS("GPS.txt"); is to initialize the text file containing GPS data
- FileGPS >> GPS; is to store the GPS data from the text file into the GPS variable declared above
- putText(m, GPS, Point(0, 470), FONT_HERSHEY_SIMPLEX, 0.4, CV_RGB(199, 21, 133), 0.1); is to set the parameters for insert GPS data into the frame

## 4. Results
Upon detection, a pink boundary box will appear for visual impact. When the pink boundary box appears, a screenshot will be made and stored to a specified directory for further analysis. A beeping sound will be produced as well for auditory impact.

For areas with GPS, live GPS coordinates will be shown on the feed.

## 5. Built with:
- CUDA
- cuDNN
- OpenCV

## 6. Credits and Contact
Full credits goes to: https://github.com/pjreddie/darknet

Feel free to contact me regarding any questions

>>Ian: ianlim0309@gmail.com
