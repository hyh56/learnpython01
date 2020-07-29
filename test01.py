print('hello world to huyh 2020-07-29')

import numpy as np
import datetime as dt



arr1 = np.empty((1,10))

#对数组的理解可以使用索引。每一个维度都可以看成是一层索引，
#层层往下，就形成一种树的结构。


#递归求解阶乘
def jiecheng(n):
    if n>=0:
        if n>1:
            return n*jiecheng(n-1)
        else:
            return 1
    else:
        print('请输入非负数！')
        return -1

#递归求解斐波那契数列
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


#堆栈--计算顺序
'''
#例如fib(4)
fib(4)=fib(3)+fib(2)
fib(3)=fib(2)+fib(1)
fib(2)=fib(1)+fib(0)
计算fib(1) fib(0)
fib(2)
计算fib(1)
fib(3)
fib(2)=fib(1)+fib(0)
计算fib(1) fib(0)
fib(2)
fib(4)
'''

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n):
            a,b = b,a+b
        return a

#print(fib(eval(input('请输入一个非负数n:'))))
N = 40
dt_now = dt.datetime.now()
a = fib(N)
td1 = dt.datetime.now()-dt_now
print(a,'  ',td1.total_seconds()*1000,'毫秒')
dt_now = dt.datetime.now()
a = fib2(N)
td1 = dt.datetime.now()-dt_now
print(a,'  ',td1.total_seconds()*1000,'毫秒')














