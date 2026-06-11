import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #Original Footage
    cv2.imshow("Original Footage",frame)
    # Remove mirror effect
    frame = cv2.flip(frame, 1)   # Horizontal flip

    cv2.imshow("Corrected Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()