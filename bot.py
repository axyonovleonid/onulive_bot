import enum
import telebot
import os
from flask import Flask, request


class State(enum.Enum):
    default = 0
    forward = 1


bot = telebot.TeleBot('1434687229:AAGOTUvkeFy7dqx7zIrY6kPBxJ2IcxIDa5s')
server = Flask(__name__)


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(
        url="https://dashboard.heroku.com/apps/onulive-bot")  # этот url нужно заменить на url вашего Хероку приложения
    return "?", 200


server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
# keyboard1.row("Расписание пар", 'Звонки', 'Карта интернетов')
# keyboard1.row('Факультеты', 'Общежития', 'Руководства')
# keyboard1.row('Общение ', 'Документация/руководства')
# keyboard1.row('Связь', 'Обратная связь')

keyboard1.row("Общение", "Карта интернетов")
keyboard1.row("Расписание", "Звонки")
keyboard1.row("О факультетах", "Руководство")
keyboard1.row("Об общежитиях", "Документация/FAQ")
keyboard1.row("Связь", "Фидбек")
keyboard1.row('SEND NUDES')

faculties = telebot.types.ReplyKeyboardMarkup(True, False)
faculties.row("БИОФАК", "ГГФ", "ЭПФ", "ИСТФАК")
faculties.row("ЖУРФАК", "МФИТ", "МОПС", "ФПСР")
back_text = "Назад"
faculties.row("РГФ", "ФИЛФАК", "ХИМФАК", back_text)

dorms = telebot.types.ReplyKeyboardMarkup(True, False)
dorms.row("Общежитие №1", "Общежитие №2", "Общежитие №3")
dorms.row("Общежитие №4", "Общежитие №5", "Общежитие №6")
dorms.row("Общежитие №7", "Общежитие №8", "Общежитие №9")
dorms.row(back_text)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Я искусственный интеллект Мечников.\n\n"
                                      "Меня создали, чтобы помогать тебе в учёбе и не потеряться в цифровом "
                                      "пространстве ОНУ.\n\n "
                                      "Выбери нужную категорию и найди то, что необходимо, нажимая на кнопки снизу.",
                     reply_markup=keyboard1)


single_return = telebot.types.ReplyKeyboardMarkup(True, False)
single_return.row("Фидбек")

feedback_markup = telebot.types.ReplyKeyboardMarkup(True, False)
feedback_markup.row("Предложить новость")
feedback_markup.row("Поблагодарить шекелем", "Пожаловаться на бота")
feedback_markup.row(back_text)

connections_markup = telebot.types.ReplyKeyboardMarkup(True, False)
connections_markup.row("Студсовет", "Профком")
connections_markup.row(back_text)

states = {}


@bot.message_handler(content_types=['text'])
def button1(message):
    if message.chat.id not in states:
        states[message.chat.id] = State.default

    if message.text.lower() == 'звонки':
        bot.send_photo(message.chat.id, 'https://i.imgur.com/OUMs1ZI.jpg',
                       caption="Это наше расписание в ОНУ "
                               "независимо от факультета. \n\n"
                               "Сохрани это изображение в телефон, чтобы оно было у тебя под рукой.\n\n"
                               "Но ты всегда можешь мной воспользоваться, чтобы я тебе его заново отправил.")
    elif message.text.lower() == 'карта интернетов':
        bot.send_message(message.chat.id,
                         "Это наша \"карта интернетов\"\.\n\n Твоя личная ссылка\-навигатор по всем нашим доступным каналам и чатам, включая личные каналы студентов из ОНУ\. \n\n"
                         "Чтобы добавить свой канал, ты можешь обратиться к @dovganyan\. \n\n"
                         "[Карта интернетов](https://telegra.ph/Karta-Internetov-ONU-12-14)",
                         parse_mode="MarkdownV2")
    elif message.text.lower() == "фидбек":
        bot.send_message(message.chat.id, "Выбери одну из категорий", reply_markup=feedback_markup)
    elif message.text.lower() == "пожаловаться на бота":
        states[message.chat.id] = State.forward
        bot.send_message(message.chat.id, "Ублюдок, мать твою, а ну иди сюда, говно собачье, тут решил ко мне лезть "
                                          "ты, засранец вонючий, мать твою!! А, ну иди сюда, попробуй меня трахнуть! "
                                          "Я тебя сам трахну, ублюдок, онанист чёртов, будь ты проклят!!! Иди, идиот, "
                                          "трахать тебя, и всю твою семью, говно собачье, жлоб вонючий, дерьмо, сука, "
                                          "падла!! Иди сюда, мерзавец, негодяй, гад! Иди сюда ты, говно, жопа!!")
    elif message.text.lower() == "связь":
        bot.send_message(message.chat.id, "Выбери одну из категорий.", reply_markup=connections_markup)

    elif message.text.lower() == "общение":
        bot.send_message(message.chat.id,
                         "В этом чате происходит общение всех студентов с ОНУ\. Заходи и наслаждайся непривычной для "
                         "тебя атмосферой \"флуда\"\. \n\n"
                         "[Переход в чат](https://t.me/onu_flood)",
                         parse_mode="MarkdownV2")

    elif message.text.lower() == "send nudes":
        bot.send_message(message.chat.id, "@smeshnotebesuka")

    elif message.text.lower() == "расписание":
        bot.send_message(message.chat.id, "В разработке.", reply_markup=faculties)
    elif message.text.lower() == "о факультетах":
        bot.send_message(message.chat.id, "В разработке.", reply_markup=faculties)
    elif message.text.lower() == "об общежитиях":
        bot.send_message(message.chat.id, "В разработке.", reply_markup=dorms)
    elif message.text.lower() == "документация/faq":
        bot.send_message(message.chat.id, "В разработке.")
    elif message.text.lower() == "руководство":
        bot.send_message(message.chat.id, "В разработке.")
    elif message.text.lower() == "поблагодарить шекелем":
        bot.send_message(message.chat.id, "4441114423016052 - МОНОБАНК. \n\n"
                                          "5168755420701571 - ПРИВАТБАНК. \n\n"
                                          "Карта для благодарности команде ONU live.", reply_markup=feedback_markup)
    elif message.text.lower() == back_text.lower():
        states[message.chat.id] = State.default
        bot.send_message(message.chat.id, "Возвращаемся.", reply_markup=keyboard1)
    elif message.text.lower() == 'предложить новость':
        bot.send_message(message.chat.id, "Сюда Вы можете предложить свою новость, связанную с ОНУ.")
        states[message.chat.id] = State.forward
    else:
        if states[message.chat.id] is State.forward:
            states[message.chat.id] = State.default
            bot.forward_message(chat_id="-1001289477077", from_chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id, "Кабанчк отправлен")

#       bot.send_message(chat_id='-1001289477077', text=message)
