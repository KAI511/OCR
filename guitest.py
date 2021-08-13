import cv2
import easyocr
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
a=file_path


IMAGE_PATH = a
reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(IMAGE_PATH)
i=0

img=cv2.imread(IMAGE_PATH)
for detection in result:
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int (val)for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
    img=cv2.putText(img,text,top_left,font,0.5,(0,0,255),2,cv2.LINE_AA)
    print(result[i])
    i=i+1
    
plt.figure(figsize=(10,10))
plt.imshow(img)  
plt.show()