import tkinter as tk
from tkinter import *
from tkinter import ttk
import pickle
from PIL import Image,ImageTk
def sim():
    l1=[b1.get(),b2.get(),b01.get(),b02.get()]
    l2=[b3.get(),b4.get(),b03.get(),b04.get()]
    l3=[b5.get(),b6.get(),b05.get(),b06.get()]
    l4=[b7.get(),b8.get(),b07.get(),b08.get()]
    l5=[b9.get(),b10.get(),b09.get(),b010.get()]
    l6=[b11.get(),b12.get(),b011.get(),b012.get()]
    l7=[b13.get(),b14.get(),b013.get(),b014.get()]
    l8=[b15.get(),b16.get(),b015.get(),b016.get()]
    l9=[b17.get(),b18.get(),b017.get(),b018.get()]
    l10=[b19.get(),b20.get(),b019.get(),b020.get()]
    l=[btt.get(),l1,l2,l3,l4,l5,l6,l7,l8,l9]
    f=open("daytable.dat","wb")
    pickle.dump(l,f)
    f.close()
    f2=open("daytable.dat","rb")
    ll=[]
    while True:
        try:
            k=pickle.load(f2)
            ll.append(k)
        except:
            break
    print(ll)
    f2.close()
    a.destroy()
    
    
l=[]
a=tk.Tk()
a.geometry('1920x1080')
a.title('Timetable')
a.configure(bg='#6B69D6')
b1=StringVar()
b2=StringVar()
b3=StringVar()
b4=StringVar()
b5=StringVar()
b6=StringVar()
b7=StringVar()
b8=StringVar()
b9=StringVar()
b10=StringVar()
b11=StringVar()
b12=StringVar()
b13=StringVar()
b14=StringVar()
b15=StringVar()
b16=StringVar()
b17=StringVar()
b18=StringVar()
b19=StringVar()
b20=StringVar()

s=PhotoImage(file='timetable.png')
img=Label(a,image=s)
img.pack()
c=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b1)
c.place(x=234,y=38)
c1=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b2)
c1.place(x=284,y=38)

c2=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b3)
c2.place(x=330,y=38)
c3=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b4)
c3.place(x=380,y=38)

c4=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b5)
c4.place(x=420,y=38)
c5=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b6)
c5.place(x=470,y=38)

c6=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b7)
c6.place(x=510,y=38)
c7=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b8)
c7.place(x=560,y=38)

c8=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b9)
c8.place(x=600,y=38)
c9=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b10)
c9.place(x=650,y=38)

c10=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b11)
c10.place(x=700,y=38)
c11=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b12)
c11.place(x=740,y=38)

c12=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b13)
c12.place(x=790,y=38)
c13=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b14)
c13.place(x=830,y=38)

c14=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b15)
c14.place(x=870,y=38)
c15=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b16)
c15.place(x=920,y=38)

c16=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b17)
c16.place(x=965,y=38)
c17=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b18)
c17.place(x=1020,y=38)

c18=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b19)
c18.place(x=1060,y=38)
c19=Entry(a,text='Enter',width=3,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b20)
c19.place(x=1110,y=38)

#--------------------------
b01=StringVar()
b02=StringVar()
b03=StringVar()
b04=StringVar()
b05=StringVar()
b06=StringVar()
b07=StringVar()
b08=StringVar()
b09=StringVar()
b010=StringVar()
b011=StringVar()
b012=StringVar()
b013=StringVar()
b014=StringVar()
b015=StringVar()
b016=StringVar()
b017=StringVar()
b018=StringVar()
b019=StringVar()
b020=StringVar()


c01=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b01)
c01.place(x=234,y=75)
c02=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b02)
c02.place(x=234,y=100)

c03=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b03)
c03.place(x=330,y=75)
c04=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b04)
c04.place(x=330,y=100)

c05=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b05)
c05.place(x=420,y=75)
c06=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b06)
c06.place(x=420,y=100)

c07=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b07)
c07.place(x=510,y=75)
c08=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b08)
c08.place(x=510,y=100)

c09=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b09)
c09.place(x=600,y=75)
c010=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b010)
c010.place(x=600,y=100)

c011=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b011)
c011.place(x=700,y=75)
c012=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b012)
c012.place(x=700,y=100)

c013=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b013)
c013.place(x=790,y=75)
c014=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b014)
c014.place(x=790,y=100)

c015=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b015)
c015.place(x=875,y=75)
c016=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b016)
c016.place(x=875,y=100)

c017=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b017)
c017.place(x=965,y=75)
c018=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b018)
c018.place(x=965,y=100)

c019=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b019)
c019.place(x=1060,y=75)
c026=Entry(a,text='Enter',width=8,fg='Black',bg='Lightblue',font='Arial',bd=2,textvariable=b020)
c026.place(x=1060,y=100)

ct=Label(a,text='Tutor mail',bg='pink',font='Arial')
ct.place(x=200,y=175)
btt=StringVar()
cc15=Entry(a,text='Enter',width=10,fg='Black',bg='Lightyellow',font='Arial',bd=2,textvariable=btt)
cc15.place(x=275,y=175)

button=Button(a,text='Enter',command=sim)
button.place(x=1200,y=600)
a.mainloop()
