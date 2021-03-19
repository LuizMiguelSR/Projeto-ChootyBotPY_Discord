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
      nome1 = ("!config","!talic","!drop [PB]","!ping","!adeus","!oi","!kasino")
      value1 = ("Configurações do server","Chance de sucesso ao talicar","Mostra o drop de cada PB","Retorna com ms","Até logo","Boas vindas","Vai DJ!",)
      embed = discord.Embed(title="", description=f"{ctx.message.author.mention} comandos de ajuda", color=0xfdf7f7)
      embed.set_thumbnail(url="https://i.imgur.com/l7gm6w1.png")
      embed.set_footer(text="Site: www.newrf.com.br")
      embed.set_author(name="ChootyBot - AJUDA ", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
      embed.add_field(name="Comandos", value=f"```{nome1[0]:<15}{value1[0]:<6}\n{nome1[1]:<15}{value1[1]:>6}\n{nome1[2]:<15}{value1[2]:>6}\n{nome1[3]:<15}{value1[3]:>6}\n{nome1[4]:<15}{value1[4]:>6}\n{nome1[5]:<15}{value1[5]:>6}```", inline=True)
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(comando(client))