from bot import RsynClient
from secrets import Secrets
from reddit.badMovies import RedditBadMovieClient

if __name__ == "__main__":
    secrets = Secrets('secrets.json')
    movie_client = RedditBadMovieClient(secrets)
    discord_bot = RsynClient(secrets, movie_client)
    discord_bot.run()
    # TODO: Host this in AWS