import numpy as np
import random, copy

def array_clustering(num_array):
    return_list = []

    if type(num_array) == list:
        num_array.sort()
    else:
        raise Exception('num_array must be type of list')
    max_num_element = []
    max_num = max(num_array)
    count_num = 0
    num_var_all = np.var(num_array)  # 总体离散
    avr_num_var_all = num_var_all / len(num_array)  # 平均离散

    while num_array:

        num_var = np.var(num_array)  # 当前总体离散
        avr_num_var = num_var / len(num_array)  # 当前平均离散
        if avr_num_var > max_num:
            max_num_element.append(num_array.pop(num_array.index(max(num_array))))
            continue
        if max_num_element:
            # print('max_num_element: %s' % max_num_element)
            return_list.append(max_num_element)
            return_list += array_clustering(num_array)
            break

        split_num_list = [x for x, y in zip(num_array, range(len(num_array))) if
                          np.var(num_array[:y + 1]) <= avr_num_var_all]
        if not split_num_list:
            break
        count_num += 1
        # print('第%s 类：%s' % (count_num, split_num_list))
        return_list.append(split_num_list)
        num_array = num_array[len(split_num_list):]
    # return return_list
    return sort_list(return_list)

def sort_list(input_list):
    num_dict = {}
    return_list = []
    len_num = len(input_list)
    for x in range(len_num):
        num_dict[min(input_list[x])] = x

    key_list = list(num_dict.keys())
    key_list.sort()
    for xx in key_list:
        return_list.append(input_list[num_dict[xx]])

    return return_list


if __name__ == '__main__':
    # a = [1.0058, 2.0115, 2.2479, 33, 45, 50, 24, 50, 49, 48, 44, 47, 46, 100, 200, 300, 400, 1000, 1010, 1001,
    #  1020]

    a = [1.0058, 2.0115, 2.2479, 24, 33, 44, 45, 46, 47, 48, 49, 50, 50, 100, 100, 200]
    cc = array_clustering(a)
    print('is : %s' % cc)
    # print(sort_list(cc))
    # print('is : %s' % array_clustering([0.1008, 0.1016, 0.2031, 0.2047, 0.2063, 0.307, 0.3094, 0.3118, 0.3142, 0.4125, 0.4157, 0.4189, 0.4221, 0.4254, 0.5276, 0.5358, 0.54, 0.643, 0.8979, 0.9048, 1.0258, 1.866, 2.3561,
    #                                     2.4869, 9.2485, 9.1776, 11.3642]))
