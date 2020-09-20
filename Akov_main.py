#!/usr/bin/env python3
import discord
import random
import os
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

Prefix = "." 
client = commands.Bot(command_prefix = Prefix, help_command=None)

activity = ["with your mom", "with plutonium rods", "the game of LIFE", "Minecraft", "Spotify", "Ping-Pong", "with Balls", "dead", "BIOCHEMISTRY: A SHORT COURSE by John L. Tymoczko, Jeremy M. Berg, and Lubert Stryer", "against Albert", "someone's nerves", "with Akov's reproduction cycle", "with my own code", "COC"]
status = cycle(activity)



@client.event
async def on_ready():
    change_status.start
    await client.change_presence(activity=discord.Game(random.choice(activity)))
    print('We have logged in as {0.user}'.format(client))
    return

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    return
    
@client.event
async def on_remember_remove(member):
    print(f'{member} has left the server.')
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif random.random() < 0.001:
        funfact = [f"<@{message.author.id}> \n **¡Apuesto a que no sabias que yo era parte de la inquisicion espanola!**",
                   f"<@{message.author.id}> Have I ever told you the story of darth plageous the black death?",
                   f"<@{message.author.id}> Pssssst, would you like to know Leo's phone number \n Im willing to give it to you for just $4 today",
                   f"<@{message.author.id}> **DID YOU KNOW #19742** \n This portion of code was actually yeeted off of Leo's bot "
                   ]
        await message.channel.send(random.choice(funfact))
        return
    elif message.content.endswith("tonight"):
        comments = [f"<@{message.author.id}> Hey man, go do your home work",
                    f"<@{message.author.id}> Late to the game as always",
                    f"<@{message.author.id}> not today, sorry",
                    ]
        if random.random() < 0.05:
            await message.channel.send(random.choice(comments))
            return
    elif "among us" in message.content.lower():
        if random.random() < 0.0333:
            await message.channel.send(f"<@{message.author.id}> Kinda sus of you to mention that game")
            return
    elif message.content.endswith("pic"):
        await message.channel.send("https://picsum.photos/200/300 \n ***MY MAN*** \n **Here** \n **You** \n **Go**")
        pass
    await client.process_commands(message)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{ctx.author} cleared {amount} messages \n      **LIKE A BOSS**")
    return

@client.command()
async def bing(ctx):
    await ctx.send(f"Bong! {round(client.latency *1000)} ms" )
    return

@client.command()
async def ping(ctx):
    await ctx.send(f"Yikes, look like your Pong is overdue \n {round(client.latency *69420)} ms \n \n \n try *Bonging* next time instead")
    return

@client.command()
async def pic(ctx):
    await ctx.send("https://picsum.photos/200/300 \n ***MY MAN*** \n **Here** \n **You** \n **Go**")

@client.command()
async def record(ctx):
    print(ctx.channel)
    print(ctx.author)
    print(ctx.message.content)
    await ctx.send("message recorded")
    return

@client.command()
async def query(ctx,*, question):
    responses=["yes", "definitely", "Perhaps", "No", "Let me ask my manager \n \n \n \n he said no", "Let me ask my manager \n \n \n \n he said yeah, aslong as you take off your shoes", "I highly doubt it", "I usually know the answer to these \n but your presence is throwing me off", "96% \n sure", "The answer is 42", "When in doubt, go figure it out","Its a yes, but Wikipedia is not a reliable source","Ask Leo's bot, I gave him all the answers",]
    await ctx.send(f"Heres what I think about: {question} \n  {random.choice(responses)}")
    return

@client.command()
async def dice(ctx):
    dice=["1", "2", "3", "4", "5", "6"]
    await ctx.send(f"You got a  {random.choice(dice)}")
    return

@client.command()
async def cointoss(ctx):
    coin=["Heads","Tails"]
    await ctx.send(f"The coin has landed  {random.choice(coin)}")
    return

@client.command(pass_context=True)
async def note(ctx,*, message):
    author = ctx.message.author
    await author.send(f"{message}")
    await ctx.send ("message sent to DMs")
    return

@client.command(pass_context=True)
async def pnote(ctx,*, message):
    author = ctx.message.author
    await author.send(f"{message}")
    await ctx.channel.purge(limit=1)
    return

#@client.command(pass_context=True)
#async def pm(ctx,*, message):
#    Admin = get(ctx.guild.members)
#    if guild.member in message:
#        await ctx.guild.member.mention.send(f"{message}")
#        await ctx.channel.purge(limit=1)
#    else:
#        await ctx.send ("make sure to add a recipient")
#    return

@client.command(pass_context=True)
async def v(ctx):
    await ctx.send("20w38a")
    return




@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed1 = discord.Embed(color = discord.Color.dark_blue())
    embed1.set_author(name="Help")
    embed1.add_field(name=".bing", value="Returns Bong count", inline=False)
    embed1.add_field(name='.record "type the message here" ', value='Leave a message for Akov', inline=False)
    embed1.add_field(name='.query "type the question here"', value="Ask Akov a question", inline=False)
    embed1.add_field(name='.note "type the note here"', value="send yourself a note in dm", inline=False)
    embed1.add_field(name='.pnote "type the private note here"', value="send yourself a private note in dm", inline=False)
    #embed1.add_field(name='.pm "type the anonymous message here"', value="send someone an anonymous dm", inline=False)    
    embed1.add_field(name=".pic", value="Request an image of something EpIc", inline=False)
    embed1.add_field(name=".clear", value="clear some messages", inline=False)
    embed1.add_field(name=".dice", value="Roll the dice", inline=False)
    embed1.add_field(name=".cointoss", value="Toss a coin", inline=False)
    embed1.add_field(name=".rules", value="Follow these rules", inline=False)
    embed1.add_field(name=".help", value="Get some help", inline=False)
    embed1.add_field(name=".tip", value="Get some tips", inline=False)    
    await ctx.send(author, embed=embed1)

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

@client.command(pass_context=True)
async def tip(ctx):
    author = ctx.message.author
    tip = [
        "Use Common Sense sometimes","Avoid Spotify and Youtube Premium by making a playlist on Youtube then ask Leo's Boombox to play the playlist", "Start a Roth IRA account", "invest in Doge Coin", "Bros come before Hoes", "Don't get hooked of Heroin", "Just do it", "Set Goals", "Do **Not** visit North Korea", "Do **Not** intervene in the election process","Avoid income tax by not getting paid", "If you are allergic to peanuts \n Don't eat them", "Minecraft", "Try Roblox", "Subscribe to Dudes of 708","Check out our website @7o8.tech","Become a Patreon", "Avoid salty food items when diagnosed with hyertension", "Don't use Q-tips in your ears","Buy some of Leo's Bathwater", "Set Goals","Set Routines","Take advantage of opportunities", "Avoid Jeff","ping <@!578715287491182595>","Don't eat Legos","Wear a mask","Use protection","Send an anonymous message to @drongo using @akov", "donate to <@!578715287491182595> so he can get a new body pillow", "Check out our instagram page @dudesof708","Check out Max's instagram & facebook photography account @maxpressphotography","Make sure to follow rule #6","Use the help command on any bot to trigger a help message","La biblioteca esta ahi", "bing dont ping", "type .tip for more awesome tips"
    ]
    embed3 = discord.Embed(color = discord.Color.dark_blue())
    embed3.add_field(name=(f"Tip #{round(random.random()*1000)}"), value=random.choice(tip), inline=False)
    await ctx.send(author, embed=embed3)

@tasks.loop(hours=24)
async def change_status():
    await client.change_presence(activity=discord.Game(next(activity)))

    
client.run("token")
