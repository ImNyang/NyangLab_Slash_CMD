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

@bot.slash_command()
async def 길드(ctx):
    g = ctx.guild
    name = g.name
    afk_voice = g.afk_channel
    banner = g.banner
    system_channel = g.system_channel
    bitrate_limit = g.bitrate_limit
    bitrate_limit = bitrate_limit = str(bitrate_limit)
    bitrate_limit = bitrate_limit.strip("0")
    bitrate_limit = bitrate_limit.strip("000")
    bitrate_limit = bitrate_limit.strip(".")
    emoji_limit = g.emoji_limit 
    filesize_limit = g.filesize_limit
    boost_role = g.premium_subscriber_role
    owner = g.owner
    icon_url = g.icon_url
    is_icon_animated = g.is_icon_animated()
    invite_url_background = g.splash
    member_count = g.member_count
    created_at = g.created_at
    region = g.region
    #invite = await g.invites()

    embed = discord.Embed(title=f"{name}", description=f"{member_count}명의 맴버들과 함께하고 있어요! 이 멋진 봇과 함께요!", color=0xd6ffdb)
    embed.set_thumbnail(url=f"{icon_url}")
    embed.add_field(name="----⚙️일반⚙️----", value="ㅣ모든 서버들이 사용이 가능해요!ㅣ", inline=False)
    embed.add_field(name="🤿ㅣAFK 음성 채널", value=f"{afk_voice}", inline=True)
    embed.add_field(name="🗓ㅣ서버 생성일 UTC", value=f"{created_at}", inline=True)
    embed.add_field(name="🌏ㅣ서버 메인 언어", value=f"{region} (현재 제대로 표시되지 않습니다.)", inline=True)
    embed.add_field(name="📥ㅣ디스코드 관리자 공지 채널", value=f"{system_channel}", inline=True)
    embed.add_field(name="----💎부스트💎----", value="ㅣ부스트일 경우 더 많은 것들이 True로 되어 있어요!ㅣ", inline=False)
    embed.add_field(name="🏷ㅣ부스트 역할", value=f"{boost_role}", inline=True)
    embed.add_field(name="🌌ㅣ서버 아이콘 움직임", value=f"{is_icon_animated}", inline=True)
    embed.add_field(name="🖥ㅣ디스코드 초대 링크 배경화면", value=f"{invite_url_background}", inline=True)
    embed.add_field(name="📃ㅣ서버 배너", value=f"{banner}", inline=True)
    embed.add_field(name="🎤ㅣ서버 비트레이트 한계", value=f"{bitrate_limit}kbps", inline=True)
    embed.add_field(name="😀ㅣ이모지 최대 갯수", value=f"{emoji_limit}개", inline=True)
    embed.add_field(name="🗄ㅣ파일 최대 용량", value=f"{filesize_limit} KIB", inline=True)
    embed.set_footer(text=f"{name}", icon_url=f"{icon_url}")

    await ctx.send(embed=embed)

bot.run(str(os.getenv('TOKEN')))