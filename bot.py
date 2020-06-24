import discord
import json

class RsynClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.secrets = RsynClient.load_secrets()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        if message.author == self.user or message.author.bot:
            return  

        print('Message from {0.author}: {0.content}'.format(message))   
        
        if 'gordon' in message.content.lower():
            await self.hello_gordon(message)
            
    async def hello_gordon(self, message: discord.Message) -> None:
        await message.channel.send('hello gordon', tts=True)
        # voice_state: discord.VoiceState = message.author.voice
        # author_voice_channel: discord.VoiceChannel = voice_state.channel

        # if not author_voice_channel:
        #     return
        
        # author_voice_client: discord.VoiceClient = author_voice_channel.connect() 
        # author_voice_client..send('hello gordon', tts=true)
        # message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi1.sndcdn.com%2Fartworks-QwRMSCwG63LDTzm8-nfxz6A-t500x500.jpg&f=1&nofb=1')

    @staticmethod
    def load_secrets() -> str:
        with open('secrets.json', 'r') as secrets_file:
            secrets_json = secrets_file.read()
            return json.loads(secrets_json)

    def run(self):
        super().run(self.secrets['clientSecret'])
        print(self.secrets['clientSecret'])
        
