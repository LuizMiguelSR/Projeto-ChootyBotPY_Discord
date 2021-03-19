from discord.ext import commands

#definir classe
class kasino(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def kasino(self, ctx):
        await ctx.send("Você resgatou um :stars: KASINO! :stars:\nhttps://youtu.be/LCDaw0QmQQc")

def setup(client):
    client.add_cog(kasino(client))