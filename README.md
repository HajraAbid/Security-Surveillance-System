# Security Surveillance System with Face Recognition and Alarm

## Overview

This **Security Surveillance System** utilizes **face recognition** to identify individuals in real-time. When a recognized person is detected, their name and timestamp are logged in an attendance file. If an **unrecognized face** is detected, an **alarm** is triggered to alert the user.

## Features
- Real-time **face recognition** using the webcam.
- **Automatic attendance logging** in a CSV file.
- **Alarm trigger** when an unrecognized face is detected.
- Customizable alarm sound.

## Requirements
- Python 3.x
- OpenCV
- face_recognition
- numpy
- winsound (Windows only)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/security-surveillance.git
Install the required Python packages:


pip install opencv-python face_recognition numpy
Place images of known individuals in the basic images folder for recognition.

Usage
Run the script to start the security surveillance system:


python security_surveillance.py
The system will use the webcam to monitor faces in real-time.

Recognized faces will be logged in an AttendanceRec.csv file.

Unrecognized faces will trigger an alarm sound.

Press q to exit the program.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
