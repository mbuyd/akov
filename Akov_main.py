#!/usr/bin/env python3
import asyncio
import json
from itertools import cycle
from random import choice, random
import discord
from discord.ext import commands, tasks
from discord.utils import find, get
import requests
from requests import get as get2
#from ignore import *

client = commands.Bot(command_prefix = ".", case_insensitive=True)
#client.remove_command("help")


#from __init__:
#client.add_command(reddit)
#client.add_command(hdh)
###############

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
tg1 = dic["tg1"]
tg2 = dic["tg2"]
th = dic["th"]
test1 = dic["test1"]
chtest1 = client.get_channel(test1)
internshipchan = dic["internshipchan"]
botchan = dic["botchan"]
botlandchan = dic["botlandchan"]
updatechan = dic["updatechan"]
foodchan = dic["foodchan"]
adminchan = dic["adminchan"]
internreply = dic["internreply"]
shawn_reply = dic["shawn_reply"]
bacon = dic["bacon"]
farewell = dic["farewell"]
interntrig = "internship" or "intern" or "opportunity" or "event" or "apply" or "job" or "program" 
waittrig = "wait, its all" or "wait its all" or "wait, it's all" or "wait it's all"
Say = dic["Say"]
prostate = dic["Prostate"]
t = "a" or "b" or "c"
test = dic["test"]
status = cycle(json.load(open("Arrays/activity.json", "r"))["activity"])
hp = dic["hotplate"]

serverid = client.get_guild(691848461217169438)


#Events####################################################################################################################

@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    #print(f'{member} has joined the server.')
    channel = await member.create_dm() 
    await channel.send("Welcome to the 708 server \n use the prefixes (!help, ~help, .commands) to trigger some of our bots")

    
@client.event
async def on_member_remove(server, member):
    if server == serverid:
        await client.get_channel(adminchan).send(f'{member} {choice(farewell)}')
        #print(f'{member} has left the server.')
        channel = await member.create_dm() 
        await channel.send("You are such a Bruh")
    else:
        return


@tasks.loop(hours=8)
async def change_status():
    #await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="Pregnancy test", type=5))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif random() < 0.0001:
        funfact = [f"<@{message.author.id}> \n **¡Apuesto a que no sabias que yo era parte de la inquisicion espanola!**",
                   f"<@{message.author.id}> Have I ever told you the story of darth plageous the wise?",
                   f"<@{message.author.id}> Pssssst, would you like to know Leo's phone number \n Im willing to give it to you for just $4 today",
                   f"<@{message.author.id}> WierdChamp",
                   f"<@{message.author.id}> PauseChamp",
                   f"<@{message.author.id}> PogChamp"
                                      ]
        await message.channel.send(choice(funfact))
    elif message.content.endswith("tonight") or message.content.endswith("tonight?"):
        comments = [f"<@{message.author.id}> Hey man, go do your home work",
                    f"<@{message.author.id}> Late to the game as always",
                    f"<@{message.author.id}> not today, sorry"
                    ]
        if random() < 0.05:
            await message.channel.send(choice(comments))
    elif "among us" in message.content.lower():
        if random() < 0.03:
            await message.channel.send(f"<@{message.author.id}> Kinda sus of you to mention that game")
    elif message.content.endswith(" pic"):
        await message.channel.send("https://picsum.photos/200/300 \n ***MY MAN*** \n **Here** \n **You** \n **Go**")
    elif akov in message.content.lower() or "akov" in message.content.lower():
        response = [f"<@{message.author.id}> Ya Wassup",
                    f"<@{message.author.id}> Tech Support here, how can I help you",
                    f"<@{message.author.id}> I thought you forgot about me :robot: :cry:",
                    f"<@{message.author.id}> No",
                    f"<@{message.author.id}> Yes"]
        await message.channel.trigger_typing()
        await asyncio.sleep(4) 
        await message.channel.send(choice(response))
        await client.process_commands(message)
    elif "internship" in message.content.lower() or "intern" in message.content.lower() or "opportunity" in message.content.lower() or "event" in message.content.lower() or "apply" in message.content.lower() or "job" in message.content.lower() or "program" in message.content.lower():
        if message.author.id == Gid or message.author.id == Gis:
            if message.channel.id == internshipchan:
                if random() < 0.005:
                    await message.channel.send (choice(internreply))
                    await client.process_commands(message)
                pass
            pass
        pass
    elif "bacon" in message.content.lower():
        if message.channel.id == foodchan:
            await message.channel.send(choice(bacon))
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

###Dad Bot response
    #elif "im" in message.content.lower() or "I am" in message.content.lower():
        #if random() < 0.7:
            #await message.channel.send ("always has been")
            #emoji = discord.utils.get(message.guild.emojis, name='monkaGun')
            #if emoji:
                #await message.add_reaction(emoji)
                #pass
            #await client.process_commands(message)
        #elif random() > 0.9:
            #await message.channel.send ("Never has been")
            #emoji = discord.utils.get(message.guild.emojis, name='monkaStab')
            #if emoji:
                #await message.add_reaction(emoji)
                #pass
            #await client.process_commands(message)
###
    elif random() < 0.001:
        emoji = discord.utils.get(message.guild.emojis, name='leoFoot')
        if emoji:
            await message.add_reaction(emoji)
            await client.process_commands(message)
            pass
    elif message.author.id == Sha:
        if random() < 0.20:
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

#Commands################################################################################################################

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"{ctx.author} cleared {amount} messages \n      **LIKE A BOSS**")

@client.command()
async def c(ctx, amount=5):
    author = ctx.message.author.id
    if author != Max:
        await ctx.send(choice(Say))
        pass
    elif author == Max:
        await ctx.channel.purge(limit=amount+1)
    else:
        await client.process_commands(message)

@client.command(aliases=["b"])
async def bing(ctx):
    await ctx.send(f"Bong! {round(client.latency *1000)} ms" )
    
@client.command()
async def ping(ctx):
    await asyncio.sleep(4)
    await ctx.send(th)
    await ctx.send(f"Yikes, look like your Pong is overdue \n {round(client.latency *69420)} ms \n \n \n try *Binging* next time instead")
    StopAsyncIteration

@client.command(pass_context=True)
async def v(ctx):
    await ctx.send("1.0.5.1")

@client.command(pass_context=True, aliases=["s"])
async def say(ctx,* , message):
    author = ctx.message.author.id
    if author != Max:
        await ctx.send(choice(Say))
        pass
    elif author == Max:
        await ctx.channel.purge(limit=1)
        await ctx.send(message)
    else:
        await client.process_commands(message)

@client.command(pass_context=True)
async def tts(ctx,* , message):
    author = ctx.message.author.id
    if author != Max:
        await ctx.send(choice(Say))
        pass
    elif author == Max:
        await ctx.channel.purge(limit=1)
        await ctx.send(message, tts=True)
    else:
        await client.process_commands(message)

@client.command(pass_context=True)
async def thanos(ctx):
            await ctx.channel.purge(limit=1)
            await ctx.send(tg1) 
            await asyncio.sleep(10)
            await ctx.send(tg2)
            StopAsyncIteration

@client.command(pass_context=True)
async def probe(ctx, member: discord.Member):
            message = await ctx.send(f"Probing {member}'s prostate.")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate..")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate...")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate.")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate..")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate...")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate.")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate..")
            await asyncio.sleep(0.3)
            await message.edit(content=f"Probing {member}'s prostate...")
            await asyncio.sleep(0.3)
            if member.id == Max:
                await message.edit(content=f" {member} has **passed** their prostate exam with flying colors")
            elif member.id == Ako or member.id == Amy or member.id == Cal or member.id == Ske:
                await message.edit(content=f" {member} does not have a prostate")
            else:
                await message.edit(content=f" {member} {choice(prostate)}")
            StopAsyncIteration

#@client.command()
#async def test(ctx):
#  message = await ctx.send("hello")
#  await asyncio.sleep(1)
#  await message.edit(content="newcontent")

#@client.command()
#async def test2(ctx):
#    await ctx.channel.trigger_typing()
#    await asyncio.sleep(4) 
#    await ctx.send ("typetest complete")

#@client.command()
#async def test3(ctx):
#    if ctx.channel.is_news():
#        await ctx.send ("yes this is the anouncement channel")
#    else:
#        await ctx.send ("no")


#Random Commands####################################################################################################

@client.command()
async def query(ctx,*, question):
    query = json.load(open("Arrays/query.json", "r"))["query"]
    await ctx.send(f"Heres what I think about: {question} \n {choice(query)}") 

@client.command(aliases=["d"])
async def dice(ctx):
    dice=["**1**", "**2**", "**3**", "**4**", "**5**", "**6**"]
    await ctx.send(f"You got a \n {choice(dice)}")

@client.command(aliases=["ct"])
async def cointoss(ctx):
    coin=["**Heads**","**Tails**"]
    await ctx.send(f"The coin has landed \n {choice(coin)}")

#class Messaging:
#Messaging Commands#######################################################################################################
@client.command(pass_context=True, aliases=["n"])
async def note(ctx,*, message):
    author = ctx.message.author
    await author.send(f"{message}")
    await ctx.send ("message logged in DMs")
    
@client.command(pass_context=True, aliases=["pn"])
async def pnote(ctx,*, message):
    author = ctx.message.author
    await author.send(f"{message}")
    await ctx.channel.purge(limit=1)
    
@client.command(pass_context=True, aliases=["pm"])
async def pmessage(ctx, member: discord.Member, *, content):
    await ctx.channel.purge(limit=1)
    channel = await member.create_dm() 
    await channel.send(content)

@client.command(pass_context=True, aliases=["m"])
async def message(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() 
    await channel.send(content)
    await ctx.send("message sent to DMs")


#Embeds and Arrays######################################################################################################

@client.command(pass_context=True, aliases=["t"])
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

@client.command(pass_context=True, aliases=["q"])
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
    #embed1.add_field(name="c", value="Clear messages like a ninja", inline=True)
    embed1.add_field(name="rules", value="View server rules", inline=True)
    embed1.add_field(name="bing", value="Returns Bong count", inline=True)
    embed1.add_field(name='query', value="Ask Akov a question", inline=True)
    embed1.add_field(name='note ', value="dm yourself a note", inline=True)
    embed1.add_field(name='pnote ', value="dm yourself a private note", inline=True)
    embed1.add_field(name="pm", value="Send a private direct msg", inline=True)
    embed1.add_field(name="m", value="Send a direct msg", inline=True)
    embed1.add_field(name="dice", value="Roll the dice", inline=True)
    embed1.add_field(name="cointoss", value="Toss a coin", inline=True)
    embed1.add_field(name="meme", value="look at dank memes", inline=True)
    embed1.add_field(name="tip", value="Get some tips", inline=True)
    embed1.add_field(name="quote", value="Hear an infamous quote", inline=True)
    embed1.add_field(name="reddit", value="See a recent image from your favorite subreddit", inline=True)
    embed1.add_field(name="probe", value="Check a friend's prostate*", inline=True)
    embed1.add_field(name="poll", value="Run a channel poll", inline=True)
    embed1.add_field(name="quote", value="Hear an infamous quote", inline=True)
    embed1.add_field(name="credits", value="Check out who contributes to the bot", inline=True)
    
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

#@client.command()
#async def test(ctx):
#  message = await ctx.send("hello")
#  await asyncio.sleep(1)
#  await message.edit(content="newcontent")

@client.command()
async def pauseChamp(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send ("<:pauseChamp:790088324789960714>")

@client.command()
async def Cap(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send ("<:me:787879095635410985>")


#@client.command()
#async def survey(ctx, text, *emojis: discord.Emoji):
#    await ctx.channel.purge(limit=1)
#    msg = await ctx.send(text)
#    for emoji in emojis:
#        await msg.add_reaction(emoji)

@client.command()
async def poll(ctx, question, option1=None, option2=None, option3=None, option4=None, option5=None, option6=None, option7=None, option8=None, option9=None, option10=None ):
    author = ctx.message.author
    await ctx.channel.purge(limit=1)
    embed6 = discord.Embed(color = discord.Color.dark_blue())
    embed6.set_author(name=f"{question}")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    o6=0
    o7=0
    o8=0
    o9=0
    o10=0
    #embed6.add_field(name="Development", value="Cap_Russia", inline=False)
    if option1==None and option2==None:
        #<:yes:802705662017798164>,<:no:802705662017798164>
        embed6.add_field(name= "options",value="**✅ = Yes**\n**❌ = No**")
        message = await ctx.send(embed=embed6)
        pollid = message.id
        await ctx.send (pollid)
        await message.add_reaction('✅')
        await message.add_reaction('❌')
        #if emoji == "✅":embed6.add_field(name= "options",value=f"**✅ = Yes** {o1+1}\n**❌ = No {o2}**") 
        #if emoji == "❌":embed6.add_field(name= "options",value=f"**✅ = Yes** {o1}\n**❌ = No {o2+1}**") 
        #await message.edit(embed=embed6)
    elif option3==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**2⃣ = {option2}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
    elif option4==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**2⃣ = {option2}**\n**3⃣ = {option3}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
    elif option5==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**2⃣ = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣')
    elif option6==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**2⃣ = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**\n**5⃣ = {option5}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣') 
        await message.add_reaction('5⃣')
    elif option7==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**2⃣ = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**\n**5⃣ = {option5}**\n**6⃣ = {option6}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣') 
        await message.add_reaction('5⃣')
        await message.add_reaction('6⃣')
    elif option8==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**:two: = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**\n**5⃣ = {option5}**\n**6⃣ = {option6}**\n**7⃣ = {option7}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣') 
        await message.add_reaction('5⃣')
        await message.add_reaction('6⃣')
        await message.add_reaction('7⃣')
    elif option9==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**:two: = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**\n**5⃣ = {option5}**\n**6⃣ = {option6}**\n**7⃣ = {option7}**\n**8⃣ = {option8}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣') 
        await message.add_reaction('5⃣')
        await message.add_reaction('6⃣')
        await message.add_reaction('7⃣')
        await message.add_reaction('8⃣')
    elif option10==None:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**:two: = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**\n**5⃣ = {option5}**\n**6⃣ = {option6}**\n**7⃣ = {option7}**\n**8⃣ = {option8}**\n**9⃣ = {option9}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣') 
        await message.add_reaction('5⃣')
        await message.add_reaction('6⃣')
        await message.add_reaction('7⃣')
        await message.add_reaction('8⃣')
        await message.add_reaction('9⃣')
    else:
        embed6.add_field(name= "options",value=f"**1⃣ = {option1}**\n**:two: = {option2}**\n**3⃣ = {option3}**\n**4⃣ = {option4}**\n**5⃣ = {option5}**\n**6⃣ = {option6}**\n**7⃣ = {option7}**\n**8⃣ = {option8}**\n**9⃣ = {option9}**\n**🔟 = {option10}**")
        message = await ctx.send(embed=embed6)
        await message.add_reaction('1⃣')
        await message.add_reaction('2⃣')
        await message.add_reaction('3⃣')
        await message.add_reaction('4⃣')
        await message.add_reaction('5⃣')
        await message.add_reaction('6⃣')
        await message.add_reaction('7⃣')
        await message.add_reaction('8⃣')
        await message.add_reaction('9⃣')
        await message.add_reaction('🔟')

    
@client.command(pass_context=True)
async def credits(ctx):
    embed5 = discord.Embed(color = discord.Color.dark_blue())
    embed5.set_author(name="Akov \n 1.0.2")
    embed5.add_field(name="Development", value="Cap_Russia", inline=False)
    message = await ctx.send(embed=embed5)
    embed5.add_field(name="Program Management", value="Cap_Russia", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    embed5.add_field(name="Testing", value="Cap_Russia \n NotaBot", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    embed5.add_field(name="Multimedia", value="Cap_Russia \n Unsplash ", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    embed5.add_field(name="Beta Testers", value="Cap_Russia \n Not a bot \n drongo \n resident hacker \n epic gamer", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    embed5.add_field(name="Novelty and Functionality", value="Cap_Russia \n drongo \n resident hacker \n Calm Leo \n Amy \n kuzz", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    embed5.add_field(name="Documentation", value="Cap_Russia \n resident hacker", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    embed5.add_field(name="Special Thanks to", value="Cap_Russia \n resident hacker \n epic gamer \n drongo", inline=False)
    await asyncio.sleep(0.4)
    await message.edit(embed=embed5)
    StopAsyncIteration










###########

##__init__##
sixtyfour = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/64'
cafev = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/18'
canyonvista = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/24'
clubmed = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/15'
foodworx = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/11'
#goodys = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/06'
oceanview = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/05'
pines = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/01'
#roots = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/32'
bistro = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/27'

data64 = requests.request(url=sixtyfour, allow_redirects=False, method = "GET")
dataventanas = requests.request(url=cafev, allow_redirects=False, method = "GET")
datacanyon = requests.request(url=canyonvista, allow_redirects=False, method = "GET")
dataclubmed = requests.request(url=clubmed, allow_redirects=False, method = "GET")
datafoodworx = requests.request(url=foodworx, allow_redirects=False, method = "GET")
#datagoodys = requests.request(url=goodys, allow_redirects=False, method = "GET")
dataoceanview = requests.request(url=oceanview, allow_redirects=False, method = "GET")
datapines = requests.request(url=pines, allow_redirects=False, method = "GET")
#dataroots = requests.request(url=roots, allow_redirects=False, method = "GET")
databistro = requests.request(url=bistro, allow_redirects=False, method = "GET")

@client.command(pass_context=True)
async def hdh(ctx, place, item):
    if place == "sixty four" or place == "64" or place == "sixtyfour":
        if item in data64.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")
        
    elif place == "cafeventanas" or place == "cafev" or place == "cafe ventanas" or place == "cafe v":
        if item in dataventanas.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    elif place == "canyonvista" or place == "cv" or place == "canyon" or place == "canyon vista":
        if item in datacanyon.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    elif place == "clubmed" or place == "club med":
        if item in dataclubmed.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    elif place == "foodworx":
        if item in datafoodworx.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    elif place == "oceanview" or place == "ov" or place == "ovt" or place == "ocean view":
        if item in dataoceanview.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    elif place == "pines":
        if item in datapines.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    elif place == "bistro" or place == "the bistro":
        if item in databistro.text.lower():
            await ctx.send (f'{item} is in {place}')
        else: await ctx.send (f"{item} is not on {place}'s menu right now")

    else: await ctx.send (f"{place} is not yet in the database")

@client.command(pass_context=True)
async def hotplate(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(10) 
    await ctx.send (f'{choice(hp)}')
    return
#    author = ctx.message.author
#    await open_list(ctx.author)

#    users = await get_list_data()
#    embed7 = discord.Embed(color = discord.Color.dark_green())
#    embed7.set_author(ctx.author)
#    embed7.add_field(name = "Hotplate", value = f"{item} @ {place}")
#    await ctx.send(embed = embed7)

#@client.command()
#async def add(ctx, item, place):
#    users = await get_list_data
#    await ctx.send (f"{item} @ {place} was added to your hotplate")
#    users[str(user.id)]["hotplate"] = item, place
#    with open("hotplate.json","w") as h:
#        json.dump(users,h)

#async def open_list(user):
#    users = await get_list_data()
    
#    if str(user.id) in users:
#        return False
#    else:
#        users[str(user.id)]["hotplate"]

#    with open("hotplate.json","w") as h:
#        json.dump(users,h)
#    return True

#async def get_list_data():
#    with open("hotplate.json","r") as h:
#        users = json.load(h)
#    return users

    #12:00 https://www.youtube.com/watch?v=HPaadO_sRD4

@client.command(pass_context=True, aliases=["r"])
async def reddit(ctx, message):
    headers = {'User-Agent': 'Akov Anonymous Version 1.0.5'}
    reddit_post = get2(f'https://www.reddit.com/r/{message}/random.json', headers = headers).json()
    if (reddit_post[0]['data']['children'][0]['data']['over_18']):
        if ctx.channel.is_nsfw():
            try:
                await ctx.send ("https://media1.giphy.com/media/Ju7l5y9osyymQ/200.webp?cid=ecf05e47odh3oakayaeewhq3nd5so2hflyfhzmuwmt4ony9s&rid=200.webp")
                #await ctx.send(reddit_post[0]['data']['children'][0]['data']['url'])
            except:
                await ctx.send("Subreddit does not exist \n Try another")
    else: 
        try:
            await ctx.send(reddit_post[0]['data']['children'][0]['data']['url'])
        except:
            await ctx.send("Subreddit does not exist \n Try another")


#Econ#

@client.command(pass_context=True,aliases=["bal"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    balance_amt = users[str(user.id)]["balance"]

    embed8 = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.dark_green())
    embed8.set_author(ctx.author)
    embed8.add_field(name = "Balance", value = balance_amt)
    await ctx.send(embed = embed8)

@client.command(aliases=["sftty"])
async def skip_filing_taxes_this_year(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    earnings = random.range(101)
    await ctx.send(f"your insignificant financial presence in this world went unnoticed by the IRA. \n You managed to save your precious {earnings} dogecoins.")
    users[str(user.id)]["balance"] += earnings

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(users.id)] = {}
        users[str(users.id)]["balance"] = 0
    with open ("treasury.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("treasury.json","r") as f:
        users = json.load(f)















client.run(Token)
#https://discordpy.readthedocs.io/en/latest/faq.html
