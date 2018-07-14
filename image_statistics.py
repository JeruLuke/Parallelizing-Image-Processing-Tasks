import os
import cv2

path = r'C:\Users\Jackson\Desktop'
img_formats = ['.png', '.jpg', '.jpeg']

overall_size = 0
count = 0
for  f in os.listdir(path):
    if any(c in f for c in img_formats):
        img = cv2.imread(os.path.join(path, f))
        overall_size+= img.size
        count+= 1

print('Collective size of all {} images in the predefined path is {} MB'.format(count, overall_size/10**6))
