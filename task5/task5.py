import cv2
import numpy as np


image = cv2.imread("task5\colorFullImg.png")

if image is None:
    print("Image not found!")
    exit()

#Extracting Blue,Green, and Red channels 
blue, green, red = cv2.split(image)

#Operations

blue_img = cv2.merge([blue, np.zeros_like(blue), np.zeros_like(blue)])
green_img = cv2.merge([np.zeros_like(green), green, np.zeros_like(green)])
red_img = cv2.merge([np.zeros_like(red), np.zeros_like(red), red])
green_removed = cv2.merge([blue, np.zeros_like(green), red])

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Blue Channel", blue_img)
cv2.imshow("Green Channel", green_img)
cv2.imshow("Red Channel", red_img)
cv2.imshow("Merged Without Green", green_removed)

# Saving images
cv2.imwrite("blue_channel.png", blue_img)
cv2.imwrite("green_channel.png", green_img)
cv2.imwrite("red_channel.png", red_img)
cv2.imwrite("merged_without_green.png", green_removed)

print("All images saved successfully.")

cv2.waitKey(0)
cv2.destroyAllWindows()