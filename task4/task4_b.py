import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    # Resize to half
    half_frame = cv2.resize(frame, (w//2, h//2))

    # Converting to grayscale
    gray = cv2.cvtColor(half_frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Half Size Grayscale", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()