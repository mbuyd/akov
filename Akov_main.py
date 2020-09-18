import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle
client = discord.Client()
Prefix = "." 
 
client = commands.Bot(command_prefix = Prefix)
activity = ["with your mom", "with plutonium rods", "the game of LIFE", "Minecraft", "Spotify", "Ping-Pong", "with Balls", "dead", "BIOCHEMISTRY: A SHORT COURSE by John L. Tymoczko, Jeremy M. Berg, and Lubert Stryer", "against Albert", "someone's nerves", "with Akov's reproduction cycle", "with my own code"]
status = cycle(activity)

author = message.author
message.content = message.content.lower()


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
                   f"<@{message.author.id}> **DID YOU KNOW #19742 \n This portion of code was actually yeeted off of Leo's bot "
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
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    return

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} was banned for {reason}")
    return

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban.entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} was unbanned")
            return


@tasks.loop(hours=24)
async def change_status():
    await client.change_presence(activity=discord.Game(next(activity)))
    
client.run("token")
