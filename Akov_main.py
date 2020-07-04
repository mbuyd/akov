import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    return
    

@client.event
async def on_remember_remove(member):
    print(f'{member} has left the server.')
    return

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{ctx.author} cleared {amount} messages \n      **LIKE A BOSS**")
    return

@client.command()
async def bing(ctx):
    await ctx.send(f"Bong! {round(client.latency *1000)} ms" )
    return

@client.command(aliases=["is","check"])
async def ball(ctx,*, question):
    responses=["yes", "definitely", "yes"]
    await ctx.send(f"You asked: {question} \n Your answer is: {random.choice(responses)}")
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

@client.command
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")



for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzI3NjAzMTA0ODA3MjU2MTY4.XvuPog.H5ZZSrgmCH6oK2ndsTHeYz7yK3U")