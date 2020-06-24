from __future__ import annotations
import praw
from typing import List

from secrets import Secrets

class RedditBadMovieClient:
    def __init__(self, secrets: Secrets):
        self.secrets = secrets
        self.reddit = praw.Reddit(
            client_id="4pQR_oo7AJTdlg", 
            client_secret=self.secrets.reddit_client_secret(),
            user_agent="rsyn-bad-movies/0.1")

    def get_top_five(self) -> List[BadMovie]:
        bad_movies = self.reddit.subreddit("badmovies")

        movies = []

        # Get top Suggestions of the week
        for submission in bad_movies.top(time_filter="week", limit=10, params={'flair_name': 'Suggestion'}):
            submission: praw.models.Submission
            if submission.url:
                movies.append(submission)
        
        # We originally got 10 in case a few were missing urls, 
        # now just take the first 5 of those
        movies = movies[:5]

        return [BadMovie(movie.title, movie.url, movie.score, movie.comments.list()) for movie in movies]


class BadMovie:
    def __init__(self, title: str, url: str, upvotes: int, commments: List[str]):
        self.title = title
        self.url = url
        self.upvotes = upvotes
        self.commments = commments

