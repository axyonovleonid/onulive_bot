import enum
import os

import telebot
from flask import Flask, request

# API_TOKEN = os.environ.get('TOKEN')
API_TOKEN = '1434687229:AAGOTUvkeFy7dqx7zIrY6kPBxJ2IcxIDa5s'

ECHO_CHANNEL_ID = "-1001289477077"


class State(enum.Enum):
    default = 0
    news = 1
    issue = 2
    nudes = 3


bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)

keyboard1.row("Общение", "Карта интернетов")
keyboard1.row("Расписание", "Звонки")
keyboard1.row("О факультетах", "Руководство")
keyboard1.row("Об общежитиях", "Документация/FAQ")
keyboard1.row("Связь", "Фидбек")
keyboard1.row('SEND NUDES')

back_text = "Назад"

faculties = telebot.types.ReplyKeyboardMarkup(True, False)

facultiesNames = {"БИОФАК": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ГГФ": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ЭПФ": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ИСТФАК": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ЖУРФАК": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "МФИТ": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "МОПС": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ФПСР": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "РГФ": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ФИЛФАК": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  "ХИМФАРМ": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}

faculties.row("БИОФАК", "ГГФ", "ЭПФ", "ИСТФАК")
faculties.row("ЖУРФАК", "МФИТ", "МОПС", "ФПСР")
faculties.row("РГФ", "ФИЛФАК", "ХИМФАРМ", back_text)

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


@bot.message_handler(func=lambda message: True, content_types=['text'])
def processMessage(message):
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
        states[message.chat.id] = State.issue
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
    elif message.text.lower() in map(lambda m: m.lower(), facultiesNames.keys()):
        bot.send_message(message.chat.id, "[Силлабус]({})".format(facultiesNames.get(message.text.upper())),
                         parse_mode="MarkdownV2")
    elif message.text.lower() == "send nudes":
        states[message.chat.id] = State.nudes
        bot.send_message(message.chat.id, "@smeshnotebesuka")
        bot.send_message(message.chat.id, """Идеи для нюдсов:📸🤳

 • Боком и попкой оп
 • В душе/ванной вода стекает по ключицам в slow mo
 • Когда тело похоже на античную статую
 • Когда партнер трогает свое тело
 • Обожаю, когда на нюдсах есть любимые особенности партнера — родинки и вены на руках
 • Игры со светом и тенью
 • С растениями и минералами, в стиле зеленых ведьм

С персиками, напитками и цветами — они вызывают чувственные ассоциации 🍑🧉💕

 • Чтобы был элемент загадки и недосказанности, которые будоражат воображение
 • Чтобы на фото были разные текстуры, которыми приятно прикасаться к коже: ткани, вода
 • Игра света делает фото интереснее и сочнее. От полумрака до прямых лучей
 • Люблю, когда там есть лицо, не все, можно лишь полуулыбку. Мимика губ — это настроение
 • Эстетика, она в загадке, а не когда я вижу все секреты тела
 • Попы мальчиков
 • Нюдсы в зеркале — полный кайф, так приятно смотреть на себя на фотках потом
 • С тенью от проектора ночного неба (звездочки на теле)
 • Где только части тела, и не сразу понятно, что это
 • Фото в ванне с пеной
 • Через запотевшее стекло или штору
 • Мягкие и чарующие, словно ты нежная роза

Хороший ракурс и атмосфера!🪞🛁

 • Игра со светом с помощью настольной лампы
 • Возбуждаться от прикосновений к своему телу
 • Включить на фоне сексуальную музыку и немного потанцевать
 • Когда лучи солнца на теле
 • От парня лучшее — стояк через штаны
 • Верх без одежды, но соски словно случайно прикрыты чем-то
 • В прозрачном нижнем белье
 • Тень от обнаженного тела на стене
 • Черно-белые чувственные
 • В круглом небольшом зеркале, словно Венера Милосская
 • Фото определенных частей тела: напряженные руки в венах, влажный рот, мурашки на коже
 • В одежде, просвечивающей темные соски, и еще гладкая темная кожа
 • Которые напоминают искусство возрождения
 • В лучах утреннего солнца

Влажные, когда слюна стекает или смазка 💦💦

 • В трусах со спины, когда видно спину и попу, все линии
 • Когда от маленькой груди падает тень небольшая, и она такая маленькая и аккуратная
 • Тело с мокрыми тканями: в мокрой футболке или платье
 • Женское изящество с сигаретой
 • На природе""")

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
        states[message.chat.id] = State.news
    else:
        forwardMessage(message)


@bot.message_handler(func=lambda message: True,
                     content_types=['audio', 'document', 'photo', 'sticker', 'video', 'voice'])
def processMessage(message):
    if message.chat.id not in states:
        states[message.chat.id] = State.default
    forwardMessage(message)


def forwardMessage(message):
    if states[message.chat.id] is not State.default:
        bot.send_message(ECHO_CHANNEL_ID, "#{}".format(states[message.chat.id].name))
        bot.forward_message(chat_id=ECHO_CHANNEL_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(ECHO_CHANNEL_ID, "================================".format(states[message.chat.id].name))
        bot.send_message(message.chat.id, "Спасибо")
        states[message.chat.id] = State.default


@server.route("/{}".format(API_TOKEN), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    # bot.set_webhook(url='https://b11f0a08c65b.ngrok.io/' + API_TOKEN)
    bot.set_webhook(url="https://onulive-bot.herokuapp.com/{}".format(API_TOKEN))
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
