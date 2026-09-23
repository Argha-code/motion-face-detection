# Motion-Triggered Face Detection & Alert System

A computer-vision and embedded-system project that combines a PIR motion sensor with real-time face detection using Python, OpenCV, and CVZone. An Arduino UNO controls an LED and buzzer based on the detected conditions.

## Features

* PIR-based motion detection
* Real-time face detection using OpenCV and CVZone
* Serial communication between Python and Arduino UNO
* LED and buzzer alert when motion and a face are detected
* Handles different motion/face detection conditions

## System Logic

| PIR Motion | Face Detection | Result                                 |
| ---------- | -------------- | -------------------------------------- |
| No motion  | No face        | No motion and no face                  |
| Motion     | No face        | Motion detected, but face not detected |
| Motion     | Face           | Motion and face detected               |

## Technologies Used

* Python
* OpenCV
* CVZone
* Serial Communication
* Arduino UNO
* PIR Motion Sensor
* LED
* Buzzer

## Hardware

* Arduino UNO
* PIR motion sensor
* LED
* 220Ω resistor
* Buzzer
* USB cable
* Computer/laptop with webcam

## Pin Connections

| Component | Arduino Pin |
| --------- | ----------- |
| PIR OUT   | D2          |
| LED       | D8          |
| Buzzer    | D9          |

