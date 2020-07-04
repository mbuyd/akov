import requests
import os
import string
import json
import smtplib
import discord
from discord import commands

class Orachikov(commands.Cog):
    def ___init___(self, client):
        self.client = client

#events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Orachikov is online")


#commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send (f"Pong! {round(client.latency *1000)} ms" )

def setup(client):
    client.add_cog(Orachikov(client))

sixtyfour = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/64'
cafev = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/18'
canyonvista = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/24'
clubmed = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/15'
foodworx = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/11'
goodys = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/06'
oceanview = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/05'
pines = 'https://hdh-web.ucsd.edu/dining/apps/diningservices/Restaurants/MenuItem/01'



#data64 = requests.request(url=sixtyfour allow_redirects=False, method = "GET")
dataventanas = requests.request(url=cafev, allow_redirects=False, method = "GET")
datacanyon = requests.request(url=canyonvista, allow_redirects=False, method = "GET")
#dataclubmed = requests.request(url=clubmed, allow_redirects=False, method = "GET")
#datafoodworx = requests.request(url=foodworx, allow_redirects=False, method = "GET")
#datagoodys = requests.request(url=goodys, allow_redirects=False, method = "GET")
#dataoceanview = requests.request(url=oceanview, allow_redirects=False, method = "GET")
datapines = requests.request(url=pines, allow_redirects=False, method = "GET")

#####print (data.text)####


#if "orange chicken" in data64.text:
#    print ("Orange Chicken @ 64")

if "Gyro" in dataventanas.text:
    print ("Gyro @ CafeV")
if "grits" in dataventanas.text:
    print ("Shrimp & Grits @ CafeV")


if "Salmon Sandwich" in datacanyon.text:
    print ("Salmon Sandwich @ Canyon Vista")

#if "" in dataclubmed.text:
#    print (" @ Club Med")

#if "" in datafoodworx.text:
#    print (" @ Foodworx")

#if "" in datagoodys.text:
#    print (" @ Goodies")

#if "" in dataoceanview.text:
#    print ("@ Oceanview")

if "Lemon Herb Salmon" in datapines.text:
    print ("Lemon Herb Salmon @ Pines")
if "Chicken Alfredo Pasta" in datapines.text:
    print ("Chicken Alfredo Pasta @ Pines")


else:
    print ("done")