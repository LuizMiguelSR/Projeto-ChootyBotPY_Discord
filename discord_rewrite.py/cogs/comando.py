import discord
from discord.ext import commands

#definir classe
class comando(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def ajuda(self, ctx):
      embed = discord.Embed(title="📑 LISTA DE COMANDOS 📑", description=f"Olá {ctx.message.author.mention} abaixo temos a lista com os comandos do nosso bot.", color=0xef1515)
      embed.set_author(name="ChootyBot", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
      embed.set_image(url="https://i.imgur.com/XYb0400.jpg")
      embed.add_field(name="!config", value="Configurações do Server", inline=True)
      embed.add_field(name="!oi", value="Boas vindas", inline=True)
      embed.add_field(name="!ping", value="Retorna com seu ms", inline=True)
      embed.add_field(name="!kasino", value="Vai DJ!", inline=True)
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(comando(client))