import discord
from discord.ext import commands

#Bot Command
bot = commands.Bot(command_prefix='!')






@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round (bot.latency * 1000)} ms")



@bot.event
async def on_ready():
    print("Bot is live")
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"hello, {ctx.author.mention}")

"""!warn @mention-user"""
@bot.command(pass_context=True)
async def warn(ctx, *, user: discord.Member = None):
    if ctx.author.guild_permissions.administrator:
        await ctx.send(f"you have been warned`` {user.mention}")
        await user.send(f"you have been warned`` {user.mention}")
    else:
        await ctx.send("{ctx.author.mention} you dont have permissions to use this command")

"""!addrole (rolename)  @mention-user"""
@bot.command()
async def addrole(ctx, role: discord.Role , user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)  
        await ctx.send(f" Successfully give {role.mention} Role to {user.mention}")
    else:
        await ctx.send(f"{ctx.author.mention} you don't have permissioms to use this command")
        

"""!removerole (rolename) @mention-user"""
@bot.command()
async def removerole(ctx, role:discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        await ctx.send(f"Successfully remove {role.mention} Role to {user.mention} ")
    else:
        await ctx.send(f"{ctx.author.mention} you don't have permissions to use this command")
        
        


"""!kick @mention-user"""
@bot.command()
async def kick( ctx, user: discord.Member,*, reason=None):
    if ctx.author.guild_permissions.administrator:
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} has been removed")
    else:
        await ctx.send(f"{ctx.author.mention} you don't have permissions tp use this command")
        



bot.run('your bot token')
