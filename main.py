import discord
import os, random
from discord.ext import commands
from discord.ext.commands import check
from base64 import b64decode, b64encode

#Questions
from questions.intro import Practice_Questions



TOKEN = "DISCORD_TOKEN_HERE"

bot = commands.Bot("!")



@bot.event
async def on_ready():
	print("\033c")
	print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):

	#Encode/decode certain strings
	if "to base64" in message.content:

		userInput = str(message.content).split("to")[0]

		#Checks to see if last character is space and removes it (<userInput>_to base64)
		if userInput[-1] == " ":
			userInput = userInput[:-1]

		userInput_Binary = b64encode(userInput.encode('ascii')).decode("utf-8", "ignore")

		await message.channel.send(userInput_Binary)

	if "from base64" in message.content:

		userInput = str(message.content).split("from")[0]

		#Checks to see if last character is space and removes it (<userInput>_to base64)
		if userInput[-1] == " ":
			userInput = userInput[:-1]

		userInput_Binary = b64decode(userInput.encode('ascii')).decode("utf-8", "ignore")

		await message.channel.send(userInput_Binary)
	
	#allows other commands to work, info=https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
	await bot.process_commands(message)


@bot.command()
async def askme(ctx):
	commands_channel_id = 832108977600987187
	cyberheavenBot_channel_id = 991494665553592340
	
	if ctx.channel.id != commands_channel_id or ctx.channel.id != cyberheavenBot_channel_id:
		await ctx.channel.send(f"Wrong Channel Please use <#832108977600987187>")
		return

	QuestionSelection = random.randint(1, (len(Practice_Questions) - 1))

	Question = Practice_Questions[QuestionSelection]["Question"]
	Answer = Practice_Questions[QuestionSelection]["Answer"].lower()

	# Prints the question
	await ctx.send(f"{QuestionSelection}.) {Question}")


	# Waits for response
	while True:
		msg = await bot.wait_for("message", check=check)

		UserAnswer = str(msg.content).lower()

		#Same Author
		if msg.author.id == ctx.author.id:
			#Same Discord Channel
			if msg.channel.id == ctx.channel.id:
				

				#Checks if the answer is correct
				if UserAnswer == Answer:
					await ctx.send("Correct!")
					break

				else:
					await ctx.send(f"Incorrect, {Answer} was the correct answer")
					break






if __name__ == "__main__":
    
    bot.run(TOKEN)
