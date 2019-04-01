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
      bot.send_message(msg.chat.id, 'Digite 1 para receber informações sobre a doação de leite materno.\nDigite 2 para receber as localizações dos bancos de leite materno do Espírito Santo - Brasil.')
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
    bot.send_message(msg.chat.id , "Olá Juliana, obrigada por se cadastrar! Meu nome é Leiticia e irei te ajudar a partir de agora!\nDigite 1 para receber informações sobre a doação de leite materno.\nDigite 2 para receber as localizações dos bancos de leite materno do Espírito Santo - Brasil."%nome)
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
    conn = sqlite3.connect('leite.db')
    cursor = conn.cursor()
    sql = 'SELECT * FROM leite'
    cursor.execute(sql)
    db1 = cursor.fetchall()
    for i in db1:
      if chat_id == i[0]:
        nome = i[1]
        bot.send_message( msg.chat.id , "%s Você já sabe que a amamentação por dois anos ou mais, de forma exclusiva nos primeiros seis meses, é fundamental para a sua saúde e a saúde do seu bebê.\nNa realidade, a amamentação é importante para qualquer mulher e bebê.\nPor isso, se uma mulher tem leite sobrando, poderá sim beneficiar outras crianças doando o seu leite.\nToda mulher saudável que estiver amamentando ou extraindo o seu leite manualmente ou com bomba e apresente produção de leite superior às necessidades de seu bebê é uma doadora em potencial.\nEla não pode estar fazendo uso de medicamentos que sejam incompatíveis com a amamentação, fazer uso de álcool ou drogas ilícitas e fumar mais do que dez cigarros por dia.\nNa imensa maioria das vezes, não há nenhuma contraindicação para uma mãe amamentar seu bebê, se esse for o seu desejo.\nAs restrições, quando existem, podem ser definitivas ou temporárias e serão checadas nos Bancos de Leite antes da doação.\nO leite humano extraído da mama e doado é destinado a recém-nascidos prematuros, com baixo peso e/ou gravemente doentes.\nA doadora não tem nenhum custo para doar leite.\nE também não pode receber alguma compensação em troca.\nA doação de leite no Brasil é sempre voluntária.\nO Banco de Leite não paga para receber leite e nem pode vender leite sob hipótese alguma.\nO que devo fazer para doar leite materno? \nO primeiro passo é entrar em contato com um Banco de Leite da Rede Brasileira de Bancos de Leite Humano (RBLH) ou posto de coleta.\nPara saber o endereço e telefone desses locais, DIGITE 2.\nA interessada pode telefonar para a unidade mais próxima de sua casa e receber todas as orientações.\nUm funcionário do Banco de Leite ou Posto de Coleta poderá ir à casa da mulher e recolher o leite retirado.\nEsse serviço é oferecido pela maioria dos locais, gratuitamente.\n(Referência: Sociedade Brasileira de Pediatria)"%nome )
        break
	
  elif texto == '2':
    bot.send_message( msg.chat.id , "Localização")

  else:
    bot.send_message( msg.chat.id , "Infelizmente não tenho nenhuma opção para a sua resposta, por favor tente uma outra resposta.\nDigite 1 para receber informações sobre a doação de leite materno do Espírito Santo - Brasil" )

print("bot funcionando !!")
bot.polling()
