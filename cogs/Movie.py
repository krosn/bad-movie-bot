from discord import Member
from discord.ext import commands
from typing import List

from reddit.badMovies import RedditBadMovieClient, BadMovie

class MovieCog(commands.Cog):
    def __init__(self, bot: commands.Bot, movie_client: RedditBadMovieClient):
        self.bot = bot
        self.movie_client = movie_client
            
    @commands.command()
    async def movie(self, ctx) -> None:
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
            await ctx.channel.send(post)