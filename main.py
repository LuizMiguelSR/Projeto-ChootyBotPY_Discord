#lista dos import's
import discord
from discord.ext import commands
from asyncio import sleep


#lista de modulos
modulos = ["cogs.comando","cogs.ping","cogs.welcome","cogs.config","cogs.kasino","cogs.premium"]

#evento do client
client = commands.AutoShardedBot(commands.when_mentioned_or('!'))

#evendo do on_ready
@client.event
async def on_ready():
    print(f"{client.user.name} está Online.")
    await client.change_presence(activity=discord.Streaming(name="!ajuda", url="https://www.twitch.tv/123"))

#função de cálculo
def som(n: float, n2: float, n3: float):
	return n + n2 + n3

#comando reultado
@client.command()
async def talic(ctx, x: float, y: float, z: float):
	try:
		result = som(x, y, z)
		await ctx.send(f"A chance de sucesso é: {result}%")

	except:
		pass

#carregar modulos & token
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)
    
    client.run("TOKEN")
