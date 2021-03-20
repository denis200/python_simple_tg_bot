import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 1)
    but1 = "Прайс"
    but2 = "Прайс(Опт)"
    but3 = "Доставка"
    but4 = "Купить | Задать вопрос"
    markup.add(but1,but2,but3,but4)
    send_msg = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name} </b>!\n Выбирай то,что тебя интересует!"
    bot.send_message(message.chat.id,send_msg,parse_mode='html',reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'прайс':
        final = "\t\t<em>Распродажа!</em>\n Сегодня вы можете приобрести одноразовую\
электронную сигарету Rick and Morty на 2200 тяжек с тремя вкусами:\
\n\n1) Персик и гоава\n2) Мохито\n3) Вишня\n\n <b>Цена: 600 рублей</b>."
    elif get_message_bot == 'прайс(опт)':
        final = "Доступна оптовая продажа нашей продукции как от 5 штук, так и напрямую от производителя\
  из китая большими партиями.Для уточнения цен вы можете связаться со мной,нажав кнопку 'Задать вопрос'"
    elif get_message_bot == 'доставка':
        final = "Доставка в основном осуществляется почтой россии.При заказе от нескольких штук,часть \
доставки компенсируется мною.Если вы находитесь в Москве,возможен самовывоз."
    elif get_message_bot == 'купить | задать вопрос':
        final="Для покупки товара и возникнувшим вопросам писать сюда : @soundze"
    else:
        final="Что то пошло не так( Напиши /start для начала."
    bot.send_message(message.chat.id,final,parse_mode='html')
if __name__ == '__main__':
    bot.polling()
