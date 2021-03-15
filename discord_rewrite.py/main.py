#lista dos import's
import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or

#lista de modulos
modulos = ["cogs.comando","cogs.ping","cogs.welcome","cogs.config","cogs.kasino"]

#evento do client
client = AutoShardedBot (command_prefix="!", case_insensitive=True)

#evendo do on_ready
@client.event
async def on_ready():
    print(f"{client.user.name} está Online.")
    await client.change_presence(activity=discord.Streaming(name="!ajuda", url="https://www.twitch.tv/123"))

#carregar modulos & token
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)
    
    client.run("token")