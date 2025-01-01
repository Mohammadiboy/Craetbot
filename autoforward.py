#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل


from pyrogram import Client, filters, errors, enums
import mysql.connector
import sys, os, signal
from urllib.parse import unquote, quote
import asyncio
from random import randint, choice, uniform
import time
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputTextMessageContent, InlineQueryResultArticle)
import re
from urllib.parse import unquote, quote

mydb = mysql.connector.Connect(
    host='localhost',
    user='',
    password='',
    database=''
) #اطلاعات دیتابیس
mydb.commit()
mycu = mydb.cursor()
mydb.autocommit = True

def query(q):
    global mycu, mydb
    mydb = mysql.connector.Connect(
        host='localhost',
        user='',
        password='',
        database=''
    ) #اطلاعات دیتابیس
    mydb.commit()
    mycu = mydb.cursor()
    mydb.autocommit = True
    mycu.execute(q)
    return mycu.fetchall()
    
def upq(q):
    global mycu,mydb
    mydb = mysql.connector.Connect(
        host='localhost',
        user='',
        password='',
        database=''
    ) #اطلاعات دیتابیس
    mydb.commit()
    mycu = mydb.cursor()
    mydb.autocommit = True
    mycu.execute(q)
    mydb.commit()

def get_step(id):
    try:
        return query(f'SELECT * FROM `data` WHERE `id`={id}')[0][1]
    except:
        return 'no'

app_id = #app id
app_hash = '' #app hash
app = Client('AutoForwards',app_id,app_hash,bot_token="TOKEN") #توکن اتوفوروارد
admin = [00000000] #ایدی عددی ادمین

menu = ReplyKeyboardMarkup(
        [
            [
                "📢 ثبت کانال"
            ],
            [
                "⚙️ تنظیمات",
                "❌ حذف کانال"
            ],
            [
                "⚖️ قوانین ربات",
                "📚 راهنمای ربات"
            ]
    ],resize_keyboard=True
)

back = ReplyKeyboardMarkup(
        [
            [
                "🔙 بازگشت"
            ]
    ],resize_keyboard=True
)
#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل
def get_string(id):
        return query(f'SELECT * FROM `bots` WHERE `id`={id}')[0][18]

async def check_status(chatid,userid):
    try:
        return (await app.get_chat_member(chatid, userid)).status in [enums.ChatMemberStatus.OWNER,enums.ChatMemberStatus.ADMINISTRATOR]
    except:
        return False

@app.on_message(filters.private & filters.regex('/reload'))
async def reloadingbot(client,message):
    await message.reply('reloaded!')
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@app.on_message(filters.channel)
async def Forwarding(client,message):
    username = message.chat.username.lower()
    check = query(f"SELECT * FROM `channels` WHERE `username`='{username}'")
    if len(check) > 0:
        for data in check:
            admin = data[1]
            admindata = query(f"SELECT * FROM `data` WHERE `id`={admin}")
            account = admindata[0][8]
            if str(account) == 'unlimited' or str(account) == 'free' or int(time.time()) - int(account) >= 2592000:
                continue
            bots = query(f"SELECT * from `bots` WHERE `admin`={admin} AND `autofor`='%E2%9C%85' AND `lastfor` < {int(time.time())} AND pyro != 'no'")
            for bot in bots:
                one_id = bot[0]
                name = unquote(bot[5])
                upq(f'UPDATE `bots` SET `lastfor`={int(time.time())+600} WHERE `id`={one_id}')
                mybot = Client(name=str(one_id),session_string=get_string(one_id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                if len(mybot.name) == 351:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                if len(mybot.name) == 356:
                    mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                await mybot.connect()
                async for it in mybot.get_dialogs():
                    try:
                        if it.chat.type == enums.ChatType.SUPERGROUP:
                            await mybot.forward_messages(it.chat.id, message.chat.username, message.id)
                    except Exception as e:
                        if str(e).isnumeric() == True:
                            continue
                        elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                            await mybot.leave_chat(it.chat.id)
                            continue
                        elif "[400 CHAT_RESTRICTED]" in str(e):
                            await mybot.leave_chat(it.chat.id)
                            continue
                        elif "[401 AUTH_KEY_UNREGISTERED]:" in str(e) or "[401 USER_DEACTIVATED]:" in str(e) or "[401 USER_DEACTIVATED_BAN]:" in str(e) or "[401 SESSION_EXPIRED]:" in str(e) or "[401 SESSION_REVOKED]:" in str(e):
                            await mybot.disconnect()
                            break
                        elif "[403 CHAT_SEND_MEDIA_FORBIDDEN]" in str(e):
                            await mybot.leave_chat(it.chat.id)
                            continue
                        elif "[400 PEER_FLOOD]" in str(e):
                            ReportAcc[id] = True
                            continue
                        elif "[420 FLOOD_WAIT_X]" in str(e):
                            await mybot.disconnect()
                            e = str(e)
                            flood = e.split(' seconds')[0].split('of ')[1]
                            if int(flood) < 300:
                                tfo = int(time.time()) + int(flood)
                                await asyncio.sleep(int(flood))
                                await mybot.connect()
                                continue
                            else:
                                upq(f'UPDATE `bots` SET `lastfor`={tfo} WHERE `id`={one_id}')
                                break
                        else:
                            continue
                    except:
                        continue
                try:
                    await client.send_message(admin, f'عملیات فوروارد خودکار پیام کانال @{username} با تبچی {name} باموفقیت انجام شد.')
                except:
                    pass

@app.on_message(filters.private & filters.regex('(/start|🔙 بازگشت)'))
async def startingbot(client,message):
    bots = query(f'SELECT * FROM bots WHERE `admin` = {message.from_user.id}')
    if len(bots) > 0:
        upq(f"UPDATE data SET `step` = 'no' WHERE `id`={message.from_user.id}")
        await message.reply("👋 سلام  به اُتو فوروارد اقای تبچی خوش آمدید!", reply_markup=menu)
    else:
        await message.reply("🌟با سلام خدمت شما کاربر گرامی این ربات ، ربات مکمل اقای تبچی میباشد (@MrTabchi2Bot)!\n⚠️ این ربات برای کاربرانی میباشد که در ربات تبچی ساز تبچی ساخته اند!\n😊 به وسیله این ربات امکان قفل کانال خود و فوروارد خودکار فراهم شده!\nاگر شما هم مایل به استفاده از این ربات و ساخت تبچی اختصاصی خود هستید هم اکنون وارد ربات شوید و حساب طلایی تهیه نمایید!\n\n🌹 با تشکر مدیریت اقای تبچی\nخاص ترین ها را با ما تجربه کنید!\n🤖 : @MrTabchi2Bot\n📢 : @MrTabchi2")
        
@app.on_message(filters.private & filters.regex('📢 ثبت کانال'))
async def submitchannel(client,message):
    upq(f"UPDATE data SET `step` = 'setchannel' WHERE `id`={message.from_user.id}")
    await message.reply("🌟 برای ثبت کانال لطفا نام کاربری کانال عمومی خود را با  @ ارسال نمایید!\n🔻 لطفا توجه داشته باشید که این ربات (@MrTabchi4bot) باید ادمین کانال موردنظر باشد!", reply_markup=back)
    
@app.on_message(filters.private & filters.regex('❌ حذف کانال'))
async def deletechannel(client,message):
    channels = query(f'SELECT * FROM `channels` WHERE `admin`={message.from_user.id}')
    if len(channels) > 0:
        keyboard = []
        for channel in channels:
            keyboard.append([InlineKeyboardButton(f"@{channel[0]}", callback_data=f"del-{channel[0]}")])
        keyboard = InlineKeyboardMarkup(keyboard)
        await message.reply('💪 جهت حذف کانال ،کانال موردنظر را انتخاب نمایید', reply_markup=keyboard)
    else:
        await message.reply('هنوز هیچ کانالی ثبت نکردی که 🙁')
        
@app.on_message(filters.private & filters.regex('⚖️ قوانین ربات'))
async def ghavanin(client,message):
    await message.reply("⚖️ قوانین اُتو فوروارد به شرح زیر میباشد!\n\n#قوانین_ساخت :\n1️⃣ - هرگونه تخلف با استفاده از ربات های ساخته شده باعث حذف ربات متخلف و هیچگونه مسءولیتی رو نمیپذیریم!\n2️⃣ - هرگونه سو استفاده از ربات ها به منظور آسیب به هاست یا هک یا نفوذ به آن تخلف محسوب شده ربات متخلف و حساب کاربری آن در ربات ساز مسدود میگردد!\n#قوانین_پشتیبانی :\n1️⃣ - هرگونه فحاشی و توهین به پشتیبانی تخلف محسوب شده و حساب کاربر متخلف مسدود میگردد!\n2️⃣ - از ارسال پیام های مکرر و بی دلیل مانند : (الو - هوی - کجا رفتین - چیشد و ...) بپرهیزید و جهت دریافت پاسخ حداکثر یک روز صبر نمایید!\n3️⃣ - هرگونه ایجاد مزاحمت یا اقدام به گول زدن پشتیبانی با استفاده از ساخت رسید جعلی و ... با تشخیص پشتیبانی شخص متخلف از ربات مسدود میگردد!\n#قوانین_خریدحساب_و_امتیاز :\n1️⃣ - تمامی پرداخت ها با درگاه امن پی پینگ انجام میشود و خودکار میباشد! و هیچگونه کلاه برداری وجود ندارد!\n2️⃣ - درصورت ناموفق بودن تراکنش یا ارتقا پیدا نکردن حساب با دریافت اسکرین شات از رسید و ارسال آن به بخش پشتیبانی اقدام به ارتقا حساب خود نمایید!\n3️⃣ - پس از پرداخت وجه و استفاده از حساب امکان عودت وجه وجود ندارد!\n\n🤝 در صورت استفاده و یا ساخت ربات با استفاده از تبچی ساز به این معناست که شما قوانین را پذیرفته اید!")
    
@app.on_message(filters.private & filters.regex('📚 راهنمای ربات'))
async def Help(client,message):
    await message.reply("😊کار با این ربات بسیار سادست فقط کافیه اول وارد ربات اصلی بشید (@MrTabchi2Bot)!\n⚙️ بعد حساب طلایی بخرید و ربات بسازید بعدش هم وارد این ربات بشید و کانالتون ثبت کنید و از بخش تنظیمات ربات خودتون انتخاب کنید و تمام!")
    
@app.on_message(filters.private & filters.regex('⚙️ تنظیمات'))
async def Settings(client,message):
    bots = query(f'SELECT * FROM `bots` WHERE `admin`={message.from_user.id}')
    if len(bots) > 0:
        keyboard = []
        for bot in bots:
            name = unquote(bot[5])
            vaz = unquote(bot[19])
            name = vaz+' '+name
            keyboard.append([InlineKeyboardButton(f"{name}", callback_data=f"bot-{bot[0]}")])
        keyboard = InlineKeyboardMarkup(keyboard)
        await message.reply('⚠️ به تنظیمات خوش آمدید جهت استفاده از فوروارد خودکار در هر تبچی فقط کافیست روی ربات موردنظر کلیک کنید\n😌 پس از کلیک هر تبلیغاتی که در چنل ارسال شود با همان تبچی به سوپرگروه ها فوروارد خواهد شد\n😅 امکان استفاده از چند تبچی نیز وجود دارد!', reply_markup=keyboard)
    else:
        await message.reply('شما رباتی نساخته اید.')
        
@app.on_callback_query(filters.regex('^bot-(.*)$'))
async def deletebot(client,callback_query):
    id = callback_query.data.split('-')[1]
    if len(query(f"SELECT * FROM `bots` WHERE `id`={id} AND `admin`={callback_query.from_user.id}")) > 0:
        vaz = query(f'SELECT * FROM `bots` WHERE `id`={id}')[0][19]
        if vaz == '%E2%9D%8C':
            upq(f"UPDATE `bots` SET `autofor`='%E2%9C%85' WHERE `id`={id}")
        else:
            upq(f"UPDATE `bots` SET `autofor`='%E2%9D%8C' WHERE `id`={id}")
        bots = query(f'SELECT * FROM `bots` WHERE `admin`={callback_query.from_user.id}')
        if len(bots) > 0:
            keyboard = []
            for bot in bots:
                name = unquote(bot[5])
                vaz = unquote(bot[19])
                name = vaz+' '+name
                keyboard.append([InlineKeyboardButton(f"{name}", callback_data=f"bot-{bot[0]}")])
            keyboard = InlineKeyboardMarkup(keyboard)
        await callback_query.edit_message_text('⚠️ به تنظیمات خوش آمدید جهت استفاده از فوروارد خودکار در هر تبچی فقط کافیست روی ربات موردنظر کلیک کنید\n😌 پس از کلیک هر تبلیغاتی که در چنل ارسال شود با همان تبچی به سوپرگروه ها فوروارد خواهد شد\n😅 امکان استفاده از چند تبچی نیز وجود دارد!', reply_markup=keyboard)
    else:
        await callback_query.edit_message_text('این ربات متعلق به شما نیست.')

@app.on_callback_query(filters.regex('^del-(.*)$'))
async def deletechannel(client,callback_query):
    id = callback_query.data.split('-')[1]
    if len(query(f"SELECT * FROM `channels` WHERE `username`='{id}' AND `admin`={callback_query.from_user.id}")) > 0:
        upq(f"DELETE FROM `channels` WHERE `username`='{id}' AND `admin`={callback_query.from_user.id}")
        channels = query(f'SELECT * FROM `channels` WHERE `admin`={callback_query.from_user.id}')
        if len(channels) > 0:
            keyboard = []
            for channel in channels:
                keyboard.append([InlineKeyboardButton(f"@{channel[0]}", callback_data=f"bot-{channel[0]}")])
            keyboard = InlineKeyboardMarkup(keyboard)
            await callback_query.edit_message_text('✅ این کانال از لیست کانال های شما پاک شد!', reply_markup=keyboard)
        else:
            await callback_query.edit_message_text('✅ این کانال از لیست کانال های شما پاک شد!')
    else:
        channels = query(f'SELECT * FROM `channels` WHERE `admin`={message.from_user.id}')
        if len(channels) > 0:
            keyboard = []
            for channel in channels:
                keyboard.append([InlineKeyboardButton(f"@{channel[0]}", callback_data=f"bot-{channel[0]}")])
            keyboard = InlineKeyboardMarkup(keyboard)
            await callback_query.edit_message_text('⚠️ این کانال از لیست کانال های شما پاک شده است!', reply_markup=keyboard)
        else:
            keyboard = InlineKeyboardMarkup([])
            await callback_query.edit_message_text('⚠️ این کانال از لیست کانال های شما پاک شده است!')

@app.on_message(filters.private & filters.text)
async def steps(_,message):
    if get_step(message.from_user.id) == 'setchannel':
        text = message.text.replace('@','').lower()
        if len(query(f"SELECT * FROM `channels` WHERE `username` = '{text}' AND `admin` = {message.from_user.id}")) < 1:
            if await check_status('@'+text, message.from_user.id):
                upq(f"UPDATE `data` SET `step` = 'no' WHERE `id`={message.from_user.id}")
                upq(f"INSERT INTO `channels` VALUES('{text}', '{message.from_user.id}', '{int(time.time())}')")
                await message.reply('✅ کانال شما ثبت گردید!\n😅 هم اکنون هر پیامی در کانال ارسال شود در تبچی فوروارد میگردد!', reply_markup=menu)
            else:
                await message.reply('❌ ربات در کانال ادمین نمیباشد!')
        else:
            await message.reply('❌ این کانال قبلا ثبت شده است!')
    
app.run()

#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل