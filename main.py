from pydoc import describe
import discord
import PingPongWr
import random
import os

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    await member.send(f'{member.mention}님 서버에 오신 것을 환영합니다. 인증을 해 서버로 입장해주세요!')

@bot.slash_command(guild_ids=[993042304325664791])
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

class Ping(discord.ui.View): # Create a class called View that subclasses discord.ui.View
    @discord.ui.button(label="새로고침", style=discord.ButtonStyle.primary, emoji="🔁") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message(f"🏓ㅣ`Pong! {round(round(bot.latency, 4)*1000)}ms`") # Send a message when the button is clicked

@bot.slash_command() # Create a slash command
async def 핑(ctx):
    await ctx.respond(f"🏓ㅣ`Pong! {round(round(bot.latency, 4)*1000)}ms`", view=Ping()) # Send a message with our View class that contains the button

bot.run(str(os.getenv('TOKEN')))
