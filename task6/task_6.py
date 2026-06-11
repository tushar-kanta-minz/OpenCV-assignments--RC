import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Initial kernel size (must be odd)
blur_size = 5

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)

    # Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)

    # Display kernel size on image
    cv2.putText(
        blurred,
        f"Blur Kernel: {blur_size}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255),
        2
    )

    cv2.imshow("Blurred Feed", blurred)
    cv2.imshow("Canny Edges", edges)

    key = cv2.waitKey(1) & 0xFF

    # Increase blur
    if key == ord('w'):
        blur_size += 2

    # Decrease blur
    elif key == ord('s'):
        blur_size -= 2
        if blur_size < 1:
            blur_size = 1

        if blur_size % 2 == 0:
            blur_size += 1

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()