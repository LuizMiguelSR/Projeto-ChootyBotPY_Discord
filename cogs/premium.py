import discord
from discord.ext import commands

#definir classe
class premium(commands.Cog):
    def __init__(self, client):
        self.client = client

#evento webhook
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def premium(self, ctx):
        embed = discord.Embed(title="Link para donates", url="https://picpay.me/luiz.miguel.sr", description="", color=0xfdf7f7)
        embed.set_thumbnail(url="https://i.imgur.com/l7gm6w1.png")
        embed.set_image(url="https://i.imgur.com/XIkYkHu.png")
        embed.set_author(name="ChootyBot - AJUDA ", url="", icon_url="https://i.imgur.com/lI01A4T.jpg")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(premium(client))
