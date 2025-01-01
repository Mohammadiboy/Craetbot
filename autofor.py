#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل

from pyrogram import Client, filters, errors, enums
import mysql.connector
import re
import uuid
import traceback
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
import sys, os, signal
import json
import time as t
from urllib.parse import unquote, quote
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
import random
import asyncio
from pyrogram.raw import functions, types
import traceback

app_id = #app id
app_hash = '' #app hash
mydb = mysql.connector.Connect(
    host='localhost',
    user='',
    password='',
    database=''
) #اطلاعات دیتابیس
mydb.commit()
mycu = mydb.cursor()
mydb.autocommit = True

def repeat(string, length):
    cur, old = 1, string
    while len(string) < length:
        string += old[cur-1]
        cur = (cur+1)%len(old)
    return string

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
    
def get_string(id):
    botdata = query(f'SELECT * FROM `bots` WHERE `id` ={id}')[0]
    return botdata[18]

#اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل

while True:
    try:
        bots = query(f"SELECT * FROM `ads` WHERE `time` < {int(t.time())}")
        if len(bots) > 0:
            for bot in bots:
                ti = int(t.time()) + (int(bot[4]) * 60)
                id = bot[0]
                hash = bot[1]
                admin = bot[5]
                type = bot[2]
                adminn = query(f'SELECT * FROM `bots` WHERE `id`={id}')
                if len(adminn) < 1 or adminn[0][11] != admin or adminn[0][18] == 'no':
                    update_database(f"DELETE FROM `ads` WHERE `id` = {id}")
                    continue
                ads = query(f"SELECT * FROM `banners` WHERE id={id} AND `type` = 'forward' AND `admin`={admin}")
                if len(ads) == 0 and type == 'forward':
                    update_database(f"DELETE FROM `ads` WHERE `Hash` = '{hash}'")
                    continue
                    
                ad = query(f"SELECT * FROM `banners` WHERE id={id} AND `type` = 'send' AND `admin`={admin}")
                if len(ad) == 0 and type == 'send':
                    update_database(f"DELETE FROM `ads` WHERE `Hash` = '{hash}'")
                    continue
                
                admindata = query(f"SELECT * FROM `data` WHERE `id` = {admin}")
                account = admindata[0][8]
                if str(account) == 'unlimited' or str(account) == 'free' or int(t.time()) - int(account) >= 2592000:
                    update_database(f"DELETE FROM `ads` WHERE `admin` = {admin}")
                    continue
                update_database(f"UPDATE `ads` SET `time` = {ti} WHERE `Hash` = '{hash}'")
                try:
                    mybot = Client(name=str(id),session_string=get_string(id),api_id=int(app_id),api_hash=app_hash,no_updates =True)
                    if len(mybot.name) == 351:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sI?"
                    if len(mybot.name) == 356:
                        mybot.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                    mybot.connect()
                    for dialog in mybot.get_dialogs():
                        try:
                            if dialog.chat.type == enums.ChatType.SUPERGROUP and random.randint(1,4) == 3:
                                if type == 'forward':
                                    uniq = random.randint(0,len(ads)-1)
                                    banner = ads[uniq]
                                    mybot.invoke(functions.messages.ForwardMessages(from_peer=mybot.resolve_peer(banner[3]),id=[int(banner[2])], to_peer=mybot.resolve_peer(dialog.chat.id),schedule_date=int(t.time()) + random.randint(10,320),random_id=[random.randint(0,100000000)]))
                                    
                                elif type == 'send':
                                    uniq = random.randint(0,len(ad)-1)
                                    banner = ad[uniq]
                                    mybot.invoke(functions.messages.ForwardMessages(from_peer=mybot.resolve_peer(banner[3]),id=[int(banner[2])], to_peer=mybot.resolve_peer(dialog.chat.id),schedule_date=int(t.time()) + random.randint(10,320),random_id=[random.randint(0,100000000)], drop_author=True))
                        except errors.FloodWait as e:
                            try:
                                mybot.disconnect()
                            except:
                                pass
                            tix = int(t.time()) + e.value + random.randint(60,120)
                            update_database(f"UPDATE `ads` SET `time` = {tix} WHERE `Hash` = '{hash}'")
                            break
                        except ConnectionError:
                            try:
                                mybot.connect()
                            except:
                                pass
                            continue
                        except errors.MessageIdInvalid:
                            try:
                                mybot.disconnect()
                            except:
                                pass
                            update_database(f"DELETE FROM `banners` WHERE `id` = {id} `admin` = {admin} `ch` = '{banner[3]}' AND `msgid` = '{banner[2]}'")
                            break
                        except errors.ChatWriteForbidden:
                            try:
                                mybot.leave_chat(dialog.chat.id)
                            except:
                                pass
                            try:
                                mybot.disconnect()
                            except:
                                pass
                            continue
                        except (errors.AuthKeyUnregistered, errors.UserDeactivatedBan, errors.UserDeactivated, errors.SessionExpired, errors.SessionRevoked):
                            update_database(f"DELETE FROM `ads` WHERE `Hash` = '{hash}'")
                            try:
                                mybot.disconnect()
                            except:
                                pass
                            break
                        except:
                            print(traceback.format_exc())
                            continue
                    try:
                        mybot.disconnect()
                    except:
                        pass
                except (errors.AuthKeyUnregistered, errors.UserDeactivatedBan, errors.UserDeactivated, errors.SessionExpired, errors.SessionRevoked):
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    update_database(f"DELETE FROM `ads` WHERE `id` = {id}")
                    continue
                except:
                    try:
                        mybot.disconnect()
                    except:
                        pass
                    print(traceback.format_exc())
                    continue
        else:
            t.sleep(20)
    except:
        print(traceback.format_exc())
        continue
    #اولین اپن کننده @Alfred_s1 و @DevOscar
#تنها فقط این دو اوپن ککنده هستن به هیچ وجه ادیت نکنید

#اپن شده در چنل = https://t.me/Virtualservices_3

#کیر تو رحم ننه هرکی بدون منبع بزنه مخصوصا اولین اپن کننده و آیدی چنل