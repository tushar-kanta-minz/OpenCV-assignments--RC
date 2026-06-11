import cv2
import mediapipe as mp
import numpy as np

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

mp_draw = mp.solutions.drawing_utils

# Open Camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read first frame
ret, frame = cap.read()

if not ret:
    print("Cannot access camera")
    exit()

# Create canvas
h, w, _ = frame.shape
canvas = np.zeros((h, w, 3), dtype=np.uint8)

prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Problem in video capture")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Index finger tip
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            # Index finger lower joint
            y_pip = int(hand_landmarks.landmark[6].y * h)

            # Draw when index finger is up
            if y < y_pip:

                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                cv2.line(
                    canvas,
                    (prev_x, prev_y),
                    (x, y),
                    (0, 255, 0),
                    5
                )

                prev_x, prev_y = x, y

            else:
                prev_x, prev_y = 0, 0

    # Overlay drawing on webcam frame
    output = cv2.addWeighted(frame, 1, canvas, 1, 0)

    # Instructions
    cv2.putText(
        output,
        "S: Save  C: Clear  Q: Quit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.imshow("Virtual Drawing Board", output)

    key = cv2.waitKey(1) & 0xFF

    # Save Drawing
    if key == ord('s'):
        cv2.imwrite("drawing.png", canvas)
        print("Drawing saved as drawing.png")

    # Clear Drawing
    elif key == ord('c'):
        canvas[:] = 0
        print("Canvas Cleared")

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()