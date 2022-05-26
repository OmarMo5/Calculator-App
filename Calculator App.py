import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
frm=tk.Tk()
w=400
h=550
ws=(frm.winfo_screenwidth()-w)/2
hs=(frm.winfo_screenheight()-h)/2-50
frm.geometry("%dx%d+%d+%d"%(w,h,ws,hs))
frm.title("Calculator")
frm.configure(bg='lightblue')
varlbl=tk.StringVar()
lbl=tk.Entry(frm,width=35,border="4px solid #eee",font=("None 15 bold"),textvariable=varlbl).grid(row=0,column=0,pady=10)

class AllData:
    # def clearOneCahr(self):
    #     y = ""
    #     text = varlbl.get()
    #     neg = -1
    #     for x in text:
    #         y += text[:neg] #text.replace("",text[-1])
    #         varlbl.set(y)
    #         neg += -1
    #         break
    # global ToAddAll

    ToAddAll = varlbl.get()
    def inpo(self):
        self.ToAddAll += "^"
        varlbl.set(self.ToAddAll)
    def inmod(self):
        self.ToAddAll += "%"
        varlbl.set(self.ToAddAll)
    def insum(self):
        self.ToAddAll += "+"
        varlbl.set(self.ToAddAll)
    def insmin(self):
        self.ToAddAll += "-"
        varlbl.set(self.ToAddAll)
    def inmul(self):
        self.ToAddAll += "*"
        varlbl.set(self.ToAddAll)
    def indiv(self):
        self.ToAddAll += "/"
        varlbl.set(self.ToAddAll)

    def inqul(self):
        expp = varlbl.get()
        self.ToAddAll = ""
        varlbl.set(self.ToAddAll)
        oper = ""
        for x in expp:
            if (x.isdigit()): pass
            else:
                oper = x
                y = expp.find(oper)
        num1 = int(expp[0:y])
        num2 = int(expp[y+1:])
        if(oper=="+"):
            resl = num1 + num2
            varlbl.set(resl)
        elif(oper=="-"):
            resl = num1 - num2
            varlbl.set(resl)
        elif(oper=="*"):
            resl = num1 * num2
            varlbl.set(resl)
        elif(oper=="/"):
            resl = num1 / num2
            varlbl.set(resl)
        elif(oper=="%"):
            resl = num1 % num2
            varlbl.set(resl)
        else:
            resl = pow(num1,num2)
            varlbl.set(resl)

    def sqr(self):
        import math
        sqrTonum = math.sqrt(int(varlbl.get()))
        varlbl.set(int(sqrTonum))
    def expo(self):
        import math
        expTonum = math.exp(int(varlbl.get()))
        varlbl.set(expTonum)
    def factorial(self):
        y=1
        toFact = int(varlbl.get())
        for x in range(1,toFact+1):
           y *= x
        varlbl.set(y)

    def in0(self):
        self.ToAddAll += "0"
        varlbl.set(self.ToAddAll)
    def in1(self):
        self.ToAddAll += "1"
        varlbl.set(self.ToAddAll)
    def in2(self):
        self.ToAddAll += "2"
        varlbl.set(self.ToAddAll)
    def in3(self):
        self.ToAddAll += "3"
        varlbl.set(self.ToAddAll)
    def in4(self):
        self.ToAddAll += "4"
        varlbl.set(self.ToAddAll)
    def in5(self):
        self.ToAddAll += "5"
        varlbl.set(self.ToAddAll)
    def in6(self):
        self.ToAddAll += "6"
        varlbl.set(self.ToAddAll)
    def in7(self):
        self.ToAddAll += "7"
        varlbl.set(self.ToAddAll)
    def in8(self):
        self.ToAddAll += "8"
        varlbl.set(self.ToAddAll)
    def in9(self):
        self.ToAddAll += "9"
        varlbl.set(self.ToAddAll)
    def DeAll(self):
        self.ToAddAll = ""
        varlbl.set(self.ToAddAll)
DaToAcc = AllData()

frame=tk.Frame(frm)
btn=tk.Button(frame,text="CE",height="2",width="7",font=12,background="lightblue",command=DaToAcc.DeAll)
btn1=tk.Button(frame,text="C",height="2",width="7",font=12,background="lightblue",command=DaToAcc.DeAll)#command=DaToAcc.clearOneCahr)
btn2=tk.Button(frame,text="x^y",height="2",width="7",font=12,background="#BBB",command=DaToAcc.inpo)
btn3=tk.Button(frame,text="%",height="2",width="7",font=12,background="#BBB",command=DaToAcc.inmod)

btn4=tk.Button(frame,text="Sqr",height="2",width="7",font=12,background="#BBB",command=DaToAcc.sqr)
btn5=tk.Button(frame,text="!",height="2",width="7",font=12,background="#BBB",command=DaToAcc.factorial)
btn6=tk.Button(frame,text="Exp",height="2",width="7",font=12,background="#BBB",command=DaToAcc.expo)
btn7=tk.Button(frame,text="<",height="2",width="7",font=12,background="lightblue")

btn8=tk.Button(frame,text="1",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in1)
btn9=tk.Button(frame,text="2",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in2)
btn10=tk.Button(frame,text="3",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in3)
btn11=tk.Button(frame,text="+",height="2",width="7",font=12,background="#BBB",command=DaToAcc.insum)

btn12=tk.Button(frame,text="4",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in4)
btn13=tk.Button(frame,text="5",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in5)
btn14=tk.Button(frame,text="6",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in6)
btn15=tk.Button(frame,text="-",height="2",width="7",font=12,background="#BBB",command=DaToAcc.insmin)

btn16=tk.Button(frame,text="7",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in7)
btn17=tk.Button(frame,text="8",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in8)
btn18=tk.Button(frame,text="9",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in9)
btn19=tk.Button(frame,text="*",height="2",width="7",font=12,background="#BBB",command=DaToAcc.inmul)

btn20=tk.Button(frame,text="0",height="2",width="7",font=12,background="lightblue",command=DaToAcc.in0)
btn21=tk.Button(frame,text=".",height="2",width="7",font=12,background="lightblue")
btn22=tk.Button(frame,text="=",height="2",width="7",font=12,background="#BBB",command=DaToAcc.inqul)
btn23=tk.Button(frame,text="/",height="2",width="7",font=12,background="#BBB",command=DaToAcc.indiv)

btn24=tk.Button(frame,text="Clear",height="2",width="15",font=("none 15 bold"),background="lightblue",foreground="black",command=lambda :frm.destroy())

frame.grid()
btn.grid(row=1,column=0,pady=10)
btn1.grid(row=1,column=1,padx=7)
btn2.grid(row=1,column=2,padx=7)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=2,column=3)
btn8.grid(row=3,column=0,pady=10)
btn9.grid(row=3,column=1)
btn10.grid(row=3,column=2)
btn11.grid(row=3,column=3)
btn12.grid(row=4,column=0,pady=10)
btn13.grid(row=4,column=1)
btn14.grid(row=4,column=2)
btn15.grid(row=4,column=3)
btn16.grid(row=5,column=0)
btn17.grid(row=5,column=1)
btn18.grid(row=5,column=2)
btn19.grid(row=5,column=3)
btn20.grid(row=6,column=0,pady=10)
btn21.grid(row=6,column=1)
btn22.grid(row=6,column=2)
btn23.grid(row=6,column=3)
btn24.grid(row=7,column=0,columnspan=4)
frm.mainloop()
