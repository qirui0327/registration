import matplotlib.pyplot as plt
import numpy as np
 
arr= np.full((512 ,512,100),-1000)
start_point = [200,300,400]
square_value = [-500,0,100]
for i in range(len(start_point)):
    print(i)
    start_row,end_row = start_point[i] - 15,start_point[i] +15
    start_col,end_col = start_point[i] - 15,start_point[i] +15
    arr[start_row:end_row,start_col:end_col] =square_value[i]

for index in range (arr.shape[2]):
    plt.imshow(arr[:,:,index],cmap='grey')
    plt.show()
    plt.close()

