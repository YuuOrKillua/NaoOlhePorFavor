from pydoc import cli
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import pyttsx3
import youtube_dl
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

TOKEN = 'SECRET'

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='>', intents=intents)

@client.event
async def on_ready():
    print('Logado Como {0.user}'.format(client))

@client.command()
async def oi(ctx):
    await ctx.send('Cala boca!')
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel

@client.command()
async def tchau(ctx):
    await ctx.send('Foi tarde, seu arrombado.')

@client.command(pass_context = True)
async def entrar(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        
    else:
        await ctx.send("Você precisa estar em um canal de voz pra usar esse comando, sua mula!")

@client.command(pass_context = True)
async def sair(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Finalmente escapei desse subdesenvolvido!")
    else:
        await ctx.send("Eu não estou em um canal de voz sua mula!")

@client.command(pass_context = True)
async def carente():
    Humor = input('Como esta seu humor?')
    name = input('Qual seu nome?')

    i = ['feliz', 'triste', 'baiana', 'carente']

    if Humor in i:
        if Humor == 'feliz':
            print('Siga sempre em frente e se precisar de força, olhe para o lado e eu estarei lá torcendo por você.')
            engine.say(name + 'Siga sempre em frente e se precisar de força, olhe para o lado e eu estarei lá torcendo por você.')
            engine.runAndWait()
        if Humor == 'triste':
            print('Quer um abraço? Fodase existe posiçäo fetal pra que? hein, porra.')
            engine.say(name + 'Quer um abraço? Fodase existe posiçäo fetal pra que? hein, porra.')
            engine.runAndWait()
        if Humor == 'baiana':
            print('Levanta da rede baiano já faz sete dias e você deitado ai porra.')
            engine.say(name + 'Levanta da rede baiana já faz sete dias e voce deitada ai porra.')
            engine.runAndWait()
        if Humor == 'carente':
            print('Ta carente compra um hamerti, filha da puta.')
            engine.say(name + 'Ta carente compra um hamerti, filha da puta.')
            engine.runAndWait()
    else:
        print('Vai se fuder, escória humana!!!')
        engine.say(name + 'Vai se fuder, escória humana!!!')
        engine.runAndWait()

@client.command()
async def tocar(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def pausar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def continuar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def parar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

    
client.run(TOKEN)
