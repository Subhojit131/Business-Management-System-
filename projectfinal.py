
from tkinter import*
def main():    
    
    #cost of the products
    bread=14
    coffee=20
    soap=5
    chocolate=9
    chips=5
    juice=25
    shampo=3
    sp={'bread':22,'coffee':35,'soap':10,'chocolate':20,'chips':10,'juice':25,'shampo':1}
    #the functions of the widgets 
    def annualprofit():
        a=''
        b=0
        f1=open('Sales report','r')
        for lines in f1:
            if lines.startswith('p') :
                a=lines[14:]
                b=float(a)+b
        print(b)
        window1 = Toplevel()
        window1.geometry('350x150')
        labelnew=Label(window1,text="Profit made till now"+myentry10.get()) 
        labelnew2=Label(window1,text=b)
        labelnew.pack()
        labelnew2.pack()         
    
    
    def profit(n):
        avg=bread*int(myentry3.get())+coffee*int(myentry4.get())+soap*int(myentry5.get())+chocolate*int(myentry6.get())+chips*int()+juice*int(myentry7.get())+shampo*int(myentry9.get())
        profit=float(n)-avg
        return profit
        
        
    def save():
        #Code to be written
        f1=open('Sales report','a+')
        f1.write('name:- '+myentry.get()+'\n')
        if gen_var.get()==1:
            f1.write('gender:- Male'+'\n')
        else:
            f1.write('gender:- Female'+'\n')
        b=str(nam(1))
        f1.write('Amount:- '+b+'\n')
        f1.write('Discount:- '+myentry11.get()+'%'+'\n')
        f1.write('Date:- '+myentry10.get()+'\n')
        label7=Label(root,text="info saved to file Sales Report")
        label7.grid(row=15)
        c=str(profit(b))
        f1.write('profit made:- '+c+'\n')
        f1.close()
        
        
        
    
    def Refresh():
        root.destroy()
        main()
        
        
        
                    
    def nam(n=0):
        window = Toplevel()
        window.geometry('450x450')
        if n==0:
            newlabel = Label(window, text = "Bill")
            newlabel.grid(row=0,column=4)
        else:
            newlabel = Label(window, text = "Saved info")
            newlabel.grid(row=0,column=4)
        var=myentry.get()
        label0=Label(window,text="Name:- ")
        label=Label(window,text=var)
        label0.grid(row=1,column=0)
        label.grid(row=1,column=1)
        labelg=Label(window,text='Gender:- ')
        if gen_var.get()==1:
            label2=Label(window,text="male")
        else:
            label2=Label(window,text="female")
        labelg.grid(row=2,column=0)
        label2.grid(row=2,column=1)    
        #tobill=0
        bread_var=myentry3.get()
        coffee_var=myentry4.get()
        soap_var=myentry5.get()
        chocolate_var=myentry6.get()
        chips_var=myentry7.get()
        juice_var=myentry8.get()
        shampo_var=myentry9.get()
        date=myentry10.get()
        discount_var=myentry11.get()
        avg= sp["bread"]*int(bread_var)+sp['coffee']*int(coffee_var)+sp["soap"]*int(soap_var)+sp["chocolate"]*int(chocolate_var)+sp["chips"]*int(chips_var)+sp["juice"]*int(juice_var)+sp["shampo"]*int(shampo_var)
        disc=avg*int(discount_var)/100
        if int(discount_var)>=1:
            tobill=avg-disc
        else:
            tobill=avg
        labelb=Label(window,text="Total Amount:- ")
        label3=Label(window,text=tobill)
        labelb.grid(row=3,column=0)
        label3.grid(row=3,column=1)
        label5=Label(window,text='Discount:- ')
        label6=Label(window,text=discount_var+"%")
        label5.grid(row=4,column=0)
        label6.grid(row=4,column=1)
        labeld=Label(window,text="Date:- ")
        label4=Label(window,text=date)
        labeld.grid(row=5,column=0)
        label4.grid(row=5,column=1)
        return(tobill)
        
        
         
    
        
     
            
                    
        

    #creating root windows and the widget variables        
    root=Tk()
    date=StringVar()
    var = StringVar()
    gen_var=IntVar()
    bread_var=IntVar()
    coffee_var=IntVar()
    soap_var=IntVar()
    chocolate_var=IntVar()
    chips_var=IntVar()
    juice_var=IntVar()
    shampo_var=IntVar()
    discount_var=IntVar()
    root.title("Business Management System")
    root.geometry("450x450")
    #making widgets 
    mylabel= Label(root, text="Enter your name ")
    myentry= Entry(root)
    mylabel2= Label(root, text="Enter your gender ")
    rd1=Radiobutton(root,text="male",variable=gen_var,value=1)
    rd2=Radiobutton(root,text="female",variable=gen_var,value=2)
    mylabel3= Label(root, text="Enter number of bread ")
    myentry3= Entry(root,textvariable=bread_var)
    mylabel4= Label(root, text="Enter number of coffee packets ")
    myentry4= Entry(root,textvariable=coffee_var)
    mylabel5= Label(root, text="Enter number of soap ")
    myentry5= Entry(root,textvariable=soap_var)
    mylabel6= Label(root, text="Enter number of chocolets")
    myentry6= Entry(root,textvariable=chocolate_var)
    mylabel7= Label(root, text="Enter number of chips")
    myentry7= Entry(root,textvariable=chips_var)
    mylabel8= Label(root, text="Enter number of juce cartons")
    myentry8= Entry(root,textvariable=juice_var)
    mylabel9= Label(root, text="Enter number of shampoo pouches")
    myentry9= Entry(root,textvariable=shampo_var)
    mylabel10=Label(root,text="enter the date")
    myentry10=Entry(root,textvariable=date)
    mylabel11=Label(root,text="Enter the discount percent")
    myentry11=Entry(root,textvariable=discount_var)

    mybutton=Button(root,text="Enter",command=nam)


    #adding widgets to the screen
    mylabel.grid(row=0,column=0)
    myentry.grid(row=1,column=0)
    mylabel2.grid(row=3,column=0)
    rd1.grid(row=4,column=0)
    rd2.grid(row=4,column=1)
    mylabel3.grid(row=5,column=0)
    myentry3.grid(row=5,column=1)
    mylabel4.grid(row=6,column=0)
    myentry4.grid(row=6,column=1)
    mylabel5.grid(row=7,column=0)
    myentry5.grid(row=7,column=1)
    mylabel6.grid(row=8,column=0)
    myentry6.grid(row=8,column=1)
    mylabel7.grid(row=9,column=0)
    myentry7.grid(row=9,column=1)
    mylabel8.grid(row=10,column=0)
    myentry8.grid(row=10,column=1)
    mylabel9.grid(row=11,column=0)
    myentry9.grid(row=11,column=1)
    mylabel10.grid(row=12,column=0)
    myentry10.grid(row=13,column=0)
    mylabel11.grid(row=12,column=1)
    myentry11.grid(row=13,column=1)
    mybutton.grid(row=14,column=0)
    #creating the main menu
    mainmenu = Menu(root)
    mainmenu.add_command(label = "Save", command= save)  
    mainmenu.add_command(label = "Refresh", command= Refresh)
    mainmenu.add_command(label = "Annual profits", command=annualprofit)
    mainmenu.add_command(label = "Exit", command= root.destroy)
    
    root.config(menu = mainmenu)
    


    root.mainloop()
main()