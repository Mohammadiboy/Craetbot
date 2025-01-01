#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل

from pyrogram import Client, filters, errors
import mysql.connector
import re
import uuid
import traceback
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
import sys, os, signal
import json
import time as t
from urllib.parse import unquote, quote
from datetime import datetime
from pyrogram.errors import FloodWait
from random import randint

app_id = #app_id
app_hash = '' #app_hash
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
        
def get_string(id):
    return query(f'SELECT * FROM `bots` WHERE `id`={id}')[0][18]
     
def update_database(q):
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

while True:
    try:
        tim = int(t.time())
        ix = '%E2%9C%85'
        i = query(f"SELECT * FROM `bots` WHERE `limit` IS NOT NULL AND `pyro`!='no' AND `limit` < {tim} AND `joiner` = '{ix}'")
        if len(i) > 0:
            for bot in i:
                joinertype = bot[21]
                if joinertype == 'all':
                    links = query(f"SELECT `hash` FROM `hash`")
                else:
                    links = query(f"SELECT `id` FROM `grouplist` WHERE `type`='{joinertype}'")
                id = bot[0]
                print(bot[0])
                admin = bot[11]
                adeads = len(links) - 10
                joinnum = bot[16]
                name = unquote(bot[5])
                admindata = query(f"SELECT * FROM `data` WHERE `id` = {admin}")
                account = admindata[0][8]
                if str(account) == 'unlimited' or str(account) == 'free' or int(t.time()) - int(account) >= 2592000:
                    update_database(f"UPDATE bots SET joiner='%E2%9D%8C' WHERE id={id}")
                    continue
                if int(joinnum) > adeads:
                    update_database(f"UPDATE bots SET joiner='%E2%9D%8C' WHERE id={id}")
                    continue
                link = links[int(joinnum)][0]
                new = int(joinnum) +1
                try:
                    mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                    if len(mybot.name) == 351:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                    if len(mybot.name) == 356:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                    mybot.connect()
                    flood = int(t.time()) + randint(50,120)
                    update_database(f"UPDATE `bots` SET `limit`={flood} WHERE id={id}")
                    if joinertype == 'all':
                        mybot.join_chat("https://t.me/joinchat/"+link)
                    else:
                        mybot.join_chat(link)
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    update_database(f"UPDATE bots SET joinnum={new} WHERE id={id}")
                except (errors.UserAlreadyParticipant, errors.InviteRequestSent):
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    update_database(f"UPDATE bots SET joinnum={new} WHERE id={id}")
                    continue
                except (errors.InviteHashExpired, errors.UsernameInvalid):
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    update_database(f"UPDATE bots SET joinnum={new} WHERE id={id}")
                    if joinertype == 'all':
                        update_database(f"DELETE FROM hash WHERE hash='{link}'")
                    else:
                        update_database(f"DELETE FROM `grouplist` WHERE id='{link}'")
                    continue
                except errors.FloodWait as e:
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    flood = int(t.time()) + e.value
                    update_database(f"UPDATE `bots` SET `limit`={flood} WHERE id={id}")
                    break
                except (errors.ChannelsTooMuch, errors.AuthKeyUnregistered, errors.UserDeactivated, errors.UserDeactivatedBan, errors.SessionExpired, errors.SessionRevoked):
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    update_database(f"UPDATE bots SET joiner='%E2%9D%8C' WHERE id={id}")
                    break
                except Exception as e:
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    print(e)
                    break
        else:
            t.sleep(10)
    except Exception as e:
        print(e)
        continue

print('OK')

#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل