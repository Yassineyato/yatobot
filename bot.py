from keep_alive import keep_alive
import discord
from discord.ext import commands
from dotenv import load_dotenv




bot = commands.Bot(command_prefix='Y!')
    
load_dotenv()
token = "NjUxNTQ4NTE1MzAyMTEzMjgw.Xe4kbg.ynPVs9WHhsgDIZ-RvYfWEeh8ggc"

client = discord.Client()
bot = commands.Bot(command_prefix='Y!')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Support \ twitch.tv/creativealienum <3'))   #status
    print('connected to Discord!')



@client.event
async def on_message(message): 
    if message.content.find('slm')!= -1:
            await message.channel.send('> wa 3alaykom assalam')
        
    if message.content.find('Y!twitch')!= -1:
            await message.channel.send('> Twitch Link: https://twitch.tv/yatosan10')
    if message.content.find('Y!help')!= -1:
        await message.channel.send('> Y!slm   ---> reply with :wa 3alaykom assalam \n > Y!twitch --> twitch stream link \n')
    if message.content.find('Ghizlane?')!= -1:
            await message.channel.send('> A7sn girl fl3alam :heart: :alien: :green_heart: , I love her so much UwU')
    if message.content.find('Y!support')!= -1:
        await message.channel.send('''```json
"Creative Alienum : https://www.twitch.tv/creativealienum
                    https://www.nimo.tv/creativealienum
Yassine Yato :https://www.twitch.tv/yatosan10 
Anas FD : https://www.nimo.tv/live/5248539937
Edthrow : https://www.nimo.tv/edcrow03."
```''')
            
client.run(token)