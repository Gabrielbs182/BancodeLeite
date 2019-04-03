import telebot
import sqlite3
import time
from datetime import datetime

arq = open("token.txt","r")

token = arq.read()

arq.close()

bot = telebot.TeleBot( token )

periodo = int(input('Informe o periodo (em meses(maximo de 12)) que deseja efetuar os disparos: '))

def inteiro(lista): #transformar uma lista string em uma lista de inteiro
  a = []
  lista = lista.split('/')
  for i in lista:
    x = int(i)
    a.append(x)
  return a

while True:

  conn = sqlite3.connect(<DB>) #conectando o banco
  cursor = conn.cursor()
  sql = 'SELECT * FROM DB'
  cursor.execute(sql)
  db1 = cursor.fetchall()

  for i in db1: #percorrendo a lista, recebendo a data atual, transformando as listas str em lista int
    agora = datetime.now()
    dataAtual = '{}/{}/{}'.format(agora.day, agora.month, agora.year)
    controle = i[2]
    controle = inteiro(controle)
    dataAtual = inteiro(dataAtual)

    #condicinal que compara a data com o controle
    if controle[2] < dataAtual[2] or controle[2] == dataAtual[2] and controle[1] < dataAtual[1] or controle[2] == dataAtual[2] and controle[1] == dataAtual[1] and controle[0] <= dataAtual[0]:
      chat_id = i[0]
      nome = i[1]
      ident = i[3]
      bot.send_message(chat_id, 'Prezada %s, o banco de leite encontra-se com abastecimento prejudicado.\nPrecisamos de sua ajuda para manter a alimentação de recém nascidos das UTI’s.\nCompareça ao banco de leite humano mais proximo para contribuir com essa causa, para localização e informações sobre bancos de leites proximos digite 2'%nome)
      print('\n')
      print('mensagem enviada para o usuario: %s'%nome)
      controle[2] = dataAtual[2]
      controle[0] = dataAtual[0]
      controle[1] = dataAtual[1] + periodo #atualiza a data

      if controle[1] > 12: #condicinal que leva em consideração o limite de 12 meses
        controle [2] += 1
        controle [1] -= 12

      b = ''
      for i in range (len(controle)): #transforma a lista de inteiro em str novamente para aplicar no banco de dados
        if i != 2:
          b += str(controle[i])+'/'
        else:
          b += str(controle[i])          
      controle = b

      print(controle, " - Nova data controle")
      #inserindo a data ao banco de dados
      cursor.execute("""
      UPDATE DB
      SET data = ?
      WHERE id = ?
      """, (controle,ident))
      conn.commit()
      print('\n')
      print("Dados atualizados, data do proximo disparo (%s), para o usuario %s"%(controle,nome))

    else: #condicional que vai deixar o codigo ocioso por 24 horas
      dataAtual = '{}/{}/{}'.format(agora.day, agora.month, agora.year)
      print('\n')
      print("Não há mais disparos para o dia de hoje %s"%dataAtual)
      print('\n')
      print('Uma nova verificação sera efetuada dentro de 24 Horas')
      time.sleep(24*60*60)
  conn.close()

  time.sleep(5) #periodo entre um disparo e outro (opcional)
