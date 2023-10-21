import matplotlib.pyplot as plt
import numpy as np
 

# draw cricle
def draw_circle(matrix, center_row, center_col, radius, value):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if (i - center_row)**2 + (j - center_col)**2 <= radius**2:
                matrix[i][j] = value
# draw sqaure
def draw_square(matrix,start_point,center_point,half_side_length,value):
    start_row,end_row = start_point - half_side_length,start_point +half_side_length
    start_col,end_col = center_point - half_side_length,center_point +half_side_length
    matrix[start_row:end_row,start_col:end_col] =value

# draw_square(arr,180,250,10,0)
# draw_circle(arr, 250, 250, 20, -500)
# draw_square(arr,420,250,30,100)


for index in range (1,100):
    arr= np.full((512 ,512,100),-1000)
    if index == 1:
       draw_square(arr,180,250,10,0)
    elif  2<=index<=51:
        draw_square(arr,180,250,10,0)
        draw_circle(arr, 250, 250, 20, -500)
    else:
        draw_square(arr,180,250,10,0)
        draw_circle(arr, 250, 250, 20, -500)
        draw_square(arr,420,250,30,100)
    plt.imshow(arr[:,:,index],cmap='grey')
    plt.title(f'Slice {index + 1}')
    plt.axis('off')
    plt.savefig(f'D://slice_{index + 1}.png')

