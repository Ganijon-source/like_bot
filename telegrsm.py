from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


likes = 0
dislikes = 0


def botcha(update: Update, context: CallbackContext):
    global likes, dislikes
    message = update.message.text
    user_name = update.message.from_user.first_name or update.message.from_user.username


    if message in ["👍", "👍🏻", "👍🏼", "👍🏽", "👍🏾", "👍🏿"]:
        likes += 1
        update.message.reply_text(f"👍 Like: {likes}\n👎 Dislike: {dislikes}")

    elif message in ["👎", "👎🏻", "👎🏼", "👎🏽", "👎🏾", "👎🏿"]:
        dislikes += 1
        update.message.reply_text(f"👍 Like: {likes}\n👎 Dislike: {dislikes}")

    elif message in ["😂", "😁", "🤣", "😅"]:
        update.message.reply_text("Nega kulasiz? Biror latifa bo'lsa, ulashsangiz, ham kulamiz!")

    elif message in ["🤲", "🤲🏻", "🤲🏼", "🤲🏽", "🤲🏾", "🤲🏿"]:
        update.message.reply_text(f"Omin, aytganiz kelsin {user_name}.")

    elif message.lower() in ["salom", "assalomu alaykum", "hello", "hi", "hey"]:
        update.message.reply_text(f"Va alaykum salom, {user_name}! Nima gap")

    elif "qalesan" in message.lower() or 'qalesiz' in message.lower() or 'qonnay' in message.lower():
        update.message.reply_text("Yaxshi rahmat, o'zingizda-chi? 🙋")
    elif 'zur' in message.lower() or 'yaxshi' in message.lower():
        update.message.reply_text("Gap!")

    elif message.lower() in ["rahmat", "spasibo", "thank you", "thanks"]:
        update.message.reply_text("Arzimaydi! Yana qanday yordamim tegishi mumkin?")

    elif "kim" in message.lower():
        update.message.reply_text("Kim")
    elif "nimaga" in message.lower():
        update.message.reply_text("Bu savolga javob berish uchun ko'p kitob o'qish kerak")
    elif "qanday" in message.lower():
        update.message.reply_text("Qandayligini o'zingiz bilasiz!")
    elif "savol" in message.lower() or 'question' in message.lower():
        update.message.reply_text("Qanaqa savol?")
    elif "yordam" in message.lower() or 'help' in message.lower:
        update.message.reply_text(f"Sizga qanday yordam bera olaman, {user_name}")
    else:
        update.message.reply_text(f"Qiziqarli suhbat uchun raxmat {user_name}! Lekin hozircha 👍 yoki 👎 yuborishni unutib qo'ymang. 🙂")


def trash_bot(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! 👍 yoki 👎 ni yuboring, men sanab boraman.")

def main():
    TOKEN = '7542472244:AAF_uzh6u6yy9wVZcGJ7r-Z9rhR51byUv04'
    updater = Updater(TOKEN)  

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", trash_bot))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, botcha))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
