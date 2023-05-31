#encoding: utf-8
import numpy as np

def power_diff_numpy(input_x,input_y,input_z):
    # TODO:完成numpy实现的过程，参考实验教程示例
    #--------------------------------------------------#
    x_shape = np.shape(input_x)
    y_shape = np.shape(input_y)
    x_new_shape = np.reshape(input_x, (-1, y_shape[-1]))
    y = np.reshape(input_y, (-1))
    output = []
    # 通过循环完成计算，每次循环计算y个数的PowerDifference操作
    for i in range(x_new_shape.shape[0]):
        output.append(np.power(x_new_shape[i, :] - y, input_z))
    output = np.reshape(output, x_shape)
    #--------------------------------------------------#
    return output

