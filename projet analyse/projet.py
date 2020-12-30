from pylab import *
from scipy.integrate import quad #c'est une bibliothèque pour qu'on peut calculer l'integrale
import numpy as np #abréviation du bibliothèque numpy pour être facile à utiliser
import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
class Rectangle(object): #class rectange 
    def __init__(self, a, b, n, f,c):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa=c
    def integrate(self,f):
        x=self.x# contiens les xi
        y=f(x)#les yi 
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h * s
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i]  , 0     , 0   ] # ordonnees des sommets
            self.aa.plot(x_rect, y_rect,"g")
        yflist_fine = f(xlist_fine)
        self.aa.plot(xlist_fine, yflist_fine)
        self.aa.plot(xl, yl,"rd")
        self.aa.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )
        
class Trapezoidal(object):
    def __init__(self, a, b, n, f,d):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.bb=d
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            self.bb.plot(x_rect, y_rect,"g")
        yflist_fine = f(xlist_fine)
        self.bb.plot(xlist_fine, yflist_fine)
        self.bb.plot(xl, yl,"cs")
        self.bb.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )
    ##############################################################################
class  RectangleM (object): 
    def __init__(self, a, b, n, f,c):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa=c
    def integrate(self,f):
        x=self.x
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        return h*s
       
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl=f(xl);
        xlist_fine=np.linspace(self.a, self.b, resolution)        
        for i in range(self.n):            
            m=(xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] 
            y_rect = [0  , f(m), f(m)  , 0 , 0 ] 
            self.aa.plot(x_rect, y_rect,"r")
            self.aa.plot(m,f(m),"g*")
            
        yflist_fine = f(xlist_fine)
        self.aa.plot(xlist_fine, yflist_fine,'b')
        self.aa.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )
  #################################################################################
class Simpson(object):
    def __init__(self, a, b, n, f,c): 
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n #
        self.aa=c
    def integrate(self,f):
        x=self.x 
        y=f(x)
        h = float(x[1] - x[0])
        n = len(x) - 1
        if n % 2 == 1:
            n =n-1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
       
        return h * s / 3.0
    def Graph(self,f,resolution=1001):
        xl = self.x 
        yl = f(xl) 
        xlist_fine=np.linspace(self.a, self.b, resolution)
       
        for i in range(self.n):
            x1=np.linspace(xl[i], xl[i+1], resolution)
            m=(xl[i]+xl[i+1])/2
            bg=xl[i]
            bd=xl[i+1]
            l0 = (x1-m)/(bg-m)*(x1-bd)/(bg-bd)
            l1 = (x1-bg)/(m-bg)*(x1-bd)/(m-bd)
            l2 = (x1-bg)/(bd-bg)*(x1-m)/(bd-m)
            P = f(bg)*l0 + f(m)*l1 + f(bd)*l2
            self.aa.plot(x1,P,'b')
            self.aa.plot(m,f(m),"g*")
        yflist_fine = f(xlist_fine)
        self.aa.plot(xlist_fine, yflist_fine,'b')
        self.aa.plot(xl, yl,'r')
        
        self.aa.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )
    ###################################################################################    
class mclass:
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window,highlightbackground="gray", highlightthickness=2, width=100, height=100, bd= 5)
        self.fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=100, height=100, bd= 5)
        
        ########################################################################
        self.func_txt=StringVar()
        self.func_txt.set("      F(x):")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4 , fg = '#00004d', font = "Helvetica 12 bold italic")
        self.label_func.grid(row=1,column=0)# affichage label de f(x)
        self.box = Entry(self.fr1,borderwidth=3,bg='#ccccff')
        self.box.grid(row=1,column=1)
        ########################################################################self.a_txt=StringVar()
        self.a_txt=StringVar()
        self.a_txt.set("               a:               ")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT, anchor="w", height=4 , fg = '#00004d', font = "Helvetica 12 bold italic")
        self.label_a.grid(sticky = E,row=2,column=0)
        self.boxa = Entry(self.fr1,width=20,borderwidth=3,bg='#ccccff')
        self.boxa.grid(sticky = W,row=2,column=1)
       ################################################################################################# 
        self.b_txt=StringVar()
        self.b_txt.set("               b:                ")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4, fg = '#00004d', font = "Helvetica 12 bold italic")
        self.label_b.grid(sticky = E,row=3,column=0)
        self.boxb = Entry(self.fr1,width=20,borderwidth=3,bg='#ccccff')
        self.boxb.grid(sticky = W,row=3,column=1)
        ##################################################################################################
        self.n_txt=StringVar()
        self.n_txt.set("               N:               ")
        self.label_n=Label(self.fr1, textvariable=self.n_txt,justify=RIGHT, anchor="w", height=4 , fg = '#00004d', font = "Helvetica 12 bold italic")
        self.label_n.grid(sticky = E,row=4,column=0)
        self.boxn = Entry(self.fr1,width=20,borderwidth=3,bg='#ccccff')
        self.boxn.grid(sticky = W,row=4,column=1)
       ################################################################################################# 
        #self.b_txt=StringVar()
        #self.b_txt.set("               b:                ")
        #self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4, fg = '#00004d', font = "Helvetica 12 bold italic")
        #self.label_b.grid(sticky = E,row=3,column=0)
        #self.boxb = Entry(self.fr1,width=20,borderwidth=3,bg='#ccccff')
        #self.boxb.grid(sticky = W,row=3,column=1)
        ##################################################################################################
        self.methode_txt=StringVar()
        self.methode_txt.set("Méthode:  ")
        self.label_methode=Label(self.fr1, textvariable=self.methode_txt,justify=RIGHT, anchor="w", height=4 , fg = '#00004d', font = "Helvetica 12 bold italic")
        self.label_methode.grid(sticky = E,row=5,column=0)
        self.n=StringVar()
        self.combo=ttk.Combobox(self.fr1,textvariable=self.n)
        self.combo['values'] = (' Simpson',  
                                  ' Trapèze', 
                                  ' rectangle', 
                                  ' Milieu') 
        self.combo.grid(sticky = W,row=5,column=1)
        self.combo.current(0) 
        
        
    
        
        #################################################################
        self.button = Button (self.fr1, width =35,text="plot",bg='#9999ff',command=self.plot)
        self.button.grid(row=6,column=0,columnspan=3)
        #########################################################
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
        self.fig = Figure(figsize=(6,6))
        #self.Graph(f)
        self.a = self.fig.add_subplot(111)
        #self.a.set_title ("Rectangle", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("#ccccb3")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        
    
        
        
        ###########################################
        
    def plot (self):
        try:
            if self.combo.get()==' rectangle':
                f= lambda x: eval(self.box.get())
                x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
                pp=f(x)
            
                self.a.cla()
                self.a.set_xlim([float(self.boxa.get()), float(self.boxb.get())])
           # self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
                self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.set_title ("La méthode de Rectangle", fontsize=22 ,color = 'red')
                self.a.set_ylabel("y=f(x)", fontsize=14)
                self.a.set_xlabel("x", fontsize=14)
                self.a.grid(True)
                R = Rectangle(float(self.boxa.get()),float(self.boxb.get()),int(self.boxn.get()), f,self.a)
            #self.a.plot(x, f(x),color='blue')
                R.Graph(f)
                self.fig.canvas.draw()
            if self.combo.get()==' Trapèze':
                f= lambda x: eval(self.box.get())
                x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
                pp=f(x)
            
                self.a.cla()
                self.a.set_xlim([float(self.boxa.get()), float(self.boxb.get())])
           # self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
                self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.set_title ("La méthode de trapèze", fontsize=22,color = 'red')
                self.a.set_ylabel("y=f(x)", fontsize=14)
                self.a.set_xlabel("x", fontsize=14)
                self.a.grid(True)
                T = Trapezoidal(float(self.boxa.get()),float(self.boxb.get()), int(self.boxn.get()), f,self.a)
            #self.a.plot(x, f(x),color='blue')
                T.Graph(f)
                self.fig.canvas.draw()
            if self.combo.get()==' Milieu':
                f= lambda x: eval(self.box.get())
                x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
                pp=f(x)
            
                self.a.cla()
                self.a.set_xlim([float(self.boxa.get()), float(self.boxb.get())])
           # self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
                self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.set_title ("La méthode de Milieu", fontsize=22,color = 'red')
                self.a.set_ylabel("y=f(x)", fontsize=14)
                self.a.set_xlabel("x", fontsize=14)
                self.a.grid(True)
                M = RectangleM(float(self.boxa.get()),float(self.boxb.get()), int(self.boxn.get()), f,self.a)
            #self.a.plot(x, f(x),color='blue')
                M.Graph(f)
                self.fig.canvas.draw()
            if self.combo.get()==' Simpson':
                f= lambda x: eval(self.box.get())
                x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
                pp=f(x)
            
                self.a.cla()
                self.a.set_xlim([float(self.boxa.get()), float(self.boxb.get())])
           # self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
                self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()),float(self.boxb.get()), 1))
                self.a.set_title (" méthode Simpson ", fontsize=22,color = 'red')
                self.a.set_ylabel("y=f(x)", fontsize=14)
                self.a.set_xlabel("x", fontsize=14)
                self.a.grid(True)
                S= Simpson(float(self.boxa.get()),float(self.boxb.get()), int(self.boxn.get()), f,self.a)
            #self.a.plot(x, f(x),color='blue')
                S.Graph(f)
                self.fig.canvas.draw()
        except ValueError:
            messagebox.showwarning("ValueError", "veuillez votre saisi")
window= Tk()
start= mclass(window)
window.mainloop()