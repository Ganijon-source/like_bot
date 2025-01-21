import requests

BOT_TOKEN = '7542472244:AAF_uzh6u6yy9wVZcGJ7r-Z9rhR51byUv04'
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
reactions = {
    'likes': 0,
    'dislikes': 0
}

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"offset": offset} if offset else {}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text, reply_to_message_id=None):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    if reply_to_message_id:
        payload["reply_to_message_id"] = reply_to_message_id
    requests.post(url, data=payload)

def handle_reactions(update):
    global reactions
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")
    user_name = message.get("from", {}).get("first_name", "User")

    if text in ["👍", "👍🏻", "👍🏼", "👍🏽", "👍🏾", "👍🏿"]:
        reactions['likes'] += 1
        send_message(chat_id, f"👍 Like: {reactions['likes']}\n👎 Dislike: {reactions['dislikes']}")

    elif text in ["👎", "👎🏻", "👎🏼", "👎🏽", "👎🏾", "👎🏿"]:
        reactions['dislikes'] += 1
        send_message(chat_id, f"👍 Like: {reactions['likes']}\n👎 Dislike: {reactions['dislikes']}")

    elif text in ["😂", "😁", "🤣", "😅"]:
        send_message(chat_id, "Nega kulasiz? Biror latifa bo'lsa, ulashsangiz, ham kulamiz!")

    elif text in ["🤲", "🤲🏻", "🤲🏼", "🤲🏽", "🤲🏾", "🤲🏿"]:
        send_message(chat_id, f"Omin, aytganiz kelsin {user_name}.")

    elif text.lower() in ["salom", "assalomu alaykum", "hello", "hi", "hey"]:
        send_message(chat_id, f"Va alaykum salom, {user_name}! Nima gap")

    elif "qalesan" in text.lower() or 'qalesiz' in text.lower() or 'qonnay' in text.lower():
        send_message(chat_id, "Yaxshi rahmat, o'zingizda-chi? 🙋")
    elif 'zur' in text.lower() or 'yaxshi' in text.lower():
        send_message(chat_id, "Gap!")

    elif text.lower() in ["rahmat", "spasibo", "thank you", "thanks"]:
        send_message(chat_id, "Arzimaydi! Yana qanday yordamim tegishi mumkin?")

    elif "kim" in text.lower():
        send_message(chat_id, "Kim")
    elif "nimaga" in text.lower():
        send_message(chat_id, "Bu savolga javob berish uchun ko'p kitob o'qish kerak")
    elif "qanday" in text.lower():
        send_message(chat_id, "Qandayligini o'zingiz bilasiz!")
    elif "savol" in text.lower() or 'question' in text.lower():
        send_message(chat_id, "Qanaqa savol?")
    elif "yordam" in text.lower() or 'help' in text.lower():
        send_message(chat_id, f"Sizga qanday yordam bera olaman, {user_name}")
    else:
        send_message(chat_id, f"Qiziqarli suhbat uchun raxmat {user_name}! Lekin hozircha 👍 yoki 👎 yuborishni unutib qo'ymang. 🙂")

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            if "message" in update:
                handle_reactions(update)

if __name__ == "__main__":
    main()
