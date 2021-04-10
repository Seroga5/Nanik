import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("привет"):
        await message.channel.send("Хай!")
    if message.content.startswith("ютуб наник"):
        await message.channel.send("https://www.youtube.com/channel/UCksYmKgBV-IhzfbOEhyHyAg")
    if message.content.startswith("тик ток наник"):
        await message.channel.send("https://vm.tiktok.com/ZSJYjHJwr/")
    if message.content.startswith("всем привет"):
        await message.channel.send("О привет!")
    if message.content.startswith("о бот ты кто?"):
        await message.channel.send("Я Nanik меня создал мой босс Nanik_228")
    if message.content.startswith("кто создатель серва?"):
        await message.channel.send("О это Nanik_228!")
client.run('ODIyNzc0NjAwMDY4NjI4NTAw.YFXKjw.dDrtC4__aGzrU-xDrGv5WCSZKA0')
