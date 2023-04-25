from tkinter import *
import tkinter.messagebox as mb
import csv
from tkinter import ttk
#from PIL import ImageTk,Image
from datetime import datetime
n=datetime.now()
j=n.strftime('%Y')
c='CHETTINAD VIDYASHRAM STUDENT COUNCIL ELECTION'+' '+j
root=Tk()
root.iconbitmap('Logo.ico')
root.title(c)
root.geometry('600x300')
lh1 = Label(root, text ='CHETTINAD VIDYASHRAM',font=('Italic',16)).place(x=175,y = 20)
lh2 = Label(root, text ='STUDENT COUNCIL ELECTION'+' '+j,font=('Italic',13)).place(x=160,y = 60)




lis=[]#create a list to upload contestants details into results file
d={}
t=0000
def ret():
    with open('voters.csv','r')as c:
        l=list(csv.reader(c))
    return l
    c.close()
h=ret()
def givehouse(lm):                   #returns house of voter 
    th=''
    with open('voters.csv','r')as c:
        lit=list(csv.reader(c))
        for a in lit:
            if a[0]==str(lm):
                th=a[4]
    return th

def configcapts(th):#gives names of captain of the voters house
    l=['nota']
    with open('contestants.csv','r')as v:
        li=list(csv.reader(v))
        for a in li:
            if a[5]==th and a[4]=='captain':
                l.append(a[1])
    return l
def configure(L):#gives names of headboy/girl
    k=[]
    with open('contestants.csv','r')as v:
        li=list(csv.reader(v))
        for a in li:
            if a[4]==L:
                k.append(a[1])
    return k

def final(k):               #uses teachers code to submit response to result file
    with open('voters.csv','r')as voter:
        l=list(csv.reader(voter))
        flag = 0
        for a in l:
            if a[0]==k:
                flag = 1 
                mb.showinfo('Submission','All Responses Submitted')
                for a in d.items():
                    l=[]
                    p=list(a[0])
                    l.extend(p)
                    l.append(a[1])
                    lis.append(l)
                with open('results.csv','w',newline='')as w:
                    k=csv.writer(w)
                    k.writerows(lis)                
                    w.close()
                break
        if flag == 0: 
           print(k)
           mb.showinfo('WARNING','ERROR CODE')

def result():
    result_win = Tk()
    result_win.geometry('600x300')
    result_win.iconbitmap('Logo.ico')
    result_win.title(c)
    result_lh = Label(result_win,text ='RESULT: STUDENT COUNCIL ELECTION'+' '+j,font=('Italic',13))
    result_lh.place(x=140,y = 20)
    lst = lis
    hdby =[]
    hdgl =[]
    cap_sapphire =[]
    cap_ruby = []
    cap_emerald = []
    cap_pearl = []
    for a in lst:
        if a[4] == 'headboy':
            hdby.append(a)
        if a[4] == 'headgirl':
            hdgl.append(a)
        if a[4] == 'captain' and a[5] == 'sapphire' :
            cap_sapphire.append(a)
        if a[4] == 'captain' and a[5] == 'ruby' :
            cap_ruby.append(a)
        if a[4] == 'captain' and a[5] == 'emerald' :
            cap_emerald.append(a)
        if a[4] == 'captain' and a[5] == 'pearl' :
            cap_pearl.append(a)
     
    yaxis =60
    if len(hdby) >0:
        hdby_win = max(hdby, key=lambda x: x[6])
        lbl_headboy = Label(result_win,text =  "Head Boy:  "+hdby_win[1].title()+"    (Votes received: "+str(hdby_win[6])+") ",font=('Italic',13)).place(x =30,y=yaxis)
        yaxis+=30
    if len(hdby) >0:
        hdgl_win = max(hdgl, key=lambda x: x[6])
        lbl_headgirl = Label(result_win,text = "Head Girl:  "+hdgl_win[1].title()+"    (Votes received: "+str(hdgl_win[6])+") ",font=('Italic',13)).place(x =30,y=yaxis)
        yaxis+=30
    
    if len(cap_sapphire) >0:
        cs_win = max(cap_sapphire, key=lambda x: x[6])
        lbl_cs_win = Label(result_win,text = "Sapphire-Captain:  "+cs_win[1].title()+"    (Votes received: "+str(cs_win[6])+") ",font=('Italic',13)).place(x =30,y=yaxis)
        yaxis+=30
    
    if len(cap_ruby) >0:
        cr_win = max(cap_ruby, key=lambda x: x[6])
        lbl_cr_win = Label(result_win,text = "Ruby-Captain:  "+cr_win[1].title()+"    (Votes received: "+str(cr_win[6])+") ",font=('Italic',13)).place(x =30,y=yaxis)
        yaxis+=30
    
    if len(cap_emerald) >0:
        ce_win = max(cap_emerald, key=lambda x: x[6])
        lbl_cp_win = Label(result_win,text = "Emerald-Captain:  "+ce_win[1].title()+"    (Votes received: "+str(ce_win[6])+") ",font=('Italic',13)).place(x =30,y=yaxis)
        yaxis+=30
    
    if len(cap_pearl) >0:
        cp_win = max(cap_pearl, key=lambda x: x[6])
        lbl_cs_win = Label(result_win,text = "Pearl-Captain:  "+cp_win[1].title()+"    (Votes received: "+str(cp_win[6])+") ",font=('Italic',13)).place(x =30,y=yaxis)
        yaxis+=30
    
    qtbbtn = Button(result_win,text=' Quit ',command=result_win.destroy).place(x = 280, y = 240)
    

def start(y):#voters enroll
    top=Toplevel()
    top.title(c)
    top.iconbitmap('Logo.ico')

    l1=Label(top,text='1. Select Captain   ',font=('Italic',14)) 
    l1.grid(column=0,row=2,pady=15,padx=10)
    combo1=ttk.Combobox(top,width=30)
    t8=givehouse(y)
    combo1['values']=configcapts(t8)
    combo1['state'] = 'readonly'
    combo1.grid(column=1,row=2,pady=15,padx=10)
    
    def cast(L,x,y,th=''):      #appends the details of leaders and no.of votes in lis(global one)
        if L=='nota':     #L:choice selected,x:post
            pass
        else:
            with open('contestants.csv','r')as v:#adds the contestants to list that appends to results file
                li=list(csv.reader(v))
                for a in li:
                    if a[4]=='captain':
                        if a[1]==L and a[4]==x and a[5]==th:
                            a=tuple(a)
                            if a not in d.keys():
                                d[a]=1
                            else:
                              d[a]+=1
                    else:
                        if a[1]==L and a[4]==x:
                            a=tuple(a)
                            if a not in d.keys():
                                d[a]=1
                            else:
                                d[a]+=1
        for a in h:
            if a[1]==y:
                h.pop(a)
            else:
                pass

    def CASTCAPT():
        combo1.bind("<<ComboboxSelected>>")
        t=combo1.get()
        cast(t,'captain',y,t8)

    l2=Label(top,text='2. Select Head boy  ',font=('Italic',14))
    l2.grid(column=0,row=3,pady=15,padx=10)
    combo2=ttk.Combobox(top,width=30)
    combo2['values']=configure('headboy')
    combo2['state'] = 'readonly'
    combo2.grid(column=1,row=3,pady=15,padx=10)
 
    def CASTHB():
        combo2.bind("<<ComboboxSelected>>")
        t=combo2.get()
        cast(t,'headboy',y)
    
    l3=Label(top,text='3. Select Head girl ',font=('Italic',14))
    l3.grid(column=0,row=4,pady=15,padx=10)
    combo3=ttk.Combobox(top,width=30, )
    combo3['values']=configure('headgirl')
    combo3['state'] = 'readonly'
    combo3.grid(column=1,row=4,pady=15,padx=10)

    def CASTHG():
        combo3.bind("<<ComboboxSelected>>")
        t3=combo3.get()
        cast(t3,'headgirl',y)

    def elect():
       if (len(combo1.get()) >0) and (len(combo1.get())>0) and (len(combo1.get())>0) :
        CASTCAPT()
        CASTHB()
        CASTHG()
        top.destroy()
       else: 
        mb.showinfo('Voting Incomplete','Please complete voting')   
        combo1.focus_set()
        
    butd=Button(top,text=' Voting Done ',command=elect)
    butd.grid(column=1,row=6,pady=15,padx=10)

''' btnc=Button(top,text=' Elect ', command=CASTCAPT)
    btnc.grid(column=2,row=2,pady=15,padx=10)
    btnb=Button(top,text=' Elect ',command=CASTHB)
    btnb.grid(column=2,row=3,pady=15,padx=10)
    btng=Button(top,text=' Elect ',command=CASTHG)
    btng.grid(column=2,row=4,pady=15,padx=10) '''

def clicked():
    global t
    flag = 0
    t=int(txt.get())
    with open('voters.csv','r')as v:
        lit=csv.reader(v)
        for a in lit:
            if int(a[0])==t:
                flag = 1
                callback(t)
                start(t)
                break
        if(flag ==0):
                mb.showinfo('WARNING','CREDENTIALS NOT FOUND')
     
def FINISH():
    y1=str(t)
    final(y1)

id = [var[0] for var in h]
def callback(combo_va):
    combo_val = txt.get()
    if combo_val in id: 
        id.remove(combo_val)
        txt['values'] = id
        txt.set("")

l=Label(root,text='Enter Roll No: ',font=('Italic',12)).place(x = 80, y= 100)
txt=ttk.Combobox(root,values = id, width=10 )
txt.place(x = 200, y= 100)

but=Button(root,text='Start Voting',width = 13 ,font=('Italic',11),command=clicked).place(x = 290, y = 96)

#t2=ttk.Entry(root,width=13).place(x = 200, y = 140)

butgl=Button(root,text='Finish ALL Voting',width = 13 ,font=('Italic',11),command=FINISH).place(x = 220, y = 136)

qtbres = Button(root,text='Declare Results',width = 13 ,font=('Italic',11),command=result).place(x = 220, y = 180)

qtbbtn = Button(root,text='Quit',width = 13 ,font=('Italic',11),command=root.destroy).place(x = 220, y = 240)

root.mainloop()




