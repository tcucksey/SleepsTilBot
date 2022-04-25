#!/usr/bin/env python3
#import discord library and logging services
import discord
import os
import dotenv

from dotenv import load_dotenv
from discord.ext import commands
import logging

#create token ID var - should replace this with an env variable later
TOKEN = os.getenv('DISCORD_TOKEN')

#test line for initial setup debug
print("I'm awake!")

#configure logging 
logging.basicConfig(level=logging.INFO)

#create a command definition
bot = commands.Bot(command_prefix='!')

#remove and define custom help command
bot.remove_command("help")
@bot.command(name="help")
async def help(ctx):
	await ctx.channel.send("Here's how to use me: \n**!events**: List all registered events \n**!add_event**: EDIT ME \n**!cancel_event**:  EDIT ME \n**!sleeps** _<EVENTNAME>_: Tell me how many sleeps til this event starts \n**!help** See this menu \n**!ping**: Check I'm awake \n**!bonk** reply to someone with this command if they need to go to horny jail. \n")


#command for finding upcoming events
@bot.command(name="events")
async def events(ctx):
	await ctx.reply("I'll learn how to do that soon hopefully :) ")
	#list all events with a start date after today; delete events that have passed
	
@bot.command(name="add_event")
async def add_event(ctx):
	await ctx.reply("I'll make a note of it!")
	#repeat name and start date
	
@bot.command(name="cancel_event")
async def cancel_event(ctx):
	await ctx.reply("I'll take it off the list!")
	#repeat event name deleted
	

#Command for how many sleeps til?
@bot.command(name="sleeps")
async def sleeps(ctx, arg1):
	await ctx.reply("it's probably soon, I'm not that smart yet!  This section's still under construction\n")
	#look up event name
	await ctx.reply("Checking if I know about that one...\n")
	eventName = arg1
	#finder logic here
	found = "FALSE"	
	await ctx.reply(f"You asked about {arg1}")

	#event not found	
	if found == "FALSE":
		await ctx.reply("I don't know about that event!  If you entered it right, make sure it's been added properly.")
	else:
		#event found - dif today's date from date of event and reply
		await ctx.reply("I know about that one!  It's x many sleeps away")

#test ping command
@bot.command(name="ping")
async def ping(ctx):
	await ctx.reply("pong")
	
@bot.command(name="bonk")
async def bonk(ctx):
	msgID = ctx.message.reference.message_id
	msg = await ctx.fetch_message(msgID)
	msgAuth = msg.author.id
	await ctx.reply(f"**BONK!**. <@{msgAuth}>, <@{ctx.message.author.id}> has decided you're too horny.  Cool off.\n https://media.tenor.com/images/8171c146496d29c960e05759926482ae/tenor.gif")

bot.run(TOKEN)
