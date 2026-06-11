import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    # Quarter size
    small = cv2.resize(frame, (w//2, h//2))

    # Top-left : Original
    top_left = small

    # Top-right : Vertically Flipped
    top_right = cv2.flip(small, 0)

    # Bottom-left : HSV
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    hsv_display = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Bottom-right : Red Channel Only
    red = np.zeros_like(small)
    red[:, :, 2] = small[:, :, 2]

    # Combine images
    top_row = np.hstack((top_left, top_right))
    bottom_row = np.hstack((hsv_display, red))

    final_output = np.vstack((top_row, bottom_row))

    cv2.imshow("4-Quadrant Webcam", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()