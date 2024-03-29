"""
I bit this code from geeksforgeeks.com
https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/
"""


# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
 

"""I need to make this into a function so that I can call it from the drone. Eventually, I need to make it so that it can see the centre of the main line.""" 
img = cv2.imread('testimage.png')
points = []

def line_detection(img):
    # Reading the required image in
    # which operations are to be done.
    # Make sure that the image is in the same
    # directory in which this python program is    
    
    # Convert the img to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection method on the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # This returns an array of r and theta values
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    
    
    # The below for loop runs till r and theta values
    # are in the range of the 2d array
    for r_theta in lines:
        
        arr = np.array(r_theta[0], dtype=np.float64)
        r, theta = arr
        # Stores the value of cos(theta) in a
        a = np.cos(theta)
    
        # Stores the value of sin(theta) in b
        b = np.sin(theta)
    
        # x0 stores the value rcos(theta)
        x0 = a*r
    
        # y0 stores the value rsin(theta)
        y0 = b*r
    
        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
        x1 = int(x0 + 1000*(-b))
    
        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
        y1 = int(y0 + 1000*(a))
    
        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
        x2 = int(x0 - 1000*(-b))
    
        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
        y2 = int(y0 - 1000*(a))
        points.extend([x1, y1, x2, y2])
        # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
        # (0,0,255) denotes the colour of the line to be
        # drawn. In this case, it is red.
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
     
    
    # All the changes made in the input image are finally
    # written on a new image houghlines.jpg
    cv2.imwrite('linesDetected.jpg', img)
    return print("success")
"""Now I need to find the largest line"""

def largest_line(points):
    """The strategy is to determine if each line is horizontal or vertical"""
    d = len(points)
    print(d)
    e = d/8
    print(e)
    print(int(e))
    f = int(e)
    width = []
    for i in f:
        """1 is horizontal, 2 is vertical. I am mostly looking for vertical lines, but I need the direction"""
        direction = 1
        if points[i * 8] == -1000:
            direction = 1

        else:
            direction = 2
        
        if direction == 1:
            width.extend(abs(points[(i * 8) + 1] - points[(i*8)+5]))
        else:
            width.extend(abs(points[(i * 8)] - points[(i*8)+4]))


    return width
        
line_detection(img)
print(points)
width = largest_line(points)
print(width)