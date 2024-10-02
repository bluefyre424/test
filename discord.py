import discord
import random
import asyncio
from discord.ext import commands

# Bot setup
bot = commands.Bot(command_prefix="!")
bounty_location = None
reward = 10  # UEC reward for correct guesses
star_systems = ["Stanton I", "Stanton II", "Stanton III"]

# Function to randomly select the bounty's location
async def set_bounty():
    global bounty_location
    while True:
        # Choose a random location from the star systems
        bounty_location = random.choice(star_systems)
        print(f"New bounty set at {bounty_location}")

        # Announce the new bounty (optional)
        channel = discord.utils.get(bot.get_all_channels(), name='general')  # Adjust 'general' to your desired channel
        if channel:
            await channel.send("A new bounty is on the move between the Stanton systems! Guess its current location!")

        # Wait for a random time between 2 to 5 minutes
        await asyncio.sleep(random.randint(120, 300))

# Start the bounty guessing game
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    bot.loop.create_task(set_bounty())  # Start the bounty location task

# Command to guess the bounty's location
@bot.command()
async def guess(ctx, *, guessed_location: str):
    global bounty_location
    guessed_location = guessed_location.strip()

    if guessed_location not in star_systems:
        await ctx.send(f"{guessed_location} is not a valid star system. Please choose from: {', '.join(star_systems)}")
        return

    if guessed_location == bounty_location:
        await ctx.send(f"Congratulations {ctx.author.mention}, you guessed correctly! You earn {reward} UEC!")
        # Add UEC reward logic here (optional)
    else:
        await ctx.send(f"Sorry {ctx.author.mention}, the bounty is not in {guessed_location}.")

# Start the bot
bot.run('YOUR_BOT_TOKEN')
