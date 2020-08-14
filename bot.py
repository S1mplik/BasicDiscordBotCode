import discord
from discord.ext import commands


Token = 'NzQzNTYwMjM1NDE4OTEwNzUw.XzWcbg.M3tq46Fcd2E-uSQnajEKGA3OxVo'
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Bot se úspěšne zapnul a čeká na další rozkazi na discord serveru FunGaming.eu')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Začátečník')
    await client.add_roles(member, role)
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms' )

@client.command()
async def pomoc(ctx):
    await ctx.send('Pokud potřebujete pomoci tak se běžte přesunout do místnosti Podpory pokud chcete někoho nahlásit stačí napsat zprávu do textové místnosti Podpora do zprávy napište hlavně jméno a přestupek to vše stačí pak se přesuňte do voice channelu Podpora a vyčkejte max. 2 minut pokud si vás helper nevyzvedne tak mu napište private message')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Byl zabanován hráč{member.mention}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name,user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} tento hráč byl odbanován')
            return

client.run(Token)
