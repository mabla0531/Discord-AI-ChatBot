import discord
import chatgptapi

tokenfile = open("bottoken.txt")
bottoken = tokenfile.read()
tokenfile.close()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@1080163297891979264>'):
        print(message.content[22:].strip())
        query = message.content[22:].strip()
        response = chatgptapi.process_message(query)
        await message.channel.send(response)

if (__name__ == "__main__"):
    client.run(bottoken)