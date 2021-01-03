from tkinter import*
from tkinter import Tk,StringVar,ttk
import random
import time;
import datetime

root =  Tk()
root.geometry("1350x750+0+0")
root.title("Train Ticket")
root.configure(background = 'black')

Tops = Frame(root  ,width = 1350, height = 100,bd = 14,relief = 'raise')
Tops.pack(side = TOP)

f1 = Frame(root , width = 900,height = 650,bd = 8,relief = "raise")
f1.pack(side=LEFT)
f2 = Frame(root,width = 440, height = 650,bd = 8,relief = "raise")
f2.pack(side = RIGHT)

frametopRight = Frame(f2,width=440,height = 650,bd=12,relief = "raise")
frametopRight.pack(side = TOP)
frameBottomRight = Frame(f2,width = 440,height = 50,bd=16,relief = "raise")
frameBottomRight.pack(side = BOTTOM)

f1a = Frame(f1,width = 900,height = 330,bd = 8,relief = "raise")
f1a.pack(side =TOP)
f2a = Frame(f1,width = 900,height = 320,bd = 6,relief = "raise")
f2a.pack(side =BOTTOM)

topleft1 = Frame(f1a,width = 300, height = 200,bd=16,relief = "raise")
topleft1.pack(side = LEFT)
topleft2 = Frame(f1a,width = 300, height = 200,bd=16,relief = "raise")
topleft2.pack(side = RIGHT)
topleft3 = Frame(f1a,width = 300, height = 200,bd=16,relief = "raise")
topleft3.pack(side = RIGHT)

#----------------------------------------------------------------------------------------------

bottomleft1 = Frame(f2a,width = 450,height = 450,bd=14, relief = "raise")
bottomleft1.pack(side=LEFT)

bottomleft2 = Frame(f2a,width = 450,height = 450,bd=14, relief = "raise")
bottomleft2.pack(side=RIGHT)

#---------------------------------------------------------------------------------------------

Tops.configure(background = 'black')
f1.configure(background = 'black')
f2.configure(background = 'black')
lblTitile = Label(Tops,font = ('arial',45,'bold'),text = "Railway Ticket Booking System" ,bd = 10,width = 41,justify = 'center')
lblTitile.grid(row = 0,column = 0)

Date1 = StringVar()
time1 = StringVar()
Ticketclass = StringVar()
TicketPrice = StringVar()
Child_Ticket  =  StringVar()
Adult_Ticket =  StringVar()
From_Destination = StringVar()
To_Destination = StringVar()
Fee_Receipt = StringVar()
Route = StringVar()
Receipt_Ref = StringVar()

Ticketclass.set("")
TicketPrice.set("")
Adult_Ticket.set("")
Child_Ticket.set("")
From_Destination.set("")
To_Destination.set("")
Fee_Receipt.set("")
Route.set("")
Receipt_Ref.set("")

#-----------------------------------------------------------------------------------------------------------

lblReceipt = Label(frametopRight,font = ('arial',14,'bold'),text = "Travelling Ticket Systems" ,bd = 10,width=30,justify = 'center')
lblReceipt.grid(row = 0,column = 0)
lblClass1 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Class" ,relief = 'sunken',width=8,justify = 'center')
lblClass1.grid(row = 0,column = 0)
lblClass2 = Label(frameBottomRight,font = ('arial',14,'bold'),relief = 'sunken',width=8,justify = 'center')
lblClass2.grid(row = 1,column = 0)
lblTicket1 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Ticket" ,relief = 'sunken',width=8,justify = 'center')
lblTicket1.grid(row = 0,column = 1)
lblTicket2 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Ticket" ,relief = 'sunken',width=8,justify = 'center')
lblTicket2.grid(row = 1,column = 1)
lblAdult1 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Adult" ,relief = 'sunken',width=8,justify = 'center')
lblAdult1.grid(row = 0,column = 2)
lblAdult2 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Adult" ,relief = 'sunken',width=8,justify = 'center')
lblAdult2.grid(row = 1,column = 2)
lblChild1 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Child" ,relief = 'sunken',width=8,justify = 'center')
lblChild1.grid(row = 0,column = 3 )
lblChild2 = Label(frameBottomRight,font = ('arial',14,'bold'),text = "Child" ,relief = 'sunken',width=8,justify = 'center')
lblChild2.grid(row = 1,column = 3 )
#------------------------------------------------------------------------------

lblsp = Label(frameBottomRight,font = ('arial',14,'bold'),width=34,height=1,relief='sunken',
        justify='center')
lblsp.grid(row=9,column=0,columnspan=4)

#-----------------------------------------------------------------------------

lblFrom1= Label(frameBottomRight,font = ('arial',14,'bold'),text="From",relief='sunken',width=8,justify='center')
lblFrom1.grid(row = 3,column = 1 )
lblFrom2= Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblFrom2.grid(row = 3,column = 2 )
#----------------------------------------------------------------------
lblTo1= Label(frameBottomRight,font = ('arial',14,'bold'),text="To",relief='sunken',width=8,justify='center')
lblTo1.grid(row = 4,column = 1 )
lblTo2= Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblTo2.grid(row = 4,column = 2 )
lblPrice1 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblPrice1.grid(row=5,column=1)
lblPrice2 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblPrice2.grid(row=5,column=2 )
#-------------------------------------------------------------------------
lblsp = Label(frameBottomRight,font = ('arial',14,'bold'),width=34,height=2,relief='sunken',justify='center')
lblsp.grid(row=6,column=0,columnspan=4)
#--------------------------------------------------------------------------
lblRefNo1 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblRefNo1.grid(row=7,column=0 )
lblRefNo2 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblRefNo2.grid(row=8,column=0 )
lblTime1 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblTime1.grid(row=7,column=1 )
lblTime2 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',textvariable = time1,width=8,justify='center')
lblTime2.grid(row=8,column=1 )
lblDate1 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblDate1.grid(row=7,column=2 )
lblDate2 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',textvariable = Date1,width=8,justify='center')
lblDate2.grid(row=8,column=2 )
lblRoute1 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblRoute1.grid(row=7,column=3 )
lblRoute2 = Label(frameBottomRight,font = ('arial',14,'bold'),relief='sunken',width=8,justify='center')
lblRoute2.grid(row=8,column=3 )
#------------------------------------------------------------------
def btnClick(numbers):
  global operator
  operator = operator+str(numbers)
  text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def iExit():
     qExit = messagebox.askyesno("Quit System","Do you want to quit?")
     if qExit > 0:
       root.destroy()
       return

def Travel_cost():
  if (var9.get() == "Delhi" and var1.get() == 1 and var4.get() == 1):
    Tcost = float(300.2)
    Single = float(var12.get())
    Adult_Tax = "R",str('%.2f'%((Tcost * Single) * 0.03))
    Adult_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0.03)))
    Tax.set(Adult_Tax)
    SubTotal.set(Adult_Fees)
    Ticketclass.set("Standard")
    TicketPrice.set(Adult_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Delhi")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)

  elif (var9.get() == "Delhi" and var1.get() == 1 and var5.get() == 1):
    Tcost = float(300.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("Economy")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Delhi")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)

  elif (var9.get() == "Kochi" and var1.get() == 1 and var4.get() == 1):
    Tcost = float(400.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("Economyn")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Kochi")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)
    
  elif (var9.get() == "Kochi" and var1.get() == 1 and var5.get() == 1):
    Tcost = float(440.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("Economy")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Kochi")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)
    
  elif (var9.get() == "Mumbai" and var1.get() == 1 and var4.get() == 1):
    Tcost = float(360.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("Economy")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Mumbai")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)
    
  elif (var9.get() == "Mumbai" and var1.get() == 1 and var5.get() == 1):
    Tcost = float(360.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("Economy")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Mumbai")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)

  elif (var9.get() == "Chennai" and var1.get() == 1 and var4.get() == 1):
    Tcost = float(500.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("First Class")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Chennai")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)
    
  elif (var9.get() == "Chennai" and var1.get() == 1 and var5.get() == 1):
    Tcost = float(500.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("First Class")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Chennai")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)

  elif (var9.get() == "Banglore" and var1.get() == 1 and var4.get() == 1):
    Tcost = float(387.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("First Class")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Banglore")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)
    
  elif (var9.get() == "Banglore" and var1.get() == 1 and var5.get() == 1):
    Tcost = float(387.2)
    Single = float(var12.get())
    Child_Tax = "R",str('%.2f'%((Tcost * Single) * 0))
    Child_Fees =  "R",str('%.2f'%((Tcost * Single)))
    TotalCost = "R", str('%.2f'%((Tcost * Single) +  ((Tcost * Single)*0)))
    Tax.set(Child_Tax)
    SubTotal.set(Child_Fees)
    Ticketclass.set("First Class")
    TicketPrice.set(Child_Fees)
    Child_Ticket.set("No")
    Adult_Ticket.set("Yes")
    From_Destination.set("Salem")
    To_Destination.set("Banglore")
    Fee_Price.set(TotalCost)
    Total.set(TotalCost)
    Route.set("Direct")

    x = random.randit(109,5876)
    randomRef = str(x)
    Receipt_Ref.set("TFL"+ randomRef)

def chkbutton_value():
  if(var10.get()==1):
    var12.set("")
    entSingle.configure(state = NORMAL)
  elif var10.get()== 0:
    entSingle.configure(state = DISABLE)
    var12.set("0")
  if (var11.get() == 1):
    var6.set("0")
    entReturn.confiure(state = NORMAL)
  elif var11.get()== 0:
    entReturn.configure(state = DISABLE)
    var67.set("0")
    
def Reset():
  var1.set("0")
  var2.set("0")
  var3.set("0")
  var4.set("0")
  var5.set("0")
  var6.set("0")
  var7.set("0")
  var8.set("0")
  var9.set("0")
  var10.set("0")
  var11.set("0")
  var12.set("0")
  SubTotal.set("0")
  Total.set("0")
  Ticketclass.set("")
  TicketPrice.set("")
  Child_Ticket.set("")
  Adult_Ticket.set("")
  From_Destination.set("")
  To_Destination.set("")
  Fee_Price.set("")
#---------------------------------------------------------------------------------
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()
var11 = StringVar()
var12 = StringVar()
Tax = StringVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")



 
Date1 = StringVar()
time1 = StringVar()
SubTotal = StringVar()
Total = StringVar()
text_Input = StringVar()
operator = ""
#-------------------------------------------------------------------------------------------------------------------------------
Date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime("%H:%M:%S"))
#--------------------------------------------------------------------------------------------------------------------------------------------------------
lblClass = Label(topleft1 , font=('arial',22,'bold'),text = 'Class',bd = 8)
lblClass.grid(row = 0,column = 0,sticky = W)
chkStandard = Checkbutton(topleft1 , font=('arial',16,'bold'),text = 'Standard',variable = var1,onvalue = 1,offvalue = 0)
chkStandard.grid(row = 1,column = 0,sticky = W)
chkEconomy= Checkbutton(topleft1 , font=('arial',16,'bold'),text = 'Economy',variable = var2,onvalue = 1,offvalue = 0)
chkEconomy.grid(row = 2,column = 0,sticky = W)
chkFirstClass = Checkbutton(topleft1 , font=('arial',16,'bold'),text = 'first Class',variable = var3,onvalue = 1,offvalue = 0)
chkFirstClass.grid(row = 3,column = 0,sticky = W)
#-----------------------------------------------------------------------------
lblselect= Label(topleft3 , font=('arial',20,'bold'),text = 'Select a Destination',bd = 8)
lblselect.grid(row = 0,column = 0,sticky = W,columnspan = 2)
lblDestination = Label(topleft3 , font=('arial',20,'bold'),text = 'Destination',bd = 2)
lblDestination.grid(row = 1,column = 0,sticky = W)
cboDestination = ttk.Combobox(topleft3,textvariable = var9,state = 'readonly', font=('arial',22,'bold'),width = 20)
cboDestination['value'] = ('Delhi','Chennai','Mumbai','Banglore','Kochi')
cboDestination.current(0)
cboDestination.grid(row = 1,column = 1)

chkAdult = Checkbutton(topleft3 , font=('arial',20,'bold'),text = 'Adult',variable = var4,onvalue = 1,offvalue = 0)
chkAdult.grid(row = 2,column = 0,sticky = W)
chkChild = Checkbutton(topleft3 , font=('arial',20,'bold'),text = 'Child',variable = var5,onvalue = 1,offvalue = 0)
chkChild.grid(row = 3,column = 0,sticky = W)
#------------------------------------------------------------------------------
lblClass = Label(topleft2 , font=('arial',22,'bold'),text = 'Ticket Type',bd = 8)
lblClass.grid(row = 0,column = 0,sticky = W)
chkSingle = Checkbutton(topleft2 , font=('arial',16,'bold'),text = 'Single',variable = var10,onvalue = 1,offvalue = 0,command = chkbutton_value)
chkSingle.grid(row = 1,column = 0,sticky = W)
Entsingle = Entry(topleft2 , font=('arial',20,'bold'),textvariable = var12,bd=2,width = 8,state = DISABLED)
Entsingle.grid(row=1,column=1,sticky=W)
chkReturn= Checkbutton(topleft2 , font=('arial',16,'bold'),text = 'Return',variable = var11,onvalue = 1,offvalue = 0,command= chkbutton_value)
chkReturn.grid(row = 2,column = 0,sticky = W)
entReturn= Entry(topleft2 , font=('arial',16,'bold'),textvariable = var6,bd = 2,width=8,state =DISABLED)
entReturn.grid(row = 2,column = 1,sticky = W)

lblComment = Label(topleft2 ,  font=('arial',22,'bold'),text = 'Comment',bd=8)
lblComment.grid(row =3 ,column = 0,sticky = W)
entComment= Entry(topleft2 , font=('arial',16,'bold'),textvariable = var7,bd = 2,width=8)
entComment.grid(row = 3,column = 1,sticky = W)
#----------------------------------------------------------------------------

text_Input = StringVar()
txtDisplay = Entry(bottomleft2 ,font = ('arial',10,'bold') ,textvariable = text_Input,bd = 16,justify = 'right',width=36)
txtDisplay.grid(columnspan = 4)

btn7 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "7",command = lambda:btnClick(7),width=4).grid(row = 2,column = 0)               
btn8 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "8",command = lambda:btnClick(8),width=4).grid(row = 2,column = 1)
btn9 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "9",command = lambda:btnClick(9),width=4).grid(row = 2,column = 2)     
Addition = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "+",command = lambda:btnClick("+"),width=4).grid(row = 2,column = 3)
#--------------------------------------------------------------------
btn4 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "4",command = lambda:btnClick(4),width=4).grid(row = 3,column = 0)               
btn5 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "5",command = lambda:btnClick(5),width=4).grid(row = 3,column = 1)
btn6 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "6",command = lambda:btnClick(6),width=4).grid(row = 3,column = 2)     
Subtraction = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
              text = "-",command = lambda:btnClick("-"),width=4).grid(row = 3,column = 3)
#----------------------------------------------------------------------------------
btn1 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "1",command = lambda:btnClick(1),width=4).grid(row = 4,column = 0)               
btn2 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "2",command = lambda:btnClick(2),width=4).grid(row = 4,column = 1)
btn3 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "3",command = lambda:btnClick(3),width=4).grid(row = 4,column = 2)     
Multiplication = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
              text = "*",command = lambda:btnClick("*"),width=4).grid(row = 4,column = 3)
#--------------------------------------------------------------------------------------------
btn0 = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "0",command = lambda:btnClick(0),width=4).grid(row = 5,column = 0)     
btnClear = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
           text ="C",width = 4,command = btnClearDisplay).grid(row = 5,column = 1)
btnEquals = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
            text = "=",width=4,command = btnEqualsInput).grid(row = 5,column = 2)
Division = Button(bottomleft2, padx = 8,pady = 8,bd = 8,fg = "black",font = ('arial',10,'bold'),
       text = "/", bg = "powder blue",command = lambda:btnClick("/"),width=4).grid(row = 5,column = 3)                   
#-----------------------------------------------------------------------------------
lblStateTax = Label(bottomleft1,font = ('arial',24,'bold'),text = "State Tax",bd = 16,anchor = "w")
lblStateTax.grid(row=3,column=2)
txtStateTax = Entry(bottomleft1,font = ('arial',16,'bold'),textvariable = Tax,bd=10,width =28,bg="#ffffff",justify = 'right')
txtStateTax.grid(row=3,column=3)

lblSubTotal = Label(bottomleft1,font = ('arial',24,'bold'),text = "Sub Total",bd = 6,anchor = "w")
lblStateTax.grid(row=4,column=2)
txtStateTax = Entry(bottomleft1,font = ('arial',16,'bold'),textvariable = SubTotal,bd=10,width =28,bg="#ffffff",justify = 'right')
txtStateTax.grid(row=4,column=3)

lblTotalCost = Label(bottomleft1,font = ('arial',10,'bold'),text = "Total Cost",bd = 6,anchor = "w")
lblTotalCost.grid(row=3,column=2)
txtTotalCost = Entry(bottomleft1,font = ('arial',10,'bold'),textvariable = Tax,bd=10,insertwidth =4,bg="#ffffff",justify = 'right')
txtTotalCost.grid(row=5,column=3)

#--------------------------------------------------------------

lblSpace = Label(bottomleft1,font = ('arial',24,'bold'),text = "  \n",bd=16,anchor='w')
lblSpace.grid(row=6,column=0,columnspan=4)

#--------------------------------------------------------------------------------------------------

lblSpace = Label(bottomleft1,font = ('arial',24,'bold'),text = "  \n",bd=16,anchor='w')
lblSpace.grid(row=6,column=2)

#------------------------------------------------------------------------------------------------

lblSpace = Label(bottomleft2,font = ('arial',24,'bold'),text = "  \n",bd=16,anchor='w')
lblSpace.grid(row=6,columnspan=4)

#------------------------------------------------------------------------------------------------

"""lblReceipt = Label(frameBottomRight,font = ('arial',12,'bold'),text = "Receipt",bd=2,anchor='w')
lblReceipt.grid(row=9,column=0,sticky=W)
txtReceipt = Text(frameBottomRight,width=40,height=7,bg="white",bd=8,font = ('arial',11,'bold'))
txtReceipt.grid(row=10,column=0,columnspan=4)"""

lblsp = Label(frameBottomRight,font = ('arial',14,'bold'),width=34,height=1,relief='sunken',justify='center')
lblsp.grid(row=9,column=0,columnspan=4)

#--------------------------------------------------------------------------------------------------------------
btnTotal = Button(frameBottomRight,text = 'Convert',padx=2,pady=2,bd=2,fg="black",
           font = ('arial',12,'bold'),width=6,height=1,command = Travel_cost).grid(row=10,column=0)
btnClear = Button(frameBottomRight,text = 'Clear',padx=2,pady=2,bd=2,fg="black",
           font = ('arial',12,'bold'),width=6,height=1,command = Reset).grid(row=10,column=1)
btnReset = Button(frameBottomRight,text = 'Reset',padx=2,pady=2,bd=2,fg="black",
           font = ('arial',12,'bold'),width=6,height=1,command = Reset).grid(row=10,column=2)
btnExit = Button(frameBottomRight,text = 'Exit',padx=2,pady=2,bd=2,fg="black",
           font = ('arial',12,'bold'),width=6,height=1,command = iExit).grid(row=10,column=3)

#---------------------------------------------------------------------------------------

lblsp = Label(frameBottomRight,font = ('arial',14,'bold'),width=34,height=2,relief='sunken',justify='center')
lblsp.grid(row=11,column=0,columnspan=4)

#--------------------------------------------------------------------------------------------------------------------------

root.mainloop()


            
