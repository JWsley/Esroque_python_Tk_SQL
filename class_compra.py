from class_estoque import *
import mysql.connector

class Compra:
    def __init__(self):
        self.add = Estoque()
        self.codstr = []
        self.conet = mysql.connector.connect(
            host = 'Localhost',
            user= 'root',
            password = 'q1w2e3',
            database = 'estoque'

        )
        self.curs = self.conet.cursor()
        self.history_buy = []
        self.verifyy = bool
       

    def comprar(self,cod):
        list = []
        verify = cod
        self.curs.execute(f'select cod from produto;')
        var = self.curs.fetchall()
        for i  in var:
            list.append(var)

        listcode = str(list)
        self.curs.execute(f'')

        print(listcode)
       
        print(verify)
        if verify in listcode:
            self.verifyy = True
            convert = int(cod)
            self.history_buy.append(convert)
            
    
    
    
    
    
    def quanbuy(self,cod,quan):
                cConvert = cod
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ')
                print('---=======--------=======-------=====-----=====---')
                print('        •••Digite a quantidade Desejada•••        ')
                print('---=======--------=======-------=====-----=====---')
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                quantidade = quan
                intcode = int(cConvert)
                self.curs.execute(f'update produto set  quan = (quan + {quantidade}) where cod = {intcode}')
                self.conet.commit()
                print(f' QUANTIDADE SOLICITADA::•╫╫ {quantidade} ╫╫• FORAM  COMPRADOS COM SUCESSO!!') 
                