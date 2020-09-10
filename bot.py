import telebot
import parser
from findproducts.data_manager import DataManager
from message_parser import MsgParser
from findproducts.class_findproducts import ProductsFinder
from product_mesage import ProductMesage
from config import TOKEN
#from class_findproducts import ProductsFinder
dm = DataManager()
prod_finder = ProductsFinder(dm.load())

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет я робот который помогает подобрать продукты для употребления пищи. Введи пожалуйста разницу между колличестовм жиров, белков, углеводов и воды на 100г в данном формате:  "proteins > 10 , water < 8"  , где proteins - это протеин, water - вода, а 10 и 8 значения для сравнения')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    find_args = MsgParser(text).extracted_params()
    filtered_products = prod_finder.find_all(find_args)
    if len(filtered_products) == 0:
        bot.send_message(chat_id, "Не найденно продуктов")        
    for product in filtered_products:        
        answer = ProductMesage(product).transform_to_str()        
        bot.send_message(chat_id, answer)
    
       
bot.polling()



#@bot.message_handler(commands=['start', 'ne'])
#def start_handler(message):
    #for prod in dm.load(format='list'):
        #bot.send_message(message.chat.id, prod.get('name'))
#bot.polling()