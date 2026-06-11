#Python Script by the Student
import cv2

#Operation1:
frame = cv2.imread("robot_vision.jpg")

#Operation2: Converting color space
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Operation3: Drawing a bounding box
cv2.rectangle(gray_frame,(10,10),(100,100),(0,255,0),3)

#Operation4: Displaying the result
cv2.imshow("Robot Vision", gray_frame)
cv2.waitKey(1)


"""
A.(wrong)- OpenCV loads color images in BGR order by default not RGB
---> Blue, Green, Red

B.(Correct)- gray_frame is a single-channel image (_, _, 1) not ( _, _, 3). and the color tuple (0,255,0) is intended for a 3_channel BGR image

c.(Correct) -waitKey(1) is waits only for 1 milliseconds

D.(Incorrect)- (10,10) - top-left corner & (100,100) - bottom-right corner of the rectangle. Not the center and width/height

"""