import telebot
from config import TOKEN
from validator import validate_code, calculate_stats

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(
        message,
        "Привет! Я Валидатор Кодов. Отправь строку с кодами через запятую, например: abc123, test99, x4"
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    # Разбиваем по запятой, убираем пробелы
    codes = [c.strip() for c in text.split(',') if c.strip()]

    valid_codes = []
    for code in codes:
        if validate_code(code):
            valid_codes.append(code)

    stats = calculate_stats(valid_codes)

    if valid_codes:
        result = f"✅ Нашёл {len(valid_codes)} валидных кодов:\n"
        result += ", ".join(valid_codes) + "\n"
        result += stats
    else:
        result = "❌ Ни один код не прошёл проверку. Попробуй ещё раз — формат: код1, код2, код3"

    bot.reply_to(message, result)

if __name__ == '__main__':
    print("Бот запущен…")
    bot.polling(none_stop=True)
