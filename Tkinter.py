# In GUI programming, tkinter is a popular module
from tkinter import *

# Rudimentary coding
# Function pack
shell1=Tk()
shell1.geometry('500x390+10+10')
label1=Label(shell1,text='Hi, Slade!')
label1.pack(side='top',padx=100)
label2=Label(shell1,text='I\'m you\'re new friend.')
label2.pack(side='bottom',fill='x')
label3=Label(shell1,text='sample1')
label3.pack(anchor='ne')
label4=Label(shell1,text='sample2')
label4.pack(side='right')
label5=Label(shell1,text='sample3')
label5.pack(anchor='w')
label6=Label(shell1,text='sample4')
label6.pack()
shell1.mainloop() # More to be seen in the book, page 231
# Function grid
shell2=Tk()
shell2.geometry('500x450+10+10')
label7=Label(shell2,text='pos1')
label8=Label(shell2,text='pos2')
label9=Label(shell2,text='pos3')
label10=Label(shell2,text='pos4')
label11=Label(shell2,text='pos5')
label12=Label(shell2,text='pos6')
label7.grid(row=0,column=0,padx=50,ipadx=49,pady=30,ipady=29)
label8.grid(row=1,column=0)
label9.grid(row=2,column=0)
label10.grid(row=0,column=1)
label11.grid(row=0,column=3)
label12.grid(row=1,column=1)
shell2.mainloop() # More to be seen in the book, page 233

# Advanced coding
#1.Text Label
TL=Tk()
TL.geometry('300x160+0+0')
TL.wm_title('Text Label') # Name of the shell
label1=Label(TL,text='Upper\n--Lower',\
             height=6,width=24,relief='ridge',\
             bg='yellow',fg='blue',bd=8,\
             anchor='center',font='宋体',cursor='no')
label1.pack(side='top')
TL.mainloop()
#2.Picture Lable
PL=Tk()
PL.geometry('300x160+0+0')
PL.wm_title('Picture Label')
pic=PhotoImage(file='Mr.Math.gif')# No jpg, only gif
label1=Label(PL,image=pic,height=140,width=140,relief='sunken',\
             anchor='center',cursor='no')
label1.pack()
PL.mainloop()
#3.Button Demo
import sys
BD=Tk()
BD.geometry('800x390+0+0')
BD.wm_title('Button Demo')
def demolabel(x):
    Demo=Tk()
    Demo.geometry('300x90+0+0')
    Demo.wm_title('Really!')
    labe3=Label(Demo,text='Of course')
    labe3.grid()
pic=PhotoImage(file='Mr.Math.gif')# If to be used again, deffine again
label1=Label(BD,text='Hi, it\'s me.\nYour favourite friend',\
             height=4,width=80,bg='black',fg='white',\
             anchor='center',cursor='arrow')
label2=Label(BD,image=pic,height=140,width=140,relief='sunken',\
             anchor='center',cursor='no')
label1.grid(row=0,column=5)
label2.grid(row=1,column=5)
btn1=Button(BD,text='Confirm(e)',height=2,width=12,bd=5)
btn1.bind('<KeyPress-E>',sys.exit)
btn1.grid(row=2,column=8,padx=5,pady=100)
btn2=Button(BD,text='Really?',height=2,width=12,bd=5)
btn2.bind('<Button-1>',demolabel)
btn2.grid(row=2,column=2,padx=5,pady=100)
BD.mainloop()
#4.Entry Demo(1)
from re import *
def ValidateText():
    valtex=et1.get()
    if re.findall('^[0-9a-zA-Z_]{1,}$',str(valtex)): #re.findall
        return True
    else:
        return False
def answ():
    if str(et1.get())=='2870992411' and str(et2.get())=='Lian62951413':
        label4['text']='Login Successful!'
    else:
        label4['text']='ID or/and Password Incorrect.'
ED=Tk()
ED.geometry('800x370+0+0')
ED.wm_title('Entry Demo')
pic=PhotoImage(file='Mr.Math.gif')
label1=Label(ED,text='Hi, it\'s me.\nYour favourite friend',\
             height=3,width=27,bg='black',fg='white',font=32,\
             anchor='center',cursor='no')
label1.grid(row=0,column=0)
label2=Label(ED,text='ID:',\
             height=4,width=40,font=20,\
             anchor='center',cursor='arrow')
label2.grid(row=2,column=0)
label3=Label(ED,text='Password:',\
             height=4,width=40,font=20,\
             anchor='center',cursor='arrow')
label3.grid(row=3,column=0)
ev1=StringVar()
ev2=StringVar()
et1=Entry(ED,textvariable=ev1,font=18,\
          validate='focusout',validatecommand=ValidateText)
et1.grid(row=2,column=1)
et1.focus_force()
et2=Entry(ED,textvariable=ev2,show='*',font=18)
et2.grid(row=3,column=1)
btn1=Button(ED,text='Login',command=answ)
btn1.grid(row=4,column=0)
btn2=Button(ED,text='Exit',command=sys.exit)
btn2.grid(row=4,column=1)
label4=Label(ED,text='Interfacial Area',relief='ridge',font=16)
label4.grid(row=7,column=0)
ED.mainloop()
#4.Entry Demo(2)





























































