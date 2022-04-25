#!/usr/bin/env python3
#import discord library and logging services
import discord
import logging

#create token ID var
TOKEN = 'OTY3ODcxNTE3NDgyNDQyODMy.YmWmlw.0LyKnDT9pn0pdhhl1CWvE6i8ef4'

#test line for initial setup debug
#print("Docker is working!")

#configure logging 
#logging.basicConfig(level=logging.INFO)

#create the client object
client = discord.Client()

#init message
@client.event
async def on_ready():
	print("Hello!  I've joined your server as {0.user}".format(client))

#bot events go here:
@client.event
#async message handling
async def on_message(message):
	#don't talk to yourself
	if message.author == client.user:
		return
	#general response to greetings
	if message.content.startswith("$hello"):
		await message.channel.send(f"Hello, {message.author.display_name}!")
		return
	#general response to goodbyes
	if message.content.startswith("$bye"):
		await message.channel.send(f"Goodbye {message.author.display_name}!")
		return
	else:
		print("sent {message.content} \nby {message.author.display_name}")
	

client.run(TOKEN)
