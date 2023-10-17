import matplotlib.pyplot as plt
import numpy as np
 
arr= np.full((512 ,512,100),-1000)
arr[1][1] = -500
arr[2][2] = 0
arr[3] [3]= 100
for index in range (arr.shape[2]):
    plt.imshow(arr[:,:,index],cmap='grey')
    plt.title(f'Slice {index + 1}')
    plt.axis('off')
    plt.savefig(f'D://slice_{index + 1}.png')
