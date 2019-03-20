import telebot
import sqlite3
from datetime import datetime

bot = telebot.TeleBot( <TOKEN> )

@bot.message_handler(commands=['start'])
def send_start(msg):

  teste = 0
  chat_id = msg.chat.id
  nome = msg.chat.first_name
  agora = datetime.now()
  data = '{}/{}/{}'.format(agora.day, agora.month, agora.year)

  conn = sqlite3.connect('DB')
  cursor = conn.cursor()
  sql = 'SELECT * FROM DB'
  cursor.execute(sql)
  db1 = cursor.fetchall()

  for i in db1:
    if i[0] == chat_id:
      teste = 1
      bot.send_message(msg.chat.id , "Olá %s você já possui cadastro, muito obrigada !!"%nome)
      bot.send_message(msg.chat.id, 'Digite 1 para receber informações sobre a doação de leite materno \nDigite 2 para receber as localizações dos bancos de leite.')
      print("Usuario já possui cadastro")
      print(chat_id)
      print(type(chat_id))
      print(nome)
      break

  if teste == 0:
    cursor.execute("""
    INSERT INTO DB (chat_id, nome, data)
    VALUES (?,?,?)
    """, (chat_id,nome,data))
    conn.commit()
    bot.send_message(msg.chat.id , "Olá %s muito obrigada por se cadastrar ^^ \ncom certeza a sua doação vai fazer muita diferença na vida de algum pequeno. \nDigite 1 para receber informações sobre a doação de leite materno \nDigite 2 para receber as localizações dos bancos de leite."%nome)
    print("Novo usuario Cadastrado!")
    print(chat_id)
    print(type(chat_id))
    print(nome)

  conn.close()
  

@bot.message_handler( content_types=['text'] )
def texto(msg):
  texto = msg.text
  chat_id = msg.chat.id

  if chat_id == <ADMIN CHAT_ID> and texto == '5':
    conn = sqlite3.connect('DB')
    cursor = conn.cursor()
    sql = 'SELECT * FROM DB'
    cursor.execute(sql)
    db1 = cursor.fetchall()
    for i in db1:
      nome = i[1]
      chat_id = i[0]
      bot.send_message(chat_id, 'Prezada %s, o banco de leite encontra-se com abastecimento prejudicado.\nPrecisamos de sua ajuda para manter a alimentação de recém nascidos das UTI’s.\nCompareça ao banco de leite humano mais proximo para contribuir com essa causa, para localização e informações sobre bancos de leites proximos digite 2'%nome)
    conn.close()

  elif texto == '1':
	  bot.send_message( msg.chat.id , "Texto de informações" )
  elif texto == '2':
    bot.send_message(msg.chat.id, 'Texto de informações')
  else:
    bot.send_message( msg.chat.id , "Infelizmente não tenho nenhuma opção para a sua resposta, por favor tente uma outra resposta.\nDigite 1 para receber informações sobre a doação de leite materno \nDigite 2 para receber as localizações dos bancos de leite." )

print("bot funcionando !!")
bot.polling()
