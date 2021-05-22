import re
import discord
from discord import reaction
from discord import user
from discord import asset
from discord import message
from discord import member
from discord import guild
from discord import emoji
from discord import role
from discord.ext import commands
from discord.gateway import DiscordVoiceWebSocket
from discord.role import Role
import requests
from GoogleNews import GoogleNews
from discord import Embed
#import libarari
import json


bot = commands.Bot(command_prefix='!')

#removing commands
bot.remove_command("help")



#get google news data
googlenews = GoogleNews()
googlenews.search('computers')

resutl = googlenews.gettext()



#get quote code data
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" +json_data[0] ['a']
    return quote

#quote code
@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.channel.send(quote)

bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round (bot.latency * 1000)} ms")



@bot.event
async def on_ready():
    print("Bot is live")
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"hello, {ctx.author.mention}")

@bot.command()
async def news(ctx):
    await ctx.send(resutl)


@bot.command(pass_context=True)
async def warn(ctx, *, user: discord.Member = None):
    if ctx.author.guild_permissions.administrator:
        await ctx.send(f"``▏you have been warned`` {user.mention}")
        await user.send(f"``▏``you have been warned`` {user.mention}")
    else:
        await ctx.send("you dont have permissions to use this command")

# give role 
@bot.command()
async def addrole(ctx, role: discord.Role , user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)  
        await ctx.send(f"▏``Successfully give`` {role.mention} ``Role to`` {user.mention} ")
    else:
        await ctx.send("you dont have permissions to use this command")

# remove role
@bot.command()
async def remove(ctx, role:discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        await ctx.send(f"``▏Successfully remove`` {role.mention} ``Role to`` {user.mention}")
    else:
        await ctx.send("you dont have permission to use this command")


# kick member
@bot.command()
async def kick( ctx, user: discord.Member,*, reason=None):
    if ctx.author.guild_permissions.administrator:
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} has been removed")
    else: 
        await ctx.send(f"you dont have permissions to use this command")

#self- role
@bot.event
async def on_raw_reaction_add(payload):
    Ourmessageid = 845685655790026783

    if Ourmessageid == payload.message_id:
        member = payload.member
        guild = member.guild
        
        emoji = payload.emoji.name
        if emoji == 'programmer':       
            role = discord.utils.get(guild.roles, name="programmer")
        await member.add_roles(role)


#help
helpvar = [
    "type !inspire",
    "type !ping",
    "type !hello"
    "type !hello"
]

@bot.command()
async def help(ctx):
    await ctx.send(helpvar)

bot.run('ODQzNTUwMTk3NTU5NTkwOTMz.YKFfVw.sfK80g0CsLwGyFWGV3p0FX4hl5c')