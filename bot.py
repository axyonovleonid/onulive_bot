import telebot

bot = telebot.TeleBot('1434687229:AAGOTUvkeFy7dqx7zIrY6kPBxJ2IcxIDa5s')

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
feedback_markup.row("Главное меню")

connections_markup = telebot.types.ReplyKeyboardMarkup(True, False)
connections_markup.row("Студсовет", "Профком")
connections_markup.row("Главное меню")


@bot.message_handler(content_types=['text'])
def button1(message):
    if message.text.lower() == 'звонки':
        bot.send_photo(message.chat.id, 'https://i.imgur.com/OUMs1ZI.jpg',
                       caption="Это наше расписание в ОНУ "
                               "независимо от факультета. \n\n"
                               "Сохрани это изображение в телефон, чтобы оно было у тебя под рукой.\n\n"
                               "Но ты всегда можешь мной воспользоваться, чтобы я тебе его заново отправил.")
    if message.text.lower() == 'карта интернетов':
        bot.send_message(message.chat.id,
                         "Это наша \"карта интернетов\"\.\n\n Твоя личная ссылка\-навигатор по всем нашим доступным каналам и чатам, включая личные каналы студентов из ОНУ\. \n\n"
                         "Чтобы добавить свой канал, ты можешь обратиться к @dovganyan\. \n\n"
                         "[Карта интернетов](https://telegra.ph/Karta-Internetov-ONU-12-14)",
                         parse_mode="MarkdownV2")
    if message.text.lower() == "фидбек":
        bot.send_message(message.chat.id, "Выбери одну из категорий", reply_markup=feedback_markup)
    if message.text.lower() == "пожаловаться на бота":
        bot.send_message(message.chat.id, "Ублюдок, мать твою, а ну иди сюда, говно собачье, тут решил ко мне лезть "
                                          "ты, засранец вонючий, мать твою!! А, ну иди сюда, попробуй меня трахнуть! "
                                          "Я тебя сам трахну, ублюдок, онанист чёртов, будь ты проклят!!! Иди, идиот, "
                                          "трахать тебя, и всю твою семью, говно собачье, жлоб вонючий, дерьмо, сука, "
                                          "падла!! Иди сюда, мерзавец, негодяй, гад! Иди сюда ты, говно, жопа!!")
    if message.text.lower() == "связь":
        bot.send_message(message.chat.id, "Выбери одну из категорий.", reply_markup=connections_markup)

    if message.text.lower() == "общение":
        bot.send_message(message.chat.id,
                         "В этом чате происходит общение всех студентов с ОНУ\. Заходи и наслаждайся непривычной для "
                         "тебя атмосферой \"флуда\"\. \n\n"
                         "[Переход в чат](https://t.me/onu_flood)",
                         parse_mode="MarkdownV2")

    if message.text.lower() == "send nudes":
        bot.send_message(message.chat.id, "@smeshnotebesuka")

    if message.text.lower() == "расписание":
        bot.send_message(message.chat.id, "В разработке.")
    if message.text.lower() == "о факультетах":
        bot.send_message(message.chat.id, "В разработке.")
    if message.text.lower() == "об общежитиях":
        bot.send_message(message.chat.id, "В разработке.")
    if message.text.lower() == "документация/faq":
        bot.send_message(message.chat.id, "В разработке.")
    if message.text.lower() == "руководство":
        bot.send_message(message.chat.id, "В разработке.")

    if message.text.lower() == "поблагодарить шекелем":
        bot.send_message(message.chat.id, "5168755420701571\n\n"
                                          "Карта для благодарности команде ONU live.", reply_markup=feedback_markup)

    if message.text.lower() == "главное меню":
        bot.send_message(message.chat.id, "Возвращаемся.", reply_markup=keyboard1)


bot.polling()
