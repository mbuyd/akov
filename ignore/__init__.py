from random import choice, random
import json
from discord.ext import commands
import requests
from requests import get as get2
import os
from bs4 import BeautifulSoup

dic = json.load(open("dictionary.json"))
botlandchan = dic["botlandchan"]

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

@commands.command(pass_context=True)
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

@commands.command(pass_context=True)
async def hotplate(ctx, message):
    return

@commands.command(pass_context=True, aliases=["r"])
async def reddit(ctx, message):
    headers = {'User-Agent': 'Akov Anonymous Version 1.0.3'}
    reddit_post = get2(f'https://www.reddit.com/r/{message}/random.json', headers = headers).json()
    if (reddit_post[0]['data']['children'][0]['data']['over_18']):
        if ctx.channel.is_nsfw():
            try:
                await ctx.send(reddit_post[0]['data']['children'][0]['data']['url'])
            except:
                await ctx.send("Subreddit does not exist \n Try another")
    else: 
        try:
            await ctx.send(reddit_post[0]['data']['children'][0]['data']['url'])
        except:
            await ctx.send("Subreddit does not exist \n Try another")
