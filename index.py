#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل

from pyrogram import Client, filters, errors, StopPropagation, enums
import mysql.connector
import re
import uuid
import traceback
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
import sys, os
import time as t
from pyrogram.raw import functions, types
from urllib.parse import unquote, quote
from datetime import datetime
import asyncio
from random import randint
import uvloop
from tronapi import Tron
import requests

# @GoldTabBot
try:
    app_id = #app_id
    app_hash = '' #app_hash
    uvloop.install()
    app = Client(name="mrtab",in_memory=True,api_id=app_id,api_hash=app_hash,bot_token="") #توکن تبچی ساز
    admin = [0000000000] #ایدی ادمین
    apps = {}
    ReportAcc = {}
    join = {}
    codelogin = {}
    userha = {}
    seccess = {}
    mydb = mysql.connector.Connect(
        host='localhost',
        user='',
        password='',
        database=''
    ) #اطلاعات دیتابیس
    mydb.commit()
    mycu = mydb.cursor()
    mydb.autocommit = True
    
    device_model = [
        "Samsung Galaxy A51",
        "Inspiron N5040",
        "G41T-M7",
        "Samsung Galaxy A53 5G",
        "G41T-M7",
        "Inspiron N5040",
        "Samsung Galaxy A21s",
        "OnePlusONEPLUS A5010",
        "Jelly Bean"
    ]
    app_version = [
        "Android 8.6.2",
        "Desktop 4.0.1",
        "Desktop 4.0.2",
        "Android 8.7.4",
        "Desktop 4.0.1",
        "Desktop 4.0.2",
        "Android 8.7.4",
        "Android 5.2.1",
        "Android 4.2.0"
    ]
    system_version = [
        "11 R? (30)",
        "Windows 10",
        "Windows 7",
        "12 S? (31)",
        "Windows 8.1",
        "Windows 10",
        "12 S? (31)",
        "SDK 27",
        "MR1 (17)"
    ]
    lang_code = [
        "fa",
        "en",
        "ru",
        "de",
        "zh"
    ]
    
    menu = ReplyKeyboardMarkup(
        [
            [
                "⚙️ ساخت ربات"
            ],
            [
                "🛍 فروشگاه",
                "🔐 حساب کاربری",
                "🤖 ربات های من"
            ],
            [
                "🛒 خرید اکانت",
                "🌐 بازاریابی (موجودی رایگان)"
            ],
            [
                "⚖️ قوانین",
                "☎️ پشتیبانی",
                "📑 راهنما"
            ]
        ],resize_keyboard=True)
    panel = ReplyKeyboardMarkup(
        [
            [
                "آمار ربات"
            ],
            [
                "حساب طلایی",
                "تمدید حساب",
                "حساب رایگان"
            ],
            [
                "ارسال",
                "فوروارد"
            ],
            [
                "تغییر موجودی",
                "تغییر فرصت"
            ],
            [
                "/start"
            ]
        ],resize_keyboard=True)
    panelback = ReplyKeyboardMarkup(
        [
            [
                "/panel"
            ]
        ],resize_keyboard=True)
    helpkey = ReplyKeyboardMarkup(
        [
            [
                "دریافت آموزش ویدیویی ساخت ربات"
            ],
            [
                "↪️ برگشت"
            ]
        ],resize_keyboard=True)
    ghava = ReplyKeyboardMarkup(
        [
            [
                "دریافت قوانین به صورت عکس"  
            ],
            [
                "↪️ برگشت"
            ]
        ],resize_keyboard=True)
    BackKey = ReplyKeyboardMarkup(
        [
            [
                "↪️ برگشت"
            ]
        ],resize_keyboard=True)
    shopkey = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("افزایش موجودی", callback_data="afz")]
            ,
            [InlineKeyboardButton("تمدید حساب", callback_data="did"),InlineKeyboardButton("خرید/ارتقا حساب", callback_data="by")]
            ,
            [InlineKeyboardButton("خرید فرصت ساخت", callback_data="forsat")]
        ])
    
    def query(q):
        global mycu
        try:
            mycu.execute(q)
            return mycu.fetchall()
        except mysql.connector.errors.OperationalError as e:
            if e.errno == 2055:
                mydb = mysql.connector.Connect(
                    host='localhost',
                    user='',
                    password='',
                    database=''
                ) #اطلاعات دیتابیس
                mydb.commit()
                mycu = mydb.cursor()
                mydb.autocommit = True
                query(q)
        
    def get_string(id):
        return query(f'SELECT * FROM `bots` WHERE `id`={id}')[0][18]
        
    def check(i):
        if i.user.status in [enums.UserStatus.RECENTLY, enums.UserStatus.ONLINE]:
            return True
    
    def update_database(q):
        global mycu,mydb
        try:
            mycu.execute(q)
            mydb.commit()
        except mysql.connector.errors.OperationalError as e:
            if e.errno == 2055:
                mydb = mysql.connector.Connect(
                    host='localhost',
                    user='',
                    password='',
                    database=''
                ) #اطلاعات دیتابیس
                mydb.commit()
                mycu = mydb.cursor()
                mydb.autocommit = True
                update_database(q)
        
    def new_user(id,invite='0'):
        global mycu,mydb
        try:
            sql = "INSERT INTO data (id, step, type, invi, time, bots, phone, coun, account, balance, joiner, pass, adsbalance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (f'{id}', 'no', 'free', f'{invite}', f'{int(t.time())}', 'no', '0', '3', '0', '100', 'no', 'no', '0')
            mycu.execute(sql, val)
            mydb.commit()
        except mysql.connector.errors.OperationalError as e:
            if e.errno == 2055:
                mydb = mysql.connector.Connect(
                    host='localhost',
                    user='',
                    password='',
                    database=''
                ) #اطلاعات دیتابیس
                mydb.commit()
                mycu = mydb.cursor()
                mydb.autocommit = True
                new_user(id,invite)
    
    def get_data(user):
        try:
            return query(f'SELECT * FROM data WHERE id={user}')[0]
        except:
            pass
    
    def get_invi(user):
        try:
            return query(f'SELECT * FROM data WHERE id={user}')[0][3]
        except:
            return '0'
    
    def get_bots(user):
        try:
            return query(f'SELECT * FROM data WHERE id={user}')[0][5]
        except:
            return 'no'
            
    def save_hash(hash):
        hashs = query(f"SELECT * FROM `hash` WHERE `hash` = '{hash}'")
        if len(hashs) == 0:
            update_database(f"INSERT INTO `hash` VALUES('{hash}')")
    # Alfred_s1
    def helpkeyb(id):
        data = get_data(id)
        balance = int(data[9])
        if data[2] == 'gold':
            moj = '✅'
        elif balance >= 45000:
            moj = '✅'
        else:
            moj = '❌'
        
        if data[2] == 'gold' and data[8] != 'unlimited' and int(t.time()) - int(data[8]) < 2592000:
            buyhes = '✅'
        else:
            buyhes = '❌'
            
        count = query(f'SELECT * FROM bots WHERE admin={id}')

        if len(count) > 0:
            makebot = '✅'
        else:
            makebot = '❌'

        return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("فرصت ساخت", callback_data="forsathelp")]
            ,
            [InlineKeyboardButton("موارد موردنیاز", callback_data="require"),InlineKeyboardButton("تبچی چیست؟!", callback_data="whatstab")]
            ,
            [InlineKeyboardButton("روش شارژ حساب", callback_data="increasebal"),InlineKeyboardButton("تمدید حساب", callback_data="tamdidhelp"),InlineKeyboardButton("پشتیبانی ربات", url="https://t.me/Advertisingadmin3")]
            ,
            [InlineKeyboardButton(f"1 - شارژ حساب : [{moj}]", callback_data="buybal")]
            ,
            [InlineKeyboardButton(f"2 - خرید حساب : [{buyhes}]", callback_data="buyhes")]
            ,
            [InlineKeyboardButton("آموزش ویدیویی", url="https://t.me/MrTabchi2/2316"),InlineKeyboardButton(f"3 - ساخت ربات : [{makebot}]", callback_data="makebot")]
            ,
            [InlineKeyboardButton("امکانات ربات", callback_data="toolsbot"),InlineKeyboardButton("پنل و مدیریت ربات ها", callback_data="managebot")]
            ,
            [InlineKeyboardButton("راهنمای عضویت خودکار", callback_data="autoHelp")]
        ])
    
    def get_id():
        for id in range(1000,10000):
            iddata = query(f'SELECT * FROM bots WHERE id={id}')
            if len(iddata) == 0:
                break
        return id
    
    def get_step(from_id):
        UserData = query(f'SELECT * FROM data WHERE id={from_id}')
        return UserData[0][1]
    
    def repeat(string, length):
        cur, old = 1, string
        while len(string) < length:
            string += old[cur-1]
            cur = (cur+1)%len(old)
        return string
        
    def save_word(name, type):
        for word in name.split(' '):
            words = query(f"SELECT * FROM `wordlist` WHERE `word`='{word}' AND `type`='{type}'")
            if len(words) == 0 and len(word) > 1:
                try:
                    update_database(f"INSERT INTO `wordlist` VALUES('{word}', '{type}')")
                except:
                    pass
        return True
        
    def get_word(type):
        words = query(f"SELECT * FROM `wordlist` WHERE `type`='{type}'")
        if len(words) > 3:
            num = randint(2,4)
        else:
            num = randint(2,len(words)-1)
        list = ""  
        group = ["چتکده", "چت کده", "گروه", "چت", "گپ"]
        x = randint(0,len(group)-1)
        group = group[x]
        list += group+" "
        for _ in range(num):
            n = randint(0,len(words)-1)
            list += words[n][0]+" "
            
        return list
#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
    def number_format(num): 
        num = str(num)
        if len(num) < 4:
            return num
        elif len(num) == 4:
            return num[0]+','+num[1]+num[2]+num[3]
        elif len(num) == 5:
            return num[0]+num[1]+','+num[2]+num[3]+num[4]
        elif len(num) == 6:
            return num[0]+num[1]+num[2]+','+num[3]+num[4]+num[5]
        elif len(num) == 7:
            return num[0]+','+num[1]+num[2]+num[3]+','+num[4]+num[5]+num[6]
        elif len(num) == 8:
            return num[0]+num[1]+','+num[2]+num[3]+num[4]+','+num[5]+num[6]+num[7]
        elif len(num) == 9:
            return num[0]+num[1]+num[2]+','+num[3]+num[4]+num[5]+','+num[6]+num[7]+num[8]
        else:
            return num

    def get_bot(id):
        return query(f'SELECT * FROM bots WHERE id={id}')[0]

    def reloadbot():
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    def sendto_key(id):
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👤 دریافت لیست اعضا", callback_data=f"ltp-{id}")]
                ,
                [InlineKeyboardButton("📝 ارسال بنر", callback_data=f"stp-{id}"),InlineKeyboardButton("📑 فوروارد بنر", callback_data=f"ftp-{id}")]
                ,
                [InlineKeyboardButton("برگشت", callback_data=f"manageall")]
        ])
        
    def joiner_type(id):
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("♻️ گروه های پیشفرض (رندوم)", callback_data=f"opjo-all-{id}")]
                ,
                [InlineKeyboardButton("💰گروه های ارز،بورس،فارکس", callback_data=f"opjo-arz-{id}")]
                ,
                [InlineKeyboardButton("👩‍❤️‍👨 دوست یابی ، چت آزاد ، تبلیغ آزاد", callback_data=f"opjo-azad-{id}")]
                ,
                [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
        ])
        # @DevOscar اوپن شد توسط
    def get_address(id):
        wallet = query(f"SELECT * FROM `wallet` WHERE id={id}")
        if len(wallet) == 0:
            full_node = 'https://api.trongrid.io'
            solidity_node = 'https://api.trongrid.io'
            event_server = 'https://api.trongrid.io'

            tron = Tron(full_node=full_node,
                    solidity_node=solidity_node,
                    event_server=event_server)

            account = tron.create_account
            wallet = account.address.base58
            key = account.private_key
            update_database(f"INSERT INTO `wallet` VALUES('{id}', '{wallet}', '{key}')")
            return address
        else:
            return wallet[0][1]
            
    def get_price_trx():
        result = requests.get('https://api.nobitex.ir/v2/orderbook/TRXIRT').json()['bids'][0][0]
        result = int(result)/10
        return int(result)
        
    def get_balance_trx(wallet):
        url = f"https://api.trongrid.io/v1/accounts/{wallet}"
        response = requests.get(url)
        data = response.json()
        return data["balance"] / 1000000

    async def check_memeber_joined(chatid,userid):
        ti = get_bots(userid)
        if not ti.isnumeric() or int(ti) <= int(t.time()):
            try:
                try:
                    update_database(f"UPDATE data SET time={int(t.time())} WHERE id={userid}")
                except:
                    pass
                result = (await app.get_chat_member(chatid, userid)).status in [enums.ChatMemberStatus.OWNER,enums.ChatMemberStatus.MEMBER,enums.ChatMemberStatus.ADMINISTRATOR]
                update_database(f"UPDATE data SET `bots`={int(t.time())+600} WHERE id={userid}")
                return result
            except:
                return False
        else:
            return True

    @app.on_message(filters.private & filters.text,group=1)
    async def bot(client,message):
        global mycu,mydb
        try:
            if message.text == '/reload' and message.from_user.id in admin:
                await message.reply('reloaded')
                reloadbot()
            
            if message.text == '/start':
                i = query(f'SELECT * FROM data WHERE id={message.chat.id}')
                if len(i) == 0:
                    new_user(message.chat.id)
                update_database(f"UPDATE `data` SET `step` = 'no' WHERE `id`={message.chat.id}")
                await message.reply("<b>سلام کاربر گرامی، به ربات آقای تبچی، پیشرفته ترین و قدرتمند ترین سیستم ساخت ربات تبلیغگر خوش آمدید.</b>\n\nربات های تبلیغاتی خود را با استفاده از سیستم  قدرتمند و هوشمند آقای تبچی ساخته و مدیریت نمایید و بیشترین جذب و بازدهی را کسب کنید.\n\n<b>امکانات ربات های ساخته شده با آقای تبچی :\n\n1 - بدون یک ثانیه هنگی و خاموش\n2 - عدم هنگی\n3 - عضویت در 500 سوپرگروه و انجام تبلیغات\n4 - امکان مدیریت ربات در از طریق ربات آقای تبچی\n5 - دارای امکان عضویت خودکار در سوپرگروه ها و گروه ها\n6 - مناسب برای انجام افزایش بازدهی کانال و فروش محصولات\n7 - دارای ارسال و فوروارد هوشمند ، انجام عملیات ها به صورت تکی و کلی حتی در صورت محدود شدن اکانت\n8 - امکان انتقال و یا فروش ربات به افراد دیگر\n9 - امکان مشاهده آمار ربات به صورت تکی و کلی\n10 - امکان افزودن کاربران جذب شده در ربات به گروه ها\n</b>\n\n<b>برای شروع بر روی دکمه '⚙️ ساخت ربات' کلیک نمایید.</b>", reply_markup=menu, parse_mode=enums.ParseMode.HTML)
            
            elif re.match('/start (\d+)', message.text):
                ids = re.findall('/start (\d+)', message.text)[0]
                if ids.isnumeric() == True and len(ids) < 13 and len(ids) > 1 and int(ids) != int(message.from_user.id):
                    i = query(f'SELECT * FROM data WHERE id={message.chat.id}')
                    if len(i) == 0:
                        new_user(message.chat.id, f'coin-{ids}')
                try:
                    await message.reply("<b>سلام کاربر گرامی، به ربات آقای تبچی، پیشرفته ترین و قدرتمند ترین سیستم ساخت ربات تبلیغگر خوش آمدید.</b>\n\nربات های تبلیغاتی خود را با استفاده از سیستم  قدرتمند و هوشمند آقای تبچی ساخته و مدیریت نمایید و بیشترین جذب و بازدهی را کسب کنید.\n\n<b>امکانات ربات های ساخته شده با آقای تبچی :\n\n1 - بدون یک ثانیه هنگی و خاموش\n2 - عدم مسدود شدن اکانت توسط تلگرام\n3 - عضویت در 500 سوپرگروه و انجام تبلیغات\n4 - امکان مدیریت ربات در از طریق ربات آقای تبچی\n5 - دارای امکان عضویت خودکار در سوپرگروه ها و گروه ها\n6 - مناسب برای انجام افزایش بازدهی کانال و فروش محصولات\n7 - دارای ارسال و فوروارد هوشمند ، انجام عملیات ها به صورت تکی و کلی حتی در صورت محدود شدن اکانت\n8 - امکان انتقال و یا فروش ربات به افراد دیگر\n9 - امکان مشاهده آمار ربات به صورت تکی و کلی\n10 - امکان افزودن کاربران جذب شده در ربات به گروه ها\n</b>\n\n<b>برای شروع بر روی دکمه '⚙️ ساخت ربات' کلیک نمایید.</b>",reply_markup=menu, parse_mode=enums.ParseMode.HTML)
                except:
                    pass
            
            elif await check_memeber_joined('@MrTabchi2', message.from_user.id) == False:
                try:
                    await message.reply('☑️ جهت کار با تبچی نیاز هست که عضو کانال پشتیبانی بشی!\n@MrTabchi2\n    🔹 سپس ربات را استارت کنید : /start', parse_mode=enums.ParseMode.HTML)
                except:
                    pass
                return
            
            elif "coin-" in get_invi(message.from_user.id):
                id = get_invi(message.from_user.id).split('-')[1]
                exit = query(f"SELECT * FROM data WHERE id={id}")
                if len(exit) > 0:
                    UserData = exit
                    balance = int(UserData[0][9])
                    balance += 300
                    update_database(f"UPDATE data SET balance={balance} WHERE id={id}")
                    try:
                        await client.send_message(int(id), 'شما یک کاربر دعوت کردید و 300 تومان موجودی گرفتید.')
                    except:
                        pass
                update_database(f"UPDATE data SET invi='0' WHERE id={message.from_user.id}")
            #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            if message.text == '↪️ برگشت':
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                await message.reply('<b>👈🏻 به منوی اصلی برگشتید.</b>', reply_markup=menu, parse_mode=enums.ParseMode.HTML, quote=True)
            
            elif message.text == '☎️ پشتیبانی': 
                await message.reply('🤔 <b>راهنمای ارتباط با بخش پشتیبانی آقای تبچی : </b>\n\n درصورتی که میخواهید مشکلی در ربات یا سیستم پرداخت گزارش کنید حتما یک اسکرین شات از #مشکل همراه با توضیحات ارسال کنید \nاز سلام و احوال پرسی با پشتیبان خودداری کنید و مشکل خود را مطرح کنید.\nبرای پیگیری و اعتراض به مسدودی در ربات حتما دلیل #مسدود شدن خود را ذکر کنید.\n#آموزش کامل استفاده از ربات در بخش آموزش ساخت ربات قرار داده شده است ، سوالاتی که در بخش راهنمای ربات وجود دارند پاسخ داده نخواهند شد.\nقبل از ارتباط با بخش پشتیبانی حتما موارد بالا را مطالعه کنید در غیر این صورت پاسخی از طرف پشتیبان دریافت نخواهید کرد.\n \n<b>آیدی تلگرام پشتیبانی @Advertisingadmin3 است.\nافرادی که ریپورت هستند از @Advertisingadmin3 استفاده نمایند.\nآیدی تلگرام ربات تبچی ساز @MrTabchi2bot است.\nآیدی تلگرام کانال اخبار و ترفند های آقای تبچی  @MrTabchi2 است.</b>\n\n<b>پس از ارسال پیام خود منتظرباشید تا پشتیبان پاسخ شما را بدهد.</b>', reply_markup=menu, parse_mode=enums.ParseMode.HTML, quote=True)
                
            elif message.text == '🛒 خرید اکانت':
                i = query(f"SELECT * FROM bots WHERE admin='00000000'")
                if len(i) > 0:
                    keyboard = []
                    for bot in i:
                        id = bot[0]
                        name = bot[4]
                        name = name.replace(name[6]+name[7]+name[8],'***')
                        keyboard.append([InlineKeyboardButton(f"{name}", callback_data=f"ifk-{id}"),InlineKeyboardButton("اطلاعات اکانت", callback_data=f"ifk-{id}"),InlineKeyboardButton("خرید اکانت", callback_data=f"buk-{id}")])
                    inikey = InlineKeyboardMarkup(keyboard)
                    await message.reply('<b>لیست اکانت های موجود :</b>', reply_markup=inikey, parse_mode=enums.ParseMode.HTML, quote=True)
                else:
                    await message.reply('❌ <b>هیچ اکانتی برای خرید موجود نیست.</b>', reply_markup=menu, parse_mode=enums.ParseMode.HTML, quote=True)
                    
            elif message.text == '🔐 حساب کاربری':
                UserData = query(f'SELECT * FROM data WHERE id={message.chat.id}')
                Id = UserData[0][0]
                Type = UserData[0][2]
                phone = UserData[0][6]
                coun = UserData[0][7]
                account = UserData[0][8]
                balance = UserData[0][9]
                timesh = int(t.time())
                botdata = query(f'SELECT * FROM bots WHERE admin={message.chat.id}')
                scoun = len(botdata)
                timeof = int(t.time())
                if account != 'unlimited' and account != 'free':
                    account = int(account)
                    day1 = 2592000 - (timeof - account)
                    day = int(day1/60/60/24)
                    if day <= 0:
                        update_database(f"UPDATE data SET type='free' WHERE id={message.chat.id}")
                        update_database(f"UPDATE data SET account='0' WHERE id={message.chat.id}")
                        Type = 'free'
                        day = 'نامحدود'
                    else:
                        day = str(day)+' <b>روز</b>'
                else:
                    day = 'نامحدود'
                Type = Type.replace('free','رایگان')
                Type = Type.replace('gold','طلایی')
                if phone == '0' or phone == 'no' or phone == '+no':
                    phone = phone.replace('0','ثبت نشده')
                    phone = phone.replace('+no','ثبت نشده')
                    phone = phone.replace('no','ثبت نشده')
                coun = float(coun)
                if coun < 0:
                    coun = int(coun * -1)+3
                else:
                    coun = int(3 - coun)
                balance = number_format(balance)
                manageacco = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("📞 تایید شماره", callback_data="donenum"),InlineKeyboardButton("↗️ انتقال موجودی", callback_data="movebal")]
                    ])
                await message.reply(f'<b>شناسه عددی حساب کاربری : </b><code>{Id}</code>\n<b>شماره تماس حساب کاربری :</b> <code>{phone}</code>\n\n<b>نوع حساب کاربری :</b> {Type}\n<b>مهلت حساب کاربری :</b> {day}\n<b>موجودی حساب کاربری :</b> {balance} <b>تومان</b>\n\n<b>تعداد ربات ها :</b> {scoun} <b>عدد</b>\n<b>تعداد فرصت ساخت باقی مانده :</b> {coun}', parse_mode=enums.ParseMode.HTML, reply_markup=menu, quote=True)
            
            elif message.text == '⚖️ قوانین':
                await message.reply('⚖️ استفاده از ربات آقای تبچی تبچی به منزله‌ی قبول شرایط و قوانین زیر است:\n\n• ساخت ربات تبلیغ گر در آقای تبچی تبچی به معنا قبول کردن تمامی شرایط دز ان بخش میباشد!\n\n• مسئولیت حذف شدن اکانت تلگرامی توسط تلگرام در صورت اسپم بیش از حد بر عهده شما میباشد!\n\n• خرید و فروش موجودی و تبلیغ گر های ساخته شده توسط ربات برای کابران بلامانع است اما مجموعه‌ی آقای تبچی تبچی هیچ گونه تعهدی برای پیگیری تخلفات مربوطه ندارد و فقط در صورت صلاح‌دید پیگیری انجام میشود.\n\n• اگر منبع سکه های بدست آمده از طریق باگ ربات و یا خرید با کارت‌های هک شده باشد حساب هر دو طرف بدون تذکر مسدود دائم خواهد شد\n\n• دریافت لینک پرداخت از ربات و ارسال آن به سایر افراد جهت واریز وجه تخلف محسوب میشود و درصورت مشاهده حساب کاربر مسدود دائم خواهد شد.\n\n• مجموعه آقای تبچی تبچی درصورتی که به پرداخت‌های کاربر (و یا انتقال‌های درون ربات) مشکوک شود این حق را دارد که حساب وی را موقتا مسدود کند و از کاربر مربوطه تقاضای احراز هویت و مدارک لازم نماید.\n\n• تمامی مبالغ پرداختی کاربران که دارای شرایط زیر باشد قابل عودت است:\n۱- دلیل قانع کننده‌ای برای تقاضای عودت وجه باشد.\n۲- پرداخت مستقیما به مجموعه‌ی آقای تبچی بوده باشد (شامل درگاه های زرین‌پال و نکست‌پی ربات و هر شماره حسابی که از پشتیبانی ربات دریافت شده است)\n۳- مبلغ فقط به همان حسابی که پرداخت با آن انجام شده است قابل عودت است.\n۴- حساب بنام خود شخص باشد و در صورت نیاز بتواند احراز هویت نماید.\n۵- درصورتی که درخواست عودت وجه از طرف کاربر باشد کارمزدهای مربوطه از مبلغ کسر خواهد شد.\n\nآخرین ویرایش قوانین: 29 اردیبهشت ماه 1400', reply_markup=BackKey)

            elif message.text == '🌐 بازاریابی (موجودی رایگان)':
                msi = (await client.send_photo(message.chat.id, "https://t.me/HolyMory/22",caption=f'🏆 آقای تبچی\n\n👈 بزرگ ترین سامانه ساخت ربات تبلیغاتی در تلگرام\n کاملا پیشرفته و حرفه ای !\n مدیریت پیشرفته تبلیغات ها\n بدون خاموشی\n پرسرعت\n عضویت کاملا خودکار در گروه ها\n دریافت امار ربات ها به صورتی تکی و گروهی\nپشتیبانی تبلیغات تا 50000 گروه و 100,000 کاربر\n\n✅ همین حالا عضو آقای تبچی شوید و ربات تبلیغاتی خود را بسازید\nt.me/MrTabchi2bot?start={message.chat.id}', reply_to_message_id=message.id)).id
                await message.reply('با دعوت هر کاربر با بنر بالا 300 تومان موجودی دریافت میکنید!\n⚠️ هر کاربر که با لینک شما عضو ربات میشود میبایست در کانال تبچی ساز عضو شده سپس یک بار بر روی یک دکمه از ربات کلیک نماید تا موجودی به شما تعلق بگیرد.', reply_to_message_id = msi, reply_markup=menu)

            elif message.text == '🛍 فروشگاه':
                await message.reply('<b>🛒 به منوی فروشگاه وارد شدید، یک گزینه را انتخاب نمایید :</b>', reply_markup=shopkey, parse_mode=enums.ParseMode.HTML, quote=True)
            
            elif message.text == '📑 راهنما':
                await message.reply('<b>📚راهنمای کار با ربات آقای تبچی،با کلیک بر روی هر دکمه میتوانید توضیحات کامل را مشاهده کنید :</b>', reply_markup=helpkeyb(message.from_user.id), quote=True)
            
            elif message.text == '⚙️ ساخت ربات':
                UserData = query(f'SELECT * FROM data WHERE id={message.chat.id}')
                Type = UserData[0][2]
                coun = UserData[0][7]
                account = UserData[0][8]
                if Type == 'gold' and account != 'free' and account != 'unlimited' and int(t.time()) - int(account) < 2592000:
                    if int(coun) < 3:
                        update_database(f"UPDATE data SET step='sendnumber' WHERE id={message.chat.id}")
                        await message.reply('<b>☎️ لطفا شماره اکانت خود را همراه با کد کشور ارسال نمایید :</b>', parse_mode=enums.ParseMode.HTML, reply_markup=BackKey, quote=True)
                    else:
                        await message.reply('🧐 شما به محدودیت ساخت رسیدید!', reply_markup=menu)
                else:
                    await message.reply("🛑 کاربر گرامی؛ جهت ساخت ربات تبلیغ گر نیاز به حساب طلایی دارید\n👇🏻 جهت تهیه حساب طلایی از دستورالعمل زیر استفاده نمایید:\n\n👈🏻 ابتدا به بخش فروشگاه رفته روی دکمه افزایش موجودی کلیک نمایید و حساب خود را به مبلغ دلخواه شارژ نمایید.\n-\n👈🏻 پس از رسیدن موجودی حساب به مقدار لازم به بخش 'فروشگاه' مراجعه نمایید سپس بر روی دکمه ی 'خرید حساب' کلیک نمایید\n-\n👈🏻 چنانچه موجودی شما برای ارتقای حساب کافی بود نوع حساب شما به 'طلایی' تغییر پیدا خواهد کرد و 2 فرصت ساخت ربات تبلیغ گر بدست می آورید", reply_markup=menu)

            elif message.text == '🤖 ربات های من':
                botdata = query(f'SELECT * FROM bots WHERE admin={message.chat.id}')
                if len(botdata) > 0:
                    keyboard = []
                    for bot in botdata:
                        id = bot[0]
                        name = unquote(bot[5])
                        keyboard.append([InlineKeyboardButton(f"{name}", callback_data=f"bots-{id}"),InlineKeyboardButton("🔐  کد ورود", callback_data=f"lco-{id}"),InlineKeyboardButton("❌ حذف ربات", callback_data=f"delete-{id}")])
                    if len(botdata) >= 2:
                        keyboard.append([InlineKeyboardButton("👮🏻‍♂️ مدیریت کلی", callback_data="manageall")])
                    inikey = InlineKeyboardMarkup(keyboard)
                    await message.reply('<b>لیست ربات های ساخته شده شما :</b>', reply_markup=inikey, parse_mode=enums.ParseMode.HTML, quote=True)
                    keyboard = []
                else:
                    await message.reply('❌ <b>شما تاکنون رباتی در آقای تبچی نساخته اید.</b>', parse_mode=enums.ParseMode.HTML, reply_markup=menu, quote=True)
            
            elif message.text == '/panel' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                await message.reply('به پنل مدیریت خوش آمدید',reply_markup=panel) 
            #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif message.text == 'آمار ربات' and message.from_user.id in admin:
                users = len(query(f'SELECT * FROM data'))
                hashs = len(query(f'SELECT * FROM `hash`'))
                botes = len(query(f'SELECT * FROM `bots`'))
                joineron = len(query(f"SELECT * FROM `bots` WHERE `joiner` = '%E2%9C%85' AND `pyro` != 'no'"))
                tim = int(t.time())
                timesh = tim - 2592000
                golds = len(query(f"SELECT * FROM `data` WHERE `type` = 'gold' and `account` > {timesh}"))
                tabss = len(query(f"SELECT * FROM `bots` WHERE `joiner` = '%E2%9C%85' AND `limit` < {tim} AND `pyro` != 'no'"))
                forauto = len(query(f"SELECT * FROM `ads` WHERE `time` < {tim}"))
                await message.reply(f'کاربران ربات : {users}\nکاربران طلایی : {golds}\nتعداد تبچی : {botes}\nتعداد تبچی های با عضویت خودکار : {joineron}\nتعداد تبچی های در صف عضویت : {tabss}\nتعداد تبچی های در صف ارسال خودکار : {forauto}\nتعداد لینک های ذخیره شده : {hashs}',reply_markup=panel) 
            
            elif message.text == 'حساب رایگان' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='freeac' WHERE id={message.chat.id}")
                await message.reply(f'آیدی عددی کاربر را ارسال نمایید :', reply_markup=panelback)
            
            elif message.text == 'حساب طلایی' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='goldac' WHERE id={message.chat.id}")
                await message.reply(f'آیدی عددی کاربر را ارسال نمایید :', reply_markup=panelback)
            
            elif message.text == 'تمدید حساب' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='tamdidac' WHERE id={message.chat.id}")
                await message.reply(f'لطفا ایدی عددی کاربر را در خط اول و تعداد روز هایی که میخواهید حساب را تمدید نمایید در خط دوم وارد نمایید به صورت زیر\n\n856460477\n30', reply_markup=panelback)

            elif message.text == 'تغییر موجودی' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='cmoj' WHERE id={message.chat.id}")
                await message.reply(f'لطفا ایدی عددی کاربر را در خط اول و مقدار موجودی که میخواهید به کاربر اضافه یا کسر شود را در خط دوم وارد نمایید به صورت زیر\n\n856460477\n-3000', reply_markup=panelback)
            
            elif message.text == 'تغییر فرصت' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='fyt' WHERE id={message.chat.id}")
                await message.reply(f'لطفا ایدی عددی کاربر را در خط اول و مقدار فرصتی که میخواهید به کاربر اضافه یا کسر شود را در خط دوم وارد نمایید به صورت زیر\n\n856460477\n-3', reply_markup=panelback)
            
            elif message.text == 'ارسال' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='oip' WHERE id={message.chat.id}")
                await message.reply(f'لطفا متن خود را جهت ارسال بفرستید :', reply_markup=panelback)
            
            elif message.text == 'فوروارد' and message.from_user.id in admin:
                update_database(f"UPDATE data SET step='frt' WHERE id={message.chat.id}")
                await message.reply(f'لطفا متن خود را جهت فوروارد بفرستید :', reply_markup=panelback)
             
            elif get_step(message.chat.id) == 'oip':
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                datas = query(f"SELECT * FROM `data`")
                for i in datas:
                    try:
                        await client.send_message(i[0], message.text, parse_mode=enums.ParseMode.HTML, reply_markup=menu)
                    except Exception as e:
                        if "[420 FLOOD_WAIT_X]" in str(e):
                            e = str(e)
                            flood = e.split(' seconds')[0].split('of ')[1]
                            await asyncio.sleep(int(flood))
                            continue
                        else:
                            continue
                    except:
                        continue
                await message.reply('عملیات انجام شد', reply_markup=panel)
            
            elif get_step(message.chat.id) == 'cmoj':
                spl = message.text.split('\n')
                id = spl[0]
                day = spl[1]
                if id.isnumeric() == True and (day.isnumeric() == True or int(day) < 0):
                    person = query(f"SELECT * FROM `data` WHERE `id` = {id}")
                    if len(person) > 0:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        newb = int(person[0][9]) + int(day)
                        update_database(f"UPDATE data SET balance={newb} WHERE id={id}")
                        await client.send_message(id, f'{day} تومان موجودی به حساب شما افزوده شد')
                        await message.reply('عملیات انجام شد', reply_markup=panel)
                    else:
                        await message.reply('کاربر عضو ربات نمیباشد!')
                else:
                    await message.reply('لطفا یک عدد ارسال کنید')
            # Alfred_s1
            elif get_step(message.chat.id) == 'fyt':
                spl = message.text.split('\n')
                id = spl[0]
                day = spl[1]
                if id.isnumeric() == True and (day.isnumeric() == True or int(day) < 0):
                    person = query(f"SELECT * FROM `data` WHERE `id` = {id}")
                    if len(person) > 0:
                        update_database(
                            f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        newb = int(person[0][7]) - int(day)
                        update_database(
                            f"UPDATE data SET coun={newb} WHERE id={id}")
                        await client.send_message(id, f'{day} فرصت ساخت به حساب شما افزوده شد')
                        await message.reply('عملیات انجام شد', reply_markup=panel)
                    else:
                        await message.reply('کاربر عضو ربات نمیباشد!')
                else:
                    await message.reply('لطفا یک عدد ارسال کنید')
            
            elif get_step(message.chat.id) == 'tamdidac':
                spl = message.text.split('\n')
                id = spl[0]
                day = spl[1]
                if id.isnumeric() == True and day.isnumeric() == True:
                    person = query(f"SELECT * FROM `data` WHERE `id` = {id}")
                    if len(person) > 0:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        update_database(f"UPDATE data SET type='gold' WHERE id={id}")
                        acc = person[0][8]
                        if acc.isnumeric() != True or int(acc) == 0:
                            if int(day) > 30:
                                tim = int(t.time()) + ((int(day) - 30) * 24 * 60 * 60)
                            else:
                                tim = int(t.time()) + ((int(day) - 30) * 24 * 60 * 60)
                        else:
                            tim = int(acc) + (int(day) * 24 * 60 * 60)
                        update_database(f"UPDATE data SET account={tim} WHERE id={id}")
                        try:
                            await client.send_message(id, f'حساب شما {day} روز تمدید شد')
                        except:
                            pass
                        await message.reply('عملیات انجام شد', reply_markup=panel)
                    else:
                        await message.reply('کاربر عضو ربات نمیباشد!')
                else:
                    await message.reply('لطفا یک عدد ارسال کنید')
            
            elif get_step(message.chat.id) == 'freeac':
                if message.text.isnumeric() == True:
                    person = len(query(
                        f"SELECT * FROM `data` WHERE `id` = {message.text}"))
                    if person > 0:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        update_database(f"UPDATE data SET type='free' WHERE id={message.text}")
                        update_database(
                            f"UPDATE data SET account='0' WHERE id={message.text}")
                        await client.send_message(message.text, 'حساب شما رایگان شد')
                        await message.reply('عملیات انجام شد', reply_markup=panel)
                    else:
                        await message.reply('کاربر عضو ربات نمیباشد!')
                else:
                    await message.reply('لطفا یک عدد ارسال کنید')

            
            elif get_step(message.chat.id) == 'goldac':
                if message.text.isnumeric() == True:
                    person = len(query(f"SELECT * FROM `data` WHERE `id` = {message.text}"))
                    if person > 0:
                        update_database(
                            f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        update_database(
                            f"UPDATE data SET type='gold' WHERE id={message.text}")
                        tim = int(t.time())
                        update_database(
                            f"UPDATE data SET account={tim} WHERE id={message.text}")
                        await client.send_message(message.text, 'حساب شما به حساب طلایی با 30 روز مهلت تغییر یافت')
                        await client.send_message(message.chat.id, 'عملیات انجامg شد', reply_markup=panel)
                    else:
                        await client.send_message(message.chat.id, 'کاربر عضو ربات نمیباشد!')
                else:
                    await client.send_message(message.chat.id, 'لطفا یک عدد ارسال کنید')
            #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif get_step(message.chat.id) == 'sendnumber':
                newid = get_id()
                phone = message.text.replace('+','').replace(' ','').replace(')','').replace('(','').replace('-','')
                p = '+'+str(phone)
                botdata = query(f"SELECT * FROM bots WHERE phone='{p}'")
                if len(botdata) == 0 or message.from_user.id in admin:
                    if phone.isnumeric() == True:
                        codekey = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("1️⃣", callback_data="an-1"),InlineKeyboardButton("2️⃣", callback_data="an-2"),InlineKeyboardButton("3️⃣", callback_data="an-3")]
                                ,
                                [InlineKeyboardButton("4️⃣", callback_data="an-4"),InlineKeyboardButton("5️⃣", callback_data="an-5"),InlineKeyboardButton("6️⃣", callback_data="an-6")]
                                ,
                                [InlineKeyboardButton("7️⃣", callback_data="an-7"),InlineKeyboardButton("8️⃣", callback_data="an-8"),InlineKeyboardButton("9️⃣", callback_data="an-9")]
                                ,
                                [InlineKeyboardButton("✏️", callback_data="delen"),InlineKeyboardButton("0️⃣", callback_data="an-0"),InlineKeyboardButton("✅", callback_data=f"con-{newid}")]
                                ,
                                [InlineKeyboardButton("🗑 لغو عملیات", callback_data=f"cal-{newid}")]
                            ])
                        try:
                            msgsent = await message.reply('<b>🔁 درحال اتصال به سرور تلگرام .</b>', quote=True)
                            await asyncio.sleep(1)
                            await msgsent.edit('<b>🔁 درحال اتصال به سرور تلگرام ..</b>')
                            await asyncio.sleep(1)
                            await msgsent.edit('<b>🔁 درحال اتصال به سرور تلگرام ...</b>')
                            await asyncio.sleep(1)
                            await msgsent.edit('<b>✅ اتصال با موفقیت انجام شد. در حال ارسال کد ورود ...<b>')
                            await asyncio.sleep(1)
                            await msgsent.delete()
                            uniqueid = randint(0,len(device_model)-1)
                            apps[newid] = Client(name=str(newid),in_memory=True,api_id=int(app_id),api_hash=app_hash,no_updates = True,system_version = system_version[uniqueid], app_version = app_version[uniqueid], device_model = device_model[uniqueid], lang_code = lang_code[randint(0,len(lang_code)-1)])
                            await apps[newid].connect()
                            phhash = await apps[newid].send_code(p)
                            hashs = phhash.phone_code_hash
                            newid = str(newid)
                            update_database(f"UPDATE data SET step='sendcode-{newid}-{hashs}-{p}' WHERE id={message.chat.id}")
                            if codelogin.get(message.from_user.id) != None:
                                del codelogin[message.from_user.id]
                            await message.reply('<b>🌐 کد 5 رقمی دریافت شده را با کیبورد زیر وارد نمایید :</b>', reply_markup=codekey, quote=True)
                        except errors.PhoneNumberInvalid:
                            await message.reply('شماره اکانت اشتباه میباشد.')
                        except errors.PhoneNumberBanned:
                            await message.reply('اکانت شما مسدود شده است')
                        except errors.FloodWait:
                            await message.reply('این اکانت از سمت تلگرام محدود شده است')
                        except errors.ApiIdPublishedFlood:
                            await message.reply('خطا در ارسال کد مجددا تلاش کنید.')
                        except Exception as e:
                            await apps[newid].disconnect()
                            x = traceback.format_exc()
                            await client.send_message(856460477,f'Soomlething went wrongj :(\nerror : `{x}`')
                    else:
                        await message.reply('😒 شماره رو درست ارسال کن!')
                else:
                    await message.reply('⚠️این شماره قبلا در دیتابیس ثبت شده است و امکان ساخت ربات مجدد با ان وجود ندارد!')
            # @DevOscar اوپن شد توسط
            elif get_step(message.chat.id).split('-')[0] == '2fa':
                s = get_step(message.chat.id).split('-')
                newid = s[1]
                phone = s[2]
                try:
                    newid = int(newid)
                    await apps[newid].check_password(str(message.text))
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    strg = await apps[newid].export_session_string()
                    await apps[newid].disconnect()
                    join_num = [0,500,1000,1500,2000]
                    uniqueid = randint(0,len(join_num)-1)
                    num = join_num[uniqueid]
                    update_database(f"INSERT INTO bots VALUES('{newid}', 'no', '0', 'no', '{phone}', 'Tabchi', 'no', 'no', 'no', 'no', 'no', '{message.chat.id}', 'no','0', '0', '%E2%9D%8C', '0', 'no','{strg}','%E2%9D%8C','0','all')")
                    coun = get_data(message.chat.id)[7]
                    coun = int(coun)
                    coun += 1
                    update_database(f"UPDATE data SET coun={coun} WHERE id={message.chat.id}")
                    await message.reply('✅ ساخت ربات شما با موفقیت انجام شد. هم اکنون میتوانید از بخش 🤖 ربات های من اقدام به مدیریت ربات خود نمایید.', reply_markup=menu)
                except errors.PasswordHashInvalid:
                    await message.reply('تایید دو مرحله ای اشتباه است لطفا پسورد صحیح را ارسال کنید :')
                except errors.PhonePasswordFlood:
                    try:
                        await apps[newid].disconnect()
                    except:
                        pass
                    await message.reply('اکانت شما به تلاش زیاد برای ورود با پسورد تایید دو مرحله ای اشتباه محدود شده است. لطفا بعد از چند ساعت دوباره تلاش کنید.', reply_markup=menu)
                except Exception as e:
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    try:
                        await apps[newid].disconnect()
                    except:
                        pass
                    await message.reply(str(e))
            
            elif get_step(message.chat.id).split('-')[0] == 'addcon':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                con = step[2]
                update_database(f"UPDATE `data` SET step='no' WHERE id={message.chat.id}")
                if con.isnumeric():
                    con = int(con)
                mybot = await check_id(id, message)
                try:
                    await mybot.add_contact(con, message.text)
                    await mybot.disconnect()
                    await message.reply('عملیات انجام شد', quote=True, reply_markup=back_key(id))
                except errors.UsernameNotOccupied:
                    await message.reply('نام کاربری ارسالی اشتباه میباشد لطفا دوباره تلاش کنید .', quote=True, reply_markup=back_key(id))
                except errors.PeerIdInvalid:
                    await message.reply('شناسه کاربری ارسالی اشتباه میباشد لطفا دوباره تلاش کنید .', quote=True, reply_markup=back_key(id))
                except:
                    pass
            
            elif get_step(message.chat.id).split('-')[0] == 'addcont':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                update_database(f"UPDATE `data` SET step='addcon-{id}-{message.text}' WHERE id={message.chat.id}")
                await message.reply("نام مخاطب را وارد نمایید :", quote=True, reply_markup=back_key(id))
            
            elif get_step(message.chat.id).split('-')[0] == 'name':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                mybot = await check_id_message(id, message)
                await mybot.update_profile(first_name=f"{message.text}")
                await mybot.disconnect()
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                name = quote(message.text)
                update_database(f"UPDATE bots SET name='{name}' WHERE id={id}")
                await message.reply("😘 خب نام اکانت عوض شد!", reply_markup=back_key(id))
            
            elif get_step(message.chat.id).split('-')[0] == 'add':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                mybot = await check_id_message(id, message)
                txt = "عملیات انجام شد!"
                if not "joinchat" in message.text and not "+" in message.text and "https://t.me/" in message.text:
                    message.text = message.text.replace('https://t.me/','@')
                try:
                    chats = await mybot.get_chat(message.text)
                except:
                    chats = []
                if hasattr(chats,'permissions'):
                    users = mybot.get_dialogs()
                    async for it in users:
                        try:
                            if it.chat.type == enums.ChatType.PRIVATE:
                                await mybot.add_chat_members(chats.id, it.chat.id)
                        except errors.ChatWriteForbidden:
                            txt = "دسترسی ادد کاربر در گروه به ربات داده نشده"
                            break
                        except errors.FloodWait as e:
                            await mybot.disconnect()
                            flood = str(e.value)
                            txt = f"‼️ تبچی شما {flood} ثانیه محدود شده است پس از رفع محدودیت عملیات به صورت خودکار ادامه خواهد یافت."
                            tfo = int(t.time()) + int(flood)
                            floodkey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")]])
                            await msgsent.edit(txt, reply_markup=floodkey)
                            await asyncio.sleep(int(flood))
                            await msgsent.edit('درحال انجام عملیات')
                            await mybot.connect()
                            txt = "عملیات انجام شد!"
                            continue
                        except errors.ChatAdminRequired:
                            txt = "ربات جهت ادد کاربر به گروه نیاز دارد که ادمین باشد و دسترسی افزودن عضو داشته باشد"
                            break
                        except errors.UsersTooMuch:
                            txt = "تعداد اعضای گروه یا کانال شما به حداکثر رسیده و امکان افزودن عضو جدید میسر نیست"
                            break
                        except errors.ChannelInvalid:
                            txt = "تبچی شما در گروه موردنظر عضو نمیباشد یا لینک ارسالی اشتباه است"
                            break
                        except:
                            continue
                else:
                    txt = "تبچی شما در گروه موردنظر عضو نمیباشد یا لینک ارسالی اشتباه است"
                await mybot.disconnect()
                await msgsent.delete()
                await message.reply(txt, reply_markup=back_key(id))
            #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif get_step(message.chat.id).split('-')[0] == 'invite':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                if len(mybot.name) == 351:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                if len(mybot.name) == 356:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                await ConnectingBot(mybot)
                txt = "عملیات انجام شد!"
                try:
                    users = mybot.get_dialogs()
                except Exception as e:
                    users = []
                async for it in users:
                    try:
                        if it.chat.type == enums.ChatType.SUPERGROUP:
                            await mybot.add_chat_members(it.chat.id, message.text)
                    except Exception as e:
                        if "[403 USER_PRIVACY_RESTRICTED]" in str(e):
                            txt = "ادد این کاربر بسته است و امکان افزودن به گپ ها وجود ندارد!"
                            break
                        elif "USER_NOT_MUTUAL_CONTACT" in str(e):
                            txt = "این کاربر در لیست مخاطبین شما سیو نشده است!"
                            break
                        elif "USER_KICKED" in str(e):
                            continue
                        elif "CHAT_WRITE_FORBIDDEN" in str(e) or "USER_BANNED_IN_CHANNEL" in str(e):
                            continue
                        elif "USERNAME_NOT_OCCUPIED" in str(e) or "USER_ID_INVALID" in str(e):
                            txt = "یوزرنیم ارسالی اشتباه میباشد!"
                            break
                        elif "USERNAME_INVALID" in str(e):
                            txt = "یوزرنیم ارسالی اشتباه میباشد.لطفا یوزرنیم کاربر را با @ ارسال کنید."
                            break
                        elif "USER_CHANNELS_TOO_MUCH" in str(e):
                            txt = "این کاربر در گروه ها و کانال های زیادی عضو میباشد و امکان ادد به گروه جدید را ندارد!"
                            break
                        elif "[420 FLOOD_WAIT_X]" in str(e):
                            await DisConnectingBot(mybot)
                            e = str(e)
                            flood = e.split(' seconds')[0].split('of ')[1]
                            txt = f"‼️ تبچی شما {flood} ثانیه محدود شده است پس از رفع محدودیت عملیات به صورت خودکار ادامه خواهد یافت."
                            tfo = int(t.time()) + int(flood)
                            floodkey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")]])
                            await msgsent.edit(txt, reply_markup=floodkey)
                            await asyncio.sleep(int(flood))
                            await msgsent.edit('درحال انجام عملیات')
                            await ConnectingBot(mybot)
                            txt = "عملیات انجام شد!"
                            continue
                        elif "[400 PEER_FLOOD]" in str(e):
                            txt = "تبچی شما از سمت تلگرام محدود میباشد و امکان ادد کاربر را ندارد!"
                            break
                        else:
                            x = traceback.format_exc()
                            await client.send_message(856460477,f'Soomlething went wrongv :(\nerror : `{x}`')
                            break
                await DisConnectingBot(mybot)
                await msgsent.delete()
                await client.send_message(message.chat.id,txt, reply_markup=back_key(id))
            
            elif get_step(message.chat.id).split('-')[0] == 'enablepass':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                try:
                    mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                    if len(mybot.name) == 351:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                    if len(mybot.name) == 356:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                    await ConnectingBot(mybot)
                    await mybot.enable_cloud_password(password=message.text, hint="MrTabchi2bot")
                    await DisConnectingBot(mybot)
                    await message.reply('عملیات انجام شد.', reply_markup=back_key(id))
                except Exception as e:
                    await DisConnectingBot(mybot)
                    if "There is already" in str(e):
                        await message.reply('⚠️ بر روی این اکانت تایید دو مرحله ای از قبل فعال بوده است.', reply_markup=back_key(id))
                    else:
                        if "OSError: Connection lost" in str(e):
                            reloadbot()
                        await client.send_message(856460477,f'Soomlething went wrongb :(\nerror : `{e}`')
            
            elif get_step(message.chat.id).split('-')[0] == 'dpp':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                try:
                    mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                    if len(mybot.name) == 351:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                    if len(mybot.name) == 356:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                    await ConnectingBot(mybot)
                    await mybot.remove_cloud_password(password=message.text)
                    await DisConnectingBot(mybot)
                    await message.reply('عملیات انجام شد.', reply_markup=back_key(id))
                except Exception as e:
                    await DisConnectingBot(mybot)
                    if "PASSWORD_HASH_INVALID" in str(e):
                        await message.reply('پسورد ارسالی اشتباه میباشد.', reply_markup=back_key(id))
                    elif "no cloud password" in str(e):
                        await message.reply('⚠️ بر روی این اکانت تایید دو مرحله ای از قبل غیرفعال بوده است.', reply_markup=back_key(id))
                    else:
                        if "OSError: Connection lost" in str(e):
                            reloadbot()
                        await client.send_message(856460477,f'Soomlething went wrongb :(\nerror : `{e}`')
            
            elif get_step(message.chat.id).split('-')[0] == 'last':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                if len(mybot.name) == 351:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                if len(mybot.name) == 356:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                await ConnectingBot(mybot)
                await mybot.update_profile(last_name =f"{message.text}")
                await DisConnectingBot(mybot)
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                await message.reply("😊 خب نام خانوادگی اکانت با موفقیت عوض شد!", reply_markup=back_key(id))
            
            elif get_step(message.chat.id).split('-')[0] == 'shop':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                if str(message.text).isnumeric() == True:
                    if message.text != str(message.chat.id):
                        person = query(f"SELECT * FROM data WHERE id={message.text}")
                        first = query(f"SELECT * FROM data WHERE id={message.from_user.id}")
                        if len(person) > 0:
                            update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                            if first[0][2] == 'gold':
                                update_database(f"UPDATE data SET account={first[0][8]} WHERE id={message.text}")
                            update_database(f"UPDATE bots SET admin={message.text} WHERE id={id}")
                            update_database(f"UPDATE bots SET joiner='%E2%9D%8C' WHERE id={id}")
                            try:
                                await client.send_message(message.text,f'😅 کاربر [{message.chat.id}](tg://user?id={message.chat.id})  مورد نظر به شما تبچی اهدا کرد!\n♻️ از بخش 🤖 ربات های من میتوانید تبچی را مدیریت نمایید!', parse_mode="markdown")
                            except:
                                pass
                            await message.reply(f"♻️ عملیات با موفقیت انجام گردید!\n🥳 تبچی شما به [{message.text}](tg://user?id={message.text}) اهدا شد و از لیست ربات های شما پاک گردید!", parse_mode="markdown")
                        else:
                            await message.reply("🔻خطا !\n1️⃣ - کاربر مورد نظر عضو ربات نمیباشد!\n2️⃣ - ایدی عددی اشتباه ارسال شده!\n\n😊 لطفا پس از رفع خطا دوباره اقدام کنید", reply_markup=back_key(id))
                    else:
                        await message.reply("🔻خطا !\n1️⃣ - کاربر مورد نظر عضو ربات نمیباشد!\n2️⃣ - ایدی عددی اشتباه ارسال شده!\n\n😊 لطفا پس از رفع خطا دوباره اقدام کنید", reply_markup=back_key(id))
                else:
                    await message.reply("🔻خطا !\n1️⃣ - کاربر مورد نظر عضو ربات نمیباشد!\n2️⃣ - ایدی عددی اشتباه ارسال شده!\n\n😊 لطفا پس از رفع خطا دوباره اقدام کنید", reply_markup=back_key(id))
            
            elif get_step(message.chat.id).split('-')[0] == 'bio':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                try :
                    mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                    if len(mybot.name) == 351:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                    if len(mybot.name) == 356:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                    await ConnectingBot(mybot)
                    await mybot.update_profile(bio =f"{message.text}")
                    await DisConnectingBot(mybot)
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    await message.reply("😍 خب بیو با موفقیت تغییر کرد!", reply_markup=back_key(id))
                except Exception as e:
                    await DisConnectingBot(mybot)
                    if "[400 ABOUT_TOO_LONG]" in str(e):
                        await message.reply("خطا،متن ارسالی برای بیو بیشتر از 70 کاراکتر است لطفا متن کوتاه تر ارسال نمایید :", reply_markup=back_key(id))
                    else:
                        x = traceback.format_exc()
                        await client.send_message(856460477,f'Soomlething went wrongi :(\nerror : `{x}`')
            
            elif get_step(message.chat.id).split('-')[0] == 'username':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                try:
                    if "@" in message.text:
                        message.text = message.text.replace('@','')
                    mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                    if len(mybot.name) == 351:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                    if len(mybot.name) == 356:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                    await ConnectingBot(mybot)
                    await mybot.set_username(message.text)
                    await DisConnectingBot(mybot)
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    await message.reply("🥳 یوزرنیم به موفقیت عوض شد !", reply_markup=back_key(id))
                except Exception as e:
                    await DisConnectingBot(mybot)
                    if "[400 USERNAME_INVALID]" in str(e):
                        await message.reply("یوزرنیم موردنظر اشتباه میباشد یک یوزرنیم جدید ارسال نمایید!", reply_markup=back_key(id))
                    elif "[400 USERNAME_OCCUPIED]" in str(e):
                        await message.reply("یوزرنیم موردنظر قفل میباشد یک یوزرنیم جدید ارسال نمایید!", reply_markup=back_key(id))
                    else:
                        x = traceback.format_exc()
                        await client.send_message(856460477,f'Soomlething went wrongu :(\nerror : `{x}`')
            
            elif get_step(message.chat.id).split('-')[0] == 'left':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                if id != "all":
                    try:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                        link = message.text
                        if "joinchat" in message.text:
                            link = "https://t.me/joinchat/"+message.text.split('joinchat/')[1].split(' ')[0].split('\n')[0]
                        elif "t.me/+" in message.text:
                            link = "https://t.me/joinchat/"+message.text.split('t.me/+')[1].split(' ')[0].split('\n')[0]
                        elif "t.me/" in message.text:
                            link = "@"+message.text.split('t.me/')[1].split(' ')[0].split('\n')[0]
                        elif "@" in message.text:
                            link = "@"+message.text.split('@')[1].split(' ')[0].split('\n')[0]
                        else:
                            link = "@"+message.text
                        mybot = await check_id_message(id, message)
                        chat = await mybot.get_chat(link)
                        result = await mybot.leave_chat(chat.id)
                        linkkey = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                            ])
                        await msgsent.delete()
                        await client.send_message(message.chat.id,f"خروج از گروه یا کانال موردنظر باموفقیت انجام شد!", reply_markup=linkkey)
                        
                    except (errors.InviteHashExpired, errors.UsernameInvalid, errors.UsernameNotOccupied):
                        await msgsent.delete()
                        await message.reply("⚠️ کاربرگرامی لینک ارسال شده درست نمیباشد!\n🌟 لطفا لینک صحیح را ارسال نمایید!", reply_markup=back_key(id))
                    except Exception as e:
                        x = traceback.format_exc()
                        await client.send_message(856460477,f'Soomlething went wrongeyt :(\nerror : `{x}`')
                    await mybot.disconnect()
                else:
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    txt = 'عملیات انجام شد.'
                    msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                    botdata = query(f'SELECT * FROM bots WHERE admin={message.from_user.id} AND `pyro` != "no"')
                    if len(botdata) > 0:
                        for bot in botdata:
                            one_id = bot[0]
                            name = unquote(bot[5])
                            try:
                                mybot = await check_id_message(one_id, message)
                                link = message.text
                                if "joinchat" in message.text:
                                    link = "https://t.me/joinchat/"+message.text.split('joinchat/')[1].split(' ')[0].split('\n')[0]
                                elif "t.me/+" in message.text:
                                    link = "https://t.me/joinchat/"+message.text.split('t.me/+')[1].split(' ')[0].split('\n')[0]
                                elif "t.me/" in message.text:
                                    link = "@"+message.text.split('t.me/')[1].split(' ')[0].split('\n')[0]
                                elif "@" in message.text:
                                    link = "@"+message.text.split('@')[1].split(' ')[0].split('\n')[0]
                                else:
                                    link = "@"+message.text
                                chat = await mybot.get_chat(link)
                                result = await mybot.leave_chat(chat.id)
                                try:
                                    await mybot.disconnect()
                                except:
                                    pass
                            except (errors.UsernameInvalid, errors.UsernameNotOccupied):
                                txt = 'لینک ارسالی اشتباه میباشد.'
                                break
                            except AttributeError:
                                continue
                            except errors.UserNotParticipant:
                                continue
                            except Exception as e:
                                continue
                            try:
                                await mybot.disconnect()
                            except:
                                pass
                        await msgsent.delete()
                        await message.reply(txt, reply_markup=back_key(id))
                        
            elif get_step(message.chat.id).split('-')[0] == 'link':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                if id != "all":
                    try:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                        link = message.text
                        if "joinchat" in message.text:
                            link = "https://t.me/joinchat/"+message.text.split('joinchat/')[1].split(' ')[0].split('\n')[0]
                        elif "t.me/+" in message.text:
                            link = "https://t.me/joinchat/"+message.text.split('t.me/+')[1].split(' ')[0].split('\n')[0]
                        elif "t.me/" in message.text:
                            link = "@"+message.text.split('t.me/')[1].split(' ')[0].split('\n')[0]
                        elif "@" in message.text:
                            link = "@"+message.text.split('@')[1].split(' ')[0].split('\n')[0]
                        else:
                            link = "@"+message.text
                        mybot = await check_id_message(id, message)
                        result = await mybot.join_chat(link)
                        linkkey = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("➕ ارسال مجدد لینک", callback_data=f"link-{id}")]
                                ,
                                [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                            ])
                        await msgsent.delete()
                        await message.reply(f"🌟 عضویت در {result.title} باموفقیت انجام شد!", reply_markup=linkkey)
                        await mybot.disconnect()
                    except (errors.InviteHashExpired, errors.UserNotParticipant, errors.UsernameInvalid, errors.ChatInvalid, errors.UsernameNotOccupied, errors.ChannelInvalid):
                        await mybot.disconnect()
                        await message.reply("⚠️ کاربرگرامی لینک ارسال شده درست نمیباشد!\n🌟 لطفا لینک صحیح را ارسال نمایید!", reply_markup=back_key(id))
                    except errors.FloodWait as e:
                        try:
                            flood = str(e.value)
                            floods = int(t.time()) + int(flood)
                            update_database(f"UPDATE `bots` SET `limit`='{floods}' WHERE id={id}")
                            nameOfChat = await mybot.get_chat(link)
                            await mybot.disconnect()
                            nameOfChat = nameOfChat.title
                            codess = uuid.uuid4().hex.upper()[0:10]
                            join[codess] = True
                            tfo = int(t.time()) + int(flood)
                            JoinKey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")],[InlineKeyboardButton("لغو عملیات", callback_data=f"undo-{codess}")]])
                            await message.reply(f'⏱ عضویت در {nameOfChat} پس از {flood} ثانیه ...', parse_mode=enums.ParseMode.HTML,reply_markup=JoinKey)
                            linkkey = InlineKeyboardMarkup(
                                [
                                    [InlineKeyboardButton("➕ ارسال مجدد لینک", callback_data=f"link-{id}")]
                                    ,
                                    [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                            ])
                            await message.reply(f"⚠️ تبچی شما با {flood} ثانیه محدودیت عضویت مواجه شده است. پس از رفع عضویت به صورت خودکار در گروه موردنظر عضو خواهد شد.", reply_markup=linkkey)
                            await asyncio.sleep(int(flood))
                            if join[codess] != None and join[codess] == True:
                                try:
                                    linkkey = InlineKeyboardMarkup(
                                        [
                                            [InlineKeyboardButton("➕ ارسال مجدد لینک", callback_data=f"link-{id}")]
                                            ,
                                            [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                                    ])
                                    mybot = await check_id_message(id, message)
                                    result = await mybot.join_chat(link)
                                    await message.reply(f"🌟 عضویت در {result.title} باموفقیت انجام شد!", reply_markup=linkkey)
                                except:
                                    pass
                                await mybot.disconnect()
                        except:
                            await message.reply("خطا در عضویت لطفا دوباره تلاش کنید.")
                            await mybot.disconnect()
                    except errors.ChannelsTooMuch:
                        await mybot.disconnect()
                        await message.reply("تبچی شما در گروه های زیادی عضو است و امکان عضویت در گروه جدید را ندارد این محدودیت از سمت تلگرام است لطفا از چند گروه یا کانال لفت دهید سپس مجددا تلاش نمایید :", reply_markup=back_key(id))
                    except:
                        await mybot.disconnect()
                        await message.reply("خطا در عضویت لطفا دوباره تلاش کنید.")
                else:
                    txt = 'عملیات انجام شد.'
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                    botdata = query(f'SELECT * FROM bots WHERE admin={message.from_user.id} AND `pyro` != "no"')
                    if len(botdata) > 0:
                        for bot in botdata:
                            one_id = bot[0]
                            name = unquote(bot[5])
                            try:
                                mybot = await check_id_message(one_id, message)
                                link = message.text
                                if "joinchat" in message.text:
                                    link = "https://t.me/joinchat/"+message.text.split('joinchat/')[1].split(' ')[0].split('\n')[0]
                                elif "t.me/+" in message.text:
                                    link = "https://t.me/joinchat/"+message.text.split('t.me/+')[1].split(' ')[0].split('\n')[0]
                                elif "t.me/" in message.text:
                                    link = "@"+message.text.split('t.me/')[1].split(' ')[0].split('\n')[0]
                                elif "@" in message.text:
                                    link = "@"+message.text.split('@')[1].split(' ')[0].split('\n')[0]
                                else:
                                    link = "@"+message.text
                                result = await mybot.join_chat(link)
                                try:
                                    await mybot.disconnect()
                                except:
                                    pass
                            except (errors.UsernameInvalid,errors.UsernameNotOccupied):
                                txt = "⚠️ کاربرگرامی لینک ارسال شده درست نمیباشد!\n🌟 لطفا لینک صحیح را ارسال نمایید!"
                                break
                            except:
                                try:
                                    await mybot.disconnect()
                                except:
                                    pass
                                continue
                            try:
                                await mybot.disconnect()
                            except:
                                pass
                        
                        await msgsent.delete()
                        await message.reply(txt, reply_markup=back_key(id))
        except Exception as e:
            x = traceback.format_exc()
            await client.send_message(856460477,f'Soomlething went wrongr :(\nerror : `{x}`')

    @app.on_message(filters.private,group=2)
    async def step(client,message):
        try:
            if get_step(message.chat.id).split('-')[0] == 'afz':
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                if str(message.text).isnumeric() and int(message.text) >= 1000 and int(message.text) <= 500000:
                    await message.reply('فاکتور شما با موفقیت ساخته شد. جهت پرداخت بر روی دکمه زیر کلیک کنید.', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("پرداخت", url=f"ADDRESS/Payment/index.php?id={message.from_user.id}&amount={int(message.text)}")]]))
                else:
                    await message.reply('مبلغ وارد شده نامعتبر میباشد.', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="afz")]]))
            
            elif get_step(message.chat.id).split('-')[0] == 'pic':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                try:
                    mybot = await check_id_message(id, message)
                    down = await message.download()
                    await mybot.set_profile_photo(photo=down)
                    os.unlink(down)
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    pictext = "✅ تصویر پروفایل شما تنظیم شد."
                    await message.reply(pictext, reply_markup=back_key(id))
                except (errors.UsernameInvalid, errors.UsernameOccupied):
                    await message.reply("یوزرنیم موردنظر اشتباه میباشد یک یوزرنیم جدید ارسال نمایید!", reply_markup=back_key(id))
                await mybot.disconnect()
            
            elif get_step(message.chat.id).split('-')[0] == 'AutoAds':
                id = get_step(message.chat.id).split('-')[1]
                if message.forward_from_chat != None and message.forward_from_chat.username != None:
                    ad = query(f"SELECT * FROM `banners` WHERE id={id} AND `msgid` = '{message.forward_from_message_id}' AND `ch` = '{message.forward_from_chat.username}'")
                    if len(ad) == 0:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        ads = query(f"SELECT * FROM `ads` WHERE id={id} AND `type` = 'forward'")
                        if len(ads) == 0:
                            update_database(f"INSERT INTO `ads` VALUES('{id}', '{id}', 'forward', '{int(t.time())+2400}', '40', '{message.chat.id}')")
                        update_database(f"INSERT INTO `banners` VALUES('{id}', 'forward', '{message.forward_from_message_id}', '{message.forward_from_chat.username}', '{message.chat.id}')")
                        await message.reply('تبلیغ فوروارد خودکار شما ثبت شد و هر 40 دقیقه به صورت خودکار به سوپرگروه ها ارسال خواهد شد.', quote=True,reply_markup=back_sabet(id))
                    else:
                        await message.reply('این تبلیغ از قبل ثبت شده است، تبلیغ جدید فوروارد نمایید :', quote=True, reply_markup=back_sabet(id))
                else:
                    await message.reply('لطفا پیام خود را از یک کانال عمومی فوروارد کنید :', quote=True, reply_markup=back_sabet(id))
            
            elif get_step(message.chat.id).split('-')[0] == 'AutoSon':
                id = get_step(message.chat.id).split('-')[1]
                if message.text:
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    msgidc = (await client.forward_messages('TABLIGHCH', message.chat.id, message.id)).id
                    ads = query(f"SELECT * FROM `ads` WHERE id={id} AND `type` = 'send'")
                    if len(ads) == 0:
                        update_database(f"INSERT INTO `ads` VALUES('{id}', '{id}-send', 'send', '{int(t.time())+2400}', '40', '{message.chat.id}')")
                    update_database(f"INSERT INTO `banners` VALUES('{id}', 'send', '{msgidc}', 'TABLIGHCH', '{message.chat.id}')")
                    await message.reply('تبلیغ ارسال خودکار شما ثبت شد و هر 40 دقیقه به صورت خودکار به سوپرگروه ها ارسال خواهد شد.', quote=True,reply_markup=back_sabet(id))
                else:
                    await message.reply('لطفا یک متن ارسال نمایید :', reply_markup=back_sabet(id))
            
            elif message and get_step(message.chat.id) == 'frt' and message.text != 'فوروارد':
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                datas = query(f"SELECT * FROM `data`")
                for i in datas:
                    try:
                        await client.forward_messages(i[0], message.from_user.id, message.id)
                    except errors.FloodWait as e:
                        await asyncio.sleep(e.value)
                        continue
                    except:
                        continue
                await message.reply('عملیات انجام شد', reply_markup=panel)
            
            elif get_step(message.chat.id).split('-')[0] == 'snd':
                step = get_step(message.chat.id).split('-')
                id = step[2]
                type = step[1]
                txt = "عملیات انجام شد!"
                if message != None:
                    msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    msgidc = (await client.forward_messages('TABLIGHCH', message.chat.id, message.id)).id
                    if id != "all":
                        mybot = await check_id_message(id, message)
                        users = mybot.get_dialogs()
                        backkeyb = back_key(id)
                        try:
                            ReportAcc[id] = False
                            async for it in users:
                                try:
                                    if type == 'all' or it.chat.type == getattr(enums.ChatType, type.upper()):
                                        if it.chat.type == enums.ChatType.PRIVATE and ReportAcc[id] == True:
                                            continue
                                        else:
                                            await mybot.copy_message(it.chat.id, "TABLIGHCH", int(msgidc))
                                except Exception as e:
                                    if "database is locked" in str(e) or "Client has not been started yet" in str(e):
                                        await ConnectingBot(mybot)
                                        continue
                                    elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e) or "[400 USER_BANNED_IN_CHANNEL]" in str(e):
                                        try:
                                            await mybot.leave_chat(it.chat.id)
                                        except:
                                            pass
                                        continue
                                    elif "[400 PEER_FLOOD]" in str(e):
                                        ReportAcc[id] = True
                                        continue
                                    elif "[420 FLOOD_WAIT_X]" in str(e):
                                        await DisConnectingBot(mybot)
                                        e = str(e)
                                        flood = e.split(' seconds')[0].split('of ')[1]
                                        if int(flood) <= 1000:
                                            txt = f"‼️ تبچی شما {flood} ثانیه محدود شده است پس از رفع محدودیت عملیات به صورت خودکار ادامه خواهد یافت."
                                            tfo = int(t.time()) + int(flood)
                                            floodkey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")]])
                                            await msgsent.edit(txt, reply_markup=floodkey)
                                            await asyncio.sleep(int(flood))
                                            await msgsent.edit('درحال انجام عملیات')
                                            await ConnectingBot(mybot)
                                            txt = "عملیات انجام شد!"
                                            continue
                                        else:
                                            txt = f"عملیات به دلیل محدودیت {flood} ثانیه ای ربات ناتمام ماند لطفا بعد از رفع محدودیت دوباره تلاش کنید."
                                            break
                                    else:
                                        continue
                        except:
                            pass
                        await DisConnectingBot(mybot)
                    else:
                        backkeyb = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("🔙 برگشت", callback_data="manageall")]
                            ])
                        botdata = query(f'SELECT * FROM bots WHERE admin={message.from_user.id} AND `pyro` != "no"')
                        if len(botdata) > 0:
                            for bot in botdata:
                                one_id = bot[0]
                                name = unquote(bot[5])
                                try:
                                    mybot = Client(name=str(one_id),session_string=get_string(one_id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                                    if len(mybot.name) == 351:
                                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                                    if len(mybot.name) == 356:
                                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                                    await ConnectingBot(mybot)
                                    ReportAcc[id] = False
                                    try:
                                        users = mybot.get_dialogs()
                                    except Exception as e:
                                        users = []
                                        continue
                                    async for it in users:
                                        try:
                                            if type == 'all' or it.chat.type == getattr(enums.ChatType, type.upper()):
                                                if it.chat.type == enums.ChatType.PRIVATE and ReportAcc[id] == True:
                                                    continue
                                                else:
                                                    await mybot.copy_message(it.chat.id, "TABLIGHCH", int(msgidc))
                                        except Exception as e:
                                            if "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                                                try:
                                                    await mybot.leave_chat(it.chat.id)
                                                except:
                                                    pass
                                                continue
                                            elif "database is locked" in str(e) or "Client has not been started yet" in str(e):
                                                await ConnectingBot(mybot)
                                                continue
                                            elif "[400 USER_BANNED_IN_CHANNEL]" in str(e) or "[400 INPUT_USER_DEACTIVATED]" in str(e):
                                                try:
                                                    await mybot.leave_chat(it.chat.id)
                                                except:
                                                    pass
                                                continue
                                            elif "[401 AUTH_KEY_UNREGISTERED]:" in str(e) or "[401 USER_DEACTIVATED]:" in str(e) or "[401 USER_DEACTIVATED_BAN]:" in str(e) or "[401 SESSION_EXPIRED]:" in str(e) or "[401 SESSION_REVOKED]:" in str(e):
                                                break
                                            elif "[420 FLOOD_WAIT_X]" in str(e):
                                                e = str(e)
                                                flood = e.split(' seconds')[0].split('of ')[1]
                                                await DisConnectingBot(mybot)
                                                if int(flood) <= 1000:
                                                    txt = f"‼️ تبچی {name} شما {flood} ثانیه محدود شده است پس از رفع محدودیت عملیات به صورت خودکار ادامه خواهد یافت."
                                                    tfo = int(t.time()) + int(flood)
                                                    floodkey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")]])
                                                    await msgsent.edit(txt, reply_markup=floodkey)
                                                    await asyncio.sleep(int(flood))
                                                    await msgsent.edit('درحال انجام عملیات')
                                                    await ConnectingBot(mybot)
                                                    txt = "عملیات انجام شد!"
                                                    continue
                                                else:
                                                    txt = "عملیات انجام شد!"
                                                    break
                                            else:
                                                continue
                                except:
                                    await DisConnectingBot(mybot)
                                    continue
                                await DisConnectingBot(mybot)
                    await msgsent.delete()
                    await message.reply(txt, reply_markup=backkeyb)
                else:
                    await message.reply("لطفا یک متن ارسال کنید!", reply_markup=back_key(id))
                    
            elif get_step(message.chat.id).split('&')[0] == 'ojo':
                step = get_step(message.chat.id).split('&')
                id = step[1]
                hash = step[2]
                if message.text.isnumeric() == True and int(message.text) > 0:
                    update_database(f"UPDATE `ads` SET `every`='{int(message.text)}' WHERE `Hash`='{hash}'")
                    await message.reply('زمان شما تنظیم شد.', reply_markup=sabet_key(id))
                else:
                    await message.reply('زمان ارسالی میبایست به عدد و بزرگتر از 0 باشد', reply_markup=back_key(id))
                
            
            elif get_step(message.chat.id).split('-')[0] == 'opes':
                try:
                    step = get_step(message.chat.id).split('-')
                    id = step[1]
                    if 't.me/+' in message.text:
                        message.text = 'https://t.me/joinchat/'+message.text.split('+')[1]
                    if userha[message.text] != None and len(userha[message.text]) > 0:
                        update_database(f"UPDATE data SET step='fetab#{id}#{message.text}' WHERE id={message.chat.id}")
                        await message.reply(f"👤♻️ لیست گپ با موفقیت دریافت شد. تعداد اعضا فعال ذخیره شده : {str(len(userha[message.text]))} نفر . لطفا بنر خود را ارسال نمایید :", reply_markup=back_key(id))
                    else:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        await message.reply('⛔️ لیست این گپ دریافت نشده است. لطفا از بخش دریافت لیست اقدام به دریافت لیست اعضای گروه نمایید.', reply_markup=sendto_key(id))
                except Exception as e:
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    await message.reply('⛔️ لیست این گپ دریافت نشده است. لطفا از بخش دریافت لیست اقدام به دریافت لیست اعضای گروه نمایید.', reply_markup=sendto_key(id))
                    
            elif get_step(message.chat.id).split('#')[0] == 'fetab':
                try:
                    step = get_step(message.chat.id).split('#')
                    id = step[1]
                    link = step[2]
                    if id == "all":
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        accounts = query(f"SELECT * FROM `bots` WHERE `admin` = {message.from_user.id}")
                        seccess[link] = []
                        msg = await message.reply('درحال انجام عملیات ...')
                        msgidc = (await client.forward_messages('TABLIGHCH', message.chat.id, message.id)).id
                        
                        for user in userha[link]:
                            for account in accounts[:]:
                                one_id = account[0]
                                try:
                                    mybot = await check_id_message(one_id, message)
                                    await mybot.copy_message(user, "TABLIGHCH", int(msgidc))
                                    await mybot.disconnect()
                                    seccess[link].append(user)
                                    await msg.edit(f'ارسال بنر به کاربر {user} با اکانت {account[4]} انجام شد.')
                                    break
                                except Exception as e:
                                    try:
                                        await mybot.disconnect()
                                    except:
                                        pass
                                    if "[400 PEER_FLOOD]" in str(e):
                                        accounts.remove(account)
                                        await message.reply('اکانت شما '+str(account[4])+' محدود شده است.')
                                        continue
                                    elif "FLOOD_WAIT_" in str(e):
                                        accounts.remove(account)
                                        continue
                                    elif "AUTH_KEY_UNREGISTERED" in str(e) or "SESSION_REVOKED" in str(e):
                                        accounts.remove(account)
                                        await message.reply('اکانت '+str(account[4])+' مسدود شده است.')
                                        continue
                                    elif "USER_DEACTIVATED_BAN" in str(e):
                                        accounts.remove(account)
                                        await message.reply('اکانت '+str(account[4])+' مسدود شده است.')
                                        continue
                                    else:
                                        continue
                    else:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        seccess[link] = []
                        msg = await message.reply('درحال انجام عملیات ...')
                        msgidc = (await client.forward_messages('TABLIGHCH', message.chat.id, message.id)).id
                        
                        for user in userha[link]:
                            try:
                                if int(senddelay) > 0:
                                    await asyncio.sleep(int(senddelay))
                                mybot = await check_id_message(id, message)
                                await mybot.copy_message(user, "TABLIGHCH", int(msgidc))
                                await mybot.disconnect()
                                seccess[link].append(user)
                                await msg.edit(f'ارسال بنر به کاربر {user} با اکانت انجام شد.')
                            except Exception as e:
                                try:
                                    await mybot.disconnect()
                                except:
                                    pass
                                if "[400 PEER_FLOOD]" in str(e):
                                    await message.reply('اکانت شما محدود شده است.')
                                    break
                                elif "FLOOD_WAIT_" in str(e):
                                    break
                                elif "AUTH_KEY_UNREGISTERED" in str(e) or "SESSION_REVOKED" in str(e):
                                    await message.reply('اکانت مسدود شده است.')
                                    break
                                elif "USER_DEACTIVATED_BAN" in str(e):
                                    await message.reply('اکانت مسدود شده است.')
                                    break
                                else:
                                    continue
                    
                    se = len(seccess[link])
                    all = len(userha[link])
                    await msg.delete()
                    await message.reply(f'عملیات باموفقیت انجام شد. کل اعضا : {all}\nتعداد ارسال موفق : {se}', reply_markup = sendto_key(id))
                except Exception as e:
                    await message.reply(e)
                    
            elif get_step(message.chat.id).split('-')[0] == 'ftp':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                if 't.me/+' in message.text:
                    message.text = 'https://t.me/joinchat/'+message.text.split('+')[1]
                try:
                    if userha[message.text] != None and len(userha[message.text]) > 0:
                        update_database(f"UPDATE data SET step='okex#{id}#{message.text}' WHERE id={message.chat.id}")
                        await message.reply(f"👤♻️ لیست گپ با موفقیت دریافت شد. تعداد اعضا فعال ذخیره شده : {str(len(userha[message.text]))} نفر . لطفا بنر خود را فوروارد نمایید :", reply_markup=back_key(id))
                    else:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        await message.reply('⛔️ لیست این گپ دریافت نشده است. لطفا از بخش دریافت لیست اقدام به دریافت لیست اعضای گروه نمایید.', reply_markup=sendto_key(id))
                except:
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    await message.reply('⛔️ لیست این گپ دریافت نشده است. لطفا از بخش دریافت لیست اقدام به دریافت لیست اعضای گروه نمایید.', reply_markup=sendto_key(id))
                    
            elif get_step(message.chat.id).split('#')[0] == 'okex':
                try:
                    step = get_step(message.chat.id).split('#')
                    id = step[1]
                    link = step[2]
                    if id == "all":
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        accounts = query(f"SELECT * FROM `bots` WHERE `admin` = {message.from_user.id}")
                        seccess[link] = []
                        msg = await message.reply('درحال انجام عملیات ...')
                        msgidc = (await client.forward_messages('TABLIGHCH', message.chat.id, message.id)).id
                        
                        for user in userha[link]:
                            for account in accounts[:]:
                                one_id = account[0]
                                try:
                                    mybot = await check_id_message(one_id, message)
                                    await mybot.forward_messages(user, "TABLIGHCH", int(msgidc))
                                    await mybot.disconnect()
                                    seccess[link].append(user)
                                    await msg.edit(f'فوروارد بنر به کاربر {user} با اکانت {account[4]} انجام شد.')
                                    break
                                except Exception as e:
                                    try:
                                        await mybot.disconnect()
                                    except:
                                        pass
                                    if "[400 PEER_FLOOD]" in str(e):
                                        accounts.remove(account)
                                        await message.reply('اکانت شما '+str(account[4])+' محدود شده است.')
                                        continue
                                    elif "FLOOD_WAIT_" in str(e):
                                        accounts.remove(account)
                                        continue
                                    elif "AUTH_KEY_UNREGISTERED" in str(e) or "SESSION_REVOKED" in str(e):
                                        accounts.remove(account)
                                        await message.reply('اکانت '+str(account[4])+' مسدود شده است.')
                                        continue
                                    elif "USER_DEACTIVATED_BAN" in str(e):
                                        accounts.remove(account)
                                        await message.reply('اکانت '+str(account[4])+' مسدود شده است.')
                                        continue
                                    else:
                                        continue
                    else:
                        update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                        seccess[link] = []
                        msg = await message.reply('درحال انجام عملیات ...')
                        msgidc = (await client.forward_messages('TABLIGHCH', message.chat.id, message.id)).id
                        
                        for user in userha[link]:
                            try:
                                mybot = await check_id_message(id, message)
                                await mybot.forward_messages(user, "TABLIGHCH", int(msgidc))
                                await mybot.disconnect()
                                seccess[link].append(user)
                                await msg.edit(f'فوروارد بنر به کاربر {user} با اکانت انجام شد.')
                            except Exception as e:
                                try:
                                    await mybot.disconnect()
                                except:
                                    pass
                                if "[400 PEER_FLOOD]" in str(e):
                                    await message.reply('اکانت شما محدود شده است.')
                                    break
                                elif "FLOOD_WAIT_" in str(e):
                                    break
                                elif "AUTH_KEY_UNREGISTERED" in str(e) or "SESSION_REVOKED" in str(e):
                                    await message.reply('اکانت مسدود شده است.')
                                    break
                                elif "USER_DEACTIVATED_BAN" in str(e):
                                    await message.reply('اکانت مسدود شده است.')
                                    break
                                else:
                                    continue
                    
                    se = len(seccess[link])
                    all = len(userha[link])
                    await msg.delete()
                    await message.reply(f'عملیات باموفقیت انجام شد. کل اعضا : {all}\nتعداد فوروارد موفق : {se}', reply_markup = sendto_key(id))
                except Exception as e:
                    await message.reply(e)
                
            elif get_step(message.chat.id).split('-')[0] == 'ltp':
                step = get_step(message.chat.id).split('-')
                id = step[1]
                txt = 'خطا در دریافت لیست ، لطفا لینک و اکانت های خود را چک کنید.'
                msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                if 't.me/+' in message.text:
                    message.text = 'https://t.me/joinchat/'+message.text.split('+')[1]
                try:
                    if id != "all":
                        mybot = await check_id_message(id, message)
                        await msgsent.edit('♻️ درحال عضویت در گروه ...')
                        try:
                            chat = await mybot.join_chat(message.text)
                        except:
                            chat = await mybot.get_chat(message.text)
                        await msgsent.edit('📝 درحال دریافت لیست ...')
                        userha[message.text] = []
                        async for i in mybot.get_chat_members(chat.id):
                            if i.user.username and i.user.is_bot == False and check(i):
                                userha[message.text].append(f'@{i.user.username}')
                        await mybot.disconnect()
                        await msgsent.delete()
                        await message.reply(f"👤♻️ لیست گپ {chat.title or chat.first_name} با موفقیت دریافت شد. تعداد اعضا فعال ذخیره شده : {str(len(userha[message.text]))} نفر", reply_markup=sendto_key(id))
                    else:
                        txt = 'خطا در دریافت لیست ، لطفا لینک و اکانت های خود را چک کنید.'
                        botdata = query(f'SELECT * FROM bots WHERE admin={message.from_user.id}')
                        if len(botdata) > 0:
                            for bot in botdata:
                                one_id = bot[0]
                                phone = bot[4]
                                name = unquote(bot[5])
                                try:
                                    mybot = await check_id_message(one_id, message)
                                    await msgsent.edit(f'{phone} : ♻️ درحال عضویت در گروه ...')
                                    try:
                                        chat = await mybot.join_chat(message.text)
                                    except:
                                        chat = await mybot.get_chat(message.text)
                                    await msgsent.edit(f'{phone} : 📝 درحال دریافت لیست ...')
                                    userha[message.text] = []
                                    async for i in mybot.get_chat_members(chat.id):
                                        if i.user.username and i.user.is_bot == False and check(i):
                                            userha[message.text].append(f'@{i.user.username}')
                                    await mybot.disconnect()
                                    await msgsent.delete()
                                    txt = f"{phone} : 👤♻️ لیست گپ {chat.title or chat.first_name} با موفقیت دریافت شد. تعداد اعضا فعال ذخیره شده : {str(len(userha[message.text]))} نفر"
                                    break
                                except:
                                    try:
                                        await mybot.disconnect()
                                    except:
                                        pass
                                    continue
                            await message.reply(txt, reply_markup=sendto_key(id))
                except Exception as e:
                    await message.reply(txt)
            #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif get_step(message.chat.id).split('-')[0] == 'fwd':
                step = get_step(message.chat.id).split('-')
                id = step[2]
                type = step[1]
                txt = "عملیات انجام شد!"
                if message.forward_from_chat != None and message.forward_from_chat.username != None:
                    update_database(f"UPDATE data SET step='no' WHERE id={message.chat.id}")
                    msgsent = await message.reply('🔁 در حال انجام عملیات ، لطفا کمی صبر کنید ...')
                    if id != "all":
                        backkeyb = back_key(id)
                        mybot = await check_id_message(id, message)
                        try:
                            users = mybot.get_dialogs()
                        except Exception as e:
                            users = []
                        
                        async for it in users:
                            try:
                                if type == 'all' or it.chat.type == getattr(enums.ChatType, type.upper()):
                                    if it.chat.type == enums.ChatType.PRIVATE and ReportAcc[id] == True:
                                        continue
                                    else:
                                        await mybot.forward_messages(it.chat.id, message.forward_from_chat.username, message.forward_from_message_id)
                            except Exception as e:
                                if "CHAT_WRITE_FORBIDDEN" in str(e) or "[400 USER_BANNED_IN_CHANNEL]" in str(e):
                                    try:
                                        await mybot.leave_chat(it.chat.id)
                                    except:
                                        pass
                                    continue
                                elif "[400 PEER_FLOOD]" in str(e):
                                    ReportAcc[id] = True
                                    continue
                                elif "[420 FLOOD_WAIT_X]" in str(e):
                                    try:
                                        await mybot.disconnect()
                                    except:
                                        pass
                                    e = str(e)
                                    flood = e.split(' seconds')[0].split('of ')[1]
                                    txt = f"‼️ تبچی شما {flood} ثانیه محدود شده است پس از رفع محدودیت عملیات به صورت خودکار ادامه خواهد یافت."
                                    tfo = int(t.time()) + int(flood)
                                    floodkey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")]])
                                    await msgsent.edit(txt, reply_markup=floodkey)
                                    await asyncio.sleep(int(flood))
                                    await msgsent.edit('درحال انجام عملیات')
                                    await mybot.connect()
                                    txt = "عملیات انجام شد!"
                                    continue
                                else:
                                    continue
                        await mybot.disconnect()
                    else:
                        backkeyb = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("🔙 برگشت", callback_data="manageall")]
                            ])
                        botdata = query(f'SELECT * FROM bots WHERE admin={message.from_user.id} AND `pyro` != "no"')
                        if len(botdata) > 0:
                            for bot in botdata:
                                one_id = bot[0]
                                name = unquote(bot[5])
                                try:
                                    mybot = await check_id_message(one_id, message)
                                    try:
                                        users = mybot.get_dialogs()
                                    except Exception as e:
                                        users = []
                                    
                                    async for it in users:
                                        try:
                                            if type == 'all' or it.chat.type == getattr(enums.ChatType, type.upper()):
                                                if it.chat.type == enums.ChatType.PRIVATE and ReportAcc[id] == True:
                                                    continue
                                                else:
                                                    await mybot.forward_messages(it.chat.id, message.forward_from_chat.username, message.forward_from_message_id)
                                        except Exception as e:
                                            if "[403 CHAT_WRITE_FORBIDDEN]" in str(e) or "[400 USER_BANNED_IN_CHANNEL]" in str(e):
                                                try:
                                                    await mybot.leave_chat(it.chat.id)
                                                except:
                                                    pass
                                                continue
                                            elif "[401 AUTH_KEY_UNREGISTERED]:" in str(e) or "[401 USER_DEACTIVATED]:" in str(e) or "[401 USER_DEACTIVATED_BAN]:" in str(e) or "[401 SESSION_EXPIRED]:" in str(e) or "[401 SESSION_REVOKED]:" in str(e):
                                                break
                                            elif "[400 PEER_FLOOD]" in str(e):
                                                ReportAcc[id] = True
                                                continue
                                            elif "[420 FLOOD_WAIT_X]" in str(e):
                                                e = str(e)
                                                flood = e.split(' seconds')[0].split('of ')[1]
                                                if int(flood) < 1000:
                                                    try:
                                                        await mybot.disconnect()
                                                    except:
                                                        pass
                                                    txt = f"‼️ تبچی {name} شما {flood} ثانیه محدود شده است پس از رفع محدودیت عملیات به صورت خودکار ادامه خواهد یافت."
                                                    tfo = int(t.time()) + int(flood)
                                                    floodkey = InlineKeyboardMarkup([[InlineKeyboardButton("زمان باقی مانده", callback_data=f"unf-{tfo}")]])
                                                    await msgsent.edit(txt, reply_markup=floodkey)
                                                    await asyncio.sleep(int(flood))
                                                    await msgsent.edit('درحال انجام عملیات')
                                                    await mybot.connect()
                                                    txt = "عملیات انجام شد!"
                                                    continue
                                                else:
                                                    break
                                            else:
                                                continue
                                    await mybot.disconnect()
                                except:
                                    try:
                                        await mybot.disconnect()
                                    except:
                                        pass
                                    continue
                    await msgsent.delete()
                    await message.reply(txt, reply_markup=backkeyb)
                else:
                    await message.reply("لطفا پیام رو از یک کانال عمومی فوروارد کن!")
        except:
            pass
    
    def gethash(amount,userid):
        price = query(f"SELECT * FROM payments WHERE amount='{amount}' AND userid='{userid}' AND type='pay'")
        if len(price) > 0:
            random10000 = price[0][0]
        else:
            random10000 = uuid.uuid4().hex.upper()[0:10]
            update_database(f"INSERT INTO payments VALUES('{random10000}', 0, '{amount}','{userid}', 'pay')")
        return random10000
    
    def bot_key(id):
        bot = get_bot(id)
        join = unquote(bot[15])
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("♾ تبلیغات ثابت", callback_data=f"sabet-{id}")]
                ,
                [InlineKeyboardButton("🔖 اطلاعات اکانت", callback_data=f"data-{id}"),InlineKeyboardButton("📂 آمار اکانت", callback_data=f"info-{id}"),InlineKeyboardButton("☕️ حریم خصوصی", callback_data=f"privacy-{id}")]
                ,
                [InlineKeyboardButton("📨 ارسال پیام", callback_data=f"send-{id}"),InlineKeyboardButton("🗑 پاکسازی اکانت", callback_data=f"clean-{id}"),InlineKeyboardButton("✉️ فوروارد پیام", callback_data=f"forward-{id}")]
                ,
                [InlineKeyboardButton("📝 راهنمای مدیریت", callback_data=f"help-{id}"),InlineKeyboardButton("🔐 تایید دو مرحله ای", callback_data=f"pat-{id}")]
                ,
                [InlineKeyboardButton("📲 افزودن مخاطب", callback_data=f"addcont-{id}"),InlineKeyboardButton("👨‍👩‍👧‍👦 مخاطبین", callback_data=f"contact-{id}"),InlineKeyboardButton("👣 نشست ها", callback_data=f"session-{id}")]
                ,
                [InlineKeyboardButton("➖ خروج از گروه", callback_data=f"left-{id}"),InlineKeyboardButton("➕ عضویت در گروه", callback_data=f"link-{id}")]
                ,
                [InlineKeyboardButton("👤 تغییر نام", callback_data=f"name-{id}"),InlineKeyboardButton("👥 تغییر نام خانوادگی", callback_data=f"family-{id}"),InlineKeyboardButton("🔁 تغییر نام کاربری", callback_data=f"username-{id}")]
                ,
                [InlineKeyboardButton("🌆 تنظیم تصویر پروفایل", callback_data=f"pic-{id}"),InlineKeyboardButton("📑 تنظیم بیو اکانت", callback_data=f"bio-{id}")]
                ,
                [InlineKeyboardButton("🫂 افزودن عضو به گروه", callback_data=f"add-{id}"),InlineKeyboardButton("🗣 افزودن کاربر به گپ ها", callback_data=f"invite-{id}")]
                ,
                [InlineKeyboardButton('🔁 اهدا تبچی', callback_data=f"shop-{id}"),InlineKeyboardButton(f"🔗 عضویت خودکار : {join}", callback_data=f"jop-{id}")]
                ,
                [InlineKeyboardButton("برگشت", callback_data="go")]
        ])
    
    def back_sabet(id):
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("برگشت", callback_data=f"sabet-{id}")]
        ])
    
    def back_key(id):
        if id != 'all':
            return InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                ])
        else:
            return InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("برگشت", callback_data=f"manageall")]
            ])
    
    async def privacy_key(id, mybot):
        seen = await mybot.invoke(functions.account.GetPrivacy(key=types.InputPrivacyKeyStatusTimestamp()))
        en_seen = str(seen.rules[0].__init__).split('types.')[1].split('(')[0]
        seen = str(seen.rules[0].__init__).split('types.')[1].split('(')[0].replace('PrivacyValueAllowAll', 'همه').replace('PrivacyValueDisallowAll', 'هیچکس').replace('PrivacyValueAllowContacts', 'مخاطبین من').replace('PrivacyValueAllowUsers', 'هیچکس(بجز بعضی افراد)').replace('PrivacyValueDisallowUsers', 'همه(بجز بعضی افراد)').replace('PrivacyValueDisallowContacts', 'همه (بجز مخابین)').replace('PrivacyValueAllowChatParticipants', 'هیچکس').replace('PrivacyValueDisallowChatParticipants', 'همه')
        invite = await mybot.invoke(functions.account.GetPrivacy(key=types.InputPrivacyKeyChatInvite()))
        en_invite = str(invite.rules[0].__init__).split('types.')[1].split('(')[0]
        invite = str(invite.rules[0].__init__).split('types.')[1].split('(')[0].replace('PrivacyValueAllowAll', 'همه').replace('PrivacyValueDisallowAll', 'هیچکس').replace('PrivacyValueAllowContacts', 'مخاطبین من').replace('PrivacyValueAllowUsers', 'هیچکس(بجز بعضی افراد)').replace('PrivacyValueDisallowUsers', 'همه(بجز بعضی افراد)').replace('PrivacyValueDisallowContacts', 'همه (بجز مخابین)').replace('PrivacyValueAllowChatParticipants', 'هیچکس').replace('PrivacyValueDisallowChatParticipants', 'همه')
        forward = await mybot.invoke(functions.account.GetPrivacy(key=types.InputPrivacyKeyForwards()))
        en_forward = str(forward.rules[0].__init__).split('types.')[1].split('(')[0]
        forward = str(forward.rules[0].__init__).split('types.')[1].split('(')[0].replace('PrivacyValueAllowAll', 'همه').replace('PrivacyValueDisallowAll', 'هیچکس').replace('PrivacyValueAllowContacts', 'مخاطبین من').replace('PrivacyValueAllowUsers', 'هیچکس(بجز بعضی افراد)').replace('PrivacyValueDisallowUsers', 'همه(بجز بعضی افراد)').replace('PrivacyValueDisallowContacts', 'همه (بجز مخابین)').replace('PrivacyValueAllowChatParticipants', 'هیچکس').replace('PrivacyValueDisallowChatParticipants', 'همه')
        call = await mybot.invoke(functions.account.GetPrivacy(key=types.InputPrivacyKeyPhoneCall()))
        en_call = str(call.rules[0].__init__).split('types.')[1].split('(')[0]
        call = str(call.rules[0].__init__).split('types.')[1].split('(')[0].replace('PrivacyValueAllowAll', 'همه').replace('PrivacyValueDisallowAll', 'هیچکس').replace('PrivacyValueAllowContacts', 'مخاطبین من').replace('PrivacyValueAllowUsers', 'هیچکس(بجز بعضی افراد)').replace('PrivacyValueDisallowUsers', 'همه(بجز بعضی افراد)').replace('PrivacyValueDisallowContacts', 'همه (بجز مخابین)').replace('PrivacyValueAllowChatParticipants', 'هیچکس').replace('PrivacyValueDisallowChatParticipants', 'همه')
        phone = await mybot.invoke(functions.account.GetPrivacy(key=types.InputPrivacyKeyPhoneNumber()))
        en_phone = str(phone.rules[0].__init__).split('types.')[1].split('(')[0]
        phone = str(phone.rules[0].__init__).split('types.')[1].split('(')[0].replace('PrivacyValueAllowAll', 'همه').replace('PrivacyValueDisallowAll', 'هیچکس').replace('PrivacyValueAllowContacts', 'مخاطبین من').replace('PrivacyValueAllowUsers', 'هیچکس(بجز بعضی افراد)').replace('PrivacyValueDisallowUsers', 'همه(بجز بعضی افراد)').replace('PrivacyValueDisallowContacts', 'همه (بجز مخابین)').replace('PrivacyValueAllowChatParticipants', 'هیچکس').replace('PrivacyValueDisallowChatParticipants', 'همه')
        photo = await mybot.invoke(functions.account.GetPrivacy(key=types.InputPrivacyKeyProfilePhoto()))
        en_photo = str(photo.rules[0].__init__).split('types.')[1].split('(')[0]
        photo = str(photo.rules[0].__init__).split('types.')[1].split('(')[0].replace('PrivacyValueAllowAll', 'همه').replace('PrivacyValueDisallowAll', 'هیچکس').replace('PrivacyValueAllowContacts', 'مخاطبین من').replace('PrivacyValueAllowUsers', 'هیچکس(بجز بعضی افراد)').replace('PrivacyValueDisallowUsers', 'همه(بجز بعضی افراد)').replace('PrivacyValueDisallowContacts', 'همه (بجز مخابین)').replace('PrivacyValueAllowChatParticipants', 'هیچکس').replace('PrivacyValueDisallowChatParticipants', 'همه')
        await mybot.disconnect()
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(f"{seen}", callback_data=f"changep#{id}#seen#{en_seen}"),InlineKeyboardButton("آخرین بازدید :", callback_data="null")]
                ,
                [InlineKeyboardButton(f"{invite}", callback_data=f"changep#{id}#invite#{en_invite}"),InlineKeyboardButton("دعوت به گروه :", callback_data="null")]
                ,
                [InlineKeyboardButton(f"{forward}", callback_data=f"changep#{id}#forward#{en_forward}"),InlineKeyboardButton("فوروارد پیام :", callback_data="null")]
                ,
                [InlineKeyboardButton(f"{call}", callback_data=f"changep#{id}#call#{en_call}"),InlineKeyboardButton("برقراری تماس :", callback_data="null")]
                ,
                [InlineKeyboardButton(f"{phone}", callback_data=f"changep#{id}#phone#{en_phone}"),InlineKeyboardButton("مشاهده شماره :", callback_data="null")]
                ,
                [InlineKeyboardButton(f"{photo}", callback_data=f"changep#{id}#photo#{en_photo}"),InlineKeyboardButton("تصویر پروفایل :", callback_data="null")]
                , 
                [InlineKeyboardButton("🔙 برگشت", callback_data=f"bot-{id}")]
            ]
        )
        
    def sabet_key(id):
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚙️ تنظیمات", callback_data=f"setsabet-{id}")]
                ,
                [InlineKeyboardButton("✉️ فوروارد خودکار", callback_data=f"AutoFor-{id}"),InlineKeyboardButton("📨 ارسال خودکار", callback_data=f"AutoSen-{id}")]
                ,
                [InlineKeyboardButton("📑 راهنما", callback_data=f"helpsabet-{id}"),InlineKeyboardButton("⏺ بنر های ثبت شده", callback_data=f"mysabet-{id}")]
                ,
                [InlineKeyboardButton("🔙 برگشت", callback_data=f"bot-{id}")]
        ])

    async def ConnectingBot(sessionbot):
        try:
            await sessionbot.start()
        except:
            try:
                await sessionbot.stop()
                await sessionbot.start()
            except:
                pass
    async def DisConnectingBot(sessionbot):
        try:
            await sessionbot.stop()
        except:
            pass
    
    async def check_id_message(id,message):
        global app_id,app_hash,app
        account = get_data(message.from_user.id)[8]
        times = int(t.time())
        if id != 'all' and get_bot(id)[11] != str(message.from_user.id):
            await message.reply('این تبچی در لیست تبچی های شما وجود ندارد.')
            raise StopPropagation
        elif times - int(account) >= 2592000:
            await message.reply('⏰مهلت 30 روزه حساب طلایی شما به پایان رسید\nجهت تمدید حساب طلایی خود بر روی دکمه 🛍 فروشگاه کلیک نمایید!\nپس از تمدید امکان استفاده مجدد از تبچی میسر میشود!',show_alert=True)
            raise StopPropagation
        elif id != 'all' and get_bot(id)[21] == 'no':
            await message.reply('ربات شما مربوط به این ورژن تبچی ساز نیست لطفا از ربات @MrTabchi2bot استفاده نمایید یا ربات را حذف و دوباره بسازید.')
            raise StopPropagation
        elif id != 'all':
            try:
                mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                if len(mybot.name) == 351:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                if len(mybot.name) == 356:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                await mybot.start()
                await mybot.stop()
                await mybot.connect()
                return mybot
            except (errors.AuthKeyUnregistered, errors.UserDeactivated, errors.UserDeactivatedBan, errors.SessionExpired, errors.SessionRevoked):
                try:
                    await mybot.disconnect()
                except:
                    pass
                coun = get_data(message.from_user.id)[7]
                coun = int(coun)
                coun -= 1
                update_database(f"UPDATE data SET coun={coun} WHERE id={message.from_user.id}")
                update_database(f'DELETE FROM `bots` WHERE id={id}')
                update_database(f'DELETE FROM `ads` WHERE id={id}')
                update_database(f'DELETE FROM `auto` WHERE id={id}')
                await message.reply('⚠️خطا. ربات تبچی از اکانت بیرون افتاده است. به همین دلیل امکان مدیریت ربات وجود ندارد! ربات موردنظر حذف شده و فرصت ساخت به شما برگشت داده شد. لطفا دوباره اقدام به ساخت ربات کنید')
                raise StopPropagation
            except Exception as e:
                try:
                    await mybot.disconnect()
                except:
                    pass
                await app.send_message('@Pviim', str(e))
                raise StopPropagation
        else:
            return True
        
    async def check_id(id,callback_query):
        global app_id,app_hash,app
        account = get_data(callback_query.from_user.id)[8]
        times = int(t.time())
        if id != 'all' and get_bot(id)[11] != str(callback_query.from_user.id):
            await callback_query.edit_message_text('⚙️ این تبچی در لیست ربات های شما وجود ندارد!')
            raise StopPropagation
        elif times - int(account) >= 2592000:
            await callback_query.answer('⏰مهلت 30 روزه حساب طلایی شما به پایان رسید\nجهت تمدید حساب طلایی خود بر روی دکمه 🛍 فروشگاه کلیک نمایید!\nپس از تمدید امکان استفاده مجدد از تبچی میسر میشود!',show_alert=True)
            raise StopPropagation
        elif id != 'all' and get_bot(id)[21] == 'no':
            await callback_query.edit_message_text('ربات شما مربوط به این ورژن تبچی ساز نیست لطفا از ربات @AllPanelBot استفاده نمایید یا ربات را حذف و دوباره بسازید.')
            raise StopPropagation
        elif id != 'all':
            try:
                mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                if len(mybot.name) == 351:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                if len(mybot.name) == 356:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                await mybot.start()
                await mybot.stop()
                await mybot.connect()
                return mybot
            except (errors.AuthKeyUnregistered, errors.UserDeactivated, errors.UserDeactivatedBan, errors.SessionExpired, errors.SessionRevoked):
                try:
                    await mybot.disconnect()
                except:
                    pass
                coun = get_data(callback_query.from_user.id)[7]
                coun = int(coun)
                coun -= 1
                update_database(f"UPDATE data SET coun={coun} WHERE id={callback_query.from_user.id}")
                update_database(f'DELETE FROM `bots` WHERE id={id}')
                update_database(f'DELETE FROM `ads` WHERE id={id}')
                update_database(f'DELETE FROM `auto` WHERE id={id}')
                await callback_query.edit_message_text('⚠️خطا. ربات تبچی از اکانت بیرون افتاده است. به همین دلیل امکان مدیریت ربات وجود ندارد! ربات موردنظر حذف شده و فرصت ساخت به شما برگشت داده شد. لطفا دوباره اقدام به ساخت ربات کنید')
                raise StopPropagation
            except Exception as e:
                try:
                    await mybot.disconnect()
                except:
                    pass
                await app.send_message('@Pviim', str(e))
                raise StopPropagation
        else:
            return True
        
    @app.on_callback_query()
    async def calls(client,callback_query):
        global mycu,mydb
        try:
            if callback_query.data == 'delen' and get_step(callback_query.from_user.id).split('-')[0] == 'sendcode':
                newid = get_step(callback_query.from_user.id).split('-')[1]
                codekey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("1️⃣", callback_data="an-1"),InlineKeyboardButton("2️⃣", callback_data="an-2"),InlineKeyboardButton("3️⃣", callback_data="an-3")]
                                ,
                        [InlineKeyboardButton("4️⃣", callback_data="an-4"),InlineKeyboardButton("5️⃣", callback_data="an-5"),InlineKeyboardButton("6️⃣", callback_data="an-6")]
                                ,
                        [InlineKeyboardButton("7️⃣", callback_data="an-7"),InlineKeyboardButton("8️⃣", callback_data="an-8"),InlineKeyboardButton("9️⃣", callback_data="an-9")]
                                ,
                        [InlineKeyboardButton("✏️", callback_data="delen"),InlineKeyboardButton("0️⃣", callback_data="an-0"),InlineKeyboardButton("✅", callback_data=f"con-{newid}")]
                                ,
                        [InlineKeyboardButton("🗑 لغو عملیات", callback_data=f"cal-{newid}")]
                    ])
                if codelogin.get(callback_query.from_user.id) == None:
                    await client.answer_callback_query(callback_query.id,'هنوز کدی وارد نکردی که بخوای پاکش کنی :(',show_alert=True)
                else:
                    del codelogin[callback_query.from_user.id]
                    await client.answer_callback_query(callback_query.id,'کدی که وارد کرده بودی پاک شد حالا دوباره کد صحیح رو وارد کن :)',show_alert=True)
                    await callback_query.edit_message_text(f'🔐 کد وارد شده :', parse_mode=enums.ParseMode.HTML, reply_markup=codekey)
            
            elif callback_query.data.split('-')[0] == 'cal' and get_step(callback_query.from_user.id).split('-')[0] == 'sendcode':
                await client.delete_messages(callback_query.from_user.id, callback_query.message.id)
                id = get_step(callback_query.from_user.id).split('-')[1]
                if codelogin.get(callback_query.from_user.id) != None:
                    del codelogin[callback_query.from_user.id]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await client.send_message(callback_query.from_user.id, '⭕️ عملیات ساخت ربات باموفقیت لغو شد', reply_markup=menu)
            
            elif callback_query.data.split('-')[0] == 'an' and get_step(callback_query.from_user.id).split('-')[0] == 'sendcode':
                newid = get_step(callback_query.from_user.id).split('-')[1]
                codekey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("1️⃣", callback_data="an-1"),InlineKeyboardButton("2️⃣", callback_data="an-2"),InlineKeyboardButton("3️⃣", callback_data="an-3")]
                                ,
                        [InlineKeyboardButton("4️⃣", callback_data="an-4"),InlineKeyboardButton("5️⃣", callback_data="an-5"),InlineKeyboardButton("6️⃣", callback_data="an-6")]
                                ,
                        [InlineKeyboardButton("7️⃣", callback_data="an-7"),InlineKeyboardButton("8️⃣", callback_data="an-8"),InlineKeyboardButton("9️⃣", callback_data="an-9")]
                                ,
                        [InlineKeyboardButton("✏️", callback_data="delen"),InlineKeyboardButton("0️⃣", callback_data="an-0"),InlineKeyboardButton("✅", callback_data=f"con-{newid}")]
                                ,
                        [InlineKeyboardButton("🗑 لغو عملیات", callback_data=f"cal-{newid}")]
                    ])
                if codelogin.get(callback_query.from_user.id) == None:
                    codelogin[callback_query.from_user.id] = str(callback_query.data.split('-')[1])
                    await callback_query.edit_message_text(f'🔐 کد وارد شده :\n<code>{codelogin[callback_query.from_user.id]}</code>', parse_mode=enums.ParseMode.HTML, reply_markup=codekey)
                elif len(str(codelogin[callback_query.from_user.id])) >= 14:
                    await client.answer_callback_query(callback_query.id,'تعداد ارقام کد میبایست حتما 5 باشد!',show_alert=True)
                else:
                    codelogin[callback_query.from_user.id] = str(codelogin[callback_query.from_user.id])+' # '+str(callback_query.data.split('-')[1])
                    await callback_query.edit_message_text(f'🔐 کد وارد شده :\n<code>{codelogin[callback_query.from_user.id]}</code>', parse_mode=enums.ParseMode.HTML, reply_markup=codekey)
            
            elif get_step(callback_query.from_user.id).split('-')[0] == 'sendcode'  and callback_query.data.split('-')[0] == 'con':
                if codelogin.get(callback_query.from_user.id) != None and len(str(codelogin[callback_query.from_user.id])) >= 14:
                    await client.delete_messages(callback_query.from_user.id, callback_query.message.id)
                    try:
                        num = get_step(callback_query.from_user.id).split('-')
                        newid = int(num[1])
                        hashs = str(num[2])
                        phone = str(num[3])
                        code = str(codelogin[callback_query.from_user.id]).replace(' # ','').replace('#', '').replace(' ','')
                        Sign = await apps[newid].sign_in(phone,hashs,code)
                        if codelogin.get(callback_query.from_user.id) != None:
                            del codelogin[callback_query.from_user.id]
                        update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                        try:
                            await apps[newid].sign_up(phone, hashs, 'GoldTab')
                            await apps[newid].accept_terms_of_service(Sign.id.terms_hash)
                        except:
                            pass
                        strg = await apps[newid].export_session_string()
                        await apps[newid].disconnect()
                        join_num = [0,500,1000,1500,2000]
                        uniqueid = randint(0,len(join_num)-1)
                        num = join_num[uniqueid]
                        update_database(f"INSERT INTO `bots` VALUES('{newid}', 'no', '0', 'no', '{phone}', 'Tabchi', 'no', 'no', 'no', 'no', 'no', '{callback_query.from_user.id}', 'no','0', '0', '%E2%9D%8C', '0', 'no','{strg}','%E2%9D%8C','0','all')")
                        coun = get_data(callback_query.from_user.id)[7]
                        coun = int(coun)
                        coun += 1
                        update_database(f"UPDATE data SET coun={coun} WHERE id={callback_query.from_user.id}")
                        await client.send_message(callback_query.from_user.id,'✅ ساخت ربات شما با موفقیت انجام شد. هم اکنون میتوانید از بخش 🤖 ربات های من اقدام به مدیریت ربات خود نمایید.', reply_markup=menu)
                    except errors.SessionPasswordNeeded:
                        update_database(f"UPDATE data SET step='2fa-{newid}-{phone}' WHERE id={callback_query.from_user.id}")
                        await client.send_message(callback_query.from_user.id, '<b>🔐 تایید دو مرحله ای (Two-Step Verification)</b> اکانت خود را وارد نمایید :')
                    except errors.PhoneCodeInvalid:
                        try:
                            await apps[newid].disconnect()
                        except: 
                            pass
                        update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                        await client.send_message(callback_query.from_user.id, '<b>❌ کد ورود (Login code)</b> ارسالی اشتباه میباشد. لطفا مجددا مراحل ساخت را طی کنید :', reply_markup=menu)
                    except errors.PhoneCodeExpired:
                        try:
                            await apps[newid].disconnect()
                        except: 
                            pass
                        update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                        await client.send_message(callback_query.from_user.id, 'کد وارد شده منقضی شده است . دوباره تلاش کنید', reply_markup=menu)
                    except Exception as e:
                        try:
                            await apps[newid].disconnect()
                        except: 
                            pass
                        x = traceback.format_exc()
                        await client.send_message(856460477,f'Soomlething went wrongn :(\nerror : `{x}`')
                else:
                    await client.answer_callback_query(callback_query.id,'تعداد ارقام کد میبایست حتما 5 باشد!',show_alert=True)
            
            elif callback_query.data == 'afz':
                Afz_key = paykey = InlineKeyboardMarkup([
                    [InlineKeyboardButton("💎 ارز ترون", callback_data="Trx"),InlineKeyboardButton("💳 درگاه پرداخت", callback_data="darga")]
                    ,
                    [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
                ])
                await callback_query.edit_message_text('➕ از چه طریق میخواهید موجودی خود را افزایش دهید :', reply_markup=Afz_key)
                
            elif callback_query.data == 'Trx':
                confirm_pay = paykey = InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅ تایید تراکنش", callback_data="confirmTRX")]
                    ,
                    [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
                ])
                address = get_address(callback_query.from_user.id)
                await callback_query.edit_message_text(f'💰 به بخش افزایش موجودی با استفاده از ارز ترون وارد شدید :\n\n🌟 قیمت هر عدد ترون : `{get_price_trx()}` تومان میباشد.\n🔗 شبکه موردنظر : `TRC20`\n💲حداقل ترون جهت واریز : `5` ترون\n🌐 آدرس جهت واریزی ترون :\n`{address}`\n⚠️ پس از ارسال ترون به کیف پول بالا روی دکمه تایید تراکنش کلیک نمایید تا عملیات تکمیل شود، ترون ارسالی شما به کیف پول بالا به تومان حساب شده و به موجودی شما اضافه خواهد شد.', reply_markup=confirm_pay)
                
            elif callback_query.data == 'confirmTRX':
                full_node = "https://api.trongrid.io"
                solidity_node = "https://api.trongrid.io"
                event_server = "https://api.trongrid.io"
                tron = Tron(full_node=full_node, solidity_node=solidity_node, event_server=event_server)
                address = get_address(callback_query.from_user.id)
                balance = tron.trx.get_balance(address)
                trx_amount = (int(balance)-1200000)/1000000
                if int(trx_amount) >= 1:
                    wallet = query(f"SELECT * FROM `wallet` WHERE id={callback_query.from_user.id}")
                    tron.private_key = wallet[0][2]
                    tron.default_address = wallet[0][1]
                    try: 
                        rial = int(get_price_trx() * (trx_amount))
                        send = tron.trx.send_transaction('WALLET', trx_amount)
                        usdata = query(f'select * from `data` where `id`={callback_query.from_user.id}')
                        be = int(usdata[0][9]) + rial
                        update_database(f"update `data` set `balance` = {be} where `id`={callback_query.from_user.id}")
                        await callback_query.edit_message_text(f'✅ تراکنش باموفقیت انجام شد و {rial} تومان موجودی به حساب شما افزوده شد.', show_alert=True)
                    except Exception as e:
                        if 'balance is not sufficient.' in str(e):
                            await callback_query.answer('⛔️ هیچ ترونی به آدرس موردنظر واریز نشده است. در صورت ارسال ترون چند دقیقه دیگر مجددا تلاش نمایید.', show_alert=True)
                        else:
                            await app.send_message(callback_query.from_user.id, str(e))
                            await callback_query.answer('خطا. لطفا موضوع را به پشتیبانی اطلاع دهید', show_alert=True)
                else:
                    await callback_query.answer('⛔️ هیچ ترونی به آدرس موردنظر واریز نشده است. در صورت ارسال ترون چند دقیقه دیگر مجددا تلاش نمایید.', show_alert=True)
            
            elif callback_query.data == 'darga':
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                paykey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("💰 مبلغ دلخواه", callback_data="fave")]
                        ,
                        [InlineKeyboardButton("💰 10,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=10000"),InlineKeyboardButton("💰 15,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=15000")]
                        ,
                        [InlineKeyboardButton("💰 20,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=20000"),InlineKeyboardButton("💰 35,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=35000")]
                        ,
                        [InlineKeyboardButton("💰 50,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=50000"),InlineKeyboardButton("💰 100,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=100000")]
                        ,
                        [InlineKeyboardButton("💰 150,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=150000"),InlineKeyboardButton("💰 200,000 تومان", url=f"ADDRESS/Payment/index.php?id={callback_query.from_user.id}&amount=200000")]
                        ,
                        [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
                ])
                await callback_query.edit_message_text('⚠️ به بخش افزایش موجودی خوش امدید بر روی مبلغ دلخواه کلیک کنید سپس به صفحه پرداخت می روید و پس از پرداخت وجه اتوماتیک موجودی شما به مبلغ پرداختی افزایش پیدا میکند!\n\n✔️ تمامی پرداخت ها با درگاه امن پی پینگ صورت میگیرد!', reply_markup=paykey)
            
            elif callback_query.data == 'fave':
                update_database(f"UPDATE data SET step='afz' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("💵 لطفا مبلغ دلخواه خود را به تومان از 1,000 تا 1,000,000 وارد نمایید :", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="afz")]]))
            
            elif callback_query.data == 'back':
                await callback_query.edit_message_text( '<b>گزینه موردنظر خود را انتخاب نمایید :</b>', reply_markup=shopkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data == 'forsat' or callback_query.data.split('-')[0] == 'forsat':
                if get_data(callback_query.from_user.id)[2] != 'gold':
                    await callback_query.answer('شما حساب خریداری نکرده اید. روی دکمه خرید حساب کلیک کنید', show_alert = True)
                else:
                    try:
                        forsat = callback_query.data.split('-')[1]
                        forsat = int(forsat)
                        if forsat < 1 or forsat > 100:
                            return
                    except:
                        forsat = 1
                        
                    back = forsat - 1
                    next = forsat + 1
                    fiveb = forsat - 5
                    fiven = forsat + 5
                    
                    if forsat < 3:
                        coin = forsat * 20000
                    elif forsat >= 3 and forsat < 10:
                        coin = forsat * 19000
                    elif forsat >= 10 and forsat < 20:
                        coin = forsat * 18000
                    elif forsat >= 20 and forsat < 50:
                        coin = forsat * 17000
                    elif forsat >= 50 and forsat < 100:
                        coin = forsat * 16000
                    elif forsat >= 100:
                        coin = forsat * 15000

                    forsatkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("تعداد فرصت", callback_data="null")]
                            ,
                            [InlineKeyboardButton("-", callback_data=f"forsat-{back}"),InlineKeyboardButton(str(forsat), callback_data="null"),InlineKeyboardButton("+", callback_data=f"forsat-{next}")]
                            ,
                            [InlineKeyboardButton("- 5", callback_data=f"forsat-{fiveb}"),InlineKeyboardButton("+ 5", callback_data=f"forsat-{fiven}")]
                            ,
                            [InlineKeyboardButton(f"{coin} تومان", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data=f"bfo-{forsat}")]
                            ,
                            [InlineKeyboardButton("↪️ برگشت", callback_data="back")]
                    ])
                    await callback_query.edit_message_text( '🌀 در این بخش شما میتوانید با پرداخت کمی از موجودی حساب خود فرصت های ساخت بیشتری دریافت کنید.\n\n👇🏻 جهت افزایش موجودی حساب خود از دستورالعمل زیر استفاده نمایید :\n👈🏻 ابتدا به بخش 🛍 فروشگاه قسمت افزایش موجودی مراجعه نمایید سپس به طور دلخواه با استفاده از یکی از روش های موجود موجودی حساب خود را افزایش دهید\n-\n👈🏻 پس از رسیدن موجودی حساب به مقدار لازم به بخش فروشگاه مراجعه نمایید سپس بر روی دکمه ی خرید فرصت ساخت کلیک نمایید\n\n⭕️ نرخ خرید فرصت های بیشتر برای ساخت تبچی اضافه به شرح زیر زیر میباشد :', reply_markup=forsatkey)
            
            elif re.match('bfo-(\d+)', callback_query.data):
                num = re.findall('bfo-(\d+)', callback_query.data)[0]
                num = int(num)
                if num <= 1:
                    coin = num * 20000
                elif num >= 3 and num < 10:
                    coin = num * 19000
                elif num >= 10 and num < 20:
                    coin = num * 18000
                elif num >= 20 and num < 50:
                    coin = num * 17000
                elif num >= 50 and num < 100:
                    coin = num * 16000
                elif num >= 100:
                    coin = num * 15000
                UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                balance = int(UserData[0][9])
                if balance >= coin:
                    balance -= coin
                    coun = int(UserData[0][7])
                    coun -= num
                    update_database(f"UPDATE data SET coun={coun} WHERE id={callback_query.from_user.id}")
                    update_database(f"UPDATE data SET balance={balance} WHERE id={callback_query.from_user.id}")
                    await client.answer_callback_query(callback_query.id,f'🔖 خرید فرصت با موفقیت انجام شد و {num} فرصت ساخت به حساب شما افزوده شد و {coin} تومان از حساب شما کسر شد با ورود به بخش ساخت میتوانید اقدام به ساخت تبچی جدید نمایید!', show_alert=True)
                else:
                    await client.answer_callback_query(callback_query.id,f'❌ موجودی شما کافی نمیباشد !\nجهت خرید {num} فرصت ساخت شما نیاز به {coin} تومان موجودی دارید!\n🛍 لطفا موجودی خود را در قسمت فروشگاه افزایش دهید!',show_alert=True)
            
            elif callback_query.data.split('-')[0] == 'unf':
                ti = callback_query.data.split('-')[1]
                redy = int(ti) - int(t.time())
                if redy > -1:
                    await client.answer_callback_query(callback_query.id,f'⏰ {redy} ثانیه تا رفع محدودیت تبچی و انجام عملیات',show_alert=True)
                else:
                    await client.answer_callback_query(callback_query.id,'عملیات انجام شده است.',show_alert=True)
            
            elif callback_query.data == 'movebal':
                if int(get_data(callback_query.from_user.id)[9]) > 5999:
                    update_database(f"UPDATE data SET step='movebalance' WHERE id={callback_query.from_user.id}")
                    await client.delete_messages(callback_query.from_user.id, callback_query.message.id)
                    await client.send_message(callback_query.from_user.id, '<b>لطفا مقدار موجودی که قصد انتقال آن را دارید به صورت لاتین وارد نمایید : </b>', reply_markup=BackKey, parse_mode=enums.ParseMode.HTML)
                else:
                    await client.answer_callback_query(callback_query.id,'حداقل موجودی جهت انتفال 6,000 تومان میباشد.',show_alert=True)
            
            elif callback_query.data.split('-')[0] == 'undo':
                ti = callback_query.data.split('-')[1]
                if join[ti] != None:
                    join[ti] = False
                await callback_query.edit_message_text( '✅ عملیات در صف لغو شد.')
            
            elif callback_query.data == 'aujo':
                UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                joiner = UserData[0][10]
                if joiner == 'no':
                    forsatkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("🛍 خرید سرویس عضویت خودکار", callback_data="buyaj")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
                        ])
                    await callback_query.edit_message_text( '📍 به بخش خرید سرویس عضویت خودکار خوش امدید!\n\n⁉️ عضویت خودکار چیست :\nعضویت خودکار سرویسی است که شما با ان میتوانید گروه های تبچی خود را خودکار افزایش دهید به این صورت که تبچی به صورت خودکار در گروه ها عضو میشود و دیگر نیازی به ارسال لینک از سمت شما ندارد!\n\n⚠️ توجه داشته باشید این سرویس دائمی میباشد و با یک بار خرید از ان میتوانید در تمامی تبچی های خود برای همیشه استفاده نمایید!\n\nهزینه خرید این سرویس<code> 25 هزار تومان </code>میباشد!', parse_mode=enums.ParseMode.HTML, reply_markup=forsatkey)
                else:
                    await client.answer_callback_query(callback_query.id,'⚠️ شما قبلا این سرویس را خریداری کرده اید و نیاز به خرید مجدد نیست!',show_alert=True)
            
            elif callback_query.data == 'buyaj':
                UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                joiner = UserData[0][10]
                if joiner == 'no':
                    balance = int(UserData[0][9])
                    if balance >= 25000:
                        balance -= 25000
                        update_database(f"UPDATE data SET joiner='buyed' WHERE id={callback_query.from_user.id}")
                        update_database(f"UPDATE data SET balance={balance} WHERE id={callback_query.from_user.id}")
                        await client.answer_callback_query(callback_query.id, '✅ سرویس عضویت خودکار با موفقیت خریداری شد! هم اکنون میتوانید با ورود به بخش 🤖 ربات های من و انتخاب تبچی خود و کلیک بر روی عضویت خودکار ان را فعال نمایید!',show_alert=True)
                    else:
                        await client.answer_callback_query(callback_query.id,'⚠️ موجودی شما برای خرید این سرویس کافی نمیباشد!',show_alert=True)
                else:
                    await client.answer_callback_query(callback_query.id,'⚠️ شما قبلا این سرویس را خریداری کرده اید و نیاز به خرید مجدد نیست!',show_alert=True)
            # @DevOscar اوپن شد توسط
            elif callback_query.data.split('-')[0] == 'contact':
                id = callback_query.data.split('-')[1]
                mybot = await check_id(id, callback_query)
                contact = await mybot.invoke(functions.contacts.GetContacts(hash=0))
                await mybot.disconnect()
                keyContact = []
                for contacts in contact.users:
                    keyContact.append([InlineKeyboardButton(f"{contacts.first_name}", callback_data=f"incon-{id}-{contacts.id}"),InlineKeyboardButton("حذف مخاطب", callback_data=f"edc#{id}#{contacts.id}")])
                if len(keyContact) > 0:
                    keyContact.append([InlineKeyboardButton('برگشت', callback_data=f"bot-{id}")])
                    inikey = InlineKeyboardMarkup(keyContact)
                    await callback_query.edit_message_text('لیست مخاطبین اکانت شما :', reply_markup=inikey)  
                else:
                    await client.answer_callback_query(callback_query.id,'⚠️ هیچ مخاطبی بر روی اکانت شما وجود ندارد!',show_alert=True)
            
            elif callback_query.data == 'did':
                BotData = query(f'SELECT * FROM bots WHERE admin={callback_query.from_user.id}')
                UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                Type = UserData[0][2]
                if len(BotData) == 0 and Type == 'free':
                    await client.answer_callback_query(callback_query.id,'⚠️ شما هنوز حساب طلایی خریداری نکرده اید\n جهت خرید حساب ویژه به فروشگاه برگشته و روی دکمه خرید حساب کلیک نمایید!',show_alert=True)
                else:
                    counss = len(BotData)
                    if counss <= 3:
                        couns = 3
                    else:
                        couns = counss
                    if couns > 6:
                        day90 = couns * 48000
                        day60 = couns * 32000
                        day30 = couns * 16000
                    if couns == 6:
                        day90 = couns * 51000
                        day60 = couns * 34000
                        day30 = couns * 17000
                    elif couns == 5:
                        day90 = couns * 54000
                        day60 = couns * 36000
                        day30 = couns * 18000
                    elif couns == 4:
                        day90 = couns * 57000
                        day60 = couns * 38000
                        day30 = couns * 19000
                    else:
                        day90 = couns * 60000
                        day60 = couns * 40000
                        day30 = couns * 20000 # @DevOscar اوپن شد توسط
                    tamdidkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("تمدید 30 روزه", callback_data="did-30"),InlineKeyboardButton("تمدید 60 روزه", callback_data="did-60"),InlineKeyboardButton("تمدید 90 روزه", callback_data="did-90")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
                        ])
                    await callback_query.edit_message_text( f'🌐 به بخش تمدید حساب طلایی خوش امدید\n\nدر این بخش شما میتوانید با انتخاب مدت زمان تمدید با استفاده از موجودی حساب کاربری خود اقدام به تمدید حساب طلایی خود و استفاده از تبچی نمایید\nجهت افزایش موجودی حساب خود میتوانید بر روی بازگشت کلیک کرده و سپس روی افزایش موجودی بزنید!\n\n🔎 شما دارای {counss} تبچی میباشد و هزینه تمدید شما به شرح زیر میباشد!\n\n<code>✔️ هزینه تمدید حساب 30 روز {day30} تومان مبیاشد!\n✔️ هزینه تمدید حساب 60 روز {day60} تومان میباشد!\n✔️ هزینه تمدید حساب 90 روز {day90} تومان میباشد!</code>', parse_mode=enums.ParseMode.HTML, reply_markup=tamdidkey)
            # @DevOscar اوپن شد توسط
            elif re.match('did-(\d+)', callback_query.data):
                num = re.findall('did-(\d+)', callback_query.data)[0]
                num = int(num)
                BotData = query(f'SELECT * FROM bots WHERE admin={callback_query.from_user.id}')
                UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                Type = UserData[0][2]
                account = UserData[0][8]
                balance = int(UserData[0][9])
                if len(BotData) == 0 and Type == 'free':
                    await client.answer_callback_query(callback_query.id,'⚠️ شما هنوز حساب طلایی خریداری نکرده اید\n جهت خرید حساب ویژه به فروشگاه برگشته و روی دکمه خرید حساب کلیک نمایید!',show_alert=True)
                else:
                    counss = len(BotData)
                    if counss <= 3:
                        couns = 3
                    else:
                        couns = counss
                    if account == '0' or account == 'unlimited' or account == 'free' or int(t.time())-int(account) >= 2592000:
                        lasttime = int(t.time())
                        if num == 30:
                            time = lasttime
                            if couns > 6:
                                coin = couns * 16000
                            if couns == 6:
                                coin = couns * 17000
                            elif couns == 5:
                                coin = couns * 18000
                            elif couns == 4:
                                coin = couns * 19000
                            else:
                                coin = couns * 20000
                        elif num == 60:
                            time = lasttime + (30*24*60*60)
                            if couns > 6:
                                coin = couns * 32000
                            if couns == 6:
                                coin = couns * 34000
                            elif couns == 5:
                                coin = couns * 36000
                            elif couns == 4:
                                coin = couns * 38000
                            else:
                                coin = couns * 40000
                        elif num == 90:
                            time = lasttime + (60*24*60*60)
                            if couns > 6:
                                coin = couns * 48000
                            if couns == 6:
                                coin = couns * 51000
                            elif couns == 5:
                                coin = couns * 54000
                            elif couns == 4:
                                coin = couns * 57000
                            else:
                                coin = couns * 60000
                    else:
                        lasttime = int(account)
                        if num == 30:
                            time = lasttime + (30*24*60*60)
                            if couns > 6:
                                coin = couns * 16000
                            if couns == 6:
                                coin = couns * 17000
                            elif couns == 5:
                                coin = couns * 18000
                            elif couns == 4:
                                coin = couns * 19000
                            else:
                                coin = couns * 20000
                        elif num == 60:
                            time = lasttime + (60*24*60*60)
                            if couns > 6:
                                coin = couns * 32000
                            if couns == 6:
                                coin = couns * 34000
                            elif couns == 5:
                                coin = couns * 36000
                            elif couns == 4:
                                coin = couns * 38000
                            else:
                                coin = couns * 40000
                        elif num == 90:
                            time = lasttime + (90*24*60*60)
                            if couns > 6:
                                coin = couns * 48000
                            if couns == 6:
                                coin = couns * 51000
                            elif couns == 5:
                                coin = couns * 54000
                            elif couns == 4:
                                coin = couns * 57000
                            else:
                                coin = couns * 60000
                    if balance >= coin:
                        balance -= coin
                        update_database(f"UPDATE data SET balance={balance} WHERE id={callback_query.from_user.id}")
                        time = int(time)
                        update_database(f"UPDATE data SET account={time} WHERE id={callback_query.from_user.id}")
                        update_database(f"UPDATE data SET type='gold' WHERE id={callback_query.from_user.id}")
                        await client.answer_callback_query(callback_query.id,f'✅ حساب شما برای {num} روز تمدید شد و {coin} تومان از موجودی شما کسر شد!',show_alert=True)
                    else:
                        await client.answer_callback_query(callback_query.id,f'⚠️ موجودی حساب شما جهت تمدید {num} روز کافی نمیباشد شما به {coin} تومان موجودی نیاز دارید لطفا از بخش 🛍 فروشگاه سپس بخش افزایش موجودی، اقدام به افزایش موجودی کنید',show_alert=True)
            
            elif callback_query.data == 'by':
                p1 = 65000
                p2 = 110000
                p3 = 150000
                p4 = 160000
                p5 = 300000
                p6 = 450000
                p7 = 450000
                p8 = 900000
                p9 = 1200000
                eshkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("👤 حساب های مناسب برای افراد عادی :", callback_data="null")]
                            ,
                            [InlineKeyboardButton("♻️ عملیات", callback_data="null"),InlineKeyboardButton("💰 قیمت", callback_data="null"),InlineKeyboardButton("⚙️ فرصت", callback_data="null"),InlineKeyboardButton("⏳ مهلت", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-30"),InlineKeyboardButton(f"{p1} تومان", callback_data="null"),InlineKeyboardButton("3", callback_data="null"),InlineKeyboardButton("30 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-60"),InlineKeyboardButton(f"{p2} تومان", callback_data="null"),InlineKeyboardButton("3", callback_data="null"),InlineKeyboardButton("60 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-90"),InlineKeyboardButton(f"{p3} تومان", callback_data="null"),InlineKeyboardButton("3", callback_data="null"),InlineKeyboardButton("90 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🗣 حساب های مناسب برای افراد دارای کسب و کار :", callback_data="null")]
                            ,
                            [InlineKeyboardButton("♻️ عملیات", callback_data="null"),InlineKeyboardButton("💰 قیمت", callback_data="null"),InlineKeyboardButton("⚙️ فرصت", callback_data="null"),InlineKeyboardButton("⏳ مهلت", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-30-10"),InlineKeyboardButton(f"{p4} تومان", callback_data="null"),InlineKeyboardButton("10", callback_data="null"),InlineKeyboardButton("30 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-60-10"),InlineKeyboardButton(f"{p5} تومان", callback_data="null"),InlineKeyboardButton("10", callback_data="null"),InlineKeyboardButton("60 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-90-10"),InlineKeyboardButton(f"{p6} تومان", callback_data="null"),InlineKeyboardButton("10", callback_data="null"),InlineKeyboardButton("90 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🏢 حساب های مناسب برای تبلیغات شرکت و محصولات :", callback_data="null")]
                            ,
                            [InlineKeyboardButton("♻️ عملیات", callback_data="null"),InlineKeyboardButton("💰 قیمت", callback_data="null"),InlineKeyboardButton("⚙️ فرصت", callback_data="null"),InlineKeyboardButton("⏳ مهلت", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-30-30"),InlineKeyboardButton(f"{p7} تومان", callback_data="null"),InlineKeyboardButton("30", callback_data="null"),InlineKeyboardButton("30 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-60-30"),InlineKeyboardButton(f"{p8} تومان", callback_data="null"),InlineKeyboardButton("30", callback_data="null"),InlineKeyboardButton("60 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🛒 خرید", callback_data="by-90-30"),InlineKeyboardButton(f"{p9} تومان", callback_data="null"),InlineKeyboardButton("30", callback_data="null"),InlineKeyboardButton("90 روز", callback_data="null")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data="back")] # @Go l d T a  b B o t
                    ])
                await callback_query.edit_message_text("در این بخش شما میتوانید با استفاده از موجودی حساب کاربری خود اقدام به خرید حساب طلایی و استفاده از تبچی نمایید\nجهت افزایش موجودی حساب خود میتوانید بر روی بازگشت کلیک کرده و سپس روی افزایش موجودی بزنید!\n\n🌟قابلیت های تبچی :\n\n1️⃣ - امکان مدیریت کامل تبچی در پیوی تبچی ساز!\n2️⃣ - تغییر نام تبچی ها!\n3️⃣ - تغییر نام خانوادگی تبچی ها!\n4️⃣ - امکان تغییر بیو تبچی ها!\n5️⃣ - امکان تغییر عکس پروفایل تبچی ها!\n6️⃣ - امکان تغییر یوزرنیم تبچی!\n7️⃣ - امکان پاکسازی کانال ها - گروه ها - سوپر گروه های تبچی!\n8️⃣ - امکان مشاهده اطلاعات تبچی {شماره - نام - یوزرنیم - یوزرآیدی}!\n9️⃣ - امکان ارسال و فوروارد به {سوپرگروه - گروه - کاربر}!\n0️⃣1️⃣ - امکان اهدا تبچی به دیگران {یا همون فروش تبچی}!\n1️⃣1️⃣ - مشاهده آمار تبچی {سوپرگروه ها - کاربران - گروه ها- ربات ها - کانال ها}!\n2️⃣1️⃣ - امکان ادد کاربر در تمامی گروه ها!\n3️⃣1️⃣ - تبچی ضد دیلیت میباشد {درصورت اسپم نکردن}!\n4️⃣1️⃣ - امکان دریافت کد ورود\n\n\n⚠️ تمامی تبچی ها عضویت خودکار خواهند داشت!\n⚠️ تبچی CLI میباشد!\n⚠️ فرصت ساخت یعنی تعداد تبچی که میتوانید بسازید میباشد!\n⚠️ مهلت حساب هم یعنی مدت زمانی که وقت دارید از تبچی استفاده کنید و پس از اتمام مهلت بایستی اقدام به تمدید حساب نمایید!\n⚠️ هم اکنون میتوانید با انتخاب یکی از گزینه های زیر اقدام به خرید حساب نمایید!\n⭕️ این نکته را توجه داشته باشید! پس از خرید حساب یا ارتقا ان تمامی مهلت ها و فرصت های قبلی شما ریست خواهد شد!\n\n📨 آیدی پشتیبانی جهت پرسش سوالات :\n@Advertisingadmin3\n\n🎈 جهت خرید با دکمه های زیر اقدام نمایید",reply_markup=eshkey)
            #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif re.match('by-(\d+)', callback_query.data) or re.match('by-(\d+)-(\d+)', callback_query.data):
                if re.match('by-(\d+)-(\d+)', callback_query.data):
                    num = re.findall('by-(\d+)-(\d+)', callback_query.data)
                    day = num[0][0]
                    couns = num[0][1]
                else:
                    day = re.findall('by-(\d+)', callback_query.data)[0]
                    couns = 3
                couns = str(couns)
                if day == '30':
                    if couns == '3':
                        coin = 65000
                        time = t.time()
                    elif couns == '10':
                        coin = 160000
                        time = t.time()
                    elif couns == '30':
                        coin = 450000
                        time = t.time()
                elif day == '60':
                    if couns == '3':
                        coin = 110000
                        time = t.time() + (30*24*60*60)
                    elif couns == '10':
                        coin = 300000
                        time = t.time() + (30*24*60*60)
                    elif couns == '30':
                        coin = 900000
                        time = t.time() + (30*24*60*60)
                elif day == '90':
                    if couns == '3':
                        coin = 150000
                        time = t.time() + (60*24*60*60)
                    elif couns == '10':
                        coin = 450000
                        time = t.time() + (60*24*60*60)
                    elif couns == '30':
                        coin = 1200000
                        time = t.time() + (60*24*60*60)
                UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                Type = UserData[0][2]
                account = UserData[0][8]
                balance = int(UserData[0][9])
                time = int(time)
                if balance >= coin:
                    balance -= coin
                    counses = 3 - int(couns)
                    update_database(f"UPDATE data SET balance={balance} WHERE id={callback_query.from_user.id}")
                    update_database(f"UPDATE data SET account={time} WHERE id={callback_query.from_user.id}")
                    update_database(f"UPDATE data SET type='gold' WHERE id={callback_query.from_user.id}")
                    update_database(f"UPDATE data SET coun={counses} WHERE id={callback_query.from_user.id}")
                    await client.answer_callback_query(callback_query.id,f'✅ حساب طلایی {day} روز با فرصت ساخت {couns} عدد برای شما فعال شد و {coin} تومان از موجودی حساب شما کسر شد!',show_alert=True)
                else:
                    await client.answer_callback_query(callback_query.id,f'⚠️ موجودی حساب شما جهت خرید حساب {day} روز کافی نمیباشد شما  {coin} تومان موجودی نیاز دارید لطفا از بخش 🛍 فروشگاه سپس بخش افزایش موجودی، اقدام به افزایش موجودی کنید',show_alert=True)
            
            elif callback_query.data == 'whatstab':
                await callback_query.answer(' تبچی چیست ؟ تبچی یک ربات تبلیغگر میباشد که با عضویت در گروه های مختلف تبلیغات شمارا در سطح تلگرام منتشر میکند و خرید و بازدهی کانال شما را افزایش دهد!', show_alert = True)
            
            elif callback_query.data == 'require':
                await callback_query.answer('🌐 موارد موردنیاز جهت ساخت ربات:\n\n1 - شماره مجازی حداقل یک عدد هر کشوری\n2 - 45 هزار تومان حداقل موجودی خرید حساب', show_alert = True)
            
            elif callback_query.data == 'increasebal' or callback_query.data == 'buybal':
                await callback_query.answer('روش های افزایش موجودی :\n\n1 - کلیک بر روی دکمه بازاریابی، دعوت افراد و کسب موجودی به ازای هر نفر (1000) تومان\n2 - کلیک بر روی دکمه فروشگاه و ورود به بخش افزایش موجودی و پرداخت از طریق درگاه', show_alert = True)
            
            elif callback_query.data == 'buyhes':
                await callback_query.answer('پس از افزایش موجودی و دریافت تیک سبز در قسمت شارژ حساب، بر روی دکمه فروشگاه کلیک کنید سپس وارد قسمت خرید / ارتقا حساب شوید و روی دکمه خرید حساب کلیک نمایید.', show_alert = True)
            
            elif callback_query.data == 'makebot':
                await callback_query.answer('1 - بر روی دکمه ⚙️ ساخت ربات کلیک نمایید.\n2 - شماره اکانت خود را با کد کشور ارسال کنید.\n3 - بعد از ان کد ورود اکانت را وارد کنید تا ربات شما ساخته شود.', show_alert = True)
            
            elif callback_query.data == 'toolsbot':
                await callback_query.answer('ارسال و فوروارد خودکار - تغییر پروفایل ربات - عضویت خودکار - مخاطبین - مدیریت نشست ها - دریافت آمار دقیق - ارسال و فوروارد و پاکسازی - ادد کاربر و ...', show_alert = True)
            
            elif callback_query.data == 'forsathelp':
                await callback_query.answer('پس از خرید حساب و ساخت ربات ، شما میتوانید با خرید فرصت ساخت یک ربات اضافه ساخته و از آن استفاده نمایید برای خرید فرصت ساخت به بخش فروشگاه مراجعه نمایید.', show_alert = True)
            
            elif callback_query.data == 'tamdidhelp':
                await callback_query.answer('پس از به پایان رسیدن مهلت حساب خود، میتوانید از بخش فروشگاه و قسمت تمدید حساب آن را به مدت دلخواه تمدید نمایید.', show_alert = True)
            
            elif callback_query.data == 'managebot':
                await callback_query.answer('پس از ساخت ربات، بر روی 🤖 ربات های من کلیک نمایید سپس ربات خود را از لیست انتخاب و بر روی اسم ان کلیک نمایید تا پنل مدیریت برای شما نمایش داده شود.', show_alert = True)
            
            elif callback_query.data == 'autoHelp':
                await callback_query.answer('در پنل مدیریت ربات بر روی عضویت خودکار کلیک نمایید تا تیک سبز آن نمایش داده شود . پس از ان ربات به صورت خودکار در گروه ها عضو خواهد شد و نیاز به عضو کردن ربات در لینکدونی از سمت شما نیست.', show_alert = True)
            
            elif callback_query.data == 'ready':
                UserData = query(f"SELECT * FROM bots WHERE admin='1228635911'")
                if len(UserData) == 0:
                    await client.answer_callback_query(callback_query.id,'⚠️ هیچ تبچی برای فروش وجود ندارد!',show_alert=True)
                else:
                    await client.answer_callback_query(callback_query.id,'این بخش در حال اماده سازی میباشد. بزودی رونمایی خواهد شد',show_alert=True)
            
            elif re.match('bot-(\d+)', callback_query.data) or re.match('back-(\d+)', callback_query.data):
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                id = callback_query.data.split('-')[1]
                await callback_query.edit_message_text('🔐 به منوی مدیریت تبچی وارد شدید :', reply_markup=bot_key(id))
                
            elif re.match('bots-(\d+)', callback_query.data):
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                id = callback_query.data.split('-')[1]
                mybot = await check_id(id,callback_query)
                await mybot.disconnect()
                await callback_query.edit_message_text('🔐 به منوی مدیریت تبچی وارد شدید :', reply_markup=bot_key(id))
            
            elif callback_query.data.split('-')[0] == 'privacy' and callback_query.from_user.id in admin:
                id = callback_query.data.split('-')[1]
                mybot = await check_id(id, callback_query)
                await callback_query.edit_message_text('به منوی حریم خصوصی وارد شدید :', reply_markup=await privacy_key(id, mybot))
                
            elif callback_query.data.split('-')[0] == 'privacy':
                await callback_query.answer('این بخش در حال بروزرسانی است ...')
                
            elif callback_query.data.split('#')[0] == 'changep':
                id = callback_query.data.split('#')[1]
                type = callback_query.data.split('#')[2]
                vaz = callback_query.data.split('#')[3]
                mybot = await check_id(id, callback_query)
                if vaz == 'PrivacyValueAllowAll' or vaz == 'PrivacyValueDisallowUsers' or vaz == 'PrivacyValueDisallowContacts' or vaz == 'PrivacyValueDisallowChatParticipants':
                    vaz = types.InputPrivacyValueAllowContacts()
                elif vaz == 'PrivacyValueAllowContacts':
                    vaz = types.InputPrivacyValueDisallowAll()
                else:
                    vaz = types.InputPrivacyValueAllowAll()
                
                if type == 'invite':
                    type = types.InputPrivacyKeyChatInvite()
                elif type == 'forward':
                    type = types.InputPrivacyKeyForwards()
                elif type == 'call':
                    type = types.InputPrivacyKeyPhoneCall()
                elif type == 'phone':
                    type = types.InputPrivacyKeyPhoneNumber()
                elif type == 'photo':
                    type = types.InputPrivacyKeyProfilePhoto()
                elif type == 'seen':
                    type = types.InputPrivacyKeyStatusTimestamp()
                
                await mybot.invoke(functions.account.SetPrivacy(key=type, rules=[vaz]))
                await callback_query.edit_message_text('عملیات انجام شد :', reply_markup=await privacy_key(id, mybot)) 
            
            elif callback_query.data.split('-')[0] == 'session': # @G o l d T ab B o t
                id = callback_query.data.split('-')[1]
                mybot = await check_id(id,callback_query)
                sessions = await mybot.invoke(functions.account.GetAuthorizations())
                await mybot.disconnect()
                keysession = []
                for session in sessions.authorizations:
                    if session.password_pending == False and session.current != True:
                        keysession.append([InlineKeyboardButton(f"{session.app_name} - {session.device_model}", callback_data=f"inhash-{id}-{session.hash}"),InlineKeyboardButton("پایان نشست", callback_data=f"edj#{id}#{session.hash}")])
                if len(keysession) > 0:
                    keysession.append([InlineKeyboardButton('برگشت', callback_data=f"bot-{id}")])
                    inikey = InlineKeyboardMarkup(keysession)
                    await callback_query.edit_message_text('لیست نشست های فعال اکانت شما :', reply_markup=inikey)  
                else:
                    await client.answer_callback_query(callback_query.id,'⚠️ هیچ نشست فعالی بر روی اکانت شما وجود ندارد!',show_alert=True)
                # @DevOscar اوپن شد توسط
            elif callback_query.data.split('#')[0] == 'edj':
                id = callback_query.data.split('#')[1]
                hashs = callback_query.data.split('#')[2]
                mybot = await check_id(id,callback_query)
                try:
                    await mybot.invoke(functions.account.ResetAuthorization(hash=int(hashs)))
                    await callback_query.edit_message_text('عملیات انجام شد.', reply_markup=back_key(id))
                except (errors.SessionTooFresh, errors.FreshResetAuthorisationForbidden):
                    await callback_query.edit_message_text('شما به تازگی وارد اکانت شده اید و امکان انجام این عملیات میسر نیست.', reply_markup=back_key(id))  
                await mybot.disconnect()
            
            elif callback_query.data.split('-')[0] == 'helpsabet':
                id = callback_query.data.split('-')[1]
                await callback_query.edit_message_text( f'📌 به بخش راهنمای تبلیغ ثابت خوش آمدید :\n\n📑 راهنمای کلی : با استفاده از تبلیغات خودکار شما میتوانید تبلیغ های خود را به صورت تکرار شونده و ثابت با تبچی انجام دهید برای مثال هر 40 دقیقه به صورت نامحدود یک پیام را به گروه های تبچی فوروارد نمایید\n\n📍 راهنمای تبلیغ فوروارد خودکار : در این بخش شما میتوانید یک تبلیغ فوروارد نمایید تا ثبت شود ، تبلیغی که در این بخش ثبت میکنید پس از زمانی که در این بخش تعین میکنید به صورت خودکار به گروه ها ارسال میشود.\n\n⚠️ در صورتی که به راهنمایی بیشتر احتیاج دارید میتوانید به پشتیبانی آقای تبچی مراجعه نمایید :\n@Advertisingadmin3', reply_markup=back_sabet(id))
                
            elif callback_query.data.split('-')[0] == 'setsabet' or callback_query.data.split('#')[0] == 'adt':
                if 'adt' in callback_query.data:
                    sp = callback_query.data.split('#')
                    typ = sp[1]
                    id = sp[2]
                    num = int(sp[3])
                else:
                    id = callback_query.data.split('-')[1]
                    num = 0 
                    typ = 'no'
                
                ads = query(f"SELECT * FROM `ads` WHERE id={id} AND `admin`={callback_query.from_user.id}")
                if len(ads) > 0:
                    ad = query(f"SELECT * FROM `ads` WHERE id={id} AND `admin`={callback_query.from_user.id} AND `type` ='send'")
                    add = query(f"SELECT * FROM `ads` WHERE id={id} AND `admin`={callback_query.from_user.id} AND `type` ='forward'")
                    if len(ad) > 0 and len(add) > 0:
                        if typ == 'snd':
                            senddelay = int(ad[0][4])+num
                            if senddelay >= 5 and senddelay < 3600:
                                update_database(f"UPDATE `ads` SET `every`={senddelay} WHERE `id`={id} AND `admin`={callback_query.from_user.id} AND `type`='send'")
                            else:
                                senddelay = ad[0][4]
                            fordelay = add[0][4]
                        elif typ == 'fwd':
                            fordelay = int(add[0][4])+num
                            if fordelay >= 5 and fordelay < 3600:
                                update_database(f"UPDATE `ads` SET `every`={fordelay} WHERE `id`={id} AND `admin`={callback_query.from_user.id} AND `type`='forward'")
                            else:
                                fordelay = add[0][4]
                            senddelay = ad[0][4]
                        else:
                            senddelay = ad[0][4]
                            fordelay = add[0][4]
                        key = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("⏰ زمان ارسال خودکار :", callback_data="null")]
                                ,
                                [InlineKeyboardButton("- 5", callback_data=f"adt#snd#{id}#-5"),InlineKeyboardButton("- 1", callback_data=f"adt#snd#{id}#-1"),InlineKeyboardButton(str(senddelay), callback_data="null"),InlineKeyboardButton("+ 1", callback_data=f"adt#snd#{id}#1"),InlineKeyboardButton("+ 5", callback_data=f"adt#snd#{id}#5")]
                                ,
                                [InlineKeyboardButton("⏰ زمان فوروارد خودکار :", callback_data="null")]
                                ,
                                [InlineKeyboardButton("- 5", callback_data=f"adt#fwd#{id}#-5"),InlineKeyboardButton("- 1", callback_data=f"adt#fwd#{id}#-1"),InlineKeyboardButton(str(fordelay), callback_data="null"),InlineKeyboardButton("+ 1", callback_data=f"adt#fwd#{id}#1"),InlineKeyboardButton("+ 5", callback_data=f"adt#fwd#{id}#5")]
                                ,
                                [InlineKeyboardButton("🔙 برگشت", callback_data=f"sabet-{id}")]
                        ])
                    elif len(ad) > 0:
                        if typ == 'snd':
                            senddelay = int(ad[0][4])+num
                            if senddelay >= 5 and senddelay < 3600:
                                update_database(f"UPDATE `ads` SET `every`={senddelay} WHERE `id`={id} AND `admin`={callback_query.from_user.id} AND `type`='send'")
                            else:
                                senddelay = ad[0][4]
                        else:
                            senddelay = ad[0][4]
                        key = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("⏰ زمان ارسال خودکار :", callback_data="null")]
                                ,
                                [InlineKeyboardButton("- 5", callback_data=f"adt#snd#{id}#-5"),InlineKeyboardButton("- 1", callback_data=f"adt#snd#{id}#-1"),InlineKeyboardButton(str(senddelay), callback_data="null"),InlineKeyboardButton("+ 1", callback_data=f"adt#snd#{id}#1"),InlineKeyboardButton("+ 5", callback_data=f"adt#snd#{id}#5")]
                                ,
                                [InlineKeyboardButton("🔙 برگشت", callback_data=f"sabet-{id}")]
                        ])
                        #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
                    elif len(add) > 0:
                        if typ == 'fwd':
                            fordelay = int(add[0][4])+num
                            if fordelay >= 5 and fordelay < 3600:
                                update_database(f"UPDATE `ads` SET `every`={fordelay} WHERE `id`={id} AND `admin`={callback_query.from_user.id} AND `type`='forward'")
                            else:
                                fordelay = add[0][4]
                        else:
                            fordelay = add[0][4]
                        
                        key = InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("⏰ زمان فوروارد خودکار :", callback_data="null")]
                                ,
                                [InlineKeyboardButton("- 5", callback_data=f"adt#fwd#{id}#-5"),InlineKeyboardButton("- 1", callback_data=f"adt#fwd#{id}#-1"),InlineKeyboardButton(str(fordelay), callback_data="null"),InlineKeyboardButton("+ 1", callback_data=f"adt#fwd#{id}#1"),InlineKeyboardButton("+ 5", callback_data=f"adt#fwd#{id}#5")]
                                ,
                                [InlineKeyboardButton("🔙 برگشت", callback_data=f"sabet-{id}")]
                        ])
                    await callback_query.edit_message_text('به منوی تنظیمات خوش امید :', reply_markup=key)
                else:
                    await callback_query.answer('شما هنوز بنری ثبت نکرده اید.', show_alert=True)
            
            elif callback_query.data.split('-')[0] == 'AutoFor':
                id = callback_query.data.split('-')[1]
                ads = query(f"SELECT * FROM `banners` WHERE id={id} AND `type` = 'forward'")
                if len(ads) <= 10:
                    update_database(f"UPDATE `data` SET step='AutoAds-{id}' WHERE id={callback_query.from_user.id}")
                    await callback_query.edit_message_text('لطفا تبلیغ موردنظر خود را به اینجا فوروارد کنید :', reply_markup=back_sabet(id))
                else:
                    await callback_query.answer('شما در این بخش بیشتر از 10 بنر ثبت کرده اید و امکان ثبت بنر جدید را ندارید.', show_alert=True)
            
            elif callback_query.data.split('-')[0] == 'AutoSen':
                id = callback_query.data.split('-')[1]
                ads = query(f"SELECT * FROM `banners` WHERE id={id} AND `type` = 'send'")
                if len(ads) <= 10:
                    update_database(f"UPDATE `data` SET step='AutoSon-{id}' WHERE id={callback_query.from_user.id}")
                    await callback_query.edit_message_text('لطفا تبلیغ موردنظر خود را به اینجا ارسال کنید :', reply_markup=back_sabet(id))
                else:
                    await callback_query.answer('شما در این بخش بیشتر از 10 بنر ثبت کرده اید و امکان ثبت بنر جدید را ندارید.', show_alert=True)
            
            elif callback_query.data.split('#')[0] == 'edc':
                idd = callback_query.data.split('#')[1]
                ids = callback_query.data.split('#')[2]
                mybot = await check_id(idd, callback_query)
                try:
                    await mybot.delete_contacts(int(ids))
                    await callback_query.edit_message_text('عملیات انجام شد.', reply_markup=back_key(idd))
                except (errors.SessionTooFresh, errors.FreshResetAuthorisationForbidden):
                    await callback_query.edit_message_text('شما به تازگی وارد اکانت شده اید و امکان انجام این عملیات میسر نیست.', reply_markup=back_key(idd))
                await mybot.disconnect()
                
            elif callback_query.data.split('-')[0] == 'mysabet':
                id = callback_query.data.split('-')[1]
                botdata = query(f'SELECT * FROM `banners` WHERE id={id} AND `admin`={callback_query.from_user.id}')
                if len(botdata) > 0:
                    keyboard = []
                    for bot in botdata:
                        ty = bot[1]
                        msgid = bot[2]
                        ch = bot[3]
                        type = bot[1].replace('forward','فوروارد خودکار')
                        type = type.replace('send','ارسال خودکار')
                        if ty == 'send':
                            keyboard.append([InlineKeyboardButton("نمایش بنر", callback_data=f"showads&{id}&{ty}&{msgid}&{ch}"),InlineKeyboardButton(f"{type}", callback_data='no'),InlineKeyboardButton("❌ حذف تبلیغ", callback_data=f"delsabet&{id}&{ty}&{msgid}&{ch}")])
                        else:
                            keyboard.append([InlineKeyboardButton("نمایش بنر", url=f"https://t.me/{ch}/{msgid}"),InlineKeyboardButton(f"{type}", callback_data='no'),InlineKeyboardButton("❌ حذف تبلیغ", callback_data=f"delsabet&{id}&{ty}&{msgid}&{ch}")])
                    keyboard.append([InlineKeyboardButton("برگشت", callback_data=f"sabet-{id}")])
                    inikey = InlineKeyboardMarkup(keyboard)
                    await callback_query.edit_message_text('لیست تبلیغات ثبت شده شما :', reply_markup=inikey)  
                    keyboard = []
                else:
                    await callback_query.answer('هنوز تبلیغی ثبت نکردی ک!')
                    #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif callback_query.data.split('&')[0] == 'showads':
                id = callback_query.data.split('&')[1]
                ty = callback_query.data.split('&')[2]
                msgid = callback_query.data.split('&')[3]
                ch = callback_query.data.split('&')[4]
                await client.forward_messages(callback_query.from_user.id, ch, int(msgid))
                
            elif callback_query.data.split('&')[0] == 'delsabet':
                id = callback_query.data.split('&')[1]
                ty = callback_query.data.split('&')[2]
                msgid = callback_query.data.split('&')[3]
                ch = callback_query.data.split('&')[4]
                update_database(f"DELETE FROM `banners` WHERE `id`={id} AND `admin`={callback_query.from_user.id} AND `msgid`='{msgid}' AND `ch`='{ch}'")
                ads = query(f"SELECT * FROM `banners` WHERE id={id} AND `type` = 'send' AND `admin`={callback_query.from_user.id}")
                if len(ads) == 0:
                    update_database(f"DELETE FROM `ads` WHERE `id` = {id} AND `type`='send' AND `admin`={callback_query.from_user.id}")
                    
                ad = query(f"SELECT * FROM `banners` WHERE id={id} AND `type` = 'forward' AND `admin`={callback_query.from_user.id}")
                if len(ad) == 0:
                    update_database(f"DELETE FROM `ads` WHERE `id` = {id} AND `type`='forward' AND `admin`={callback_query.from_user.id}")
                
                await callback_query.edit_message_text('عملیات باموفقیت انجام شد.', reply_markup=back_sabet(id))
            
            elif callback_query.data.split('&')[0] == 'changesabet':
                hash = callback_query.data.split('&')[2]
                id = callback_query.data.split('&')[1]
                update_database(f"UPDATE data SET step='ojo&{id}&{hash}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text('زمان موردنظر خود را به دقیقه ارسال نمایید :', reply_markup=back_sabet(id))
            
            elif callback_query.data == 'go':
                botdata = query(f'SELECT * FROM bots WHERE admin={callback_query.from_user.id}')
                if len(botdata) > 0:
                    keyboard = []
                    for bot in botdata:
                        id = bot[0]
                        name = unquote(bot[5])
                        keyboard.append([InlineKeyboardButton(f"{name}", callback_data=f"bots-{id}"),InlineKeyboardButton("🔐  کد ورود", callback_data=f"lco-{id}"),InlineKeyboardButton("❌ حذف ربات", callback_data=f"delete-{id}")])
                    if len(botdata) >= 2:
                        keyboard.append([InlineKeyboardButton("👮🏻‍♂️ مدیریت کلی", callback_data="manageall")])
                    inikey = InlineKeyboardMarkup(keyboard)
                    await callback_query.edit_message_text('🔎 لیست ربات های شما :', reply_markup=inikey)  
                    keyboard = []
                else:
                    await callback_query.edit_message_text('🙁 هنوز ربات نساختی که!') 

            elif callback_query.data == 'manageall':
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                if (await check_id("all",callback_query)) == True:
                    bots = query(f'SELECT * FROM bots WHERE admin={callback_query.from_user.id}')
                    type = 'off'
                    emoji = '✅'
                    for bot in bots:
                        if unquote(bot[15]) == '❌':
                            type = 'on'
                            emoji = '❌'
                            break
                    manageallkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("📈 آمار کل", callback_data="allinfo"), InlineKeyboardButton("📢 پنل ارسال به پیوی", callback_data=f"panelsendtopv-all")]
                            ,
                            [InlineKeyboardButton("✉️ فوروارد", callback_data="forward-all"),InlineKeyboardButton("🚦 پاک سازی", callback_data="clean-all"),InlineKeyboardButton("📨 ارسال", callback_data="send-all")]
                            ,
                            [InlineKeyboardButton("➖ خروج از گروه", callback_data=f"left-all"),InlineKeyboardButton("➕ عضویت در گروه", callback_data=f"link-all")]
                            ,
                            [InlineKeyboardButton(f"🔗 عضویت خودکار : {emoji}", callback_data=f"ajoin-{type}")]
                            ,
                            [InlineKeyboardButton("🔙 برگشت", callback_data="go")]
                        ])
                    await callback_query.edit_message_text('🔎 به منوی مدیریت کلی تبچی ها وارد شدید:', reply_markup=manageallkey)  
            
            elif callback_query.data.split('-')[0] == 'panelsendtopv':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("☕️ به بخش ارسال به پیوی وارد شدید. لطفا گزینه موردنظر خود را انتخاب نمایید :", reply_markup=sendto_key(id), parse_mode=enums.ParseMode.HTML)
                
            elif callback_query.data.split('-')[0] == 'ltp':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='ltp-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("♻️ لطفا لینک گروه خود را به اینجا ارسال کنید :", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                
            elif callback_query.data.split('-')[0] == 'stp':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='opes-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("♻️ لطفا لینک گروه خود را به اینجا ارسال کنید :", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                
            elif callback_query.data.split('-')[0] == 'ftp':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='ftp-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("♻️ لطفا لینک گروه خود را به اینجا ارسال کنید :", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'ajoin':
                type = callback_query.data.split('-')[1]
                if type == 'on':
                    update_database(f"UPDATE bots SET joiner='%E2%9C%85' WHERE admin={callback_query.from_user.id}")
                    emoji = '✅'
                    type = 'off'
                    txt = 'عضویت خودکار با موفقیت روشن شد'
                else:
                    update_database(f"UPDATE bots SET joiner='%E2%9D%8C' WHERE admin={callback_query.from_user.id}")
                    type = 'on'
                    emoji = '❌'
                    txt = 'عضویت خودکار با موفقیت خاموش شد'
                manageallkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("📈 آمار کل", callback_data="allinfo"), InlineKeyboardButton("📢 پنل ارسال به پیوی", callback_data=f"panelsendtopv-all")]
                            ,
                            [InlineKeyboardButton("✉️ فوروارد", callback_data="forward-all"),InlineKeyboardButton("🚦 پاک سازی", callback_data="clean-all"),InlineKeyboardButton("📨 ارسال", callback_data="send-all")]
                            ,
                            [InlineKeyboardButton("➖ خروج از گروه", callback_data=f"left-all"),InlineKeyboardButton("➕ عضویت در گروه", callback_data=f"link-all")]
                            ,
                            [InlineKeyboardButton(f"🔗 عضویت خودکار : {emoji}", callback_data=f"ajoin-{type}")]
                            ,
                            [InlineKeyboardButton("🔙 برگشت", callback_data="go")]
                        ])
                await callback_query.edit_message_text('🔎 به منوی مدیریت کلی تبچی ها وارد شدید:', reply_markup=manageallkey)  
                await callback_query.answer(txt, show_alert = True)
            
            elif callback_query.data == 'allinfo':
                botdata = query(f'SELECT * FROM bots WHERE admin={callback_query.from_user.id}')
                backalls = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🔙 برگشت", callback_data="manageall")]
                ])
                if len(botdata) > 0:
                    allgp = 0
                    allsgp = 0
                    allch = 0
                    allpre = 0
                    count = 0
                    for bot in botdata:
                        id = bot[0]
                        if bot[6] != 'no':
                            allch += int(bot[8])
                            allsgp += int(bot[9])
                            allgp += int(bot[7])
                            allpre += int(bot[10])
                            count +=1
                    await callback_query.edit_message_text(f"🚦 تعداد کل تبچی ها : {count}\n\n🔻 مجموع امارها :\n🔸 تعداد سوپر گروه ها  : {allsgp}\n🔹 تعداد گروه ها : {allgp}\n🔸 تعداد کاربران : {allpre}\n🔸 تعداد کانال ها : {allch}", reply_markup=backalls)  
            
            elif callback_query.data.split('-')[0] == 'data':
                id = callback_query.data.split('-')[1]
                mybot = await check_id(id,callback_query)
                me = await mybot.get_me()
                phone = "+"+me.phone_number
                first_name = me.first_name
                if me.username != None:
                    username = "@"+me.username
                else:
                    username = "تنظیم نشده"
                bio = await mybot.get_chat("me")
                if bio.bio == None:
                    bio = 'تنظیم نشده'
                else:
                    bio = bio.bio
                userid = me.id
                nome = quote(first_name)
                update_database(f"UPDATE bots SET name='{nome}' WHERE id={id}")
                await mybot.disconnect()
                await callback_query.edit_message_text(f"🔅اطلاعات تبچی شما به شرح زیر میباشد :\n\n🔹شماره : <code>{phone}</code>\n🔸نام : <code>{first_name}</code>\n🔹یوزنیم : {username}\n🔸یوزرایدی : <code>{userid}</code>\n🔹کد پیگیری : <code>{id}</code>\n📑 بیو اکانت : <code>{bio}</code>", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'link':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='link-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("👋 سلام به بخش ارسال لینک خوش امدید!\n\n➖ توی این بخش شما میتونید با ارسال یا فوروارد لینک گروه یا کانال به این قسمت،گروه و کانال های تبچی خود را افزایش دهید!\n⚠️ توجه داشته باشید که لینک کانال و گپ سالم و ربات قبلا عضو کانال یا گپ نبوده باشد!\n\n🧐 لطفا لینک موردنظر را ارسال یا فوروارد نمایید!", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'left':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='left-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("🌐 لینک گروه و یا کانال خود را جهت خروج ارسال فرمایید :", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'name':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='name-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text(f"😆 خب نام جدید رو ارسال کن تا واست عوضش کنم!", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'pic':
                id = callback_query.data.split('-')[1]
                pickey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🗑 حذف تمامی تصاویر پروفایل", callback_data=f"dlp-{id}")]
                        ,
                        [InlineKeyboardButton("✅ انتخاب تصویر از گالری", switch_inline_query_current_chat="photo")]
                        ,
                        [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                    ])
                update_database(f"UPDATE data SET step='pic-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text(f"➕ لطفا عکس موردنظر برای پروفایل را ارسال نمایید :", reply_markup=pickey, parse_mode=enums.ParseMode.HTML)
                #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
            elif callback_query.data.split('-')[0] == 'dlp':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("درحال انجام عملیات ...", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                mybot = await check_id(id,callback_query)
                photos = await mybot.get_profile_photos("me")
                await mybot.delete_profile_photos([p.file_id for p in photos[0:]])
                await mybot.disconnect()
                await callback_query.edit_message_text("عملیات انجام شد.", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'invite':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='invite-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("🌟جهت ادد کاربر به تمام گروه ها یوزرنیم فرد را با @ ارسال نمایید :", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'add':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='add-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("☺️ خب حالا لینک گروه یا ایدی عددی گروه را ارسال نمایید!", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'lco':
                try:
                    id = callback_query.data.split('-')[1]
                    if get_bot(id)[11] == str(callback_query.from_user.id):
                        if True == True:
                            biokey = InlineKeyboardMarkup(
                                [
                                    [InlineKeyboardButton("🔁 بروزرسانی مجدد", callback_data=f"lco-{id}")]
                                    ,
                                    [InlineKeyboardButton("برگشت", callback_data="go")]
                                ])
                            await callback_query.edit_message_text(f"درحال انجام عملیات ...", reply_markup=biokey, parse_mode=enums.ParseMode.HTML)
                            mybot = await check_id(id,callback_query)
                            result = mybot.get_chat_history(777000, limit=1)
                            async for msg in result:
                                try:
                                    result = msg.text
                                    if result != None:
                                        if "Login code:" in result:
                                            code = result.split(': ')[1].split('.')[0]
                                        elif "Web login code" in result:
                                            code = result.split('code:')[1].split('\n')[1]
                                        else:
                                            code = "یافت نشد"
                                    else:
                                        code = "یافت نشد"
                                except:
                                    code = "یافت نشد"
                            await mybot.disconnect()
                            phone = get_bot(id)[4]
                            await callback_query.edit_message_text(f"☎️ شماره اکانت شما : <code>{phone}</code>\n🔐 آخرین کد ورود به اکانت : <code>{code}</code>", reply_markup=biokey, parse_mode=enums.ParseMode.HTML)
                        else:
                            await client.answer_callback_query(callback_query.id,'⚠️ هشدار کاربر گرامی تبچی شما مربوط به ورژن قبلی تبچی ساز میباشد و امکان مدیریت این تبچی وجود ندارد. هر چه سریع تر اقدام به حذف تبچی و دریافت فرصت نمایید.',show_alert=True)
                    else:
                        await app.edit_message_text(callback_query.from_user.id, callback_query.message.id,'⚙️ این تبچی در لیست ربات های شما وجود ندارد!')
                except:
                    await app.send_message(callback_query.from_user.id,traceback.format_exc())
            
            elif callback_query.data.split('-')[0] == 'bio':
                id = callback_query.data.split('-')[1]
                biokey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🗑 حذف بیو", callback_data=f"dlb-{id}")]
                        ,
                        [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                    ])
                update_database(f"UPDATE data SET step='bio-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text(f"😁 خب بیو خودت رو ارسال کن 70 کاراکتر باشه وگرنه تغییر نمیکنه!", reply_markup=biokey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'ifk':
                id = callback_query.data.split('-')[1]
                bot = get_bot(id)
                if bot[11] == '00000000':
                    bot = get_bot(id)
                    info = {}
                    info['bot'] = bot[6]
                    info['channel'] = bot[8]
                    info['supergroup'] = bot[9]
                    info['private'] = bot[10]
                    info['group'] = bot[7]
                    UserData = query(f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                    account = get_data(callback_query.from_user.id)[8]
                    times = int(t.time())
                    firstp = 30000
                    
                    if account == 'unlimited' or account == 'free' or int(account) == 0:
                        price = number_format(firstp+45000)
                        txt = f'اطلاعات اکانت :\n\nتعداد سوپرگروه ها : {bot[9]}\nتعداد گروه ها : {bot[7]}\nتعداد کانال ها : {bot[8]}\nتعداد پیوی ها : {bot[10]}\n\nهزینه خرید اکانت + حساب 30 روزه : {price} تومان'
                    elif times - int(account) >= 2592000:
                        price = number_format(firstp+45000)
                        txt = f'اطلاعات اکانت :\n\nتعداد سوپرگروه ها : {bot[9]}\nتعداد گروه ها : {bot[7]}\nتعداد کانال ها : {bot[8]}\nتعداد پیوی ها : {bot[10]}\n\nهزینه خرید اکانت + حساب 30 روزه : {price} تومان'
                    elif UserData[0][2] == 'gold':
                        price = number_format(firstp)
                        txt = f'اطلاعات اکانت :\n\nتعداد سوپرگروه ها : {bot[9]}\nتعداد گروه ها : {bot[7]}\nتعداد کانال ها : {bot[8]}\nتعداد پیوی ها : {bot[10]}\n\nهزینه خرید اکانت : {price} تومان'
                    await client.answer_callback_query(callback_query.id,txt,show_alert=True)
                else:
                    await callback_query.edit_message_text('<b>اکانت موردنظر در حال حاضر در دسترس نمیباشد، لطفا دوباره تلاش کنید.</b>', parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'buk':
                id = callback_query.data.split('-')[1]
                bot = get_bot(id)
                if bot[11] == '00000000':
                    bot = get_bot(id)
                    UserData = query(
                        f'SELECT * FROM data WHERE id={callback_query.from_user.id}')
                    account = get_data(callback_query.from_user.id)[8]
                    times = int(t.time())
                    firstp = 30000
                        
                    if account == 'unlimited' or account == 'free' or int(account) == 0:
                        price = firstp+45000
                    elif times - int(account) >= 2592000:
                        price = firstp+45000
                    elif UserData[0][2] == 'gold':
                        price = firstp
                    if int(UserData[0][9]) > price:
                        Nbal =  int(UserData[0][9]) - price
                        update_database(f"UPDATE data SET balance={Nbal} WHERE id={callback_query.from_user.id}")
                        if times - int(account) >= 2592000:
                            update_database(f"UPDATE data SET type='gold' WHERE id={callback_query.from_user.id}")
                            tom = int(t.time())
                            update_database(f"UPDATE data SET account='0' WHERE id={callback_query.from_user.id}")
                        elif account == 'unlimited' or account == 'free' or int(account) == 0:
                            update_database(f"UPDATE data SET type='gold' WHERE id={callback_query.from_user.id}")
                            tom = int(t.time())
                            update_database(f"UPDATE data SET account='0' WHERE id={callback_query.from_user.id}")
                        update_database(f"UPDATE bots SET admin={callback_query.from_user.id} WHERE id={id}")
                        await callback_query.edit_message_text('عملیات باموفقیت انجام شد و اکانت به بخش 🤖 ربات های من افزوده شد.')
                        await client.send_message(856460477,f"[{callback_query.from_user.id}](tg://user?id={callback_query.from_user.id})\nاین کاربر اکانت خریداری کرد", parse_mode="markdown")
                    else:
                        forp = number_format(price)
                        await client.answer_callback_query(callback_query.id,f'موجودی شما کافی نیست، موجودی موردنیاز : {forp} تومان',show_alert=True)
                else:
                    await callback_query.edit_message_text('<b>اکانت موردنظر در حال حاضر در دسترس نمیباشد، لطفا دوباره تلاش کنید.</b>', parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'shop':
                id = callback_query.data.split('-')[1]
                mybot = await check_id(id,callback_query)
                await mybot.disconnect()
                update_database(f"UPDATE data SET step='shop-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text('🚦 لطفا شناسه عددی حساب کاربر را جهت اهدای تبچی ارسال نمایید!\n😄 عملیات اهدای تبچی برگشت پذیر نمیباشد!', reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'dlb':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("درحال انجام عملیات ...", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                mybot = await check_id(id,callback_query)
                await mybot.update_profile(bio="")
                await mybot.disconnect()
                await callback_query.edit_message_text("عملیات انجام شد.", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'username':
                id = callback_query.data.split('-')[1]
                userkey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🗑 حذف نام کاربری", callback_data=f"dlu-{id}")]
                        ,
                        [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                    ])
                update_database(f"UPDATE data SET step='username-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text(f"☺️ خب نام کاربری جدید رو ارسال کن اول مطمِن شو که  یوزرنیم آزاد باشه وگرنه عوض نمیشه!", reply_markup=userkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'dlu':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("درحال انجام عملیات ...", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                mybot = await check_id(id,callback_query)
                await mybot.set_username("")
                await mybot.disconnect()
                await callback_query.edit_message_text("عملیات انجام شد.", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'clean':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='clean-{id}' WHERE id={callback_query.from_user.id}")
                if id != 'all':
                    forwardkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("همه", callback_data=f"cln-all-{id}")]
                            ,
                            [InlineKeyboardButton("گروه", callback_data=f"cln-group-{id}"),InlineKeyboardButton("سوپرگروه", callback_data=f"cln-supergroup-{id}"),InlineKeyboardButton("کانال", callback_data=f"cln-channel-{id}")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data=f"bot-{id}")]
                    ])
                else:
                    forwardkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("همه", callback_data=f"cln-all-{id}")]
                            ,
                            [InlineKeyboardButton("گروه", callback_data=f"cln-group-{id}"),InlineKeyboardButton("سوپرگروه", callback_data=f"cln-supergroup-{id}"),InlineKeyboardButton("کانال", callback_data=f"cln-channel-{id}")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data='manageall')]
                    ])
                await callback_query.edit_message_text("🧐 خب دلت میخواد کدوما رو پاکسازی کنی؟ً!", reply_markup=forwardkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data == 'cancel':
                await client.delete_messages(callback_query.from_user.id, callback_query.message.id)
                await client.send_message(callback_query.from_user.id,f"عملیات لغو شد، به منوی اصلی برگشتید:", reply_markup=menu)
            
            elif callback_query.data.split('-')[0] == 'dlt':
                id = callback_query.data.split('-')[1]
                i = query(f'SELECT * FROM bots WHERE id={id} AND admin={callback_query.from_user.id}')
                if len(i) > 0:
                    coun = get_data(callback_query.from_user.id)[7]
                    coun = int(coun)
                    coun -= 1
                    update_database(f"UPDATE data SET coun={coun} WHERE id={callback_query.from_user.id}")
                    update_database(f'DELETE FROM `bots` WHERE id={id}')
                    update_database(f'DELETE FROM `ads` WHERE id={id}')
                    update_database(f'DELETE FROM `auto` WHERE id={id}')
                    await callback_query.edit_message_text('عملیات باموفقیت انجام شد، فرصت ساخت ربات به شما برگشت داده شد.', parse_mode=enums.ParseMode.HTML)
                else:
                    await callback_query.edit_message_text('⚠️ خطا، امکان حذف این ربات وجود ندارد!', parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'cln':
                id = callback_query.data.split('-')[2]
                type = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("درحال انجام عملیات ...", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                if id != 'all':
                    mybot = await check_id(id,callback_query)
                    users = mybot.get_dialogs()
                    async for it in users:
                        try:
                            if type == 'all' or it.chat.type == getattr(enums.ChatType, type.upper()):
                                await mybot.leave_chat(it.chat.id)
                        except Exception as e:
                            if "[420 FLOOD_WAIT_X]" in str(e):
                                e = str(e)
                                flood = e.split(' seconds')[0].split('of ')[1]
                                await client.send_message(callback_query.from_user.id,f"⚠️ متاسفانه تبچی شما محدود میباشد و امکان فوروارد پیام تا {flood} ثانیه دیگر را ندارد لطفا بعد از {flood} ثانیه اقدام نمایید!", reply_markup=back_key(id))
                                break
                            elif "[400 PEER_ID_INVALID]" in str(e):
                                continue
                            elif "Client has not been started yet" in str(e):
                                await ConnectingBot(mybot)
                                continue
                            elif "database is locked" in str(e):
                                await ConnectingBot(mybot)
                                continue
                            elif "[400 CHANNEL_PRIVATE]" in str(e):
                                continue
                            elif "USER_NOT_PARTICIPANT" in str(e):
                                continue
                            else:
                                x = traceback.format_exc()
                                await client.send_message(856460477,f'Soomlething went wrongf :(\nerror : `{x}`')
                    await mybot.disconnect()
                else:
                    backkeyb = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("🔙 برگشت", callback_data="manageall")]
                        ])
                    botdata = query(f'SELECT * FROM bots WHERE admin={callback_query.from_user.id} AND `pyro` != "no"')
                    if len(botdata) > 0:
                        for bot in botdata:
                            one_id = bot[0]
                            mybot = await check_id(one_id,callback_query)
                            users = mybot.get_dialogs()
                            async for it in users:
                                try:
                                    if type == 'all' or it.chat.type == getattr(enums.ChatType, type.upper()):
                                        await mybot.leave_chat(it.chat.id)
                                except Exception as e:
                                    if "[420 FLOOD_WAIT_X]" in str(e):
                                        e = str(e)
                                        flood = e.split(' seconds')[0].split('of ')[1]
                                        break
                                    elif "[400 PEER_ID_INVALID]" in str(e):
                                        continue
                                    elif "[400 CHANNEL_PRIVATE]" in str(e):
                                        continue
                                    elif "database is locked" in str(e):
                                        continue
                                    elif "Client has not been started yet" in str(e):
                                        continue
                                    elif "[401 AUTH_KEY_UNREGISTERED]:" in str(e) or "[401 USER_DEACTIVATED]:" in str(e) or "[401 USER_DEACTIVATED_BAN]:" in str(e) or "[401 SESSION_EXPIRED]:" in str(e) or "[401 SESSION_REVOKED]:" in str(e):
                                            break
                                    else:
                                        x = traceback.format_exc()
                                        await client.send_message(856460477,f'Soomlething went wrongd :(\nerror : `{x}`')
                                        break
                            await mybot.disconnect()
                await callback_query.edit_message_text("عملیات انجام شد.", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'forward':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='forward-{id}' WHERE id={callback_query.from_user.id}")
                if id != 'all':
                    forwardkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("همه", callback_data=f"fwd-all-{id}")]
                            ,
                            [InlineKeyboardButton("گروه", callback_data=f"fwd-group-{id}"),InlineKeyboardButton("سوپرگروه", callback_data=f"fwd-supergroup-{id}"),InlineKeyboardButton("کاربر", callback_data=f"fwd-private-{id}")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data=f"bot-{id}")]
                    ])
                else:
                    forwardkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("همه", callback_data=f"fwd-all-{id}")]
                            ,
                            [InlineKeyboardButton("گروه", callback_data=f"fwd-group-{id}"),InlineKeyboardButton("سوپرگروه", callback_data=f"fwd-supergroup-{id}"),InlineKeyboardButton("کاربر", callback_data=f"fwd-private-{id}")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data='manageall')]
                    ])
                await callback_query.edit_message_text("🧐 خب دلت میخواد پیام رو به کیا فوروارد کنی؟ً!", reply_markup=forwardkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'fwd':
                id = callback_query.data.split('-')[2]
                update_database(f"UPDATE data SET step='{callback_query.data}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("😜 پیامتو فور بده اینجا که فور بدم", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'pat':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                passkey = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("❌ غیرفعال سازی", callback_data=f"dpp-{id}"),InlineKeyboardButton("✅ فعال سازی", callback_data=f"enablepass-{id}")]
                            ,
                    [InlineKeyboardButton("🔙 بازگشت", callback_data=f"bot-{id}")]
                ])
                await callback_query.edit_message_text('✔️ لطفا گزینه موردنظر خود را انتخاب نمایید :', reply_markup=passkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'help':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                passkey = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔙 بازگشت", callback_data=f"bot-{id}")]
                ])
                await callback_query.edit_message_text('➕ در این قسمت میتوانید راهنمای بخش ها را مطالعه نمایید و سوالات و مشکلات خود را از پشتیبانی بپرسید!\n\n\n➖ بخش آمار\nدر این بخش شما میتوانید امار تبچی خود (تعداد گروه ها - سوپرگروه ها - ربات ها - کانال ها - پیوی ها)  را مشاهده نمایید!\n\n➖ بخش حذف تبچی\nشما در این بخش میتوانید تبچی خود را حذف نمایید و یک فرصت ساخت دریافت نمایید!\nتوجه داشته باشید که حذف تبچی به معنا دیلیت اکانت نیست و فقط اکانت و تبچی شما از روی سرور ما پاک خواهد شد!\n\n➖ بخش پاک سازی\nدر این بخش شما میتوانید کانال ها و گروه ها و سوپرگروه های تبچی خود را پاکسازی کنید ! پاکسازی به معنای لفت دادن تبچی از گروه ها و سوپرگروه ها و کانال ها میباشد!\n\n➖ بخش ارسال\nدر این بخش شما میتوانید متن موردنظر خود را به گروه ها و سوپرگروه ها و یا پیوی ها با تبچی خود ارسال نمایید!\n\n➖ بخش فوروارد\nدر این بخش شما میتوانید بنر خود را به گروه ها و سوپرگروه ها و پیوی ها با تبچی خود ارسال نمایید!\n\n➖ بخش تغییر نام خانوادگی\nشما در این بخش میتوانید نام خانوادگی اکانت تبچی خود را تغییر بدهید!\n\n➖ بخش تغییر بیو\nشما در این بخش میتوانید بیو اکانت تبچی خود را تغییر بدهید!\n\n➖ بخش تغییر نام\nشما در این بخش میتوانید نام اکانت تبچی خود را تغییر بدهید!\n\n➖ بخش تغییر نام کاربری\nشما در این بخش میتوانید نام کاربری اکانت تبچی خود را تغییر دهید!\n\n➖ بخش اطلاعات تبچی\nشما در این بخش میتوانید اطلاعات اکانت تبچی (نام تبچی - نام خانوادگی تبچی - شماره - یوزرنیم - یوزر ایدی و کد پیگیری) را مشاهده نمایید!\n\n➖ بخش تایید دو مرحله ای\nدر این بخش شما میتوانید تایید دو مرحله ای اکانت خود را فعال و یا غیرفعال نمایید. (برای ورود به اکانت پسورد قرار دهید)\n\n➖ بخش ارسال لینک\nشما در این بخش میتوانید با ارسال لینک سوپرگروه تبچی خود را عضو ان گروه نمایید!\n\n➖ بخش اهدای تبچی\nشما در این بخش میتوانید تبچی خود را به سایر کاربران اهدا کنید!\n➖ بخش تنظیم تصویر پروفایل\nشما میتوانید در این بخش عکس پروفایل اکانت تبچی خود را تغییر دهید!\n\n➖ بخش افزودن کاربر به گپ ها\nشما در این بخش میتوانید با ارسال یوزر ایدی یا یوزرنیم یک فرد ، ان فرد را عضو تمام گروه های تبچی نمایید!\n\n➖ بخش افزودن عضو به گروه\nشما میتوانید با ارسال لینک گپ خود در این بخش تمام کاربران تبچی خود را به گروه اضافه کنید! توجه داشته باشید تبچی باید عضو گروهی که لینک ان را ارسال میکنید باشه!\n\n➖ بخش دریافت کد ورود\nشما در این بخش میتوانید کد ورودی که 15 دقیقه اخیر به اکانت ارسال شده است را دریافت نمایید!\n\n➖ بخش عضویت خودکار\nبا فعال سازی این بخش تبچی ها به طور خودکار در گروه ها عضو میشوند و دیگر نیاز به ارسال لینک نیست!\n\n⁉️ در صورت داشتن مشکل و یا سوال میتوانید ان را با ما در میان بگذارید!\n@Advertisingadmin3', reply_markup=passkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'sabet':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text('👈 به منوی تبلیغات ثابت خوش آمدید :', reply_markup=sabet_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'send':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='send-{id}' WHERE id={callback_query.from_user.id}")
                if id != 'all':
                    forwardkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("همه", callback_data=f"snd-all-{id}")]
                            ,
                            [InlineKeyboardButton("گروه", callback_data=f"snd-group-{id}"),InlineKeyboardButton("سوپرگروه", callback_data=f"snd-supergroup-{id}"),InlineKeyboardButton("کاربر", callback_data=f"snd-private-{id}")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data=f"bot-{id}")]
                        ])
                else:
                    forwardkey = InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("همه", callback_data=f"snd-all-{id}")]
                            ,
                            [InlineKeyboardButton("گروه", callback_data=f"snd-group-{id}"),InlineKeyboardButton("سوپرگروه", callback_data=f"snd-supergroup-{id}"),InlineKeyboardButton("کاربر", callback_data=f"snd-private-{id}")]
                            ,
                            [InlineKeyboardButton("🔙 بازگشت", callback_data='manageall')]
                        ])
                await callback_query.edit_message_text("🧐 خب دلت میخواد پیام رو به کیا بفرستی؟ً!", reply_markup=forwardkey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'delete':
                id = callback_query.data.split('-')[1]
                i = query(f'SELECT * FROM bots WHERE id={id} AND admin={callback_query.from_user.id}')
                if len(i) > 0:
                    deletekey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("بله", callback_data=f"dlt-{id}"),InlineKeyboardButton("خیر", callback_data='cancel')]
                    ])
                    await callback_query.edit_message_text("🥳 آیا اطمینان دارید؟!", reply_markup=deletekey, parse_mode=enums.ParseMode.HTML)
                else:
                    await callback_query.edit_message_text('⚠️ خطا، امکان حذف این ربات وجود ندارد!', parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'snd':
                id = callback_query.data.split('-')[2]
                update_database(f"UPDATE data SET step='{callback_query.data}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("😊 متن پیامت رو بفرست که ارسال کنم", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'jop':
                id = callback_query.data.split('-')[1]
                botdata = get_bot(id)
                if botdata[15] == '%E2%9D%8C':
                    await callback_query.edit_message_text('🌐 لطفا نوع گروه هایی که میخواهید تبچی شما در آن عضو شود انتخاب نمایید :', reply_markup=joiner_type(id))
                else:
                    update_database(f"UPDATE bots SET joiner='%E2%9D%8C' WHERE id={id}")
                    await client.answer_callback_query(callback_query.id, '❌ عضویت خودکار تبچی شما با موفقیت خاموش شد!', show_alert=True)
                    await app.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id, bot_key(id))
                    
            elif callback_query.data.split('-')[0] == 'opjo':
                st = callback_query.data.split('-')
                typ = st[1]
                id = st[2]
                if get_bot(id)[21] != typ:
                    if typ == 'all':
                        update_database(f"UPDATE bots SET `joinnum` = '2500' WHERE id={id}")
                    else:
                        update_database(f"UPDATE bots SET `joinnum` = '0' WHERE id={id}")
                update_database(f"UPDATE bots SET `joiner` = '%E2%9C%85', `joinertype` = '{typ}' WHERE id={id}")
                await client.answer_callback_query(callback_query.id, '✅ عضویت خودکار تبچی شما با موفقیت روشن شد!', show_alert=True)
                await app.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id, bot_key(id))
            
            elif callback_query.data.split('-')[0] == 'aucht':
                id = callback_query.data.split('-')[1]
                botdata = get_bot(id)
                if botdata[18] == 'off':
                    update_database(f"UPDATE bots SET autochat='on' WHERE id={id}")
                    await client.answer_callback_query(callback_query.id, '✅ چت خودکار تبچی شما با موفقیت روشن شد!', show_alert=True)
                    await app.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id, bot_key(id))
                else:
                    update_database(f"UPDATE bots SET autochat='off' WHERE id={id}")
                    await client.answer_callback_query(callback_query.id, '❌ چت خودکار تبچی شما با موفقیت خاموش شد!', show_alert=True)
                    await app.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id, bot_key(id))
            
            elif callback_query.data.split('-')[0] == 'addcont':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='addcont-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("لطفا نام کاربری یا شناسه عددی اکانتی که میخواهید به مخاطبین اضافه نمایید را ارسال کنید :", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'family':
                id = callback_query.data.split('-')[1]
                familykey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🗑 حذف نام خانوادگی", callback_data=f"dlf-{id}")]
                        ,
                        [InlineKeyboardButton("برگشت", callback_data=f"bot-{id}")]
                    ])
                update_database(f"UPDATE data SET step='last-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("😌 خب ی نام خانوادگی بفرست واست عوضش کنم!", reply_markup=familykey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'enablepass':
                id = callback_query.data.split('-')[1]
                familykey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("برگشت", callback_data=f"pat-{id}")]
                    ])
                update_database(f"UPDATE data SET step='enablepass-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("🔗 لطفا پسورد موردنظر خود را جهت فعال سازی تایید دو مرحله ای ارسال نمایید :", reply_markup=familykey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'dpp':
                id = callback_query.data.split('-')[1]
                familykey = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("برگشت", callback_data=f"pat-{id}")]
                    ])
                update_database(f"UPDATE data SET step='dpp-{id}' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("🔗 لطفا پسورد فعلی را جهت غیرفعال سازی تایید دو مرحله ای ارسال نمایید :", reply_markup=familykey, parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'dlf':
                id = callback_query.data.split('-')[1]
                update_database(f"UPDATE data SET step='no' WHERE id={callback_query.from_user.id}")
                await callback_query.edit_message_text("درحال انجام عملیات ...", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                mybot = await check_id(id,callback_query)
                await mybot.update_profile(last_name="")
                await mybot.disconnect()
                await callback_query.edit_message_text("عملیات انجام شد.", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
            
            elif callback_query.data.split('-')[0] == 'info':
                id = callback_query.data.split('-')[1]
                if 1 > 0:
                    if int(get_bot(id)[2]) <= int(t.time()):
                        await callback_query.edit_message_text("درحال انجام عملیات ...", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                        mybot = await check_id(id,callback_query)
                        users = mybot.get_dialogs()
                        info = {}
                        info[enums.ChatType.BOT] = 0
                        info[enums.ChatType.CHANNEL] = 0
                        info[enums.ChatType.SUPERGROUP] = 0
                        info[enums.ChatType.PRIVATE] = 0
                        info[enums.ChatType.GROUP] = 0
                        async for it in users:
                            info[it.chat.type] += 1
                        await mybot.disconnect()
                        newtime = int(t.time()) + 600
                        botam = info[enums.ChatType.BOT]
                        cham = info[enums.ChatType.CHANNEL]
                        supam = info[enums.ChatType.SUPERGROUP]
                        pram = info[enums.ChatType.PRIVATE]
                        gram = info[enums.ChatType.GROUP]
                        update_database(f"UPDATE bots SET bots={botam} WHERE id={id}")
                        update_database(f"UPDATE bots SET channels={cham} WHERE id={id}")
                        update_database(f"UPDATE bots SET supergroups={supam} WHERE id={id}")
                        update_database(f"UPDATE bots SET users={pram} WHERE id={id}")
                        update_database(f"UPDATE bots SET `groups`={gram} WHERE id={id}")
                        update_database(f"UPDATE bots SET timegetinfo={newtime} WHERE id={id}")
                        uptime = 'هم اکنون'
                    else:
                        bot = get_bot(id)
                        info = {}
                        info[enums.ChatType.BOT] = bot[6]
                        info[enums.ChatType.CHANNEL] = bot[8]
                        info[enums.ChatType.SUPERGROUP] = bot[9]
                        info[enums.ChatType.PRIVATE] = bot[10]
                        info[enums.ChatType.GROUP] = bot[7]
                        uptime = int(bot[2])-600
                        uptime = datetime.fromtimestamp(uptime).strftime('%H:%M')
                    nexts = datetime.fromtimestamp(int(get_bot(id)[2])).strftime('%H:%M')
                    botdata = get_bot(id)
                    name = unquote(botdata[5])
                    limit = botdata[13]
                    if int(limit) > int(t.time()):
                        limi = datetime.fromtimestamp(int(limit)).strftime('%H:%M')
                        await callback_query.edit_message_text(f"✅ آمار ربات {name} : \n\n👤 کاربران : <code>{info[enums.ChatType.PRIVATE]}</code> عدد\n🤖 ربات ها : <code>{info[enums.ChatType.BOT]}</code> عدد\n👥 سوپر گروه ها : <code>{info[enums.ChatType.SUPERGROUP]}</code> عدد\n🫂 گروه ها : <code>{info[enums.ChatType.GROUP]}</code> عدد\n📣 کانال ها : <code>{info[enums.ChatType.CHANNEL]}</code> عدد  \n\n‼️ تبچی شما دارای محدودیت عضویت میباشد. محدودیت در <code>{limi}</code> رفع خواهد شد\n♨️ هر 10 دقیقه یک بار آمار تبچی شما بروزرسانی میشود!\n🔄 بروزرسانی مجدد در {nexts}", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
                    else:
                        await callback_query.edit_message_text(f"✅ آمار ربات {name} : \n\n👤 کاربران : <code>{info[enums.ChatType.PRIVATE]}</code> عدد\n🤖 ربات ها : <code>{info[enums.ChatType.BOT]}</code> عدد\n👥 سوپر گروه ها : <code>{info[enums.ChatType.SUPERGROUP]}</code> عدد\n🫂 گروه ها : <code>{info[enums.ChatType.GROUP]}</code> عدد\n📣 کانال ها : <code>{info[enums.ChatType.CHANNEL]}</code> عدد  \n\n♨️ هر 10 دقیقه یک بار آمار تبچی شما بروزرسانی میشود!\n🔄 بروزرسانی مجدد در {nexts}", reply_markup=back_key(id), parse_mode=enums.ParseMode.HTML)
        
        except:
            pass
    app.run()
except Exception as e:
    print(traceback.format_exc())
    pass
    
#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل