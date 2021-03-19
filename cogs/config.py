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
      nome1 = ("Versão","Quest","Level máximo","Sell Rate","Skill Force","HDH","Elven itens","Dual Client","Máx Upgrade","Exp","Drop","Animus","Cash")
      value1 = ("2.2.2.3","OFF","55","10kk","GM","ON","OFF","ON","+6","40x normal/60x premiun","05x normal/10x premiun","200x normal/300x premiun","05 normal/10 premiun")
      embed = discord.Embed(title="", description=f"{ctx.message.author.mention} configurações do servidor", color=0xfdf7f7)
      embed.set_thumbnail(url="https://i.imgur.com/l7gm6w1.png")
      embed.set_footer(text="Site: www.newrf.com.br")
      embed.set_author(name="ChootyBot - CONFIGURAÇÕES ", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
      embed.add_field(name="Servidor New RF", value=f"```{nome1[0]:<35}{value1[0]:<6}\n{nome1[1]:<35}{value1[1]:>6}\n{nome1[2]:<35}{value1[2]:>6}\n{nome1[3]:<35}{value1[3]:>6}\n{nome1[4]:<35}{value1[4]:>6}\n{nome1[5]:<35}{value1[5]:>6}\n{nome1[6]:<35}{value1[6]:>6}\n{nome1[7]:<35}{value1[7]:>6}\n{nome1[8]:<35}{value1[8]:>6}\n{nome1[9]:<20}{value1[9]:>6}\n{nome1[10]:<20}{value1[10]:>6}\n{nome1[11]:<18}{value1[11]:>6}\n{nome1[12]:<22}{value1[12]:>6}```", inline=True)
      await ctx.send(embed=embed)

#envia para a main.py 
def setup(client):
    client.add_cog(config(client))