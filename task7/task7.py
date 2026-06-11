import cv2
import mediapipe as mp
import math

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# LED state
led_on = False

# To prevent continuous toggling
pinch_detected = False

# Distance threshold
THRESHOLD = 40

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            # Thumb tip (4)
            thumb = hand_landmarks.landmark[4]

            # Index tip (8)
            index = hand_landmarks.landmark[8]

            x1, y1 = int(thumb.x * w), int(thumb.y * h)
            x2, y2 = int(index.x * w), int(index.y * h)

            # Draw points
            cv2.circle(frame, (x1, y1), 10, (255, 0, 255), -1)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)

            # Distance calculation
            distance = math.hypot(x2 - x1, y2 - y1)

            cv2.putText(frame,
                        f"Dist: {int(distance)}",
                        (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 255, 255),
                        2)

            # Toggle LED on pinch
            if distance < THRESHOLD and not pinch_detected:
                led_on = not led_on
                pinch_detected = True

            # Reset when fingers separate
            elif distance > THRESHOLD + 15:
                pinch_detected = False

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # LED Indicator
    led_color = (0, 255, 0) if led_on else (0, 0, 255)

    cv2.circle(frame, (80, 100), 30, led_color, -1)

    status = "ON" if led_on else "OFF"
    cv2.putText(frame,
                f"LED {status}",
                (130, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                led_color,
                2)

    cv2.imshow("Pinch LED Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # ESC
        break

cap.release()
cv2.destroyAllWindows()