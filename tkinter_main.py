from cProfile import label
from dataclasses import field
from email.mime import image
from tkinter import *
from tkinter import messagebox
from time import *
from turtle import color
from class_compra import *

from db_estoque import *
from class_fabric import *
from class_venda import *

from setuptools import Command
from img import *
import posiciona

entrywhite = '#F4F4F4'





def saveEmp():
    fabr = Fabric()
    nomEmpr = empEntry.get()
    fabr.cadastro_fabric(nomEmpr)
    infm = messagebox.showinfo(title='Nice Broh.', message='Empresa cadastrada com Sucesso!!')
    f2.forget()
    f1.pack()


def saveProd():
    Estq = Db_estoque()
    nomeProd = entrynom.get()
    nomeEmp = entryEmp.get()
    Estq.cadastrar_produto(nomeProd,nomeEmp)
    if  Estq.verifyx ==True :
        infm = messagebox.showinfo(title='Nice Broh.', message='Produto  cadastrado com Sucesso!!')
        f3.forget()
        f1.pack()
    else:
        infm = messagebox.showerror(title='Nice Broh.', message='Empresa inexistente')
    


def cadProd():
    f1.forget()
    f3.pack()


def cadEmp():
    f1.forget()
    f2.pack()


def buySell():
    f1.forget()
    f4.pack()


def returnMenu():
    f4.forget()
    f1.pack()


def view():
    f1.forget()
    f5.pack()


def returnview():
    frameedit.place_forget()
    f5.forget()
    f1.pack()


def search():
    Estq = Db_estoque()
    a = searchCode.get()
    db = Estq.listar_unidade(a)
    if a != '':
        unityinfo.insert(END, db)
    else:
        for y in range(len(Estq.pls)):
            print(len(Estq.pls))
            unityinfo.insert(END, Estq.pls[y])



def openBuy():
    f4.forget()
    f6.pack()


def returnBuy():
    minif6.place_forget()
    f6.forget()
    f4.pack()

def buyverify():
    cp = Compra()
    a = entryBuy.get()
    print(a)
    cp.comprar(a)
    print(cp.verifyy)
    if cp.verifyy == True:
       minif6.place(width=411, height=157, x=131, y=259)
       

def buyconfirm():
    cp = Compra()
    verifccod = entryBuy.get()
    q = int(entryQuan.get())
    cp.quanbuy(cod = verifccod,quan = q)
    

    
def clear():
    unityinfo.delete(0,END)
      
        

def editName():
    frameedit.place(width=125, height=210, x=516, y=343)
    
def updateName():
    db = Db_estoque()
    codeT = entryminicode.get()
    name = entryNewName.get()
    db.update_produto(code = codeT,new_name = name)
    infm = messagebox.showinfo(title='Nice Broh.', message=f'Nome alterado com Sucesso!..Codigo do produto:{codeT}|Novo:{name}')



def openSell():
    f4.forget()
    f7.pack()



def returnSell():
    minif7.place_forget()
    f7.forget()
    f4.pack()



def sellVerify():
    vd = Venda()
    a = entrySell.get()
    print(a)
    vd.vender(a)
    if vd.verifyy == True:
       minif7.place(width=411, height=157, x=131, y=259)
       

def sellconfirm():
    vd = Venda()
    verifccod = entrySell.get()
    qs = entryQuanti.get()
    vd.quanSell(cod = verifccod,quan = qs)
    

entrycolor = '#0E0D0D'

app = Tk()
app.geometry('700x700+350+150')
app.resizable(width=False, height=False)
app.title('Banco sem nome...')
app.configure(bg='black')


# ========================= -= = ==========- =-=--= -==========------

app.bind('<Button-1>', posiciona.inicio_place)
app.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, app))
app.bind('<Button-2>', lambda arg: posiciona.para_geometry(app))


# ====== = = -------------======================= = == ===================
# +=================  MENU PRINCIPAL  -------------=======================
# -------------======================= -------------======================

f1 = Frame(app)
f1.pack()
f2 = Frame(app)
f3 = Frame(app)
f4 = Frame(app)
f5 = Frame(app)
f6 = Frame(app)
f7 = Frame(app)
minif6 = Frame(app)
minif7 = Frame(app)
frameedit = Frame(app)
#minif6.place(width=411, height=157, x=131, y=259)



# ====== = = -------------======================= = == ===================
# +=================  FRAME 1  -------------=======================
# -------------======================= -------------======================

backg1 = PhotoImage(file='img/principal.png')
btemp1 = PhotoImage(file='img/btEmp.png')
btprod1 = PhotoImage(file='img/btProd.png')
btmain = PhotoImage(file='img/menu_bt.png')

bthistory = PhotoImage(file='img/historybt.png')
btview = PhotoImage(file='img/viewbt.png')


back = Label(f1, image=backg1)

back.pack()


BTemp = Button(f1, image=btemp1, command=cadEmp)
BTemp.place(width=224, height=222, x=42, y=408)


BTprod = Button(f1, image=btprod1, command=cadProd)
BTprod.place(width=224, height=220, x=432, y=407)


history = Button(f1, image=bthistory, bd=0, activebackground='black')
history.place(width=44, height=46, x=645, y=5)


view = Button(f1, image=btview, bd=0, command=view)
view.place(width=51, height=46, x=579, y=5)


bt_main = Button(f1, image=btmain, bd=0, command=buySell)
bt_main.place(width=61, height=64, x=317, y=483)

# ====     == = = -------------======================= = == ===================
# +=================  FRAME 2  -------------=======================
# -------------======================= -------------======================


back2 = PhotoImage(file='img/empresa_cad.png')


backg2 = Label(f2, image=back2)


empEntry = Entry(f2, foreground='white', background=entrycolor,
                 font='Arial 40', justify=CENTER, bd=0)
empEntry.place(width=474, height=90, x=116, y=148)

backg2.pack()

saveBYT = Button(f2, image=btmain, bd=0, command=saveEmp)
saveBYT.place(width=68, height=65, x=315, y=317)

# ====     == = = -------------======================= = == ===================
# +=================  FRAME 3  -------------=======================
# -------------======================= -------------======================


back3 = PhotoImage(file='img/cad_prod.png')


backg3 = Label(f3, image=back3)
backg3.pack()

BTprod = Button(f3, image=btmain, bd=0, command=saveProd)
BTprod.place(width=64, height=57, x=321, y=641)

entrynom = Entry(f3, foreground='white', background=entrycolor,
                 bd=0, justify=CENTER, font='Arial 25')
entrynom.place(width=290, height=42, x=198, y=346)

entryEmp = Entry(f3, foreground='white', background=entrycolor,
                 bd=0, justify=CENTER, font='Arial 25')
entryEmp.place(width=290, height=38, x=199, y=492)


# ====     == = = -------------======================= = == ===================
# +=================  FRAME 4  -------------=======================
# -------------======================= -------------======================


back4 = PhotoImage(file='img/buysell.png')
imgbuy  = PhotoImage(file='img/buy_button.png')
imgsell  = PhotoImage(file='img/sell_button.png')


backg4 = Label(f4, image=back4)
backg4.pack()



buy_bt = Button(f4,image=imgbuy,command=openBuy)
buy_bt.place(width=223, height=221, x=34, y=271)

sell_bt = Button(f4,image=imgsell,command=openSell)
sell_bt.place(width=220, height=219, x=467, y=274)

main_bt = Button(f4, image=btmain, bd=0, command=returnMenu)
main_bt.place(width=66, height=61, x=313, y=628)


# ====     == = = -------------======================= = == ===================
# +=================  FRAME 5  -------------=======================
# -------------======================= -------------======================


back5 = PhotoImage(file='img/unityView.png')
buttonsea = PhotoImage(file='img/search.png')
clearimg  = PhotoImage (file='img/clearButton.png')
editimg  = PhotoImage (file='img/editButton.png')
miniConf = PhotoImage(file='img/miniConfirm.png')



backg5 = Label(f5, image=back5)
backg5.pack()

# Copiado! .place(width=71, height=65, x=316, y=629)
returnUnity = Button(f5, image=btmain, bd=0,
                     activebackground='black', command=returnview)
returnUnity.place(width=71, height=65, x=316, y=629)


searchCode = Entry(f5, bd=0, foreground='black',
                   background=entrywhite, font='Arial 25', justify=CENTER)
searchCode.place(width=358, height=41, x=141, y=183)



edit = Button(f5,image=editimg,bd=0,background='black',command=editName)
edit.place(width=53, height=59, x=549, y=278)

clear = Button(f5,image=clearimg,bd=0,background='black',command=clear)
clear.place(width=41, height=52, x=27, y=636)



entryeditFrame = PhotoImage(file='img/miniFrameView.png')

framedit = Label(frameedit,image = entryeditFrame)
framedit.pack()


miniConfirm = Button(frameedit, image=miniConf,background='black',bd=0,activebackground='black',command=updateName)
miniConfirm.place(width=40, height=47, x=40, y=160)



entryminicode = Entry(framedit,foreground='white',background='black',bd=0,justify=CENTER)
entryminicode.place(width=96, height=20, x=14, y=53)

entryNewName = Entry(framedit,foreground='white',background='black',bd=0,justify=CENTER)
entryNewName.place(width=96, height=22, x=14, y=122)

searchButton = Button(f5, image=buttonsea, bd=0, command=search)
searchButton.place(width=26, height=26, x=517, y=190)

header = Label(f5,text='COD | NOME | EMPRESA | QUANTIDADE',background='black',foreground=entrywhite,font='Arial 10')
header.place(width=264, height=29, x=218, y=288)


unityinfo = Listbox(f5, background='black',
                    foreground=entrywhite, font='Arial 10',justify=CENTER,selectbackground='white',selectforeground='black')
unityinfo.place(width=267, height=240, x=216, y=320)




# ====     == = = -------------======================= = == ===================
# +=================  FRAME 6  -------------=======================
# -------------======================= -------------======================


back6 = PhotoImage(file='img/buyFrame.png')

backg6 =Label(f6,image =back6)
backg6.pack()

buyreturn = Button(f6,image=btmain,bd=0,background='black',activebackground='black',command=returnBuy)
buyreturn.place(width=74, height=65, x=317, y=626)



entryBuy = Entry(f6, bd=0, foreground='black',
                   background=entrywhite, font='Arial 25', justify=CENTER)
entryBuy.place(width=358, height=41, x=141, y=183)


sb = Button(f6, image=buttonsea, bd=0, command=buyverify)
sb.place(width=26, height=26, x=517, y=190)



frameiimg = PhotoImage(file='img/frameBbuy.png')

frameSearch = Label(minif6,image=frameiimg)
frameSearch.pack()

entryQuan = Entry(minif6, bd=0, foreground='black',
                   background=entrywhite, font='Arial 25', justify=CENTER)
entryQuan.place(width=355, height=40, x=9, y=96)



quanbt = Button(minif6,image=buttonsea,bd=0,background='black',activebackground='black',command=buyconfirm)

quanbt.place(width=26, height=26, x=373, y=103)




# ====     == = = -------------======================= = == ===================
# +=================  FRAME 7  -------------=======================
# -------------======================= -------------======================




back7 = PhotoImage(file='img/sellFrame.png')



backg7 = Label(f7,image=back7)
backg7.pack()

Sellreturn = Button(f7,image=btmain,bd=0,background='black',activebackground='black',command=returnSell)
Sellreturn.place(width=74, height=65, x=317, y=626)



entrySell = Entry(f7, bd=0, foreground='black',
                   background=entrywhite, font='Arial 25', justify=CENTER)
entrySell.place(width=358, height=41, x=141, y=183)


ss = Button(f7, image=buttonsea, bd=0, command=sellVerify)
ss.place(width=26, height=26, x=517, y=190)



frameimg = PhotoImage(file='img/FrameBbuy.png')

frameeSearch = Label(minif7,image=frameimg)
frameeSearch.pack()

entryQuanti = Entry(minif7, bd=0, foreground='black',
                   background=entrywhite, font='Arial 25', justify=CENTER)
entryQuanti.place(width=355, height=40, x=9, y=96)



quanbt = Button(minif7,image=buttonsea,bd=0,background='black',activebackground='black',command=sellconfirm)

quanbt.place(width=26, height=26, x=373, y=103)













app.mainloop()
