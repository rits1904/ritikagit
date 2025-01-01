import cv2
import os
import numpy as np
import random

folder_path = "//home//ritika//task_3//Task"

image_files = sorted([f for f in os.listdir("//home//ritika//task_3//Task") if f.endswith(('.jpg','.png','.jpeg'))])
fire_images = sorted([f for f in image_files if f.startswith("fire")])
office_images = sorted([f for f in image_files if f.startswith("o")])

if len(fire_images) != len(office_images):
    print("invalid length, add more images!!")
    exit()

for fire , office in zip(fire_images,office_images):
    fire_img = cv2.imread(os.path.join("//home//ritika//task_3//Task",fire))
    office_img = cv2.imread(os.path.join("//home//ritika//task_3//Task",office))

    fire_img_resized = cv2.resize(fire_img,(100,100))
    fire_h, fire_w = fire_img_resized.shape[:2]
    y_offset = random.randint(0,office_img.shape[0]-fire_h)
    x_offset = random.randint(0,office_img.shape[1]-fire_w)
    office_img[y_offset:y_offset + fire_h, x_offset:x_offset + fire_w] = fire_img_resized
    cv2.imshow("imposed image",office_img)
    cv2.waitKey(0)
    print("this is my code!!")
    
    
   
