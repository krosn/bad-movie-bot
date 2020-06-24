import json

class Secrets:
    def __init__(self, secrets_filepath: str):
        self.secrets_file = secrets_filepath
    
    def _get_value(self, key: str) -> any:
        with open(self.secrets_file, 'r') as sf:
            secrets = json.load(sf)
            return secrets[key]

    def discord_client_secret(self) -> str:
        return self._get_value('discordClientSecret')

    def reddit_client_secret(self) -> str:
        return self._get_value('redditClientSecret')