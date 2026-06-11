import cv2

# Read image
img = cv2.imread("Task3/noiseImg.png")

if img is None:
    print("Error: Image not found!")
    exit()

# Denoise image
denoised = cv2.fastNlMeansDenoisingColored(
    img,
    None,
    h=10,
    hColor=10,
    templateWindowSize=7,
    searchWindowSize=21
)

# Calculate pixels
height, width, channels = img.shape
total_pixels = height * width

print("Width:", width)
print("Height:", height)
print("Total Pixels:", total_pixels)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Denoised", denoised)

cv2.imwrite("Denoise_img.png", denoised)

cv2.waitKey(0)
cv2.destroyAllWindows()