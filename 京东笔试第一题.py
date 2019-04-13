# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:59:33 2019

@author: LLLL
"""
#2019年京东暑期笔试第一题
x=[]
x=input()

def func2(s):#寻找最大间隔
    i=0
    list1=[]
    while i<len(s):
        number=0
        if int(s[i])==1:
            number=number+1
            j=i+1
            while j<len(s):
                if int(s[j])==1:
                    number=number+1
                    j=j+1
                else:
                    list1.append(number)
                    break
        i=i+1
    return max(list1)
            
def func3(s):#若尾部是1，从尾部寻找最长非0
    i=-2
    number2=1
    while 1:
        if int(s[i])==1:
            number2=number2+1
            i=i-1
        else:
            return number2
        
def func4(s):#计算头部最长
    i=0
    number3=0
    while 1:
        if int(s[i])==1:
            number3=number3+1
            i=i+1
        else:
            return number3      
            
def func1_main(s):#(判断为不是否为0)
    if int(s[-1])==0:
        s1=func2(s)
        print(s1)
    else:
        s2=func3(s)#head
        s3=func4(s)#tail
        s5=s2+s3#head+tail
        s6=func2(s)#main
        if int(s5)>int(s6):
            print(s5)
        else:
            print(s6)      
func1_main(x)
