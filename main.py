import discord
from discord import FFmpegPCMAudio
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix='',intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Drummin\''))
    print("Greg is such a wimpy little moron lmao")
    print("Mornng losers")

intents.members = True

@client.command()
async def hi(ctx):
    await ctx.send("morning losers")

@client.command()
async def rodick(ctx):
    await ctx.send("it's spelt Rodrick fucking moron")

@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='idk why'):
    harassed = ", ".join(x.name for x in members)
    await ctx.send(f'mf {harassed} just got slapped by {ctx.author} \😂 \😂 \😂')

client.run(' #insert token ')
