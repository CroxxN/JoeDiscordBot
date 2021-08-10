import os
import random
import discord
from copypasta import *
import time
from discord.ext import commands
from server import server


# my_secret = os.environ['TOKEN']
among_var = ["amogus", "among us", "amongus"]
all_among_words = ["vent", "imposter", "sus",]
amoji = '<:amoji:874539451504791553>'
nice = ["69", "sixty nine"]
client = discord.Client()
@client.event
async def on_ready():
  print("The bot is running")
  await client.change_presence(activity=discord.Game(name = "On Your Girl(&)"))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if any(word in message.content.lower() for word in among_var):
    await message.add_reaction(amoji) 
    await message.channel.send(random.choice(amongus))
    
  
  
  if any(word in message.content.lower() for word in all_among_words):
    await message.channel.send(random.choice(among_reference))
  
  if any(word in message.content for word in nice):
    await message.channel.send("nice")
  
  if message.content == "&bruh":
    await message.channel.send("Bruh")
    time.sleep(1)
    await message.delete()

  if message.content == "&trinity":
    await message.channel.send(trinity)
    await message.channel.send(trinity2)

  
  

  if '&insult' in message.content:
    if (message.mentions.__len__()>0): 
      for user in message.mentions: 
        user_id = user.id 
      if user.name != "Joe Mama":
        await message.channel.send(f"{user.mention} {random.choice(insults)}")
      if user.name == "Joe Mama":
        await message.channel.send(f"{user.mention} {praise}")
    else:
      await message.channel.send(random.choice(insults))
    time.sleep(1)
    await message.delete()


  if '&simp' in message.content:
    if (message.mentions.__len__()>0): 
      for user in message.mentions: 
        user_id = user.id 
      if user.name != "Joe Mama":
        await message.channel.send(f"{user.mention} {simp}")
      if user.name == "Joe Mama":
        await message.channel.send(f"{user.mention} {praise}")
    else:
      await message.channel.send(simp)
    time.sleep(1)
    await message.delete()

server()
client.run(os.environ['TOKEN'])