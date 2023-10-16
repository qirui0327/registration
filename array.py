from PIL import Image as im 
import numpy as np
 
arr= np.full((512 ,512),-1000)
arr[1][1] = -500
arr[2][2] = 0
arr[3] [3]= 100
img  = im.fromarray(arr) 
img.save("D://Image_from_array.png")
print(arr)