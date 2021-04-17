import telebot

token = "1725730451:AAG8bGzd5s2fMQgXeIv5ICuf5h7rN6n55-U"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])  
def help_command(message):  
    main_keyboard = telebot.types.InlineKeyboardMarkup()  
    main_keyboard.add(telebot.types.InlineKeyboardButton("Предметная область", callback_data='subject_area'))
    main_keyboard.add(telebot.types.InlineKeyboardButton("Общая область", callback_data='general_area'))
    main_keyboard.add(telebot.types.InlineKeyboardButton("Обратная связь", callback_data='feedback'))

    user = message.from_user.first_name
    bot.send_message(  
        message.chat.id,  
        'Я бот. Приятно познакомиться, ' + user + '\nВы находитесь в главном меню.',
        reply_markup=main_keyboard  
    )

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'команды':
        bot.send_message(message.from_user.id, 'Чтобы увидеть меню, напишите /start')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит. Напшите /start')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "subject_area":
                subject_keyboard = telebot.types.InlineKeyboardMarkup()  
                subject_keyboard.add(telebot.types.InlineKeyboardButton("Информатика", callback_data='informatics'))
                subject_keyboard.add(telebot.types.InlineKeyboardButton("Технология и ОБЖ", callback_data='technology'))
                subject_keyboard.add(telebot.types.InlineKeyboardButton("Робототехника", callback_data='robotics'))

                bot.send_message(  
                    call.message.chat.id,  
                    'Предметная область',
                    reply_markup=subject_keyboard
                )
            if call.data == "general_area":
                general_keyboard = telebot.types.InlineKeyboardMarkup()  
                general_keyboard.add(telebot.types.InlineKeyboardButton("Полезные ресурсы", callback_data='resources'))
                general_keyboard.add(telebot.types.InlineKeyboardButton("Позиция 2", callback_data='position'))

                bot.send_message(  
                    call.message.chat.id,  
                    'Общая область',
                    reply_markup=general_keyboard
                )

            if call.data == "feedback":
                bot.send_message(call.message.chat.id, "Обратная связь\nФорма обратной связи\nФорма добавления новых ресурсов\nПотом что нибудь придумаем")
            

            if call.data == "informatics":
                bot.send_message(  
                    call.message.chat.id,  
                    'Информатика\nСсылка 1\nСсылка 2'
                )
            
            if call.data == "technology":
                bot.send_message(  
                    call.message.chat.id,  
                    'Технология и ОБЖ\nСсылка 1\nСсылка 2'
                )
            
            if call.data == "robotics":
                bot.send_message(  
                    call.message.chat.id,  
                    'Робототехника\nСсылка 1\nСсылка 2'
                )
            
            if call.data == "resources":
                bot.send_message(  
                    call.message.chat.id,  
                    'Полезные ресурсы\nСсылка 1\nСсылка 2'
                )
            
            if call.data == "position":
                bot.send_message(  
                    call.message.chat.id,  
                    'Позиция 2\nСсылка 1\nСсылка 2'
                )
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)