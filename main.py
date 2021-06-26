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
        await ctx.send(f"``▏you have been warned`` {user.mention}")
        await user.send(f"``▏``you have been warned`` {user.mention}")
    else:
        await ctx.send("you dont have permissions to use this command")

"""!addrole (rolename)  @mention-user"""
@bot.command()
async def addrole(ctx, role: discord.Role , user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)  
        embed = discord.Embed(title = "GIVE ROLE", description =f"Successfully give {role.mention} Role to {user.mention} ")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "GIVE ROLE", description =f" {ctx.author.mention} you don't have permissions to use this command")
        await ctx.send(embed=embed)

"""!removerole (rolename) @mention-user"""
@bot.command()
async def removerole(ctx, role:discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        embed = discord.Embed(title = "REMOVE", description =f"Successfully remove {role.mention} Role to {user.mention}")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "REMOVE", description=f" {ctx.author.mention} you don't have permissions to use this command" )
        await ctx.send(embed=embed)
        


"""!kick @mention-user"""
@bot.command()
async def kick( ctx, user: discord.Member,*, reason=None):
    if ctx.author.guild_permissions.administrator:
        await user.kick(reason=reason)
        embed = discord.Embed(title = "KICK",description = f"{user.mention} has been removed")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "KICK", description=f" {ctx.author.mention} you don't have permissions to use this command" )
        await ctx.send(embed=embed)



bot.run('your bot token')
