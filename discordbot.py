# インストールした discord.py を読み込む
import discord
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import os
import datetime
import json
import uuid
from discord.ext import commands

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''
CHANNEL_ID = 222 #int
intents=discord.Intents.all()
intents.typing = False 
intents.members = True
# 接続に必要なオブジェクトを生成
client = discord.Client(intents = intents)
bot = commands.Bot(intents,command_prefix='$')

@bot.command()
async def set_channel(ctx, ch_id):
    CHANNEL_ID = ch_id
    await ctx.send('設定しました')
async def help(ctx):
    await ctx.send('匿名ちゃんねるに設定したいチャンネルのidを/ set_channel idという風に書くことでそのチャンネルに設定できます。\n匿名ちゃんねるはanonymous botに書き込み内容を直接DMすることでレスできます。')



@client.event
async def on_ready():
    print('Logined')


def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)

alnum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJELMNOPQRSTUVWXYZ"

def encode_decimal62(num, chars = alnum):
    base = len(chars)
    string = ""
    while True:
        string = chars[num % base] + string
        num = num // base
        if num == 0:
            break
    return string

def decode_decimal62(string, chars = alnum):
    base = len(chars)
    num = 0
    for char in string:
        num = num * base + chars.index(char)
    return num
    
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    anonymous_channel = client.get_channel(CHANNEL_ID)
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    time = now.strftime('%Y/%m/%d %H:%M:%S.%f')[:-4]

    dt_now = str(datetime.date.today())
    date = int(dt_now.replace('-',''))
    u_id = hex(message.author.id * date)[-6:]
    id = str(uuid.uuid3(uuid.NAMESPACE_OID,u_id))[-6:]
    print('ID:',id)
    print('TIME:',time)
    zorome = discord.File("./zoro.jpg")
    nanasi = '名無しのロッ研部員'
    	

    if message.author.bot:
        return
    if message.content == '/shazo':
        await message.channel.send('https://livedoor.blogimg.jp/sokudokuex/imgs/3/e/3e597c3d.jpg')
    if message.content == '/neko':
        if message.author.id % 2 == 1:
            await message.channel.send('. ∧∧\n(,,ﾟДﾟ)' )
        elif message.author.id % 2 == 0:
            await message.channel.send('. ∧ ∧\n(*ﾟーﾟ)' )

    if message.author.bot:
        return
    elif type(message.channel) == discord.DMChannel and client.user == message.channel.me:
        if message.attachments:
            await anonymous_channel.send( '---------------------------------\n'  + nanasi +' Date: ' +  time + '  ID:' + str(id) + '\n' + message.content + '\n')

            for i in message.attachments:
                if i.url.endswith(('png','jpg','jpeg','MOV','mp4')):
                    await anonymous_channel.send(i.url +'\n')

            await anonymous_channel.send('\n---------------------------------')
            
            
        else:
            await anonymous_channel.send( '---------------------------------\n'  +  nanasi +   ' Date: ' +  time + '  ID:' + str(id) + '\n' + message.content +'\n---------------------------------')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
