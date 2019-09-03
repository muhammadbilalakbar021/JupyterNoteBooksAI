import cv2
import numpy as np
# read image
img = cv2.imread('images13/image1.jpg', cv2.IMREAD_UNCHANGED)
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
height1 = img.shape[0]/2
width1 = img.shape[1]/2
channels = img.shape[2]
print('Image Dimension    : ', dimensions)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Image midHeight1       : ', height1)
print('Image midWidth1        : ', width1)

arr=np.asarray(img,dtype="int32")
print(arr)

x1=0
y1=0
x2=height
y2=width

print("Point1 =" , arr[x1][int((y2-y1)/2)])
print("Point2 =" , arr[int((x2-x1)/2)][y2-1])
print("Point3 =" , arr[x2-1][int((y2-y1)/2)])
print("Point4 =" , arr[int((x2-x1)/2)][y1])
print("midpoint of image",arr[int(height1)][int(width1)])