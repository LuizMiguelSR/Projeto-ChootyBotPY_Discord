import discord
from discord.ext import commands

#definir classe
class config(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def config(self, ctx):
      embed = discord.Embed(title="❗ CONFIGURAÇÕES ❗", description=f"{ctx.message.author.mention} essas são as configurações do servidor", color=0x00ff00)
      embed.set_footer(text="Site: www.newrf.com.br")
      embed.set_author(name="ChootyBot", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
      embed.add_field(name="Versão", value="2.2.3.2", inline=True)
      embed.add_field(name="Lvl Máx.", value="55", inline=True)
      embed.add_field(name="Quest", value="OFF", inline=True)
      embed.add_field(name="Sell Rate", value="10kk", inline=True)
      embed.add_field(name="Skill force", value="GM", inline=True)
      embed.add_field(name="HDH", value="ON", inline=True)
      embed.add_field(name="Elven itens", value="OFF", inline=True)
      embed.add_field(name="Dual client", value="ON", inline=True)
      embed.add_field(name="Max. Upgrade", value="+6", inline=True)
      embed.add_field(name="Exp", value="40x normal/60x premiun", inline=False)
      embed.add_field(name="Drop", value="05x normal/10x premiun", inline=False)
      embed.add_field(name="Animus", value="200x normal/300x premiun", inline=False)
      embed.add_field(name="Cash", value="05 por min. normal/10 por min. premiun", inline=False)
      await ctx.send(embed=embed)

#envia para a main.py 
def setup(client):
    client.add_cog(config(client))