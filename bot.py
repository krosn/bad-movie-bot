import discord
from discord.ext import commands
import json
from typing import List

from redditBadMovies import RedditBadMovieClient, BadMovie
from secrets import Secrets

class RsynClient(commands.Bot):
    def __init__(self, secrets: Secrets, movie_client: RedditBadMovieClient):
        super().__init__(command_prefix='^')
        self.secrets = secrets
        self.add_cog(CoomerCog(commands.Bot(self)))
        self.add_cog(MovieCog(commands.Bot(self), movie_client))

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    def run(self):
        super().run(self.secrets.discord_client_secret())


class CoomerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def command_test(self, ctx, arg):
        await ctx.send(f'{ctx.author.name} says {arg}')
            
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'HELLO {member.display_name}! I need to see your passport.')

    @commands.command(name='gordon')
    async def hello_gordon(self, ctx) -> None:
        await ctx.send('hello gordon', tts=True)


class MovieCog(commands.Cog):
    def __init__(self, bot: commands.Bot,movie_client: RedditBadMovieClient):
        self.bot = bot
        self.movie_client = movie_client
            
    @commands.command()
    async def movie(self, message: discord.Message) -> None:
        # TODO: Check that this isn't called too often
        movies: List[BadMovie] = self.movie_client.get_top_five()
        
        for i, movie in enumerate(movies):
            lines = []
            lines.append(f'Option #{i + 1}')
            lines.append(movie.title)
            lines.append(movie.url)
            lines.append(f'With {movie.upvotes} upvotes, critics are raving: ')

            for comment in movie.comments:
                lines.append(comment)

            post = '\n'.join(lines)
            await message.channel.send(post)
