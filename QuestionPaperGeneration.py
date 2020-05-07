#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python code for question bank
import random as rd
import xlrd as xl
import webbrowser

path="C:\\Users\\iota_\\OneDrive\\Desktop\\CurrencyData File.xlsx"
wb=xl.open_workbook(path)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
c=sheet.nrows
listn=[]
lists=[]
listp=[]


print('What do you want the questions to be on? (Currency, Symbols, Prices)')
a1=int(input('Enter your choice: 1-Currency, 2-Symbols, 3-Prices \n'))
print('The options will be : ')
a2=int(input('Enter your choice for options: 1-Currency, 2-Symbols, 3-Prices \n'))
if(a1==a2):
    print('Questions and Options must differ \n')
else:
    for i in range(c):
        listn.append(sheet.cell_value(i,1))
        lists.append(sheet.cell_value(i,2))
        listp.append(sheet.cell_value(i,4))
    m=open('qp.txt','w+')
    m1=open('an.txt','w+')
    n=int(input('How many question papers? (11-15)\n '))
    n1=int(input('Number of questions in every question paper? (16-20)'))
    lista=['A','B','C']
    while(1):
        if((10<n<16) and (15<n1<21)):
            break
        else:
            n=int(input('How many question papers? (11-15)\n '))
            n1=int(input('Number of questions in every question paper? (16-20)'))
    if(a1==1):
        if(a2==2):
            for i1 in range(n):
                m.write('\n'+'               '+'question paper- '+str(i1+1)+'\n')
                for j in range(n1):
                    m.write('\n'+str(j+1)+'What is the Symbol of  '+rd.choice(listn)+'?'+'\n'+' A)'+rd.choice(lists)+'    B)'+rd.choice(lists)+'  C)'+rd.choice(lists)+'\n')
        else:
            for i1 in range(n):
                m.write('\n'+'               '+'question paper- '+str(i1+1)+'\n')
                for j in range(n1):
                    m.write('\n'+str(j+1)+'What is the Price of  '+str(rd.choice(listn))+'?'+'\n'+' A)'+str(rd.choice(listp))+'    B)'+str(rd.choice(listp))+'  C)'+str(rd.choice(listp))+'\n')
    elif(a1==2):
        if(a2==1):
            for i1 in range(n):
                m.write('\n'+'               '+'question paper- '+str(i1+1)+'\n')
                for j in range(n1):
                    m.write('\n'+str(j+1)+'What is the Name of  '+rd.choice(lists)+'?'+'\n'+' A)'+rd.choice(listn)+'    B)'+rd.choice(listn)+'  C)'+rd.choice(listn)+'\n')
        else:
            for i1 in range(n):
                m.write('\n'+'               '+'question paper- '+str(i1+1)+'\n')
                for j in range(n1):
                    m.write('\n'+str(j+1)+'What is the Price of  '+rd.choice(lists)+'?'+'\n'+' A)'+str(rd.choice(listp))+'    B)'+str(rd.choice(listp))+'  C)'+str(rd.choice(listp))+'\n')
    elif(a1==3):
        if(a2==1):
            for i1 in range(n):
                m.write('\n'+'               '+'question paper- '+str(i1+1)+'\n')
                for j in range(n1):
                    m.write('\n'+str(j+1)+'what is the Name of currency containing price  '+str(rd.choice(listp))+'?'+'\n'+' A)'+rd.choice(listn)+'    B)'+rd.choice(listn)+'  C)'+rd.choice(listn)+'\n')
        else:
            for i1 in range(n):
                m.write('\n'+'               '+'question paper- '+str(i1+1)+'\n')
                for j in range(n1):
                    m.write('\n'+str(j+1)+'What is the Symbol of currency containing price  '+str(rd.choice(listp))+'?'+'\n'+' A)'+rd.choice(lists)+'    B)'+rd.choice(lists)+'  C)'+rd.choice(lists)+'\n')
    for j1 in range(n):
        m1.write('\n'+'               '+'key sheet- '+str(j1+1)+'\n')
        for x in range(n1):
            m1.write('\n'+str(x+1)+')'+rd.choice(lista)+'\n')
webbrowser.open('questions.txt')
webbrowser.open('answers.txt')
m.close()
m1.close()


# In[ ]:




