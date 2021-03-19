import discord
from discord.ext import commands

#definir classe
class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def oi(self, ctx):
        embed = discord.Embed(title="", description= f"Obrigado, {ctx.message.author.mention} seja bem vindo ao nosso discord.", color=0xfdf7f7)
        embed.set_author(name="ChootyBot - 😍 BEM VINDO 😍 ", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
        embed.set_image(url="https://i.imgur.com/KEU40LM.gif")
        await ctx.send(embed=embed)

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def adeus(self, ctx):
        embed = discord.Embed(title="", description= f"{ctx.message.author.mention} ficamos tristes com sua partida.", color=0xfdf7f7)
        embed.set_author(name="ChootyBot - 😭 ADEUS 😭 ", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
        embed.set_image(url="https://i.imgur.com/UjIb9DT.gif")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(welcome(client))