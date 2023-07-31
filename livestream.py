import cv2

capture = cv2.VideoCapture("http://192.168.138.214:8080/video")

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if not ret:  # Check if video capture is successful
        print("Error: Unable to capture video.")
        break

    cv2.imshow('livestream', frame)

    if cv2.waitKey(1) == ord('\r'):  # Use ord('\r') for the Enter (carriage return) key
        break

capture.release()
cv2.destroyAllWindows()
