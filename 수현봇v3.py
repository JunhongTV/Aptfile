import discord
import os

client = discord.Client()
game = discord.Game("수현봇v3 아직 베타 버젼입니다! !Helps을 입력해주세요!")

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!Helps":
        await message.author.send("현제 명령어 추가된거: !help, !ping, !url, !invite url, !Naver Intellectuals, !Papago" )
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")
    if message.content == "!help":
        await message.author.send("봇 제작자: 수현#1170")
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")
    if message.content == "!ping":
        await message.author.send("10 ping!")
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")    
    if message.content == "!url":
        await message.author.send("수현 디스코드 본주소: https://discord.gg/eHRK4gh 수현 디스코드 마크서버: https://discord.gg/JFRn8XJ 수현 디스코드 수현학교: https://discord.gg/khEqrdC 수현 디스코드 서포트주소: https://discord.gg/4yfmYcy")
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")   
    if message.content == "!invite url":
        await message.author.send("https://discordapp.com/oauth2/authorize?client_id=690025072559521833&permissions=537159744&scope=bot")
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")
    if message.content == "!Naver Intellectuals":
        await message.author.send("https://terms.naver.com/")
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")    
    if message.content == "!Papago":
        await message.author.send("https://papago.naver.com/")
        await message.channel.send(":regional_indicator_d: :regional_indicator_m:")

access_Token = os.environ["BOT_TOKEN"]
client.run(access_Token)
