import discord
from discord import member
from discord import embeds
from discord.ext import commands
from discord.ext.commands.converter import EmojiConverter
from discord.flags import alias_flag_value
from discord.utils import get
import requests
from GoogleNews import GoogleNews
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
        await ctx.send("you don't have permission to use this command")


# kick member
@bot.command()
async def kick( ctx, user: discord.Member,*, reason=None):
    if ctx.author.guild_permissions.administrator:
        await user.kick(reason=reason)
        embed = discord.Embed(title = "KICK",description = f"{user.mention} has been removed")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "KICK", description=f" {ctx.author.mention} you don't have permissions to use this command" )
        await ctx.send(embed=embed)


@bot.command()
async def rolemessage(ctx):
    
    await ctx.send("Give Yourself a role by reacting to emojis\n:programmer: - Programmer\n:python: - Python\n:webdeveloper: - Web Developer\n:graphisdesigner: - Graphics Designer")


#self- role
@bot.event
async def on_raw_reaction_add(payload):
    Ourmessageid = 845977291892719636

    if Ourmessageid == payload.message_id:
        member = payload.member
        guild = member.guild
        
        emoji = payload.emoji.name

        if emoji == 'programmer':       
            role = discord.utils.get(guild.roles, name="Programmer")
            await member.add_roles(role)
        
        elif emoji == 'python':
            role = discord.utils.get(guild.roles, name= "Python")
            await member.add_roles(role)
        
        elif emoji == 'webdeveloper':
            role = discord.utils.get(guild.roles, name="Web Developer")
            await member.add_roles(role)
        elif emoji == 'graphisdesigner':
            role = discord.utils.get(guild.roles, name="Graphic designer")
            await  member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    Ourmessage = 845977291892719636

    if Ourmessage == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name

        if emoji == 'programmer':
            role = discord.utils.get(guild.roles, name="Programmer")

        elif emoji == 'python':
            role = discord.utils.get(guild.roles, name="Python")

        elif emoji == 'webdeveloper':
            role = discord.utils.get(guild.roles, name="Web Developer")

        elif emoji == 'graphisdesigner':
            role = discord.utils.get(guild.roles, name="Graphic designer")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("member not found")


#give adminco
admin =     "Type !warn to warn some user \n \n Type !addrole and (role) name and (mention user)\n \n Type !remove and (role) name and (mention user)"


@bot.command()
async def admincommands(ctx):
    embed = discord.Embed(title = "Admin Commands" , description = admin, color= discord.Color.green())
    await ctx.send(embed=embed)

#help
helpvar = [
    "type !inspire",
    "type !ping",
    "type !hello"
    "type !hello"
    "type !news"
]

@bot.command()
async def help(ctx):
    await ctx.send(helpvar)

bot.run('ODQzNTUwMTk3NTU5NTkwOTMz.YKFfVw.sfK80g0CsLwGyFWGV3p0FX4hl5c')