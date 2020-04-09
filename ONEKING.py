# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:29:01 2020

@author: Aniket Maity
"""
count = 0
newList = []

T = int(input())
while(T>0):
    N = int(input())
    n=N
    NList = []
    while(N>0):
        
        a=list(map(int,input().split()))
        NList.append(a)
        N-=1
    #lst3 = [value for value in lst1 if value in lst2] 
    for i in range(n):
        copyList = []
        start = NList[i][0]
        end = NList[i][1]
        for k in range(start,end+1):
            copyList.append(k)
        newList.append(copyList)
    for i in range(0,n):
        for j in range(i+1,n):
            
            if len([value for value in newList[i] if value in newList[j]])>0:
                count+=1
                break
            
            else:
                count+=1      
    T-=1
        