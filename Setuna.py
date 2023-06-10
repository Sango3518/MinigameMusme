#　discord.pyをインポート
import discord

# .envファイルからTOKENの値を読み込み
import os
from dotenv import load_dotenv
load_dotenv()

# 初期化
client = discord.Client(intents = discord.Intents.all())

# 乱数をインポート
import random

# 時間制御のやつインポート
import asyncio

# 使用数値の生成
S1 = 0

# メイン部分
@client.event
async def on_message(message):
  if not message.author.bot:
    global S1
    if S1 == 0:
      if message.content == "Play":
        S1 = 1
        T = random.uniform(2,5)
        await asyncio.sleep(T)
        await message.channel.send("！")
        S1 = 2
        await asyncio.sleep(0.4)
        await message.channel.send("M")
        if S1 == 2:
          S1 = 3
        if S1 == 3:
          await message.channel.send("敗北")
          S1 = 0
    if S1 == 2:
      if message.content == "M":
        if S1 == 2:
          S1 = 0
          await message.channel.send("勝利！")
     
#Discordbotを指定して実行
client.run(os.getenv('TOKEN'))
