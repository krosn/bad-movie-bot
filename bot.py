import discord
import json
from typing import List

from redditBadMovies import RedditBadMovieClient, BadMovie
from secrets import Secrets

class RsynClient(discord.Client):
    def __init__(self, secrets: Secrets, movie_client: RedditBadMovieClient):
        super().__init__()
        self.secrets = secrets
        self.movie_client = movie_client

    @staticmethod
    def _message_contains(message: discord.Message, phrase: str) -> bool:
        return phrase.lower() in message.content.lower()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        if message.author == self.user or message.author.bot:
            return  

        print('Message from {0.author}: {0.content}'.format(message))   
        
        if self._message_contains(message, 'gordon'):
            await self.hello_gordon(message)

        if self._message_contains(message, 'movie'):
            await self.handle_movie(message)
            
    async def hello_gordon(self, message: discord.Message) -> None:
        await message.channel.send('hello gordon', tts=True)
        await message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi1.sndcdn.com%2Fartworks-QwRMSCwG63LDTzm8-nfxz6A-t500x500.jpg&f=1&nofb=1')

    async def handle_movie(self, message: discord.Message) -> None:
        # TODO: Check that this isn't called too often
        movies: List[BadMovie] = self.movie_client.get_top_five()
        
        for i, movie in enumerate(movies):
            lines = []
            lines.append(f'Option #{i + 1}')
            lines.append(movie.title)
            lines.append(movie.url)
            lines.append(f'With {movie.upvotes}, critics are raving: ')
            (lines.append(comment) for comment in movie.commments)

            post = '\n'.join(lines)
            await message.channel.send(post)

    def run(self):
        super().run(self.secrets.discord_client_secret())
        
