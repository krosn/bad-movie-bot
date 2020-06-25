import discord
from discord.ext import commands
import json

from cogs.Coomer import CoomerCog
from cogs.Movie import MovieCog
from secrets import Secrets
from reddit.badMovies import RedditBadMovieClient, BadMovie

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
