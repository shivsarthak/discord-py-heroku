import os
from discord.ext import commands

client = commands.Bot(command_prefix="au")
TOKEN = os.getenv("DISCORD_TOKEN")

@client.command()
async def muteAll(ctx):
    channel = client.get_channel(ctx.author.voice.channel.id)
    members = list(channel.members)
    for usr in members:
        await ctx.send(f"```[*] muting {usr.nick}```")
        await usr.edit(mute=True)


@client.command()
async def unmuteAll(ctx):
    channel = client.get_channel(ctx.author.voice.channel.id)
    members = list(channel.members)
    for usr in members:
        await ctx.send(f"```[*] unmuting {usr.nick}```")
        await usr.edit(mute=False)

if __name__ == "__main__":
    client.run(TOKEN)
