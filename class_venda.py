from class_estoque import *



class Venda:
    def __init__(self):
        self.remove = Estoque()
       
        self.conet = mysql.connector.connect(
            host = 'Localhost',
            user= 'root',
            password = 'q1w2e3',
            database = 'estoque'

        )
        self.curs = self.conet.cursor()
        self.history_sell = []
        self.verifyy = bool
        

    def vender(self,cod):
        verify = cod
        list = []
        self.curs.execute(f'select cod from produto;')
        var = self.curs.fetchall()
        for i  in var:
            list.append(var)

        listcode = str(list)

        print(listcode)

       
        print(verify)
        if verify in listcode:
                self.verifyy = True
                convert = int(verify)
                self.history_sell.append(convert)
               




    def quanSell(self,cod,quan):
                cConvert  = int(cod)
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ')
                print('---=======--------=======-------=====-----=====---')
                print('        •••Digite a quantidade Desejada•••        ')
                print('---=======--------=======-------=====-----=====---')
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                quantidade =  quan
                intcode = int(cConvert)

                self.curs.execute(f'update produto set  quan = (quan - {quantidade}) where cod = {intcode} and quan > {quantidade}')
                self.conet.commit()
                print(f' QUANTIDADE SOLICITADA::•╫╫ { quantidade } ╫╫• FORAM  VENDIDOS COM SUCESSO$!!') 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      