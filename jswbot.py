import discord
from flask import Flask
from threading import Thread

app = Flask('')

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

def run_bot():
    client.run("YOUR_DISCORD_TOKEN")

@app.route('/')
def home():
    return "Discord bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t1 = Thread(target=run_bot)
    t2 = Thread(target=run_flask)
    t1.start()
    t2.start()

if __name__ == "__main__":
    keep_alive()
