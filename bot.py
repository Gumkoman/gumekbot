from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:5azuqj7javjpphicypswpsk1jetc7j', client_id='msce0fpihm3wrlt1l10lk3b3mmydio', nick='gumekBot', prefix='!',
                         initial_channels=['gumkoman'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='b')
    async def my_command(self, ctx):
        await ctx.send(f'{ctx.author.name} turniej do 4k mmr - https://challonge.com/Tvc15a turniej 4k-5.2k mmr https://challonge.com/pl/Tvc15b!')
    @commands.command(name='czesc')
    async def polacyCommand(self, ctx):
        await ctx.channel.send("elo")


bot = Bot()
bot.run()