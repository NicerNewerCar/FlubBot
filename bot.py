import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random
import requests
import PIL
from botkeyFlub import *
import asyncio

bot = commands.Bot(command_prefix='$')

#1) voice flub
#2) the ai will take an image on the server and put flub on it in a random place
#5) Flub and bad together in same message flub bot goes brrrrrrrrrr
#6) repost deleted messages with somesort of insult

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=playing))
    #discord.opus.load_opus('opus')

#Command that makes FlubBot force a deep dream onto a photo
@bot.command()
async def flube(ctx):
    try:
        if (ctx.message.attachments[0].id > 0):
            url = ctx.message.attachments[0].url
            url = dreamer(10,url)
            await ctx.send(url)
            await ctx.send('FℲ... L˥... U∩... Bq...')
    except IndexError:
        await ctx.send('FLUB... Error... Fluuuub... Try again but with the command as a caption to a photo Fluuuuuuuuuuuuuuuuuuuubbbb!!!')
        pass

#Command that makes flubbot quote XRA
@bot.command()
async def xra(ctx):
    quotes = ['"Life. You could say it started when I was a kid. Like most folks, I\'ve always been different. But not like the others. Other kids could be cruel, they\'d call me names: dweeb, chimp, honky, dweeby-chimp, honky-dweeb, and worst of all: chomsky-honk. Did you know there\'s over eighty-seven combinations of those soul-scalding words? I found out the hard way. Life! Adolescence was better: went to the prom with a model, but she left with some jock. Dyke!"— Xavier',
              '"Fate. Destiny. Fatestinatey. People toss those words around like tennis balls. Well, I eat balls for breakfast."— Xavier','"Don\'t you see? The missing child you each seek to reconnect with is still inside you all. But you buried it. You, Paul, when you were six and you killed that spider monkey with that claw hammer, you really just squashed your heart with that hammer, and that\'s why you became a dirty pig cop."—The EverChild',
              '"Unload your troubles unto me, even if it\'s tough to swallow. I\'m used to swallowing huge loads."— Xavier',
              '"Every luxury has a deep price. Every indulgence, a cosmic cost. Each fiber of pleasure you experience causes equivalent pain somewhere else. This is the first law of emodynamics. Joy can be neither created nor destroyed. The balance of happiness is constant. Fact: Every time you eat a bite of cake, someone gets horsewhipped. Facter: Every time two people kiss, an orphanage collapses. Factest: Every time a baby is born, an innocent animal is severely mocked for its physical appearance. Don\'t be a pleasure hog. Your every smile is a dagger. Happiness is murder. Vote "yes" on Proposition 1321. Think of some kids. Some kids."— A hallucination',
              '"The pride I feel for finally fingering my father\'s killer is dampened only by the fact that I promised to kill my father\'s killer. I fingered myself. To death."— Xavier',
              '"This is what the tandem cycle of random violence breeds! A vengeful black hit-sludge with a grudge hath brought the reaper you\'ve sown in the goo of your guilt, as the créme-de-karma is roosting home to harm ya. It always ends up boning the poor."— Xavier'
              ]
    random.shuffle(quotes)
    await ctx.send(quotes[0])

#command to get flubbot to say "MY name Jeff"
@bot.command()
async def jeff(ctx):
    await ctx.send("My Name Jeff!")

#command to get flubbot to join an audio channel
@bot.command()
async def flub(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    #If flub and bad are together in the same message then flubbot will kick the
    #user and then PM them an invite
    if 'flub' in message.content.lower() and 'bad' in message.content.lower():
        await message.channel.send('<@'+str(message.author.id)+'> ,BE GONE HEATHEN!')
        await message.author.send('https://discord.gg/W9XWFGs')
        await (message.author).kick(reason=None)


    num = random.randint(0,101)
    try:
        if(message.attachments[0].id > 0) and num > 95:
            url = message.attachments[0].url
            url = dreamer(4,url)
            await message.channel.send(url)
            await message.channel.send('FℲ... L˥... U∩... Bq...')
    except IndexError:
        pass
    if num >= 90:
        await message.channel.send(speak())
    if num <= 35:
        emojis = ['<:Steve:783174768618111046>','<:pog:783174768618111046>','<:doge_rape:783174738016206908>','<:pickleflub:719426147573825606>','<:flubneedle:719426220294668298>','<:flubeyeR:719427389440131075>','<:flubeyeL:719426985138454592>']
        random.shuffle(emojis)
        await message.add_reaction(emojis[0])


#Functions:
def dreamer(num, url):
    print('dreaming...\n')
    for x in range(num):
        r = requests.post("https://api.deepai.org/api/deepdream",data={'image':url,},headers={'api-key':API_Key})
        responce = str(r.json())
        x = responce.find('output_url')
        url = ''
        for i in range(x+14,len(responce)-2):
            url += responce[i]
        return url

def speak():
    statments = ['flub Flub FLUB?','fLuUuUuB?!?!?!?!','flub flub flub flub flub flub?',
                'Im going to break into your house and flub you','FLUB!','flubber',
                'flubba','flubbed','F̡̡̧̤͕̯̱̗̝͖̫͚̞͙͙͖̻̘̙̅͑ͣ͛̈̀ͅl̵̢̢͙͖͓̰̱̗͕̻̯͈͍̰͈̣̻̿ͥ̈́͛̈̎̌̐͜͝ͅữ̸̡̢̲̬̲̲̠̝̣͎͌̃ͨ̿̉ͦ̇̏̿̇͌͌̋̆ͮͫͩ̐͘b̸͎̜̼̌͂͑̃̍ͣͧͦ̐͂ͭ̿̆ͤͤͧ͘͘͘͜','flubted','F,L,U,B,','Flub me daddy',
                'Flub me harder Daddy','FFFFFFFFFLLLLLLLLLLLLLUUUUUUUUUUUBBBBBBBBBBB',
                'f       l           u         b','F... L... U... B...','Mr.Flub i dont feel so good'
                ]
    random.shuffle(statments)
    msg = statments[0]
    return msg

bot.run(bot_token)
