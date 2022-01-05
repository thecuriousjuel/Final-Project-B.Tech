import random
import Scatter
import Mobile_Anchor
import PSO
from tkinter import *
from tkinter.ttk import *


#--------------------------------------------------------------------

class App(Frame):

    def __init__(self, parent, b = 0):
        
        frame = Frame(parent)
        frame.grid()
        
        self.printButton = Button(frame, text = "Trilateration", command = self.trilateration())
        self.printButton.grid(row = 0, column = 0, sticky = E)
        
        self.printButton = Button(frame, text = "PSO", command = self.p_s_o)
        self.printButton.grid(row = 0, column = 1, sticky = E)
        
        self.printButton = Button(frame, text = "Mobile Anchor", command = self.mobile_anchor)
        self.printButton.grid(row = 0, column = 2, sticky = E)       
        
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.grid(row = 0, column = 3, sticky = E)       
        
        #self.CreateUI(parent)    
        #self.LoadTable(parent, b)
        #frame.grid(sticky = (N,S,W,E))
        #parent.grid_rowconfigure(0, weight = 1)
        #parent.grid_columnconfigure(0, weight = 1)     

    def CreateUI(self, parent):
        tv = Treeview(parent)
        tv['columns'] = ('error', 'time_elapsed')
        tv.heading("#0", text='Algorithm', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('error', text='Error')
        tv.column('error', anchor='center', width=100)
        tv.heading('time_elapsed', text='Time Elapsed')
        tv.column('time_elapsed', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        parent.treeview = tv
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def LoadTable(self, parent, b):
        parent.treeview.insert('', 'end', text="First", values=('10:00', '10:10', 'Ok'))
        parent.treeview.insert('', 'end', text=b, values=('20:00', '20:10', 'Ok'))
        parent.treeview.insert('', 'end', text=b, values=('120:00', '20:10', 'Ok'))
    
    def trilateration(self):
        #get_list = Scatter.Trilateration(m_x, m_y, m_x1, m_y1, num_of_anchors, num_of_dumb, r)
        self.LoadTable(parent, 1)       
        
        
    def p_s_o(self):
        PSO.pso(a_x, a_y, a_x1, a_y1, num_of_anchors, num_of_dumb, r)
    
    def mobile_anchor(self):
        Mobile_Anchor.mobile(m_x1, m_y1, r)    
        
#--------------------------------------------------------------------

num_of_anchors = 5#int(input('Enter the number of Anchors : '))
num_of_dumb = 50#int(input('Enter the number of Dumb Nodes : '))
r = 30#int(input('Enter the range : '))

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

choice = 0

#--------------------------------------------------------------------
root = Tk()
#Interface(root)
App(root,0)
root.mainloop()


