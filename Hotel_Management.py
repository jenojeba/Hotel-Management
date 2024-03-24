import tkinter as tk
from datetime import date, datetime
import random

w = tk.Tk()
w.geometry('1270x690')
w.title("restaurant")
w.resizable(False, False)

def total():
    m = (int(n1.get())*8 + int(n2.get())*50 + int(n3.get())*10 + int(n4.get())*30 + int(n5.get())*45 +
         int(n6.get())*150 + int(n7.get())*100 + int(n8.get())*150 + int(n9.get())*150 + int(n10.get())*20)
    sr.delete(0, tk.END)
    sr.insert(0, "Rs " + str(m))

    today = date.today()
    a = str(today)
    spl = a.split('-')
    year = int(spl[0])
    month = int(spl[1])
    day = int(spl[2])
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    print("||.................................................. ||")
    print("||                  JJ RESTAURANT                    ||")
    print("||          682,3rd West Street,Thiyagarajanagar     ||")
    print("||                  Tirunelveli,                     ||")
    print("||                   9443002121                      ||")
    print("||                    INVOICE                        || ")
    print("||                                                   ||")
    print("|| Bill No :", random.randint(999, 100000), "\t\t\t\t", "Date : ", day, '/', month, '/', year, " ||")
    print("|| User : Optech", "\t\t\t\t\t\t", " Time : ", current_time, "\t\t\t ||")
    print("|| Counter : Sales ||")
    print("||.................................................. ||")
    print("||                       Bill                        ||")
    print("||.................................................. ||")
    print("||        Food item         |          Quantity      ||")
    print("||.................................................. ||")
    if n1.get() > 0:
        print("|| Idli\t\t\t\t\t\t\t\t\t", n1.get(), "\t\t\t\t ||")
    if n2.get() > 0:
        print("|| Dose\t\t\t\t\t\t\t\t\t", n2.get(), "\t\t\t\t ||")
    if n3.get() > 0:
        print("|| Vada\t\t\t\t\t\t\t\t\t", n3.get(), "\t\t\t\t ||")
    if n4.get() > 0:
        print("|| Chappathi\t\t\t\t\t\t\t", n4.get(), "\t\t\t\t ||")
    if n5.get() > 0:
        print("|| Puri\t\t\t\t\t\t\t\t\t", n5.get(), "\t\t\t\t ||")
    if n6.get() > 0:
        print("|| Special Lunch set\t\t\t\t\t\t", n6.get(), "\t\t\t\t ||")
    if n7.get() > 0:
        print("|| Vegetable Biriyani\t\t\t\t\t", n7.get(), "\t\t\t\t ||")
    if n8.get() > 0:
        print("|| Chicken Biriyani\t\t\t\t\t\t", n8.get(), "\t\t\t\t ||")
    if n9.get() > 0:
        print("|| Mutton Biriyani\t\t\t\t\t\t", n9.get(), "\t\t\t\t ||")
    if n10.get() > 0:
        print("|| Parotta\t\t\t\t\t\t\t\t", n10.get(), "\t\t\t\t ||")
    print("||.................................................. ||")
    print("|| Total :", str(m), "\t\t\t\t\t\t\t ||")
    print("||.................................................. ||")


t = tk.Frame(w, bd=10, relief='ridge', bg='firebrick4')
t.pack(side='top')
l = tk.Label(t, text="Restaurant Menu and billing system", bg='red', fg='blue',
             font=('arial', 30, 'bold'), width=60)
l.pack(side='top')

m = tk.Frame(w, bd=10, relief='ridge', bg='red')
m.pack(side='left')
f = tk.LabelFrame(m, bd=10, relief='ridge', bg='red')
f.pack(side='left')
b = tk.Label(w, text="Total", bg='red', fg='blue', font=('arial', 15, 'bold'), width=15, bd=5)
b.place(x=865, y=280)
s = tk.Button(w, text="Submit", bd=10, bg='green', command=total)
s.pack(side='bottom', padx=50, pady=5)
sr = tk.Entry(w, font=('arial', 18, 'bold'), bd=7, width=6)
sr.pack(side='right', padx=250, pady=0)

n1 = tk.IntVar()
n2 = tk.IntVar()
n3 = tk.IntVar()
n4 = tk.IntVar()
n5 = tk.IntVar()
n6 = tk.IntVar()
n7 = tk.IntVar()
n8 = tk.IntVar()
n9 = tk.IntVar()
n10 = tk.IntVar()

f1 = tk.Label(f, text="Food items", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
f1.grid(row=1, column=0, sticky='W')
l1 = tk.Label(f, text="Idli", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l1.grid(row=2, column=0, sticky='W')
l2 = tk.Label(f, text="Dose", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l2.grid(row=3, column=0, sticky='W')
l3 = tk.Label(f, text="Vada", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l3.grid(row=4, column=0, sticky='W')
l4 = tk.Label(f, text="Chappathi", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l4.grid(row=5, column=0, sticky='W')
l5 = tk.Label(f, text="Puri", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l5.grid(row=6, column=0, sticky='W')
l6 = tk.Label(f, text="Special Lunch set", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l6.grid(row=7, column=0, sticky='W')
l7 = tk.Label(f, text="Vegetable Biriyani", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l7.grid(row=8, column=0, sticky='W')
l8 = tk.Label(f, text="Chicken Biriyani", bg='red', fg='blue', font=('arial', 15, 'bold'), width=20, bd=5)
l8.grid(row=9, column=0, sticky='W')
l9=tk.Label(f,text="Mutton Biriyani",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
l9.grid(row=10,column=0,sticky='W')
l10=tk.Label(f,text="Parotta",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
l10.grid(row=11,column=0,sticky='W')
m1=tk.Label(f,text="Rs.8",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m1.grid(row=2,column=1,sticky='W')
m2=tk.Label(f,text="Rs.50",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m2.grid(row=3,column=1,sticky='W')
m3=tk.Label(f,text="Rs.10",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m3.grid(row=4,column=1,sticky='W')
m4=tk.Label(f,text="Rs.30",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m4.grid(row=5,column=1,sticky='W')
m5=tk.Label(f,text="Rs.45",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m5.grid(row=6,column=1,sticky='W')
m6=tk.Label(f,text="Rs.150",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m6.grid(row=7,column=1,sticky='W')
m7=tk.Label(f,text="Rs.100",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m7.grid(row=8,column=1,sticky='W')
m8=tk.Label(f,text="Rs.150",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m8.grid(row=9,column=1,sticky='W')
m9=tk.Label(f,text="Rs.150",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m9.grid(row=10,column=1,sticky='W')
m10=tk.Label(f,text="Rs.20",bg='red',fg='blue',font=('arial',15,'bold'),width=20,bd=5)
m10.grid(row=11,column=1,sticky='W')
e1=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n1)
e1.grid(row=2,column=2,sticky='W')
e2=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n2)
e2.grid(row=3,column=2,sticky='W')
e3=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n3)
e3.grid(row=4,column=2,sticky='W')
e4=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n4)
e4.grid(row=5,column=2,sticky='W')
e5=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n5)
e5.grid(row=6,column=2,sticky='W')
e6=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n6)
e6.grid(row=7,column=2,sticky='W')
e7=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n7)
e7.grid(row=8,column=2,sticky='W')
e8=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n8)
e8.grid(row=9,column=2,sticky='W')
e9=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n9)
e9.grid(row=10,column=2,sticky='W')
e10=tk.Entry(f,font=('arial',18,'bold'),bd=7,width=6,textvariable=n10)
e10.grid(row=11,column=2,sticky='W')
w.mainloop()