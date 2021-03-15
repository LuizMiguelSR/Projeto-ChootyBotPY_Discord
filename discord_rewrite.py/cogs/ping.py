from discord.ext import commands
import time

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓Pong!  `{int(ping)}ms`")
        print(f'Ping {int(ping)}ms')

def setup(client):
    client.add_cog(ping(client))