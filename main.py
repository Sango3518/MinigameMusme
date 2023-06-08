# Discord.pyをインポート
import discord

# .envファイルからTOKENの値を読み込み
import os
from dotenv import load_dotenv
load_dotenv()

# 乱数をインポート
import random

# 時間制御のやつインポート
import asyncio

# 使用数値の生成
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
UporDown = ["上がる","下がる","同じ"]
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
s11 = 0
H = 0

# 初期化
client = discord.Client(intents = discord.Intents.all())

# botが起動したかの判断用
@client.event
async def on_ready():
    print("Startup Success")

# メイン部分
@client.event
async def on_message(message):
    global s1
    if not message.author.bot:
        if s1 == 0:   
            # ヘルプ
            if message.content == "Help":
                await message.channel.send("Play:他の人がゲームで遊んでいない時にゲームを開始できるなの\nぜひ沢山遊んでほしいの！\n\nUp/Down:プレイ中にアップかダウンかを聞かれた時に使えるなの\n次の数が今出ている数より大きいか小さいかを直感で選択するなの...！\n\nYes/No:チャレンジに成功した時か数が同じだった時に使えるなの\nゲームを続けたいならYes、ゲームをやめたいならNoを送ってほしいなの！")
            # ゲームスタート
            if message.content == "Play":
                global number1
                global number2
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s1 = 1
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s1 == 1:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s1 = 2
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して150PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s2
                    s1 = 0
                    s2 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s1 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s1 = 2
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して150PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s1 = 0
                    s2 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s1 = 0
        if s1 == 2:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s1 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s1 = 3
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s1 == 3:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s1 = 2
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して150PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s1 = 0
                    s2 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s1 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s1 = 2
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して150PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s1 = 0
                    s2 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s1 = 0
        # 二周目
        if s2 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s2 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s2 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s2 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s2 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して225PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s3
                    s2 = 0
                    s3 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s2 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s2 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して225PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s2 = 0
                    s3 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s2 = 0
        # 三周目
        if s3 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s3 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s3 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s3 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s3 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して338PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s4
                    s3 = 0
                    s4 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s3 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s3 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して338PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s3 = 0
                    s4 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s3 = 0
        # 四周目
        if s4 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s4 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s4 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s4 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s4 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して506PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s5
                    s4 = 0
                    s5 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s4 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s4 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して506PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s4 = 0
                    s5 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s4 = 0
        # 五周目
        if s5 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s5 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s5 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s5 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s5 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して759PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s6
                    s5 = 0
                    s6 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s5 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s5 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して759PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s5 = 0
                    s6 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s5 = 0
        # 六周目
        if s6 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s6 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s6 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s6 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s6 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して1139PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s7
                    s6 = 0
                    s7 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s6 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s6 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して1139PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s6 = 0
                    s7 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s6 = 0
        # 七周目
        if s7 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s7 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s7 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s7 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s7 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して1709PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s8
                    s7 = 0
                    s8 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s7 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s7 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して1709PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s7 = 0
                    s8 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s7 = 0
        # 八周目
        if s8 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s8 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s8 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s8 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s8 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して2563PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s9
                    s8 = 0
                    s9 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s8 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s8 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して2563PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s8 = 0
                    s9 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s8 = 0
        # 九周目
        if s9 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s9 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s9 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s9 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s9 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して3844PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s10
                    s9 = 0
                    s10 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s9 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s10 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して3844PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s9 = 0
                    s10 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s9 = 0
        # 十周目
        if s10 == 1:
            if message.content == "No":
                await message.channel.send("遊んでくれてありがとうなの！\nまたいつでも遊びに来てなのー！")
                s10 = 0
            if message.content == "Yes":
                number1 = random.choice(numbers)
                number2 = random.choice(numbers)
                s10 = 2
                await message.channel.send(number1)
                await message.channel.send("Upだと思うなの？Downだと思うなの？")
        if s10 == 2:
            if message.content == "Up":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s10 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して5767PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    global s11
                    s10 = 0
                    s11 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s10 = 0
            if message.content == "Down":
                await message.channel.send("果たして結果は...ドキドキするなの！")
                await asyncio.sleep(1.5)
                if number1 == number2:
                    await message.channel.send(number2)
                    await message.channel.send("同じ数だったからもう一回挑戦できるなの！\nもう一回挑戦してみるなの？")
                    s10 = 1
                if number1 > number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジに成功して5767PPを手に入れたの！\nもう一回挑戦してみるなの？")
                    s10 = 0
                    s11 = 1
                if number1 < number2:
                    await message.channel.send(number2)
                    await message.channel.send("チャレンジ失敗なの...\nまた挑戦してみてほしいなの！")
                    s10 = 0
        # おまけ
        if message.content == "ムスメちゃんの予想は？":
            Musme = random.choice(UporDown)
            await message.channel.send("うーん...ムスメは"+Musme+"ような気がするなの！")
        if s11 == 1:
            s11 = 0
            await asyncio.sleep(1)
            await message.channel.send("ちょっと待つおー！！")
            await asyncio.sleep(2)
            await message.channel.send("こ、この声はモナちゃん！")
            await asyncio.sleep(1)
            await message.channel.send("どうしてここにいるなの！？")
            await asyncio.sleep(2)
            await message.channel.send("それはもちろんムスメちゃんをだm...そんなことはどうでもいいお！")
            await asyncio.sleep(1.5)
            await message.channel.send("このまま続けるとムスメちゃんのウォレットが空になっちゃうお！")
            await asyncio.sleep(2)
            await message.channel.send("ウォレット......？")
            await asyncio.sleep(1)
            await message.channel.send("どこかで聞いたことがある気がするなの......")
            await asyncio.sleep(2)
            await message.channel.send("この前クイズしたのにもう忘れてるお！？")
            await asyncio.sleep(1.5)
            await message.channel.send("ウォレットは仮想通貨を入れておくためのインターネット上のお財布だお！")
            await asyncio.sleep(2)
            await message.channel.send("あ、思い出したの！")
            await asyncio.sleep(1)
            await message.channel.send("ポケットがたくさんついてるカッコいいやつなの！")
            await asyncio.sleep(2)
            await message.channel.send("ムスメちゃん、それ間違った知識だお......")
            await asyncio.sleep(1.5)
            await message.channel.send("まあ今はそれは置いておいて、ウォレットを確認するんだお！")
            await asyncio.sleep(2)
            await message.channel.send("わかったの！")
            await asyncio.sleep(1.5)
            await message.channel.send("ふむふむ...なるほどこれは...よくわからないなの！")
            await asyncio.sleep(2)
            await message.channel.send("もう一回よく見てみるんだお")
            await asyncio.sleep(2)
            await message.channel.send("うーん......")
            await asyncio.sleep(1.5)
            await message.channel.send("よく見ると減ってるような気がしてきたの......")
            await asyncio.sleep(2)
            await message.channel.send("そうだお！")
            await asyncio.sleep(1.5)
            await message.channel.send("このままだとPPを買うために仮想通貨を使い切っちゃうから、モナが見張っておいてあげるお？")
            await asyncio.sleep(2)
            await message.channel.send("確かにその方がいい気がしてきたなの......")
            await asyncio.sleep(2)
            await message.channel.send("それじゃあシードフレーズをこの紙に書くんだお！")
            await asyncio.sleep(2)
            await message.channel.send("シードフレーズはビット先輩が教えちゃダメって言ってたやつなの！")
            await asyncio.sleep(2)
            await message.channel.send("ぐぬぬ......")
            await asyncio.sleep(1.5)
            await message.channel.send("モナが教えたところを覚ええてないのはちょっとムカつくけど、一番大事なところは覚えてたからまあ良しとするお......")
            await asyncio.sleep(2)
            await message.channel.send("これでムスメも仮想通貨アイドルになれる！！")
            await asyncio.sleep(2)
            await message.channel.send("よく覚えていたわねムスメちゃん")
            await asyncio.sleep(1.5)
            await message.channel.send("モナちゃんが怪しい動きをしてたから来てみたけど、今回私は必要なかったみたいね")
            await asyncio.sleep(2)
            await message.channel.send("あ、ビット先輩！")
            await asyncio.sleep(1.5)
            await message.channel.send("ムスメシードフレーズ教えなかったから立派な仮想通貨アイドルになったの！")
            await asyncio.sleep(2)
            await message.channel.send("うーん立派な仮想通貨アイドルになるにはもうちょっとお勉強が必要かな......")
            await asyncio.sleep(2)
            await message.channel.send("そして逃げようとしても無駄よモナちゃん！")
            await asyncio.sleep(2)
            await message.channel.send("み、見つかってるお...？")
            await asyncio.sleep(1)
            await message.channel.send("天誅！")
            await asyncio.sleep(1)
            await message.channel.send("マーミムーメモー！")
            await asyncio.sleep(2)
            await message.channel.send("またつまらぬものをBANしてしまった......")
            await asyncio.sleep(2)
            await message.channel.send("さて、モナちゃんが言ってたけど、ムスメちゃんのPPがなくなっちゃうから今回はここまで！")
            await asyncio.sleep(2)
            await message.channel.send("みんなも仮想通貨の使いすぎには注意してね！")
            await asyncio.sleep(2)
            await message.channel.send("それじゃあまたね！")
            await message.channel.send("またなのー！")
            await message.channel.send("まただお！")

#Discordbotを指定して実行
client.run(os.getenv('TOKEN'))