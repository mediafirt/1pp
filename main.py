from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("client.db")

# frsname = StringVar()
# lstname = StringVar()
# ph = StringVar()
# addr = StringVar()
# st= StringVar()
# tac = StringVar()
# pr = StringVar()



window1 = Tk()
window1.title('Login')
window1.geometry('800x500+300+100')
window1.configure(bg='#000000')
window1.iconbitmap("C:\\Users\\Device Unknown\\Desktop\\project\\icons8-login-64.ico")
window1.resizable(False,False)

frsname = StringVar()
lstname = StringVar()
ph = StringVar()
addr = StringVar()
st= StringVar()
tac = StringVar()
pr = StringVar()

# window.overrideredirect(True)
#-------------Control panel----------#
def Sign_In():
    username = admin.get()
    code = password.get()
    if username=='admin' and code=='0000':
       window1.destroy()
       global window2
       window2 = Tk()
       window2.title('Control Panel')
       window2.geometry('800x500+300+100')
       window2.configure(bg='#000000')
       window2.resizable(False,False)
       window2.iconbitmap("C:\\Users\\Device Unknown\\Desktop\\project\\icons8-control-panel-94.ico")

       img = PhotoImage(file="C:\\Users\\Device Unknown\\Desktop\project\\client.png")
       res = img.subsample(2,2)
       btn = Button(window2,image=img,width=240,height=140,bg='#00F9F1',fg='black',text='Add client',compound=TOP,font=('Microsoft YaHei UI Light',16,'bold'),command=add_client).place(x=450,y=80)
   
   

       img1 = PhotoImage(file="C:\\Users\\Device Unknown\\Desktop\\project\\icons8-services-94.png")
       res1 = img1.subsample(2,2)
       btn1 = Button(window2,image=img1,width=240,height=140,bg='#00F9F1',fg='black',text='Management Services',compound=TOP,font=('Microsoft YaHei UI Light',15,'bold'),command=ms).place(x=130,y=80)


       img2 = PhotoImage(file="C:\\Users\\Device Unknown\\Desktop\\project\\icons8-billing-94.png")
       res2 = img2.subsample(2,2)
       btn2 = Button(window2,image=img2,width=240,height=140,bg='#00F9F1',fg='black',text='Billing Management',compound=TOP,font=('Microsoft YaHei UI Light',18,'bold'),command=bm).place(x=290,y=270)
       window2.mainloop()


def on_enter_key(event):
    Sign_In()  
window1.bind('<Return>', on_enter_key)
#---------Window mangement services---------#
def ms():
    global window4
    window4 = Tk()
    window4.title('Mangement Services')
    window4.geometry('1350x695+1+1')
    window4.configure(bg='#041071')
    window4.resizable(False,False)
    window4.iconbitmap("C:\\Users\\Device Unknown\\Desktop\\project\\icons8-services-94.ico")
    def back_cp1():
        window4.withdraw()
        window2.deiconify()
    btn = Button(window4,width=7,height=1,bg='white',text='Back CP',font=('Microsoft YaHei UI Light',11,'bold'),command=back_cp1) 
    btn.place(x=10,y=5)
    window4.mainloop()


#---------Window mangement bm---------#
def bm():
    global window5
    window5 = Tk()
    window5.title('Mangement bm')
    window5.geometry('1350x695+1+1')
    window5.configure(bg='#041071')
    window5.resizable(False,False)
    window5.iconbitmap("C:\\Users\\Device Unknown\\Desktop\\project\\icons8-services-94.ico")
    def back_cp2():
        window5.withdraw()
        window2.deiconify()
    btn = Button(window5,width=7,height=1,bg='white',text='Back CP',font=('Microsoft YaHei UI Light',11,'bold'),command=back_cp2) 
    btn.place(x=10,y=5)
    window5.mainloop()



#----------Windown add client-----------------#


def add_client():
    global window3
    window3 = Tk()
    window3.title('Add Client')
    window3.geometry('1350x695+1+1')
    window3.configure(bg='#041071')
    window3.resizable(False,False)
    window3.iconbitmap("C:\\Users\\Device Unknown\\Desktop\\project\\client.ico")
    en_frame = Frame(window3,bg='#041071')
    en_frame.place(x=1,y=1,width=360,height=693)
    frm = Frame(en_frame,bg='#2AFF00')
    frm.place(x=1,y=60,width=80,height=3)
    lbl = Label(en_frame,text='Information Client',font=('Microsoft YaHei UI Light',15,'bold'),fg='#2AFF00',bg='#041071')
    lbl.place(x=88,y=43)
    frm = Frame(en_frame,bg='#2AFF00')
    frm.place(x=279,y=60,width=80,height=3)


    def on_enter2(e):
        firstname.delete(0,'end')
    def on_leave2(e):
        frs = firstname.get()
        if frs=="":
           firstname.insert(0,'firstname')
    firstname = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light  ',11),textvariable=frsname)
    firstname.place(x=62,y=83)
    firstname.insert(0,'firstname')
    firstname.bind('<FocusIn>',on_enter2)
    firstname.bind('<FocusOut>',on_leave2)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=100)

    def on_enter3(e):
        lastname.delete(0,'end')
    def on_leave3(e):
        lst = lastname.get()
        if lst=="":
           lastname.insert(0,'lastname')
    lastname = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light',11),textvariable=lstname)
    lastname.place(x=62,y=145)
    lastname.insert(0,'firstname')
    lastname.bind('<FocusIn>',on_enter3)
    lastname.bind('<FocusOut>',on_leave3)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=165)


    def on_enter4(e):
        phone.delete(0,'end')
    def on_leave4(e):
        lst = phone.get()
        if lst=="":
           phone.insert(0,'phone')
    phone = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light',11),textvariable=ph)
    phone.place(x=62,y=210)
    phone.insert(0,'phone')
    phone.bind('<FocusIn>',on_enter4)
    phone.bind('<FocusOut>',on_leave4)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=230)

    def on_enter4(e):
        address.delete(0,'end')
    def on_leave4(e):
        addr = address.get()
        if addr=="":
           address.insert(0,'address')
    address = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light',11),textvariable=addr)
    address.place(x=62,y=275)
    address.insert(0,'address')
    address.bind('<FocusIn>',on_enter4)
    address.bind('<FocusOut>',on_leave4)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=295)


    def on_enter4(e):
        store.delete(0,'end')
    def on_leave4(e):
        str = store.get()
        if str=="":
           store.insert(0,'store')
    store = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light',11),textvariable=st)
    store.place(x=62,y=340)
    store.insert(0,'store')
    store.bind('<FocusIn>',on_enter4)
    store.bind('<FocusOut>',on_leave4)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=360)



    def on_enter4(e):
        tack.delete(0,'end')
    def on_leave4(e):
        tac = tack.get()
        if tac=="":
           tack.insert(0,'tack')
    tack = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light',11),textvariable=tac)
    tack.place(x=62,y=410)
    tack.insert(0,'tack')
    tack.bind('<FocusIn>',on_enter4)
    tack.bind('<FocusOut>',on_leave4)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=430)

    def on_enter4(e):
        price.delete(0,'end')
    def on_leave4(e):
        pri = price.get()
        if pri=="":
           price.insert(0,'price')
    price = Entry(en_frame,width=30,fg='white',border=0,bg='#041071',font=('Microsoft YaHei UI Light',11),textvariable=pr)
    price.place(x=62,y=480)
    price.insert(0,'price')
    price.bind('<FocusIn>',on_enter4)
    price.bind('<FocusOut>',on_leave4)
    Frame(en_frame,width=242,height=2,bg='#0027FF').place(x=62,y=500)
    

    #--------Frame table---------------#
    trframe = Frame(window3,bg='white')
    trframe.place(x=350,y=1,width=999,height=700)
    style = ttk.Style()
    style.configure("mystyle.Treeview",rowheight=50,font=('Calibri',13))
    style.configure("mystyle.Treeview.Heading",font=('Calibri',13))

    tv = ttk.Treeview(trframe,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
    tv.heading('1',text='ID')
    tv.column('1',width='40')
    tv.heading('2',text='Firstname')
    tv.column('2',width='165')
    tv.heading('3',text='Lastname')
    tv.column('3',width='165')
    tv.heading('4',text='Phone')
    tv.column('4',width='100')
    tv.heading('5',text='Address')
    tv.column('5',width='165')
    tv.heading('6',text='Store')
    tv.column('6',width='140')
    tv.heading('7',text='Tack')
    tv.column('7',width='140')
    tv.heading('8',text='Price')
    tv.column('8',width='100')
    tv['show'] = 'headings'
    displayAll()
    tv.place(x=1,y=1,height=692)

    




    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data['values']
        firstname.set(row[1])
        lastname.set(row[2])
        phone.set(row[3])
        address.set(row[4])
        store.set(row[5])
        tack.set(row[6])
        price.set(row[7])
    def displayAll():
        tv.delete(*tv.get_children)
        for row in db.fetch():
            tv.insert('',END,values=row)
    def add_client():
        if firstname.get() == "" or lastname.get() == "" or phone.get() =="" or address.get() == "" or store.get() == "" or tack.get() == "" or price.get() == "":
           messagebox.showerror("Error","Please Fill all the Entry")
           return
        db.insert(
            firstname.get(),
            lastname.get(),
            phone.get(),
            address.get(),
            store.get(),
            tack.get(),
            price.get(),)
        messagebox.showinfo('Successful',"New customer added")
    btn = Button(window3,width=14,height=2,bg='red',text='Add Client',font=('Microsoft YaHei UI Light',11,'bold'),command=add_client) 
    btn.place(x=20,y=550)

    btn = Button(window3,width=14,height=2,bg='red',text='Update Client',font=('Microsoft YaHei UI Light',11,'bold')) 
    btn.place(x=20,y=615)

    btn = Button(window3,width=14,height=2,bg='red',text='Delete Client',font=('Microsoft YaHei UI Light',11,'bold')) 
    btn.place(x=180,y=550)

    btn = Button(window3,width=14,height=2,bg='red',text='Clear Client',font=('Microsoft YaHei UI Light',11,'bold')) 
    btn.place(x=180,y=615)

    def back_cp2():
        window3.withdraw()
        window2.deiconify()
    btn = Button(window3,width=7,height=1,bg='white',text='Back CP',font=('Microsoft YaHei UI Light',11,'bold'),command=back_cp2) 
    btn.place(x=10,y=5)
    window3.mainloop()



#------------Form Login-------------#
frame = Frame(window1,width=350,bg='#000000',height=350)
frame.place(x=220,y=70)
heading = Label(frame,text='Sign In',fg='#0484F5',bg='#000000',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=125,y=10)
def on_enter1(e):
    admin.delete(0,'end')
def on_leave1(e):
    name = admin.get()
    if name=="":
       admin.insert(0,'Admin')
admin = Entry(frame,width=30,fg='white',border=0,bg='black',font=('Microsoft YaHei UI Light',11))
admin.place(x=62,y=80)
admin.insert(0,'Admin')
admin.bind('<FocusIn>',on_enter1)
admin.bind('<FocusOut>',on_leave1)
Frame(frame,width=242,height=2,bg='#0027FF').place(x=62,y=100)
def on_enter2(e):
    password.delete(0,'end')
def on_leave2(e):
    code = password.get()
    if code=="":
        password.insert(0,'Password')
password = Entry(frame,width=30,fg='white',border=0,bg='black',font=('Microsoft YaHei UI Light',11),show="*")
password.place(x=62,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter2)
password.bind('<FocusOut>',on_leave2)
Frame(frame,width=242,height=2,bg='#0027FF').place(x=62,y=170)

Button(frame,width=15,pady=1,text='Sign In',bg='#0027FF',fg='white',border=0,font=('Microsoft YaHei UI Light',17),command=Sign_In).place(x=83,y=240)



window1.mainloop()