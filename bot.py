import discord
import json

class RsynClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.secrets = RsynClient.load_secrets()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    @staticmethod
    def load_secrets():
        with open('secrets.json', 'r') as secrets_file:
            secrets_json = secrets_file.read()
            return json.loads(secrets_json)

    def run(self):
        super().run(self.secrets['clientSecret'])
        print(self.secrets['clientSecret'])
        
