
import discord
from discord.ext import commands
from flask import Flask

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@bot.event
async def on_ready():
    print(f'봇이 다음으로 로그인합니다: {bot.user.name}')
    print(f'봇 ID: {bot.user.id}')

@bot.command()
async def ㅎㅇ(ctx):
    await ctx.send('안녕')

@bot.event
async def on_oauth_completion(data):
    # 콜백 페이지로부터 인증 완료 후의 처리를 작성합니다.
    print('OAuth 인증이 완료되었습니다.')

def run_bot():
    bot.run('MTE4OTc4Nzc4MTAxNTI4OTg1Ng.GnjDmC.P7yNXNX776fh-rcrkN_r7EhI9v2N5cJKMKIKwI')

if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.create_task(bot.start('MTE4OTc4Nzc4MTAxNTI4OTg1Ng.GnjDmC.P7yNXNX776fh-rcrkN_r7EhI9v2N5cJKMKIKwI'))
    loop.create_task(app.run())
    loop.run_forever()
