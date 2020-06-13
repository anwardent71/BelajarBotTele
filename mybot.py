import telebot
import mysql.connector

import mytoken

from datetime import date
from datetime import datetime
TOKEN = mytoken.TOKEN
Mybot = telebot.TeleBot(TOKEN)
MyDb = mysql.connector.connect(host='localhost', user='root', database='belajarbot')
sql = MyDb.cursor()
from telebot import apihelper
waktusekarang = datetime.now()

class mybot:
    def __init__(self):
        self.message

    @Mybot.message_handler(commands=['start', 'help'])
    def start(message):
        photo = open('img/icon.jpg', 'rb')
        Mybot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n"+"✍ Disini Aku akan melakukan apa yang Aku bisa"\
               +"\n👨‍💻 Admin & Developer @anwar_1410 "+"\n" "📅 Hari ini tanggal "+str(waktusekarang)+"\n" "🏫 SMK Taruna Bhakti"
        Mybot.reply_to(message, teks)

    @Mybot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "SELECT nipd,nama,kelas FROM tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if(jmldata>0):
            #print(data)
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x) + "\n"
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        Mybot.reply_to(message, str(kumpuldata))

print(MyDb)
print("-- Bot Ini Sedang Berjalan --")
Mybot.polling(none_stop=True)
