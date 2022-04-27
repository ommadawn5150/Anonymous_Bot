# インストールした discord.py を読み込む
import discord
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime



# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTYwNDM0ODMxNDUwMzI5MTM5.YkqYow.1jfylloENJpaadFaJEuxeCa43b8'
CHANNEL_ID = 960435070026539061

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('Logined')


# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('Bot:起動しました')

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')


@client.event
async def on_message(message):
  anonymous_channel = client.get_channel(CHANNEL_ID)
  dt_now = str(datetime.date.today())
  date = int(dt_now.replace('-',''))
  id = hex(message.author.id * date)[-6:]
  print(id)
  
  if message.author.bot:
    return
  elif type(message.channel) == discord.DMChannel and client.user == message.channel.me:
    await anonymous_channel.send('---------------------------------- \n' + message.content + '\n ID:' + str(id) + '\n ---------------------------------')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)