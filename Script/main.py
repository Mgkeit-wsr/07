import json
import random
import time

import telebot
from telebot import types
import requests
import mysql.connector
from mysql.connector import Error




mydb = mysql.connector.connect(
  host="185.12.127.155",
  user="hakaton",
  password="pL8pY1zF3gfC8s",
  database="hakaton"
)
mycursor = mydb.cursor()


token_api = "5332791299:AAEi8MwkMykt7MY5ikLAU6Kfe2sQaW5qRNY"
link = "t.me/hackandtonbot"

bot = telebot.TeleBot(token_api, parse_mode="MARKDOWN")
keyboard_main = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.row('🏌️ Отдохнуть', '⭐️Избранное')

def formData(response, message, type = 0):
    data_ivents = json.loads(response.content)

    with open(str(message.chat.id) + '.json', 'w', encoding='utf-8') as f:
        json.dump(data_ivents, f, ensure_ascii=False, indent=4)
        f.close()

    with open(str(message.chat.id) + '.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        i = 0
        event = data['results'][0]
        count = len(data['results'])
        iNew = i+1
        if event['location'] == 'online':
            i = 1
            event = data['results'][1]
        if(type == 1):
            i = random.randint(0, count-1)
            iNew = random.randint(0, count-1)
            event = data['results'][i]
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("ℹ️ Узнать подробнее...", url=data['results'][i]['site_url'])
        button2 = types.InlineKeyboardButton("➡️ Далее...", callback_data='/place ' + str(iNew))
        button3 = types.InlineKeyboardButton("⭐️ В избранное", callback_data='/favorite ' + str(i))
        markup.row(button1, button2)
        markup.row(button3)
        msg = "*Предлагаю посетить:*\n\n" \
              "✅ \"" + event['title'] + "\"\n" \
                                        "Адрес: " + event['address']
        if len(event['phone']) > 3:
            msg += "\n" \
                   "Телефон: " + event['phone']

        newmsg = bot.send_message(message.chat.id, msg, reply_markup=markup)
        sql = "UPDATE users SET note = '" + str(newmsg.message_id) + "' WHERE chat_id = " + str(message.chat.id)
        mycursor.execute(sql)
        mydb.commit()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, это наработка для Хакатон2022")
    bot.send_message(message.chat.id, "Сейчас же начнем с вами работать!", reply_markup=keyboard_main)

    sql = "SELECT * FROM users WHERE chat_id = %s"
    adr = (message.chat.id,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        sql = "INSERT INTO users (username, f_name, l_name, chat_id) VALUES (%s, %s, %s, %s)"
        if message.chat.last_name:
            ln = message.chat.last_name
        else:
            ln = ''
        val = (message.chat.username, message.chat.first_name, ln, message.chat.id)
        mycursor.execute(sql, val)
        mydb.commit()

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "🏌️ Отдохнуть":
        keyboard_poll = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_poll.row('🏞 Парки', '🏯 Музеи', '🍽 Покушать')
        keyboard_poll.row('🎲 Случайное событие')
        keyboard_poll.row('◀️ Назад')
        bot.send_message(message.chat.id, "Отлично! Что предпочитаешь?", reply_markup=keyboard_poll)


    elif message.text == "🏞 Парки":
        response = requests.get(
            "https://kudago.com/public-api/v1.4/places/?lang=&fields=&expand=&order_by=&text_format=&ids=&location=msk&has_showings=&showing_since=1444385206&showing_until=1444385206&categories=park&lon=&lat=&radius=")
        formData(response,message)

    elif message.text == "🏯 Музеи":
        response = requests.get(
            "https://kudago.com/public-api/v1.4/places/?lang=&fields=&expand=&order_by=&text_format=&ids=&location=msk&has_showings=&showing_since=1444385206&showing_until=1444385206&categories=museums&lon=&lat=&radius=")
        formData(response,message)

    elif message.text == "🍽 Покушать":
        response = requests.get(
            "https://kudago.com/public-api/v1.4/places/?lang=&fields=&expand=&order_by=&text_format=&ids=&location=msk&has_showings=&showing_since=1444385206&showing_until=1444385206&categories=restaurants&lon=&lat=&radius=")
        formData(response,message)

    elif message.text == "🎲 Случайное событие":
        response = requests.get(
            "https://kudago.com/public-api/v1.4/places/?lang=&fields=&expand=&order_by=&text_format=&ids=&location=msk&has_showings=&showing_since=1444385206&showing_until=1444385206&categories=-airports,amusement,animal-shelters,anticafe,art-centers,art-space,attractions,bar,brewery,bridge,business,-car-washes,cats,church,cinema,clubs,comedy-club,concert-hall,coworking,culture,dance-studio,dogs,-education-centers,fountain,handmade,homesteads,-hostels,-inn,kids,library,-metro,-monastery,museums,-observatory,other,palace,park,photo-places,prirodnyj-zapovednik,questroom,recreation,restaurants,-rynok,salons,shops,sights,-stable,-station,strip-club,suburb,-synagogue,-temple,theatre,-workshops&lon=&lat=&radius=")
        formData(response,message,1)


    elif message.text == "⭐️Избранное":
        sql = "SELECT * FROM users WHERE chat_id = %s"
        adr = (message.chat.id,)
        mycursor.execute(sql, adr)
        user = mycursor.fetchall()
        uid = user[0][0]
        sql = "SELECT * FROM bookmarks WHERE uid = %s"
        adr = (uid,)
        mycursor.execute(sql, adr)
        bookmarks = mycursor.fetchall()
        print(bookmarks)

        markup = types.InlineKeyboardMarkup(row_width=2)
        for f in bookmarks:
            b = types.InlineKeyboardButton(f[2], url=f[7])
            markup.row(b)
        bot.send_message(message.chat.id, "⭐️Вот что вы добавили в избранное:", reply_markup=markup)

    if message.text == "◀️ Назад":
        bot.send_message(message.chat.id, "*👋 Добро пожаловать в Хакатон Бот!*\n\nГлавное меню:", reply_markup=keyboard_main)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)


@bot.callback_query_handler(func=lambda call: True)
def next(call):  # <- passes a CallbackQuery type object to your function
    if call.data.find('/place ') > -1:
        sql = "SELECT * FROM users WHERE chat_id = %s"
        adr = (call.from_user.id,)
        mycursor.execute(sql, adr)
        user = mycursor.fetchall()
        uid = user[0][5]
        bot.delete_message(call.from_user.id, uid)
        place_id = call.data[7:]
        with open(str(call.from_user.id) + '.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            if len(data['results']) - 1 <= int(place_id):
                event = data['results'][0]
                place_id = 0
            else:
                event = data['results'][int(place_id)]
        if event['location'] == 'online':
            place_id += 1
            event = data['results'][place_id]

        msg = "*Предлагаю посетить:*\n\n" \
              "✅ \"" + event['title'] + "\"\n" \
              "Адрес: "+event['address'];
        if len(event['phone']) > 3:
            msg += "\n" \
                   "Телефон: " + event['phone']
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ℹ️ Узнать подробнее...", url=event['site_url'])
        button2 = types.InlineKeyboardButton("➡️ Далее...", callback_data='/place ' + str(int(place_id) + 1))
        button3 = types.InlineKeyboardButton("⭐️ В избранное", callback_data='/favorite ' + str(int(place_id)))
        markup.row(button1, button2)
        markup.row(button3)
        newmsg = bot.send_message(call.from_user.id, msg, reply_markup=markup)
        sql = "UPDATE users SET note = '"+str(newmsg.message_id)+"' WHERE chat_id = " + str(call.from_user.id)
        mycursor.execute(sql)
        mydb.commit()
    if call.data.find('/favorite ') > -1:
        place_id = call.data[10:]
        with open(str(call.from_user.id) + '.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            place = data['results'][int(place_id)]
            sql = "SELECT * FROM users WHERE chat_id = %s"
            adr = (call.from_user.id,)
            mycursor.execute(sql, adr)
            user = mycursor.fetchall()
            uid = user[0][0]
            sql = "SELECT * FROM bookmarks WHERE uid = %s and place_id = %s"
            adr = (uid,place['id'])
            mycursor.execute(sql, adr)
            check = mycursor.fetchall()
            print(place)
            if len(check) != 0:
                print(2)
            else:
                print(place)
                sql = "INSERT INTO bookmarks (uid, title, description, data, time, place_id, link) VALUES (%s, %s, %s, %s, %s,%s, %s)"
                try:
                    d = place['description']
                except KeyError:
                    place['description'] = ''
                try:
                    l = place['site_url']
                except KeyError:
                    place['site_url'] = ''
                val = (uid, place['title'], place['description'], str(place), int(time.time()), place['id'], place['site_url'])
                mycursor.execute(sql, val)
                msg = '*ОК!*\n' \
                      'Мероприятие *'+place['title']+'* добавлено в избранное!'
                bot.send_message(call.from_user.id, msg)
                mydb.commit()


# END OF CODE / DONT CHANGE
bot.infinity_polling(20)