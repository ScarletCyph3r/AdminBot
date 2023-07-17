
               #---------БЛОК 1[Данные библиотеки и Telegram Id]----------

import telebot
from telebot import types
import time

token = "There must be ur bot's token"
bot = telebot.TeleBot(token)
chatid = 'There is an id of group chat'

                #---------БЛОК 2[Приветствие и начало работы]----------

@bot.message_handler(commands=["start"])
def main(message) :
     time.sleep(0.7)
     bot.send_message(message.chat.id, text="Ваша любимая Лайла - на связи.")
     messagez(message)

                #---------БЛОК 3[Отправка шаблона анкеты - жалобы]----------

def messagez(message) :
     time.sleep(1.5)
     bot.send_message(message.chat.id,text='✶ Вот как должна оформляться жалоба(просто скопируй сообщение ниже и вставь нужную информацию в пустые поля) ↓')
     time.sleep(1)
     doc = bot.send_message(message.chat.id,text='\n♡ Никнейм того на кого подаётся жалоба:\n♡ Причина жалобы:\n♡ Никнейм того кто подаёт жалобу:')
     bot.register_next_step_handler(doc, option1)

def option1(message):
     if message.text == '/end':
         bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю сначала')
         main(message)
     else:
        messagege(message)
                  #---------БЛОК 4[Оформление и отправка анкеты - жалобы]----------

@bot.message_handler(func=lambda message : True)
def messagege(message) :
        bot.send_message(chat_id=chatid, text=message.text)
        photo=bot.send_message(message.chat.id, text='♡ Отлично. А теперь отправьте в этот чат 1 фотографию.')
        bot.register_next_step_handler(photo,photoend)
def photoend(message):
     if message.text == '/end':
         bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю сначала')
         main(message)
     else:
         echo_photomessage(message)
           # ---------БЛОК 5[Процесс принятия ботом фотографий]----------

@bot.message_handler(func=lambda message : True)
def echo_photomessage(message) :
    try :
        bot.send_photo(chat_id=chatid, photo=message.photo[0].file_id, caption=message.caption)
        buttons(message)
    except :
     onlyphoto = bot.send_message(message.chat.id, text='♡ Ошибка..пожалуйста повторите попытку не нарушая указаний бота ')
     bot.register_next_step_handler(onlyphoto, echo_photomessage)



         # ---------БЛОК 6[Действия с кнопками]----------
def buttons(message) :
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = "Нет, это всё"
    btn2 = 'Есть ещё'
    markup.add(btn1, btn2)
    time.sleep(1)
    all =bot.send_message(message.chat.id, text="♡ Это все фотографии или же есть ещё?", reply_markup=markup)
    bot.register_next_step_handler(all,buttonaction)


def buttonaction(message):
    operation = message.text
    if operation == 'Нет, это всё':
        bot.send_message(message.chat.id, text='Спасибо за содействие ♡.')
        bot.send_message(message.chat.id, text='♡ Ваша жалоба была успешно принята, чтобы отправить новую жалобу. Нажмите на /start')
    elif operation == 'Есть ещё':
        positive = bot.send_message(message.chat.id, '♡ Отлично, отправьте сюда 1 фотографию')
        bot.register_next_step_handler(positive,photoend)
    elif operation == '/end':
        bot.send_message(message.chat.id, text='Хорошо. Останавливаю все процессы и начинаю сначала')
        main(message)

    else :
        bot.send_message(message.chat.id,text='♡ Не нажимайте ничего, кроме кнопок.')
        buttons(message)



bot.polling(non_stop=True)

