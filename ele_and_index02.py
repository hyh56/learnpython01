# -*- coding: utf-8 -*-
print('hello world to huyh 2020-08-06')

'''
选择排序法：并获得排序后元素在原列表中的索引位置
'''
def select_sort_3_index(alist):
    #创建原列表索引数组
    index_alist = [i for i in range(len(alist))]
    for i in range(len(alist)-1):
        min_ele_index = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[min_ele_index]:
                min_ele_index = j
        alist[i],alist[min_ele_index] = alist[min_ele_index],alist[i]
        #交换元素位置的同时,在相同位置交换索引
        index_alist[i],index_alist[min_ele_index] = index_alist[min_ele_index],index_alist[i]
    #可打印，可返回
    print(index_alist)


if __name__ == "__main__":
    alist = [11,20,36,45,89,105,36,89,56,1]
    print(alist)
    select_sort_3_index(alist)
    print(alist)