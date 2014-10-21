from Tkinter import *

root=Tk()

sizex = 600
sizey = 400
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

labels = []

def myClick():
    del labels[:] # remove any previous labels from if the callback was called before
    myframe=Frame(root,width=400,height=300,bd=2,relief=GROOVE)
    myframe.place(x=10,y=10)
    x=myvalue.get()
    value=int(x)
    for i in range(value):
        labels.append(Label(myframe,text=" mytext "+str(i)))
        labels[i].place(x=10,y=10+(30*i))
        Button(myframe,text="Accept").place(x=70,y=10+(30*i))

def myClick2():
    if len(labels) > 0:
        labels[0].config(text="Click2!")
    if len(labels) > 1:
        labels[1].config(text="Click2!!")

mybutton=Button(root,text="OK",command=myClick)
mybutton.place(x=420,y=10)

mybutton2=Button(root,text="Change",command=myClick2)
mybutton2.place(x=420,y=80)

myvalue=Entry(root)
myvalue.place(x=450,y=10)
