import numpy as np
import pandas as pd

nc=int(input("Enter the number of columns : "))
nr=int(input("Enter the number of rows : "))
Data={}
List=[]
for i in range(nc):
    val=input("Enter the value for column : ")
    for j in range(nr):
        List.append(input())
    Data[val]=List
    List=[]

print(pd.DataFrame(Data))
print(Data)