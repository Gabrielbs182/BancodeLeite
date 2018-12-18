"""
O programa armazena os dados do usuário imediatamente após o contato com o bot em duas variáveis, (Chat_id) e (nome).
Em seguida oferece ao usuario 2 opções de interações das quais necessito da colaboração dos médicos para confecção dos textos.
Oque deve ser feito ?
Preciso ligar o programa a um banco de dados para armazenar as duas variáveis em colunas no banco de dados, uma para o chat_id
outra para o primeiro nome e uma extra para armazenar a data da ultima interação.
a data vai ter a funcionalidade de armazenar a última mensagem enviada para o usuário pelo bot, assim evitando qualquer tipo de spam
em alguma reunião futura vamos entrar em um consenso com uma data razoavel de periodicidade pela qual o bot vai mandar mensagens
assim que uma mensagem é enviada o bot armazena no banco de dados a data do dia do envio, quando essa data chega no limite ele envia outra mensagem
e atualiza novamente no banco de dados, fazendo isso automaticamente.
"""

import telebot
import sqlite3
from datetime import datetime

bot = telebot.TeleBot( <TOKEN> )

@bot.message_handler(commands=['start'])
def send_start(msg):
  chat_id = msg.chat.id
  nome = msg.chat.first_name
  print(chat_id)
  print(type(chat_id))
  print(nome)
  bot.send_message(msg.chat.id , "Olá muito obrigada por se cadastrar ^^ \ncom certeza a sua doação vai fazer muita diferença na vida de algum pequeno. \nDigite 1 para receber informações sobre a doação de leite materno ou \n2 para receber as localizações dos bancos de leite proximos a você.")

@bot.message_handler( content_types=['text'] )
def texto(msg):
  texto = msg.text
  chat_id = msg.chat.id
  if chat_id == 584039241 and texto == '5':

    conn = sqlite3.connect('leite.db')
    cursor = conn.cursor()
    sql = 'SELECT * FROM leite'
    cursor.execute(sql)
    db1 = cursor.fetchall()
    agora = datetime.now()
    data = '{}/{}/{}'.format(agora.day, agora.month, agora.year)
    for i in db1:
      print(i[2])
      print(data)
      if i[2] == data:
        msg1 = "Prezada {}, o banco de leite encontra-se com abastecimento prejudicado.\nPrecisamos de sua ajuda para manter a alimentação de recém nascidos das UTI’s.\nCompareça ao banco de leite humano mais proximo para contribuir com essa causa, para localização e informações sobre bancos de leites proximos digite '2'".format(i[1])
      chat_id = i[0]
      bot.send_message( chat_id , msg1 )

  elif texto == '1':
	  bot.send_message( msg.chat.id , "Texto de informações" )
  elif texto == '2':
    bot.send_message( msg.chat.id , "Hospital Estadual Infantil e Maternidade de Vila Velha\nHorário de funcionamento: 08 às 17 horas, de segunda a sexta-feira. \nEndereço: Avenida Ministro Salgado Filho, 918, Soteco, Vila Velha.\nContato: 3636-3151")
    bot.send_message( msg.chat.id , "Hospital Estadual Dório Silva\nHorário de funcionamento: 08 às 17 horas, de segunda a sexta-feira.\nEndereço: Avenida Eudes Scherrer de Souza, s/n, Laranjeiras, Serra.\nContato: 3138-8905")
    bot.send_message( msg.chat.id , "Hospital da Polícia Militar do Espírito Santo (HPM)\nEndereço: Bento Ferreira, em Vitória.\nContato: 3636-6568")
    bot.send_message( msg.chat.id , "Hospital das Clínicas (referência do Estado)\nHorário de funcionamento: 08 às 21 horas, de segunda a sexta-feira.\nEndereço: Avenida Marechal Campos, s.nº, Maruípe.\nContato: 3335-7424 – 3335-7377")
    bot.send_message( msg.chat.id , "Santa Casa de Misericórdia\nHorário de funcionamento:07 às 16 horas, de segunda a sexta-feira.\nEndereço: Rua Dr. João dos Santos Neves, 143, Vila Rubim, Vitória.\nContato: 3212-7246")
    bot.send_message( msg.chat.id , "Hospital Evangélico de Cachoeiro de Itapemirim\nHorário de funcionamento: 07 às 17 horas, de segunda a sexta-feira.\nEndereço: Rua Anacleto Ramos, 55, Bairro Ferroviários.\nContato: (28) 3521-7045")
    bot.send_message( msg.chat.id , "Hospital e Maternidade São José, Colatina\nHorário de funcionamento: das 07 às 17h20, de segunda a sexta-feira.\nEndereço: Ladeira Cristo Rei, Centro de Colatina.\nContato: (27) 2102-2100")
  else:
    bot.send_message( msg.chat.id , "Infelizmente não tenho nenhuma opção para a sua resposta, por favor tente uma outra resposta." )

print("bot funcionando !!")
bot.polling()
