# This code will only run in JUPYTER NOTEBOOK
# This code will only run in JUPYTER NOTEBOOK
# This code will only run in JUPYTER NOTEBOOK
# This code will only run in JUPYTER NOTEBOOK
# This code will only run in JUPYTER NOTEBOOK



import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf
po.init_notebook_mode(connected = True)
cf.go_offline()


def createdata(data):
    if(data == 1):
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
        print(df1)
        
    elif(data == 2):
        nc=int(input("Enter the number of columns : "))
        nr=int(input("Enter the number of rows : "))
        
        Data={}
        List=[]
        for i in range(nc):
            print()
            val=input("Enter the value for column : ")
            for j in range(nr):
                List.append(input())
            Data[val]=List
            List=[]
            
        df1 = pd.DataFrame(Data)
        print(df1)
        
    elif(data == 3):
        print()
        file = input('Enter the file name : ')
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
        print(df1)
        
    else:
        print('~~~ DataFrame creation failed, as YOU HAVE ENTERED WRONG CHOICE !!!')
        print('--> Please provide the appropriate choice to access the PLOT MENU __/\__') 
    return df1


def plotter(plot):
    if(plot == 1):
        finalplot = df1.iplot(kind='scatter')
    elif(plot == 2):
        finalplot = df1.iplot(kind='scatter',mode='markers' ,symbol='x',colorscale='paired')
    elif(plot == 3):
        finalplot = df1.iplot(kind='bar')
    elif(plot == 4):
        finalplot = df1.iplot(kind='hist')
    elif(plot == 5):
        finalplot = df1.iplot(kind='box')
    elif(plot == 6):
        finalplot = df1.iplot(kind='surface')
    else:
        finalplot = print('''~~~ YOU HAVE ENTERED WRONG CHOICE !!!
--> Please provide the appropriate choice to access the GRAPH MENU __/\__''') 
    return finalplot


def plotter2(plot):
    col = input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3 : ')
    col = int(col)
    
    if(col==1):
        colm = input('Enter the column you want to plot by selecting any column from dataframe head : ')
        if(plot==1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[colm].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot==6 or plot==7):
            finalplot = print('~~~ Bubble plot and surface plot require more than one column arguments !!!')
        else:
            finalplot = print('''~~~ YOU HAVE ENTERED WRONG CHOICE !!!
--> Please provide the appropriate choice to access the GRAPH MENU __/\__''') 
            
    elif(col==2):
        print('Enter the columns you want to plot by selecting from dataframe head : ')
        x = input('First column : ')
        y = input('Second column : ')
        if(plot==1):
            finalplot = df1[[x,y]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y]].iplot(kind='surface')
        elif(plot==7):
            size = input('Enter the size column for bubble plot : ')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,size=size)
        else:
            finalplot = print('''~~~ YOU HAVE ENTERED WRONG CHOICE !!!
--> Please provide the appropriate choice to access the GRAPH MENU __/\__''') 
            
    elif(col==3):
        print('Enter the columns you want to plot : ')
        x=input('First column : ')
        y=input('Second column : ')
        z=input('Third column : ')
        if(plot==1):
            finalplot = df1[[x,y,z]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y,z]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y,z]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y,z]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y,z]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y,z]].iplot(kind='surface')
        elif(plot==7):
            size = input('~~~ Please enter the size column for bubble plot __/\__')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,z=z,size=size )
        else:
            finalplot = print('''~~~ YOU HAVE ENTERED WRONG CHOICE !!!
--> Please provide the appropriate choice to access the GRAPH MENU __/\__''') 
            
    else:
        finalplot = print('--> Please enter only 1 , 2 or 3 __/\__')
    return finalplot


def main(cat):
    if(cat == 1):
        print('***** GRAPH MENU *****')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('**********************')
        plot = int(input("Enter your choice : "))
        output = plotter(plot)
        
    elif(cat == 2):
        print('***** GRAPH MENU *****')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot')
        print('**********************')
        plot = int(input("Enter your choice : "))
        output = plotter2(plot)
        
    else:
        print('~~~ YOU HAVE ENTERED WRONG CHOICE !!!')
        print('--> Please provide the appropriate choice to access the PLOT MENU __/\__')  
        
ans='m'
while ans.lower()=='m':
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN MENU %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('1. Create and display the random dataframe with 100 rows and 5 columns')
    print("2. Create and display the customized dataframe with 'n' number of columns and 'n' number of rows")
    print('3. Upload and display the csv/json/txt file')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    ch = int(input("Enter your choice : "))
    print()
    df1 = createdata(ch)
    print()
    print()
    print('*** Your DataFrame head is given below check the columns to plot using cufflinks ***')
    print()
    print(df1.head())
    print()
    
    ans='p'
    while ans.lower()=='p':
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& PLOT MENU &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print('## What kind of plot you need , the complete data plot or columns plot ##')
        print('1. Plotting all columns')
        print('2. Plotting specified columns')
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        cat = int(input("Enter your sub choice : "))
        print()
        main(cat)
        print()
        ans=input("Press 'p/P' to go to the PLOT MENU : ")
        print()
        
    print()
    ans=input("Press 'm/M' to go to the MAIN MENU : ")
    print()