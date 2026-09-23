import cv2
import serial
import time
from cvzone.FaceDetectionModule import FaceDetector

# Connect Arduino
arduino = serial.Serial("COM3", 9600)
time.sleep(2)

# Open camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not working")
    exit()

# Face detector
detector = FaceDetector(minDetectionCon=0.5)

# Latest PIR status
motion = False

# Previous alert state
alert_on = False

# Previous result
last_result = ""

# Timer
last_print_time = 0

while True:

    # Read all available Arduino messages
    while arduino.in_waiting > 0:

        message = arduino.readline().decode().strip()

        if message == "MOTION":
            motion = True

        elif message == "NO_MOTION":
            motion = False

    # Read camera continuously
    success, frame = camera.read()

    if not success:
        print("Camera not working")
        break

    # Face detection
    frame, faces = detector.findFaces(frame)

    # Check conditions
    if motion and faces:
        result = "Motion and face detected"
        current_alert = True

    elif motion and not faces:
        result = "Motion detected, but face not detected"
        current_alert = False

    elif not motion and faces:
        result = "No motion, but face detected"
        current_alert = False

    else:
        result = "No motion and no face"
        current_alert = False

    # Send only when alert changes
    if current_alert != alert_on:

        if current_alert:
            arduino.write(b'1')
        else:
            arduino.write(b'0')

        alert_on = current_alert

    # Print result only when it changes
    if result != last_result:
        print(result)
        last_result = result

    # Camera window
    cv2.imshow("Face Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Turn OFF
arduino.write(b'0')

arduino.close()
camera.release()
cv2.destroyAllWindows()