from discord import Member
from discord.ext import commands

class CoomerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def command_test(self, ctx, arg):
        await ctx.send(f'{ctx.author.name} says {arg}')
            
    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'HELLO {member.display_name}! I need to see your passport.')

    @commands.command(name='gordon')
    async def hello_gordon(self, ctx) -> None:
        await ctx.send('hello gordon', tts=True)
        await ctx.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi1.sndcdn.com%2Fartworks-QwRMSCwG63LDTzm8-nfxz6A-t500x500.jpg&f=1&nofb=1')
