import tkinter as t
w=t.Tk()
n=t.StringVar()
d=t.IntVar()
e=t.StringVar()
f=t.IntVar()
x=t.StringVar()
qr=t.StringVar()
jh=t.IntVar()
qrs=t.StringVar()
wb=t.StringVar()
fb=t.IntVar()
wr=t.IntVar()
er=t.IntVar()
fr=t.IntVar()
feb=t.IntVar()
qkr=t.StringVar()
qrsq=t.StringVar()
w.title('WELCOME TO SHARMA GROCERY STORE')
w.geometry('2000x2000')
w.config(bg='skyblue')
t.Label(w,text='enter name',fg='brown', font="Ariel", bg='white').grid(row=1,column=1)
t.Entry(w,textvariable=n).grid(row=1,column=2)
t.Label(w,text='enter phone number',fg='brown', font='Ariel',bg='white').grid(row=2,column=1)
t.Entry(w,textvariable=x).grid(row=2,column=2)
def getv():
    s=n.get()
    v=x.get()
    import mysql.connector
    cs=mysql.connector.connect(host='localhost', user='root', password='root', database='store')
    cr=cs.cursor()
    import random
    cid=str('c' + str(random.randint(1, 1000)))
    cr.execute("select cid from costumer_purchase")
    datt=cr.fetchall()
    for i in datt:
        if cid in i:
            cid=str('c' + str(random.randint(1,1000)))
    I="create table {}(item_name Varchar(20),item_price float,num_item int);".format(cid)
    cr.execute(I)
    import mysql.connector
    cs=mysql.connector.connect(host='localhost', user='root', password='root', database='store')
    cr=cs.cursor()
    cr.execute("select it_name from stock")
    ds=cr.fetchall()
    t.Label(w,text=('enter item name from',ds), fg='brown', font='Ariel',bg='white').grid(row=3,column=1)
    t.Entry(w,textvariable=e).grid(row=3,column=2)
    t.Label(w,text='enter number of items',fg='brown', font="Ariel",bg='white').grid(row=4,column=1)
    t.Entry(w,textvariable=f).grid(row=4,column=2)
    def de():
        ina=e.get()
        na=f.get()
        x="select priceper_item from stock where it_name='{}'".format(ina)
        cr.execute(x)
        da=cr.fetchone()
        dt=list(da)
        for i in dt:
            ip=i
        r="insert into {}(item_name,item_price,num_item) values('{}',{},{})".format(cid,ina,ip,na)
        cr.execute(r)
        cs.commit()
    def bill():
        cr.execute("select sum(item_price*num_item) from {}".format(cid))
        data=cr.fetchone()
        dat=list(data)
        for i in dat:
            t.Label(w,text=('your total bill is',i),fg='green', font="Ariel",bg='white').place(x=0,y=200)
        from datetime import date
        datet=str(date.today())
        r="insert into costumer_purchase(cid,cname,cphone_no,total_purchase,pur_date) values('{}','{}',{},{},'{}')".format(cid,s,v,i,datet)
        cr.execute(r)
        cs.commit()
    t.Button(w,text='enter item',bg='white',command=de).place(x=250,y=100)
    t.Button(w,text='show bill',bg='white',command=bill).place(x=150,y=150)
t.Button(w,text='enter costumer details', bg='white',command=getv).place(x=100,y=100)
def allstock():
    import tkinter as rt
    ef=rt.Tk()
    ef.config(bg='white')
    import mysql.connector
    cs=mysql.connector.connect(host='localhost', user='root', password='root', database='store')
    cr=cs.cursor()
    h="select * from stock"
    cr.execute(h)
    j=cr.fetchall()
    ed=['itemid:','itemname:', 'date_of_order:', 'order_value:', 'number_of_units:','price per item:', 'stock left:']
    for p in ed:
        rt.Label(ef,text=p,fg='purple', font=('Ariel', 14),bg='white').grid(row=ed.index(p)+1,column=1)
    for i in j:
        b=[i[0],i[1],[2],[3],[4],[5]]
        t.Label(ef,text=i[6], fg='brown', font=('Ariel', 14),bg='white').grid(row=7,column=j.index(i)+2)
    for el in b:
        t.Label(ef,text=el,fg='brown', font=('Ariel', 14), bg='white').grid(row=b.index(el)+1,column=j.index(i)+2)
def ustock():
    t.Label(w,text=('enter item name:'),fg='brown', font='Ariel',bg='white').grid(row=27,column=1)
    t.Entry(w,textvariable=qkr).grid(row=27,column=2)
    t.Label(w,text='enter number of units left:',fg='green', font='Ariel',bg='white').grid(row=28,column=1)
    t.Entry(w,textvariable=feb).grid(row=28,column=2)
    def getu():
        qkl=qkr.get()
        frgu=feb.get()
        import mysql.connector
        cs=mysql.connector.connect(host='localhost',user='root', password='root', database='store')
        cr=cs.cursor()
        we="update stock set stock_left={} where it_name='{}'".format(frgu,qkl)
        cr.execute(we)
        cs.commit()
    t.Button(w,text='enter',bg='white',command=getu).grid(row=28,column=3)
def vstock():
    t.Label(w,text=('enter item name:'),fg='brown', font='Ariel', bg='white').grid(row=27,column=1)
    t.Entry(w,textvariable=qr).grid(row=27,column=2)
    def show():
        q=qr.get()
        import mysql.connector
        cs=mysql.connector.connect(host='localhost', user='root', password='root', database='store')
        cr=cs.cursor()
        do="select DOO,stock_left,order_value from stock where it_name='{}'".format(q)
        cr.execute(do)
        p=cr.fetchone()
        cv='date of order:',p[0],'|', 'stock left:',p[1],'','order value',p[2]
        t.Label(w,text=cv,fg='brown', font='Ariel',bg='white').grid(row=10,column=5)
    t.Button(w,text='enter',bg='white',command=show).grid(row=27,column=3)
def cosd():
    t.Label(w,text="Type 1 to view today's costumer details", fg="brown", font='Ariel',bg='white').grid(row=20,column=1)
    t.Label(w,text="Type 2 to view bill details of a costumer",fg="brown", font='Ariel',bg='white').grid(row=20,column=2)
    t.Label(w,text="Type 3 to view costomer personal details",fg='brown', font='Ariel', bg='white').grid(row=20,column=3)
    t.Label(w,text="Type 4 to view costumer details of specific date ",fg="brown", font='Ariel', bg='white').grid(row=20,column=4)
    t.Entry(w,textvariable=jh).grid(row=21,column=2)
    def gjh():
        u=jh.get()
        import mysql.connector
        cs=mysql.connector.connect(host='localhost', user='root', password='root', database='store')
        cr=cs.cursor()
        if u==1:
            from datetime import date
            dateto=str(date.today())
            cr.execute("select * from costumer_purchase where pur_date='{}'".format(dateto))
            saf=cr.fetchall()
            t.Label(w,text=("TODAY'S PURCHASE DETAILS"),fg='purple', font=('Ariel', 14)).grid(row=23,column=1)
            t.Label(w,text=("cos id","cos name","cphone number","total bill","date of purchase"),fg='brown', font=('Ariel', 14)).grid(row=24,column=1)
            for b in saf:
                t.Label(w,text=b,fg='purple', font=('Ariel', 14)).grid(row=saf.index(b)+25,column=1)
        elif u==2:
            t.Label(w,text=('enter costumer name:'),fg="brown", font='Ariel',bg='white').grid(row=23,column=1)
            t.Entry(w,textvariable=qrs).grid(row=23,column=2)
            def getr():
                qs=qrs.get()
                import mysql.connector
                cs=mysql.connector.connect(host='localhost',user='root',password='root',database='store')
                cr=cs.cursor()
                cr.execute("select cid from costumer_purchase where cname='{}'".format(qs))
                ci=cr.fetchone()
                for g in ci:
                    cik=g
                cr.execute("select * from {}".format(cik))
                cdt=cr.fetchall()
                t.Label(w,text=('bill details of costumer are'),fg='purple', font='Ariel',bg='white').grid(row=27,column=1)
                t.Label(w,text=('item name,item price,number of items'),fg='purple', font='Ariel', bg='white').grid(row=28,column=1)
                cr.execute("select sum(item_price*num_item) from {}".format(cik))
                data=cr.fetchone()
                dat=list(data)
                for u in cdt:
                    t.Label(w,text=u,fg='green',font='Ariel',bg='white').grid(row=cdt.index(u)+29,column=1)
                for i in dat:
                    t.Label(w,text=('total bill',i),fg='brown', font='Ariel',bg='white').grid(row=cdt.index(u)+33,column=1)
            t.Button(w,text='enter costumer name',bg='white',command=getr).grid(row=23,column=3)
        elif u==3:
            t.Label(w,text=('enter costumer name:'),fg='brown',font='Ariel',bg='white').grid(row=23,column=1)
            t.Entry(w,textvariable=qrs).grid(row=23,column=2)
            def gett():
                import mysql.connector
                cs=mysql.connector.connect(host='localhost',user='root', password='root', database='store')
                cr=cs.cursor()
                ps=qrs.get()
                cr.execute("select * from costumer_purchase where cname='{}'".format(ps))
                ppa=cr.fetchone()
                t.Label(w,text=('personal details of',ps, 'are:'),fg='brown', font='Ariel',bg='white').grid(row=25,column=1)
                t.Label(w,text=('costumer id:',ppa[0]), fg='brown', font='Ariel',bg='white').grid(row=26,column=1)
                t.Label(w,text=('costumer name:',ppa[1]),fg='brown', font='Ariel',bg='white').grid(row=27,column=1)
                t.Label(w,text=('costumer phone number:',ppa[2]),fg='brown', font='Ariel',bg='white').grid(row=28,column=1)
                t.Label(w,text=('total bill:',ppa[3]),fg='brown', font='Ariel',bg='white').grid(row=29,column=1)
                t.Label(w,text=('date of purchase:',ppa[4]),fg='brown', font='Ariel',bg='white').grid(row=30,column=1)
            t.Button(w,text='enter costumer name',bg='white',command=gett).grid(row=23,column=3)
        elif u==4:
            t.Label(w,text=('enter date(yyyy-mm-dd):'),fg='brown', font='Ariel', bg='white').grid(row=23,column=1)
            t.Entry(w,textvariable=qrsq).grid(row=23,column=2)
            def getd():
                import mysql.connector
                cs=mysql.connector.connect(host='localhost',user='root', password='root', database='store')
                cr=cs.cursor()
                sdc=qrsq.get()
                cr.execute("select * from costumer_purchase where pur_date='{}'".format(sdc))
                saf=cr.fetchall()
                t.Label(w,text=(" PURCHASE DETAILS"),fg='purple', font=('Ariel', 14)).grid(row=23,column=1)
                t.Label(w,text=("cos id","cos name","cphone number","total bill","date of purchase"),fg="brown", font=('Ariel', 14)).grid(row=24,column=1)
                for b in saf:
                    t.Label(w,text=b,fg='purple', font=('Ariel', 14)).grid(row=saf.index(b)+25,column=1)
            t.Button(w,text='enter date',bg='white', command=getd).grid(row=23,column=3)
    t.Button(w,text='enter your choice',bg='white', command=gjh).grid(row=21,column=3)
'''def nstock():
    import mysql.connector
    cs=mysql.connector.connect(host='localhost', user='root', password='root', database='store')
    cr=cs.cursor()
    import random
    iit=str('s' + str(random.randint(1,1000)))
    cr.execute("select it_id from stock;")
    dast=cr.fetchall()
    for i in dast:
        if iit in i:
            iit=str('s' + str(random.randint(1,1000)))
    from datetime import date
    itd=str(date.today())
    t.Label(w,text=('enter item name'),fg='green', font='Ariel',bg='white').grid(row=23,column=1)
    t.Entry(w,textvariable=wb).grid(row=23,column=2)
    t.Label(w,text='enter number of units:',fg='green', font='Ariel',bg='white').grid(row=24,column=1)
    t.Entry(w,textvariable=wr).grid(row=24,column=2)
    t.Label(w,text='enter order value:',fg='green', font='Ariel',bg='white').grid(row=25,column=1)
    t.Entry(w,textvariable=fr).grid(row=25,column=2)
    t.Label(w,text='enter price of single item:',fg='green', font='Ariel', bg='white').grid(row=26,column=1)
    t.Entry(w,textvariable=er).grid(row=26,column=2)
    def getqw():
        itn=wb.get()
        iov=fr.get()
        inu=wr.get()
        ipp=er.get()
        ww="insert into stock(it_id,it_name,DOO,order_value,num_unit,priceper_item,stock_left) values('{}','{}','{}',{},{},{},{})".format(iit,itn,itd,iov,inu,ipp,i)
        cr.execute(ww)
        cs.commit()
    t.Button(w,text='enter new stock item',bg='white', command=getqw).grid(row=23,column=3)'''
t.Button(w,text='show all stock details', bg='white',command=allstock).grid(row=7,column=3)
t.Button(w,text='show specific stock detail',bg='white',command=vstock).grid(row=8,column=3)
#t.Button(w,text='add new item to stock',bg='white',command=nstock).grid(row=9,column=3)
t.Button(w,text="show costumer detail",bg='white', command=cosd).grid(row=10,column=3)
t.Button(w,text="change stockleft",bg='white',command=ustock).grid(row=24,column=3)
w.mainloop()
                                                                          








