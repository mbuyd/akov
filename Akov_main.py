#!/usr/bin/env python3
import discord
import json
from random import choice, random
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

client = commands.Bot(command_prefix = ".")

Token = json.load(open("secrets.json", "r"))["Token"]
akov = json.load(open("dictionary.json", "r"))["akov"]
Max = json.load(open("dictionary.json", "r"))["Max"]
Gid = json.load(open("dictionary.json", "r"))["Gid"]
test1 = json.load(open("dictionary.json", "r"))["test1"]
internshipchan = json.load(open("dictionary.json", "r"))["internshipchan"]
botchan = json.load(open("dictionary.json", "r"))["botchan"]
internreply = json.load(open("dictionary.json", "r"))["internreply"]
test = json.load(open("dictionary.json", "r"))["test"]
#secrettest = py.load(open("secret.py","r"))


activity = json.load(open("Arrays/activity.json", "r"))["activity"]
status = cycle(activity)

@client.event
async def on_ready():
    change_status.start
    await client.change_presence(activity=discord.Game(choice(activity)))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(activity)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif random() < 0.0005:
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
        if random() < 0.1:
            await message.channel.send(choice(comments))  
    elif "among us" in message.content.lower():
        if random() < 0.0333:
            await message.channel.send(f"<@{message.author.id}> Kinda sus of you to mention that game")
    elif message.content.endswith("pic"):
        await message.channel.send("https://picsum.photos/200/300 \n ***MY MAN*** \n **Here** \n **You** \n **Go**")
    elif message.content.startswith(akov):
        response = [f"<@{message.author.id}> Ya Wassup",
                    f"<@{message.author.id}> Tech Support here, how can I help you",
                    f"<@{message.author.id}> I thought you forgot about me :robot: :cry:"]
        await message.channel.send(choice(response))
    elif "apply" in message.content.lower():
        if message.author.id == Gid:
            if message.channel.id == internshipchan:
                if random() < 0.5:
                    await message.channel.send (internreply)
                pass
            pass
        pass
    elif "internship" in message.content.lower():
        if message.author.id == Gid:
            if message.channel.id == internshipchan:
                if random() < 0.5:
                    await message.channel.send (internreply)
                pass
            pass
        pass
    elif "event" in message.content.lower():
        if message.author.id == Gid:
            if message.channel.id == internshipchan:
                if random() < 0.5:
                    await message.channel.send (internreply)
                pass
            pass
        pass
    #elif "test" in message.content.lower():
        #await message.channel.send(test)
    else:
        pass
        #client.process_commands(message)


###################################
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{ctx.author} cleared {amount} messages \n      **LIKE A BOSS**")

@client.command()
async def sneaky_clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

    
@client.command()
async def bing(ctx):
    await ctx.send(f"Bong! {round(client.latency *1000)} ms" )
    
@client.command()
async def ping(ctx):
    await ctx.send(f"Yikes, look like your Pong is overdue \n {round(client.latency *69420)} ms \n \n \n try *Bonging* next time instead")
    
@client.command(pass_context=True)
async def v(ctx):
    await ctx.send("20w42b")

#############################################

@client.command()
async def query(ctx,*, question):
    query = json.load(open("Arrays/query.json", "r"))["query"]
    await ctx.send(f"Heres what I think about: {question} \n  {choice(query)}") 

@client.command()
async def dice(ctx):
    dice=["1", "2", "3", "4", "5", "6"]
    await ctx.send(f"You got a  {choice(dice)}")

@client.command()
async def cointoss(ctx):
    coin=["Heads","Tails"]
    await ctx.send(f"The coin has landed  {choice(coin)}")


#########################################

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
async def incognito_msg(ctx, member: discord.Member, *, content):
    await ctx.channel.purge(limit=1)
    channel = await member.create_dm() 
    await channel.send(content)

@client.command()
async def msg(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() 
    await channel.send(content)
    await ctx.send("message sent")


#############################
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
async def commands(ctx):
    author = ctx.message.author
    embed1 = discord.Embed(color = discord.Color.dark_blue())
    embed1.set_author(name="Help")
    embed1.add_field(name="v", value="display bot version", inline=True)
    embed1.add_field(name="clear", value="Clear some messages", inline=True)
    embed1.add_field(name="sneaky_clear", value="clear messages like a ninja", inline=True)
    embed1.add_field(name="rules", value="View server rules", inline=True)
    embed1.add_field(name="bing", value="Returns Bong count", inline=True)
    embed1.add_field(name='record ', value='Leave a message for Akov', inline=True)
    embed1.add_field(name='query', value="Ask Akov a question", inline=True)
    embed1.add_field(name='note ', value="dm yourself a note", inline=True)
    embed1.add_field(name='pnote ', value="dm yourself a private note", inline=True)
    embed1.add_field(name="incognito_msg", value="msg but anonymous", inline=True)
    embed1.add_field(name="msg", value="Send a msg through akov", inline=True)   
    embed1.add_field(name="dice", value="Roll the dice", inline=True)
    embed1.add_field(name="cointoss", value="Toss a coin", inline=True)   
    embed1.add_field(name="meme", value="look at dank memes", inline=True)
    embed1.add_field(name="tip", value="Get some tips", inline=True)
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
