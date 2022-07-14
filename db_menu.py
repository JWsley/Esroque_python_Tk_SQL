from class_fabric import *
from db_estoque import *
from class_compra import *
from class_venda import *
from class_notify import *
class Menu:
   def __init__(self):
      
      db_f = Fabric()
      db_e = Estoque()
      dbb_e = Db_estoque()
      db_comp = Compra()
      db_sell = Venda()
      db_notify = Notificacao()

      db_e.fabr.nomEmpr = db_f.nomEmpr


      db_notify.sell = db_sell

      while True:

          entrada = input(' ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n•00->CADASTRAR EMPRESA.\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n•1->Cadastro de produto. \n•2->Listar todos os Produtos.  \n•3->Listar produto especifico.  \n•4->Alterar Desc/nome do produto.\n•5->Comprar Produto.  \n•6->Vender Produto.       \n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n•7->Historico\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n•0->Sair.\nFaça sua escolha |: ')
          db_e.sumiu()



          if entrada == '00':
             db_f.cadastro_fabric()
          if entrada == '1':
             dbb_e.cadastrar_produto()
          if entrada == '2':
             dbb_e.listar_tudo()
          if entrada == '3':
             dbb_e.listar_unidade()
          if entrada == '4':
             dbb_e.update_produto()
          if entrada == '5':
             db_comp.comprar()
          if entrada == '6':
             db_sell.vender()
          if entrada == '7':
                   print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n1->Historico/compra.\n2->Historico/venda\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                   resp = input('Escolha:')
                   if resp == '1':
                      db_notify.notify_buy()
                   elif resp == '2':
                       db_notify.notify_sell()





          if entrada == '0':
             print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
             print('••••••Processo Encerrado•••••')
             print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
             break
          
          
          
          
          
          
      '''

                  if entrada == '7':
                      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n1->Historico/compra.\n2->Historico/venda\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                      resp = input('Escolha:')
                      if resp == '1':
                         notic.notify_buy()
                      elif resp == '2':
                          notic.notify_sell()
      '''