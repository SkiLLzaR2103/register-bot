import psycopg2 
import os 
from dotenv import load_dotenv

load_dotenv()
KEYS = os.getenv("KEYS")
SECRETE = os.getenv("SECRETE")
SECRETES = os.getenv("I")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


conn = psycopg2.connect(dbname=SECRETE, user=SECRETE, password=SECRETES, host=HOST, port=PORT)
cursor = conn.cursor()
conn.autocommit = True

from telebot import TeleBot

TOKEN = KEYS
bot = TeleBot(TOKEN)
print("Запуск бота")
@bot.message_handler()
def handle_message(message):
    text = f"Приветсвуем вас!"
    id = message.chat.id
    if message.text == "Привет":
        bot.reply_to(message, text)
    elif message.text == "Пока":
        bot.reply_to(message, "Доскорых встреч")       
    elif message.text == "1":
        bot.reply_to(message, "Введите ФИО-Возраст-Курс ")
    elif "-" in message.text:
        name = message.text.split("-")[0]
        age = message.text.split("-")[1]
        course = message.text.split("-")[2]
        print(name, age, course)
        sql = """
        INSERT INTO Students(name, age, course)
        VALUES(%s, %s, %s);
        """
        res = cursor.execute(sql, (name, int(age), course))
        print("done", res)
        conn.commit   
        bot.reply_to(message, "Регистрация успешно")  
bot.infinity_polling()

print("Остановился")