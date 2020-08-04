# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 01:43:50 2019

@author: Jaga
"""

from tkinter import *
import tkinter.messagebox as m
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


iris=load_iris()
X=iris.data
Y=iris.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=5)

w=Tk()
w.configure(bg="violet")
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

from sklearn.neighbors import KNeighborsClassifier
K=KNeighborsClassifier(n_neighbors=10)
K.fit(X_train,Y_train)
Y_pred_knn=K.predict(X_test)
acc_knn=accuracy_score( Y_test,Y_pred_knn)
acc_knn=round(acc_knn*100,2)
knn=float(acc_knn)

from sklearn.linear_model import LogisticRegression
L=LogisticRegression(solver="liblinear",multi_class="auto")
L.fit(X_train,Y_train)
Y_pred_lg=L.predict(X_test)
acc_lg=accuracy_score(Y_test,Y_pred_lg)
acc_lg=round(acc_lg*100,2)
lg=float(acc_lg)

from sklearn.tree import DecisionTreeClassifier
D=DecisionTreeClassifier()
D.fit(X_train,Y_train)
Y_pred_dt=D.predict(X_test)
acc_dt=accuracy_score(Y_test,Y_pred_dt)
acc_dt=round(acc_dt*100,2)
dt=float(acc_dt)


from sklearn.naive_bayes import GaussianNB
G=GaussianNB()
G.fit(X_train,Y_train)
Y_pred_gnb=G.predict(X_test)
acc_gnb=accuracy_score(Y_test,Y_pred_gnb)
acc_gnb=round(acc_gnb*100,2)
gnb=float(acc_gnb)

left=[1,2,3,4]
height=[knn,lg,dt,gnb]
tick_label = ['knn', 'lg', 'dt', 'nb'] 
plt.bar(left, height, tick_label = tick_label,width = 0.8, color = ['red', 'green','blue','pink'])
plt.xlabel('algorithm of ml')
plt.ylabel('accuracy')


def knn():
   m.showinfo(title="knn",message="The accuracy of knn is "+str(acc_knn)+"%")
   
def lg():
    m.showinfo(title="Logistic Regression",message="The accuracy of lg is "+str(acc_lg)+"%")
    
def dt():
    m.showinfo(title="Decision Tree",message="The accuracy of dt is "+str(acc_dt)+"%")

    
def gnb():
    m.showinfo(title="NaiveBayes",message="The accuracy of gnb is "+str(acc_gnb)+"%")


def compare():
   plt.bar(left, height, tick_label = tick_label,width = 0.8, color = ['red', 'green','blue','pink'])
   plt.xlabel('algorithm of ml')
   plt.ylabel('accuracy')
   plt.show() 
    

def submit():
   try:
       if acc_knn>=acc_lg and acc_knn>=acc_dt:
           if acc_knn>=acc_gnb:
               p=K.predict([[float(v1.get()),float(v2.get()),float(v3.get()),float(v4.get())]])
       elif acc_lg>=acc_dt and acc_lg>=acc_gnb:
               p=L.predict([[float(v1.get()),float(v2.get()),float(v3.get()),float(v4.get())]])
       elif acc_dt>=acc_gnb:
               p=D.predict([[float(v1.get()),float(v2.get()),float(v3.get()),float(v4.get())]])
       else:
               p=G.predict([[float(v1.get()),float(v2.get()),float(v3.get()),float(v4.get())]])
       if p==[0]:
           m.showinfo(title="My Message",message="Species is Setosa")
       elif p==[1]:
           m.showinfo(title="My Message",message="Species is Versicolor")
       else:
           m.showinfo(title="My Message",message="Species is Virginica")
   except ValueError:
      m.showinfo(title="Message",message="PLz enter the details then press 'Submit'")
           
                        
            

def reset():
    v1.set("")
    v2.set("")
    v3.set("")
    v4.set("")

    
L1=Label(w,text="IRIS FLOWER PREDICTION",font=("arial",20,"bold"),bg="green",fg="blue",width=39)
B1=Button(w,text="KNN",font=("arial",20,"bold"),bg="pink",fg="red",width=10,command=knn)
B2=Button(w,text="LG",font=("arial",20,"bold"),bg="pink",fg="red",width=10,command=lg)
B3=Button(w,text="DT",font=("arial",20,"bold"),bg="pink",fg="red",width=10,command=dt)
B4=Button(w,text="NB",font=("arial",20,"bold"),bg="pink",fg="red",width=10,command=gnb)
B5=Button(w,text="Compare",font=("arial",20,"bold"),bg="pink",fg="red",width=10,command=compare)
L2=Label(w,text="Sepal Length",font=("arial",20,"bold"),bg="orange",fg="chocolate",width=10)
L3=Label(w,text="Sepal Width",font=("arial",20,"bold"),bg="orange",fg="chocolate",width=10)
L4=Label(w,text="Petal Length",font=("arial",20,"bold"),bg="orange",fg="chocolate",width=10)
L5=Label(w,text="Petal Width",font=("arial",20,"bold"),bg="orange",fg="chocolate",width=10)
E1=Entry(w,font=("arial",20,"bold"),textvariable=v1)
E2=Entry(w,font=("arial",20,"bold"),textvariable=v2)
E3=Entry(w,font=("arial",20,"bold"),textvariable=v3)
E4=Entry(w,font=("arial",20,"bold"),textvariable=v4)
Bsubmit=Button(w,text="Submit",font=("arial",20,"bold"),bg="pink",fg="red",command=submit)
Breset=Button(w,text="Reset",font=("arial",20,"bold"),bg="pink",fg="red",command=reset)
L1.grid(row=1,column=1,columnspan=3)
B1.grid(row=2,column=1)
B2.grid(row=3,column=1)
B3.grid(row=4,column=1)
B4.grid(row=5,column=1)
B5.grid(row=6,column=1)
L2.grid(row=2,column=2)
L3.grid(row=3,column=2)
L4.grid(row=4,column=2)
L5.grid(row=5,column=2)
E1.grid(row=2,column=3)
E2.grid(row=3,column=3)
E3.grid(row=4,column=3)
E4.grid(row=5,column=3)
Bsubmit.grid(row=6,column=2)
Breset.grid(row=6,column=3)
w.mainloop()


