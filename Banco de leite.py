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

bot = telebot.TeleBot( <TOKEN> )

@bot.message_handler(commands=['start'])
def send_start(msg):
  chat_id = msg.chat.id
  nome = msg.chat.first_name
  print(chat_id)
  print(nome)
  bot.send_message(msg.chat.id , "Olá muito obrigada por se cadastrar ^^ \ncom certeza a sua doação vai fazer muita diferença na vida de algum pequeno. \nDigite 1 para receber informações sobre a doação de leite materno ou \n2 para receber as localizações dos bancos de leite proximos a você.")

@bot.message_handler( content_types=['text'] )
def texto(msg):
  texto = msg.text
  if texto == '1':
	  bot.send_message( msg.chat.id , "Texto de informações" )
  elif texto == '2':
    bot.send_message( msg.chat.id , "localização dos bancos de leite mais proximos" )
  else:
    bot.send_message( msg.chat.id , "Infelizmente não tenho nenhuma opção para a sua resposta, por favor tente uma outra resposta." )


print("bot funcionando !!")
bot.polling()