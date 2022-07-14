from db_estoque import *
from class_venda import *
from class_compra import *

class Notificacao:
    def __init__(self):
        self.notify = Estoque()
        self.buy =Compra()
        self.sell = Venda()
        self.conet = mysql.connector.connect(
            host = 'Localhost',
            user= 'root',
            password = 'q1w2e3',
            database = 'estoque'

        )
        self.curs = self.conet.cursor()
        self.list = []
        
        
        

       



    def notify_buy(self):
        for i in range(len(self.buy.history_buy)):
            num = int(self.sell.history_buy[i])
            print(num)
            SQLbuy = f'select * from produtos where cod = {num}'
            self.curs.execute(SQLbuy)
            list = self.mycursor.fetchall()
            for i in list:
                print(i)
                         
      
            #'''buy = f'select * from produtos where cod = {list[i]}'
            #self.curs.execute(buy)'''

                        


    def notify_sell(self):
        for i in range(len(self.sell.history_sell)):
            n = int(self.sell.history_sell[i])
            SQLsell = f'select * from produtos where cod = {n}'
            self.curs.execute(SQLsell)
                         