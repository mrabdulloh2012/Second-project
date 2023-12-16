import telebot

bot = telebot.TeleBot("6024406463:AAHWkOBKSH3O2Vzr1qDBaqgxoO3qgIR3EGk")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Assalomu alaykum")



@bot.message_handler()
def start(message):
    if message.text == "rasm":
        bot.send_photo(message.chat.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJbpDKH1RP0UXjF5YMKjj1JAiPFN8g2MMOLw&usqp=CAU" )


bot.polling(non_stop=False)
