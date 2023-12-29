# Intruder Detection System using OpenCV and Twilio

This script uses OpenCV to detect human presence through a webcam, capture an image when a human is detected, and send an alert message via Twilio when an intruder is identified.

## Description

The Python script leverages the OpenCV library to detect human presence via a webcam feed. Upon detection, the script captures an image and triggers an alert message via Twilio, notifying about the potential intrusion.

## Features

- Human detection using OpenCV
- Captures an image of the intruder
- Sends an alert message via Twilio
- Stops capturing after detecting 50 instances of human presence

## Installation

1. **Clone the repository:**

2. **Install required libraries:**

3. **Setup Twilio:**
- Sign up for a Twilio account and obtain your Account SID, Auth Token, and Twilio phone number.
- Replace `account_sid`, `auth_token`, `from_`, and `to` fields in the `sendSms()` function with your Twilio credentials and desired phone numbers.

## Usage

1. Run the Python script.
2. Point the webcam towards the area to monitor.
3. Upon detecting a human presence for 50 consecutive frames, the script captures an image and sends an alert message via Twilio.
4. Press `q` to exit the script.

## Files

- `intruder_detection.py`: Contains the Python script for intruder detection.
- `send.py`: Contains Twilio SMS sending functionality.
- `intruders/`: Directory to store captured intruder images.


