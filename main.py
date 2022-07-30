import discord
import random
import os
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
from random import randint

bot = discord.Bot()

url = str(os.getenv('PINGPONG_URL'))  # 핑퐁빌더 Custom API URL
pingpong_token = str(os.getenv('PINGPONG_TOKEN'))  # 핑퐁빌더 Custom API Token

Ping = PingPong(url, pingpong_token)  # 핑퐁 모듈 클래스 선언

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    await member.send(f'{member.mention}님 서버에 오신 것을 환영합니다. 인증을 해 서버로 입장해주세요!')

@bot.slash_command()
async def 안녕(ctx):
    await ctx.respond(f"Hello! World! `Pong! {round(round(bot.latency, 4)*1000)}ms`")

@bot.slash_command()
async def 가위바위보(ctx, user: str):  # user:str로 !game 다음에 나오는 메시지를 받아줌
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)  # 인덱스 비교로 결과 결정
    if result == 0:
        await ctx.respond(f'{user} vs {bot}  비겼습니다.')
    elif result == 1 or result == -2:
        await ctx.respond(f'{user} vs {bot}  유저가 이겼습니다.')
    else:
        await ctx.respond(f'{user} vs {bot}  봇이 이겼습니다.')

def RandomColor():
    return randint(0, 0xFFFFFF)
@bot.command()
async def 채팅(ctx, chat:str):
    data = await Ping.Pong(ctx.author.id, chat, NoTopic=False)
    embed = discord.Embed(
        title="PingPong.us로 나온 결과!",
        description=data['text'],
        color=RandomColor()
    )
    embed.set_footer(text="Using PingPongTool")
    if data['image'] is not None:
        embed.set_image(url=data['image'])
    await ctx.respond(embed=embed)

@bot.slash_command()
async def httpcat(ctx, httperror:str):
    embed=discord.Embed(title="meow")
    embed.set_author(name="http.cat", url="https://http.cat")
    embed.set_image(url=f"https://http.cat/{httperror}")
    await ctx.respond(embed=embed)

bot.run(str(os.getenv('TOKEN')))