import discord
import discord.ext
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.all() 
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

guild_id = os.getenv("guild_id")

# sync the slash command to your server
@client.event
async def on_ready():
    tree.copy_global_to(guild=discord.Object(id=guild_id))
    await tree.sync(guild=discord.Object(id=guild_id))
    print("ready")

# make the slash command
@tree.command(name="test", description="description")
async def slash_command(int: discord.Interaction):    
    await int.response.send_message("command")

# run the bot
client.run(os.getenv("token"))

