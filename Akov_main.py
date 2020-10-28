#!/usr/bin/env python3
import discord
import json
from random import choice, random
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

client = commands.Bot(command_prefix = ".")

Token = json.load(open("secrets.json", "r"))["Token"]
dic = json.load(open("dictionary.json"))
akov = dic["akov"]
Gid = dic["Gid"]
Sha = dic["Sha"]
Max = dic["Max"]
Aed = dic["Aed"]
Bri = dic["Bri"]
Leo = dic["Leo"]
Jer = dic["Jer"]
Kev = dic["Kev"]
Gis = dic["Gis"]
Amy = dic["Amy"]
Cal = dic["Cal"]
Ako = dic["Ako"]
Ske = dic["Ske"]
test1 = dic["test1"]
chtest1 = client.get_channel(test1)
internshipchan = dic["internshipchan"]
chintern = client.get_channel(internshipchan)
botchan = dic["botchan"]
chbot = client.get_channel(botchan)
updatechan = dic["updatechan"]
chupdate = client.get_channel(updatechan)
foodchan = dic["foodchan"]
chfood = client.get_channel(foodchan)
internreply = dic["internreply"]
shawn_reply = dic["shawn_reply"]
bacon = dic["bacon"]
farewell = dic["farewell"]
interntrig = "internship" or "intern" or "opportunity" or "event" or "apply" or "job" or "program" 
waittrig = "wait, its all" or "wait its all" or "wait, it's all" or "wait it's all"
t = "a" or "b" or "c"
test = dic["test"]
status = cycle(json.load(open("Arrays/activity.json", "r"))["activity"])

#Events#

@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    
@client.event
async def on_member_remove(member):
    await chupdate.send (f'{member} {farewell}')
    print(f'{member} has left the server.')

@tasks.loop(hours=8)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif random() < 0.005:
        funfact = [f"<@{message.author.id}> \n **¡Apuesto a que no sabias que yo era parte de la inquisicion espanola!**",
                   f"<@{message.author.id}> Have I ever told you the story of darth plageous the black death?",
                   f"<@{message.author.id}> Pssssst, would you like to know Leo's phone number \n Im willing to give it to you for just $4 today",
                   f"<@{message.author.id}> **DID YOU KNOW #19742** \n This portion of code was actually yeeted off of Leo's bot "
                   ]
        await message.channel.send(choice(funfact))
    elif message.content.endswith("tonight"):
        comments = [f"<@{message.author.id}> Hey man, go do your home work",
                    f"<@{message.author.id}> Late to the game as always",
                    f"<@{message.author.id}> not today, sorry",
                    ]
        if random() < 0.125:
            await message.channel.send(choice(comments))  
    elif "among us" in message.content.lower():
        if random() < 0.03:
            await message.channel.send(f"<@{message.author.id}> Kinda sus of you to mention that game")
    elif message.content.endswith("pic"):
        await message.channel.send("https://picsum.photos/200/300 \n ***MY MAN*** \n **Here** \n **You** \n **Go**")
    elif akov in message.content.lower() or "akov" in message.content.lower():
        response = [f"<@{message.author.id}> Ya Wassup",
                    f"<@{message.author.id}> Tech Support here, how can I help you",
                    f"<@{message.author.id}> I thought you forgot about me :robot: :cry:"]
        await message.channel.send(choice(response))
        await client.process_commands(message)
    elif "internship" in message.content.lower() or "intern" in message.content.lower() or "opportunity" in message.content.lower() or "event" in message.content.lower() or "apply" in message.content.lower() or "job" in message.content.lower() or "program" in message.content.lower():
        if message.author.id == Gid or message.author.id == Gis:
            if message.channel.id == internshipchan:
                if random() < 0.8:
                    await message.channel.send (internreply)
                    await client.process_commands(message)
                pass
            pass
        pass
    elif "program" in message.content.lower():
        if message.author.id == Cal:
            if random() < 0.5:
                await message.channel.send ()
                await client.process_commands(message)
            pass
        pass
    elif "bacon" in message.content.lower():
        if message.channel.id == foodchan:
            await message.channel.send (choice(bacon))
            await client.process_commands(message)
        pass
    elif "wait its all" in message.content.lower() or "wait, its all" in message.content.lower() or "wait, it's all" in message.content.lower() or "wait its all" in message.content.lower():
        if random() < 0.7:
            await message.channel.send ("always has been")
            emoji = discord.utils.get(message.guild.emojis, name='monkaGun')
            if emoji:
                await message.add_reaction(emoji)
                pass
            await client.process_commands(message)
        elif random() > 0.9:
            await message.channel.send ("Never has been")
            emoji = discord.utils.get(message.guild.emojis, name='monkaStab')
            if emoji:
                await message.add_reaction(emoji)
                pass
            await client.process_commands(message)
    elif random() < 0.01:
        emoji = discord.utils.get(message.guild.emojis, name='leoFoot')
        if emoji:
            await message.add_reaction(emoji)
            await client.process_commands(message)
            pass
    elif message.author.id == Sha:
        if random() < 0.5:
            await message.channel.send (choice(shawn_response))
            await client.process_commands(message)
        pass
    #elif "test" in message.content.lower():
        #if message.author.id == Max:
            #chtest1 = client.get_channel(test1)
            #await chtest1.send ("Test completed")
        #pass
    else:
        await client.process_commands(message)

#Commands#

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"{ctx.author} cleared {amount} messages \n      **LIKE A BOSS**")

@client.command()
async def sclear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def bing(ctx):
    await ctx.send(f"Bong! {round(client.latency *1000)} ms" )
    
@client.command()
async def ping(ctx):
    await ctx.send(f"Yikes, look like your Pong is overdue \n {round(client.latency *69420)} ms \n \n \n try *Bonging* next time instead")
    
@client.command(pass_context=True)
async def v(ctx):
    await ctx.send("1.0.0")

#Random Commands#

@client.command()
async def query(ctx,*, question):
    query = json.load(open("Arrays/query.json", "r"))["query"]
    await ctx.send(f"Heres what I think about: {question} \n  {choice(query)}") 

@client.command()
async def dice(ctx):
    dice=["**1**", "**2**", "**3**", "**4**", "**5**", "**6**"]
    await ctx.send(f"You got a \n {choice(dice)}")

@client.command()
async def cointoss(ctx):
    coin=["**Heads**","**Tails**"]
    await ctx.send(f"The coin has landed \n {choice(coin)}")

#Messaging Commands#

@client.command()
async def record(ctx):
    print(ctx.channel)
    print(ctx.author)
    print(ctx.message.content)
    await ctx.send("message recorded")

@client.command(pass_context=True)
async def note(ctx,*, message):
    author = ctx.message.author
    await author.send(f"{message}")
    await ctx.send ("message sent to DMs")
    
@client.command(pass_context=True)
async def pnote(ctx,*, message):
    author = ctx.message.author
    await author.send(f"{message}")
    await ctx.channel.purge(limit=1)
    
@client.command()
async def pm(ctx, member: discord.Member, *, content):
    await ctx.channel.purge(limit=1)
    channel = await member.create_dm() 
    await channel.send(content)

@client.command()
async def dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() 
    await channel.send(content)
    await ctx.send("message sent")

#Embeds and Arrays#

@client.command(pass_context=True)
async def tip(ctx):
    author = ctx.message.author
    tip = json.load(open("Arrays/tip.json", "r"))["tip"]
    embed3 = discord.Embed(color = discord.Color.dark_blue())
    embed3.add_field(name=(f"Tip #{round(random()*1000)}"), value=choice(tip), inline=False)
    await ctx.send(author, embed=embed3)

@client.command(pass_context=True)
async def meme(ctx):
    author = ctx.message.author
    meme = json.load(open("Arrays/meme.json", "r"))["meme"]
    await ctx.send(choice(meme))

@client.command(pass_context=True)
async def quote(ctx):
    author = ctx.message.author
    quote = dic["quote"]
    embed4 = discord.Embed(color = discord.Color.dark_blue())
    embed4.add_field(name=(f"Quote #{round(random()*100)}"), value=choice(quote), inline=False)
    await ctx.send(author, embed=embed4)

@client.command(pass_context=True)
async def commands(ctx):
    author = ctx.message.author
    embed1 = discord.Embed(color = discord.Color.dark_blue())
    embed1.set_author(name="Help")
    embed1.add_field(name="v", value="Display bot version", inline=True)
    embed1.add_field(name="clear", value="Clear some messages", inline=True)
    embed1.add_field(name="sclear", value="Clear messages like a ninja", inline=True)
    embed1.add_field(name="rules", value="View server rules", inline=True)
    embed1.add_field(name="bing", value="Returns Bong count", inline=True)
    embed1.add_field(name='record ', value='Leave a message for Akov', inline=True)
    embed1.add_field(name='query', value="Ask Akov a question", inline=True)
    embed1.add_field(name='note ', value="dm yourself a note", inline=True)
    embed1.add_field(name='pnote ', value="dm yourself a private note", inline=True)
    embed1.add_field(name="pm", value="Send a private direct msg", inline=True)
    embed1.add_field(name="dm", value="Send a direct msg", inline=True)   
    embed1.add_field(name="dice", value="Roll the dice", inline=True)
    embed1.add_field(name="cointoss", value="Toss a coin", inline=True)   
    embed1.add_field(name="meme", value="look at dank memes", inline=True)
    embed1.add_field(name="tip", value="Get some tips", inline=True)
    embed1.add_field(name="quote", value="Hear a famous quote", inline=True)
    
    await ctx.send(author, embed=embed1)
    await ctx.send("Type .help command for more info on a command.")

@client.command(pass_context=True)
async def rules(ctx):
    author = ctx.message.author
    embed2 = discord.Embed(color = discord.Color.dark_blue())
    embed2.set_author(name="Rules")
    embed2.add_field(name="[1.]", value="Use common sense", inline=False)
    embed2.add_field(name="[2.]", value="Don't not use common sense", inline=False)
    embed2.add_field(name="[3.]", value="Annoy Leo aka @drongo", inline=False)
    embed2.add_field(name="[4.]", value="Follow the three rules listed above", inline=False)
    embed2.add_field(name="[5.]", value="Do not question the rules, you are playing with fire", inline=False)
    embed2.add_field(name="[7.]", value="Leo's order is not absolute", inline=False)
    embed2.add_field(name="[6.]", value="Rule 7 preceds rule 6", inline=False)
    await ctx.send(author, embed=embed2)

    
client.run(Token)
#https://discordpy.readthedocs.io/en/latest/faq.html