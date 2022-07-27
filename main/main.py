# aki's development.   2022
# d-bot template. customize it as you want. basic discord bot


import  discord  as ds  #    py -m pip install discord
import  random   as rd
from    discord.ext import commands


token  = ''   # insert here your bot token.
prefix = '.' # replace with the prefix you want

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print(f'[+] bot online. logged in as {bot.user}')


# basic ping command
@bot.command(aliases=[])
async def command_name(ctx):
    await ctx.channel.send(f'pong! **{round(bot.latency * 1000)}**ms')

# basic random command
@bot.command(aliases = []) # put command aliases
async def random(ctx, *, question):
    random_phrases = [
        'yes', 'no',
        'probably yes', 'probably not',
        'maybe', 'maybe not'
        # put what you want
    ]
    
    choice = rd.choice(random_phrases)
    await ctx.channel.send(f'**question** : {question}\n**answer** : {choice}')


# embeds
embed = ds.Embed(
    title='yourtitle', 
    description='your first field', 
    color=ds.Colour.dark_orange
) # put the color you want


embed.set_thumbnail(url='thumbnail URL')
embed.set_footer(text='embed footer') # ex : command requested by {ctx.author}
embed.set_image(url='your image URL')
# embed.timestamp() add datetime in your embed.
embed.set_author(name='you#0101') # ex : ctx.author
embed.add_field(name='field title', value='field text')


# embed usage
@bot.command()
async def command(ctx):
    await ctx.channel.send(embed = embed)


# ds : akii#0101
bot.run(token)
