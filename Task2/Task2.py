import cv2
import time

# Open webcam
cap = cv2.VideoCapture(0)

# Variables for FPS calculation
prev_time = 0

img_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Calculating FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    # Display FPS on frame
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show webcam feed
    cv2.imshow("Webcam Feed", frame)


    key = cv2.waitKey(1) & 0xFF


    if key == ord('s'):   #when save when s key is pressed
        filename = f"image_{img_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        img_count += 1

    # Exit when 'q' is pressed
    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()