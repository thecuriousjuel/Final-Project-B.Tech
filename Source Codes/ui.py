from tkinter import *
import Scatter
import Mobile_Anchor
import PSO
import random
import leach
import analysis


t_x = []
t_y = []
t_l = 0
er = 0
ti = 0

t_x_1 = []
t_y_1 = []
t_l_1 = 0
er_1 = 0
ti_1 = 0

t_x_p = [] 
t_y_p = []
p_x_p = [] 
p_y_p = []

def fn1():  
    global t_x, t_y, t_l, er, ti
    t_x, t_y, t_l, er, ti = Scatter.Trilateration(m_x, m_y, m_x1, m_y1, num_of_anchors, num_of_dumb, r)
    print(t_l)
    

def fn2():
    global t_x_1, t_y_1, t_l_1, er_1, ti_1
    t_x_1, t_y_1, t_l_1, er_1, ti_1 = PSO.pso(a_x, a_y, a_x1, a_y1, num_of_anchors, num_of_dumb, r)

def fn3():
    global t_x_p, t_y_p
    t_x_p, t_y_p = leach.my_leach(t_x,t_y,t_l)

def fn4():
    global p_x_p, p_y_p
    p_x_p, p_y_p = leach.my_leach(t_x_1,t_y_1,t_l_1)

def fn5():
    analysis.myanalysis(t_x_p, t_y_p, p_x_p, p_y_p)

def fn6():
    Mobile_Anchor.mobile(m_x1, m_y1, r)




num_of_anchors = 5#int(input('Enter the number of Anchors : '))
num_of_dumb = 50#int(input('Enter the number of Dumb Nodes : '))
r = 30#int(input('Enter the range : '))

#global variables
t_x = []
t_y = []
t_l = 0
er = 0
ti = 0

# coordinates of anchors
m_x = []
m_y = []

# coordinates of dumb nodes
m_x1 = []
m_y1 = []

for i in range(num_of_anchors):
    z = random.randint(0,100)
    if z not in m_x:
        m_x.append(z)
    else:
        m_x.append(random.randint(0,z))

    m_y.append(random.randint(0,100))


for i in range(num_of_dumb):
    z = random.randint(0,100)
    if z not in m_x1:
        m_x1.append(z)
    else:
        m_x1.append(random.randint(0,z))

    m_y1.append(random.randint(0,100))


a_x = m_x[:]
a_y = m_y[:]

a_x1 = m_x1[:]
a_y1 = m_y1[:]

window=Tk()
frame1=Frame(window)
frame2=Frame(window)

status_bar=Label(frame2,bd=3,relief=SUNKEN,bg="black",fg="white")
status_bar.pack(fill=BOTH,expand=1)

label1=Label(frame1,text="Localization",width=20,height=3,anchor=W)
label2=Label(frame1,text="Energy Optimization",width=20,height=3,anchor=W)
label3=Label(frame1,text="Path Planning",width=20,height=3,anchor=W)

#label3=Label(status_bar,text="Your score",bg="black",fg="orange",width=15,height=2,anchor=E)
#label4=Label(status_bar,text="Computer score",bg="black",fg="orange",width=15,height=2,anchor=E)

button1a=Button(frame1,text="Using Trilateration",command=fn1,bg="red",fg="white",width=20,height=3)
button1b=Button(frame1,text="Using PSO",command=fn2,bg="red",fg="white",width=20,height=3)
button2a=Button(frame1,text="LEACH for Trilateration",command=fn3,bg="white",fg="black",width=20,height=3)
button2b=Button(frame1,text="LEACH for PSO",command=fn4,bg="white",fg="black",width=20,height=3)
button2c=Button(frame1,text="Comparative Analysis",command=fn5,bg="white",fg="black",width=20,height=3)
button3=Button(frame1,text="Mobile Anchor",command=fn6,bg="green",fg="white",width=20,height=3)

label1.grid(row=0,column=0,pady=8)
label2.grid(row=2,column=0,pady=8)
label3.grid(row=5,column=0,pady=8)

button1a.grid(row=0,column=1,padx=5,pady=5)
button1b.grid(row=1,column=1,padx=5,pady=5)
button2a.grid(row=2,column=1,padx=5,pady=5)
button2b.grid(row=3,column=1,padx=5,pady=5)
button2c.grid(row=4,column=1,padx=5,pady=5)
button3.grid(row=5,column=1,padx=5,pady=5)


#label3.grid(row=0,columnspan=3,padx=20,pady=8)
#label4.grid(row=1,columnspan=3,padx=20,pady=8)

label1a=Label(status_bar,text="15ETCS002008 - Biswajit Basak",bg="black",fg="orange",width=28,height=1,anchor=W)
label2a=Label(status_bar,text="15ETCS002033 - Rahul Kumar",bg="black",fg="orange",width=28,height=1,anchor=W)
label3a=Label(status_bar,text="15ETCS002036 - Rohan Kumar",bg="black",fg="orange",width=28,height=1,anchor=W)
label4a=Label(status_bar,text="15ETCS002048 - Tushar Agarwal",bg="black",fg="orange",width=28,height=1,anchor=W)
label5a=Label(status_bar,text="Mentor - Vaishali R Kulkarni",bg="black",fg="orange",width=28,height=1,anchor=W)


label1a.grid(row=0,column=3)
label2a.grid(row=1,column=3)
label3a.grid(row=2,column=3)
label4a.grid(row=3,column=3)
label5a.grid(row=1,column=4)

frame1.pack()
frame2.pack(fill=BOTH,expand=1)

window.mainloop()
