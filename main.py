import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import datetime
from datetime import datetime
import random
import asyncio
import pendulum
from keep_alive import keep_alive 

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="&")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Sunmi - pporappippam'))

#CANAL DE ROLES
@bot.command()
async def texto(ctx):
  channel = bot.get_channel(801276868027482164)
  with open('/home/runner/lenin/roles/roles.txt') as f:
    head = f.read()
    await channel.send(head)

@bot.command()
async def rolesedad(ctx):
  channel = bot.get_channel(801276868027482164)
  with open('/home/runner/lenin/roles/roles1.txt') as f:
    addedad = f.read()
    edad = await channel.send(addedad)
    reactions = ['🐛', '🦋']
    for i in reactions:
      await edad.add_reaction(i)

@bot.command()
async def rolespron(ctx):
  channel = bot.get_channel(801276868027482164)
  with open('/home/runner/lenin/roles/roles2.txt') as f:
    addpron = f.read()
    pronouns = await channel.send(addpron)
    reactions = ['🥝', '🍓', '🍉']
    for i in reactions:
      await pronouns.add_reaction(i)

@bot.command()
async def delroles(ctx):
  channel = bot.get_channel(801276868027482164)
  with open('/home/runner/lenin/roles/roles3.txt') as f:
    remroles = f.read()
    pronouns = await channel.send(remroles)
    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
    for i in reactions:
      await pronouns.add_reaction(i)

@bot.command()
async def rolecampanita(ctx):
  channel = bot.get_channel(801276868027482164)
  msg = ('.', '\n', 'Si deseas recibir notificaciones de las actividades por DM y por mención en los canales, puedes reaccionar en :bellhop: para agregarte el rol de <@&801508398662942790>.')
  campanita = await channel.send("".join(msg))
  reaction = '🛎️'
  await campanita.add_reaction(reaction)

@bot.event
async def on_raw_reaction_add(payload):
  user = payload.member

  if user == bot.user:
    return

  menor = discord.utils.get(user.guild.roles, name="menor")
  mayor = discord.utils.get(user.guild.roles, name="mayor")
  el = discord.utils.get(user.guild.roles, name="él")
  ella = discord.utils.get(user.guild.roles, name="ella")
  elle = discord.utils.get(user.guild.roles, name="elle/ele")
  campanita = discord.utils.get(user.guild.roles, name="notificaciones")

  if payload.channel_id == 801276868027482164:
    if payload.emoji.name == '🐛':
      await user.add_roles(menor)
    elif payload.emoji.name == '🦋':
      await user.add_roles(mayor)
    elif payload.emoji.name =='🥝':
      await user.add_roles(el)
    elif payload.emoji.name =='🍓':
      await user.add_roles(ella)
    elif payload.emoji.name =='🍉':
      await user.add_roles(elle)
    elif payload.emoji.name =='1️⃣':
      await user.remove_roles(menor)
    elif payload.emoji.name =='2️⃣':
      await user.remove_roles(mayor)
    elif payload.emoji.name =='3️⃣':
      await user.remove_roles(el)
    elif payload.emoji.name =='4️⃣':
      await user.remove_roles(ella)
    elif payload.emoji.name =='5️⃣':
      await user.remove_roles(elle)
    elif payload.emoji.name =='🛎️':
      await user.add_roles(campanita)

  lona = await bot.fetch_user(485054727755792410)

  if payload.channel_id == 801820643300474940:
    if payload.emoji.name == '🗿':
      with open('/home/runner/lenin/ayuda/ayuda2.txt') as f:
        ayuda = f.read()
        await user.send(ayuda)
        await lona.send('{} necesita ayuda con el bot'.format(user))
        
  if payload.channel_id == 801276868027482164:
    if payload.emoji.name =='🛎️':
      await lona.send('{} quiere recibir notificaciones'.format(user))
      f = open('/home/runner/lenin/roles/notificaciones-nombre.txt', 'a')
      f.write(", '<@{}>'".format(user, ', '))
      f.close()
      f = open('/home/runner/lenin/roles/notificaciones-id.txt', 'a')
      newuser = ', ' + str(user.id)
      f.write(newuser)
      f.close()

#CANAL DE VOTACIONES
@bot.command()
async def ophora(ctx):
  channel = bot.get_channel(801820643300474940)
  with open('/home/runner/lenin/votaciones/hora.txt') as f:
    hora = f.read()
    msg = await channel.send(hora)
    reactions = ['🥳', '😄', '🤪', '😭', '🥱', '😳']
    for i in reactions:
      await msg.add_reaction(i)

@bot.command()
async def opbot(ctx):
  channel = bot.get_channel(801820643300474940)
  with open('/home/runner/lenin/votaciones/bot.txt') as f:
    opbot = f.read()
    msg = await channel.send(opbot)
    reactions = ['🎉', '😐', '😭', '🗿']
    for i in reactions:
      await msg.add_reaction(i)

#ACTIVIDADES
@bot.command()
async def actividad(ctx):
  with open('actividad.txt') as f:
    text = f.read()
    await ctx.channel.send(text)
    await ctx.channel.send('Link al trailer del documental: https://www.youtube.com/watch?v=mc3MWENOHiY')

#DM NOTIFICACIONES
@bot.command()
async def notificaciones(ctx):
  with open('/home/runner/lenin/roles/notificaciones-id.txt') as f:
    users = f.read().split(', ')
    for i in users:
      with open('actividaddm.txt') as f:
        dm = f.read()
        user = await bot.fetch_user(i)
        await user.send(dm)
        await user.send('Link al trailer del documental: https://www.youtube.com/watch?v=mc3MWENOHiY') #agregar mensaje

#COMANDOS DE AYUDA
@bot.command()
async def ayuda(ctx):
  with open('/home/runner/lenin/ayuda/ayuda.txt') as f:
    ayuda = f.read()
    await ctx.channel.send(ayuda)

@bot.command()
async def canales(ctx):
  with open('/home/runner/lenin/ayuda/canales.txt') as f:
    canales = f.read()
    await ctx.channel.send(canales)

@bot.command()
async def comandos(ctx):
  with open('/home/runner/lenin/ayuda/comandos.txt') as f:
    comandos = f.read()
    await ctx.channel.send(comandos)

@bot.command()
async def drive(ctx):
  drive = ('¿Buscas el link para la carpeta de Drive? ¡Acá está!:', '\n', 'https://drive.google.com/drive/folders/1o_xuNEuH_xNnO6LWFWXJ8XqlS2TNQ6Jy?usp=sharing', '\n\n', 'Si no estás segure de dónde está lo que buscas, revisa <#765349189692817408> para ver el detalle de las actividades realizadas.')
  await ctx.channel.send("".join(drive))

@bot.command()
async def playlist(ctx):
  playlist = ('¿Buscas el link de la playlist de Spotify? ¡Acá está!:', '\n', 'https://open.spotify.com/playlist/3ZcCDnPcEucCnZWNe1Yjcq?si=0tIICg21QlGf-AwWlNrr4w')
  await ctx.channel.send("".join(playlist))
  
@bot.command()
async def redes(ctx):
  await ctx.channel.send('Síguenos en nuestras redes sociales:\nTwitter: https://www.twitter.com/OrbitburoES\nInstagram: https://www.instagram.com/OrbitburoES')
  
@bot.command(name='invitacion')
async def invitacion(ctx, *argument):
    invitelink = await ctx.channel.create_invite(max_age=86400,unique=True)
    await ctx.author.send('¡Aquí está el link de invitación al servidor que pediste! Debes usarlo en las siguientes 24 horas antes de que expire. ')
    await ctx.author.send(invitelink)
  
# #COMANDOS RANDOM

@bot.command()
async def dato(ctx):
  with open('/home/runner/lenin/random/datos.txt') as f:
    datos = f.read().splitlines()
    await ctx.channel.send(random.choice(datos))

@bot.command()
async def cita(ctx):
  with open('/home/runner/lenin/random/citas.txt') as f:
    citas = f.read().splitlines()
    await ctx.channel.send(random.choice(citas))

@bot.command()
async def kpop(ctx):
  with open('/home/runner/lenin/random/kpop.txt') as f:
    kpop = f.read().splitlines()
    await ctx.channel.send(random.choice(kpop))

@bot.command()
async def cancion(ctx):
  with open('/home/runner/lenin/random/spotify.txt') as f:
    spotify = f.read().splitlines()
    await ctx.channel.send(random.choice(spotify))

@bot.command()
async def bobesponja(ctx):
  with open('/home/runner/lenin/random/bob.txt') as f:
    bob = f.read().splitlines()
    await ctx.channel.send(random.choice(bob))

@bot.command()
async def recomendacion(ctx):
  with open('/home/runner/lenin/random/recomendacion.txt') as f:
    recomendacion = f.read().splitlines()
    await ctx.channel.send("Si tienes tiempo libre, podrías leer **{}**.\nBúscalo en la biblioteca de Drive: https://drive.google.com/drive/folders/18uO60i2t8zkg3hlu-Mb_9D3RQD2HA_M5?usp=sharing".format(random.choice(recomendacion)))

# ACTIVIDADES
@bot.command()
async def ultima(ctx):
  with open('/home/runner/lenin/ayuda/ultima.txt') as f:
    ultima = f.read()
    await ctx.channel.send(ultima)

@bot.command()
async def siguiente(ctx):
  with open('/home/runner/lenin/ayuda/siguiente.txt') as f:
    siguiente = f.read()
    await ctx.channel.send(siguiente)

#BOLA DE CRISTAL
@bot.command()
async def suerte(ctx, *args):
  with open('/home/runner/lenin/random/suerte.txt') as f:
    suerte = f.read().splitlines()
    if args == ():
      await ctx.channel.send('¡Debes hacerme una pregunta para ver tu suerte!')
    else:
      await ctx.channel.send('Mi bola de cristal dice: "{}".'.format(random.choice(suerte)))

@bot.command()
async def opinion(ctx, *args):
  with open('/home/runner/lenin/random/opinion.txt') as f:
    opinion = f.read().splitlines()
    if args == ():
      await ctx.channel.send('¡Debes agregar algo para poder darte mi opinión!')
    else:
      await ctx.channel.send(random.choice(opinion))
      
#RELOJ
@bot.command()
async def hora(ctx):
# TIMEZONES
  tz_CL = pendulum.timezone('America/Santiago')
  datetime_CL = datetime.now(tz_CL)

  tz_PE = pendulum.timezone('America/Lima')
  datetime_PE = datetime.now(tz_PE)

  tz_BO = pendulum.timezone('America/La_Paz')
  datetime_BO = datetime.now(tz_BO)

  tz_JP = pendulum.timezone('Asia/Tokyo')
  datetime_JP = datetime.now(tz_JP)

  tz_MX = pendulum.timezone('America/Mexico_City')
  datetime_MX = datetime.now(tz_MX)

  hora = ("La hora actual es:", "\n", ":flag_mx: (CDMX) **(GMT -6): **", datetime_MX.strftime("%H:%M:%S"), "\n", ":flag_pe: :flag_ec: :flag_co: **(GMT -5): **", datetime_PE.strftime("%H:%M:%S"), "\n", ":flag_bo: :flag_py: :flag_ve: **(GMT -4): **", datetime_BO.strftime("%H:%M:%S"), "\n", ":flag_ar: :flag_cl: :flag_br: :flag_uy: **(GMT -3) : **", datetime_CL.strftime("%H:%M:%S"), "\n", ":flag_kr: :flag_jp: **(GMT +9): **", datetime_JP.strftime("%H:%M:%S"))

  await ctx.channel.send("".join(hora))

#MENSAJE SIN ROL
@bot.command()
async def sinrol(ctx):
  channel = bot.get_channel(716367363968073749)
  await channel.send('<@&774766632119173131> les recordamos que deben leer las reglas de la comunidad en <#716068304162258954> y luego poner sus datos en el canal <#716076107685822535> para poder acceder al servidor')

#EASTER EGGS
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  msg = message.content

  if 'leamos' in msg.lower() or 'leido' in msg.lower() or 'lee' in msg.lower() or 'leiste' in msg.lower() or 'leyó' in msg.lower() or 'lei' in msg.lower() or 'leyendo' in msg.lower():
    await message.channel.send('¿Alguien dijo leer? ¡Recuerda leer el texto de la próxima actividad!')

  if 'trotsk' in msg.lower() or 'trosk' in msg.lower():
    await message.channel.send(':pick:')

  if 'lenin' in msg.lower():
    autolenin = ['¿Están hablando de mí?', '¿Me buscaban?', '¿Alguien dijo mi nombre?', '¡Sí, aquí estoy!', 'No es lindo hablar de alguien a sus espaldas.', '¿Yo qué?', '¿Qué pasa conmigo?', 'Ese es mi nombre, no lo gastes.']
    await message.channel.send(random.choice(autolenin))

  if ' pena' in msg.lower() or 'pena ' in msg.lower() or ' sad ' in msg.lower() or msg.endswith('sad') or 'sad' == msg.lower() or 'sad ' in msg.lower() or 'sadd' in msg.lower() or 'triste' in msg.lower() or 'llorar' in msg.lower() or 'tot' == msg.lower() or msg.endswith('tot'):
      await message.channel.send('tkm no estés triste')

  if ' feliz' in msg.lower():
      await message.channel.send('yo también bestie!')

  if 'cumpleaños' in msg.lower():
      await message.channel.send('¿Quién está de cumpleaños? ¡Feliz cumpleaños, camarada! :partying_face:')

  if 'anticomunismo' in msg.lower() or 'anticomunista' in msg.lower():
    await message.channel.send('<:yeojin2:716798849464795260>')

  if 'blackpink' in msg.lower():
    await message.channel.send('RS1 IS COMING')

  reprmusica = bot.get_channel(731919940533223514)
  secgen = bot.get_channel(716135897476628521)
  pruebot = bot.get_channel(800131110989463592)

  if msg.startswith('!p'):
    if message.channel == secgen:
      return
    elif message.channel == pruebot:
      return
    elif message.channel != reprmusica:
      await message.channel.send('Los comandos del bot de música deben ser enviados en el canal de <#731919940533223514>.')

  await bot.process_commands(message)

keep_alive()

bot.run(DISCORD_TOKEN)