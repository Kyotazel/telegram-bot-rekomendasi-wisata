import os
import telebot
from telebot import types
from dotenv import load_dotenv
import master_function as mf

load_dotenv()
Bot_Token = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(Bot_Token)

@bot.message_handler(commands=['mulai', 'start'])
def mulai(message):
    bot.reply_to(message, "Silahkan /daftar terlebih dulu")
    
@bot.message_handler(commands=['daftar'])
def daftar(message):
    response = "Berikut merupakan kategori user yang tersedia"
    markup = types.ReplyKeyboardMarkup()
    categories = mf.master_category_user()
    for idx, category in enumerate(categories):
        item = types.KeyboardButton(f"/kategori_user {category}" )
        markup.row(item)
    bot.send_message(message.chat.id, response, reply_markup=markup)
    
@bot.message_handler(commands=['kategori_user'])
def kategori_user(message):
    try:
        category_user = message.text.split()[1]
        response = "Berikut merupakan kategori wisata yang tersedia"
        markup = types.ReplyKeyboardMarkup()
        categories = mf.master_category()
        for idx, category in enumerate(categories):
            item = types.KeyboardButton(f"/kategori {category_user} {category}" )
            markup.row(item)
        bot.send_message(message.chat.id, response, reply_markup=markup)
        
    except:
        bot.reply_to(message, "Kategori user tidak sesuai")
        

@bot.message_handler(commands=['kategori'])
def kategori(message):
    try:
        category_user = message.text.split()[1]
        category = message.text.split()[2]
        dataframe_tourists = mf.select_category(category_user, category)
        
        if type(dataframe_tourists) is str:
            bot.reply_to(message, "Kategori tidak sesuai")
            return
        
        # bot.reply_to(message, "Berikut destinasi yang tersedia")
        for idx, row in dataframe_tourists.iterrows():
            response = ""
            response += f"Nama Wisata : {row['namaWisata']}\n"
            response += f"Rating  : {row['rating']}\n"
            response += f"Tautan : "
            bot.send_photo(chat_id=message.chat.id, photo=open('https://images.tokopedia.net/img/cache/700/VqbcmM/2022/10/29/bd50f436-60c4-4199-b09f-f65b2b6ad428.jpg', 'rb'), caption=response)
    except:
        bot.reply_to(message, "Kategori tidak sesuai")

print("Bot is running...")
bot.infinity_polling()