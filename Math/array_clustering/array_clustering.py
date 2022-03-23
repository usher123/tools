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
