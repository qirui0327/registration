import matplotlib.pyplot as plt
import numpy as np
 
arr= np.full((512 ,512,100),-1000)
start_point = [250,180,420]
square_value = [-500,0,100]
start_row,end_row = start_point[0] - 15,start_point[0] +15
start_col,end_col = 250 - 15,250 +15
arr[start_row:end_row,start_col:end_col] =square_value[0]

start_row,end_row = start_point[1] - 10,start_point[1] +10
start_col,end_col = 250 - 10,250 +10
arr[start_row:end_row,start_col:end_col] =square_value[1]

start_row,end_row = start_point[2] - 15,start_point[2] +15
start_col,end_col = 250 - 30,250 +30
arr[start_row:end_row,start_col:end_col] =square_value[2]

for index in range (arr.shape[2]):
    plt.imshow(arr[:,:,index],cmap='grey')
    plt.show()
    plt.close()

