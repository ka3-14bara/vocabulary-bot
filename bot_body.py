import telebot
from telebot import types
import logic_block as lg

token = open('bot_token.txt', 'r')
bot = telebot.TeleBot('token')

@bot.message_handler(commands = ['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('New word')
    button2 = types.KeyboardButton('Extract words')
    button3 = types.KeyboardButton('Remove word')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, f'Добро пожаловать, your id {message.from_user.id}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Done')
    #button2 = types.KeyboardButton('All words')
    #button3 = types.KeyboardButton('Words by 1 letter')
    #markup2.add(button2, button3)
    markup.add(button)
    if message.text.strip() == 'New word':
        bot.send_message(message.chat.id, text = "Write 1 pair of word with it translation, separate word and translation with \"-\". For example \"Apple - яблоко\" ", reply_markup=markup)
            
        
    elif message.text.strip() == 'Extract words':
        words_out=str()
        for i in lg.read_from(user_id):
                words_out += '(o) ' + f'{i}' + f'\n'
        bot.send_message(message.chat.id, text = f"{words_out}", reply_markup=markup)

    elif message.text.strip() == 'Remove word':
        bot.send_message(message.chat.id, text = f"Sorry, this function not ready. Will be soon", reply_markup=markup)

    elif message.text.strip() == 'Done':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('New word')
        button2 = types.KeyboardButton('Extract words')
        button3 = types.KeyboardButton('Remove word')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text = 'Main menu', reply_markup=markup)
    
    else:
        word_pair = message.text.strip()
        lg.saving(lg.take_in(word_pair), user_id)
        bot.send_message(message.chat.id, text = 'Main menu', reply_markup=markup)

bot.polling(none_stop=True)