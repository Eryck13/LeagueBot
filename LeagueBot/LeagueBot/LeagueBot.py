import json
import requests
import discord
from discord.ext import commands
from time import sleep
import datetime
import random 
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
#import time
token = 'NTkxMTAxOTU5NDQ5MzQ2MDY5.XQr4uA.o1T1UApN78g9TgYPcP7Uz0tbArY'

client = commands.Bot(command_prefix='!')
icon = 'https://cdn.discordapp.com/emojis/569632408895225856.gif?v=1/'
apikey = '/?api_key=RGAPI-9c7efa07-8f07-4920-a2e7-9c48408ba345'
sumstart = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
leaguestart = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
iconstart = 'http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/'
champlink = 'http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion/'
champpicstart = 'http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/' 
@client.event
async def on_ready():
    print('started')

@client.command()
async def profile(ctx, name: str):

    url1 = sumstart + name + apikey
    get1 = requests.get(url1)
    jsonreq1 = json.loads(get1.text) 
    
    id = jsonreq1['id']
    namefinished = jsonreq1['name']
    level = jsonreq1['summonerLevel']
    profileicon = jsonreq1['profileIconId']

    url2 = leaguestart + id + apikey
    get2 = requests.get(url2)
    
    jsonreq2 = json.loads(get2.text)
    
    #jsonreqfinal=json.dumps(jsonreq2)
    #for each in jsonreq2['leagueId']:
    tier=[]
    rank=[]
    points=[]
    wins=[]
    losses=[]
    type1=[]
    for each in jsonreq2:
        
        #type1 = each['queueType']
        if 'RANKED_FLEX_SR' in each['queueType']:
            #type1.remove('RANKED_FLEX_SR')
            break
        tier = each['tier']
         #tier.append(str(tier))
        rank = each['rank']
        #rank.append(str(rank)) 
        points = each['leaguePoints']
          #points.append(str(points)) 
        wins = each['wins']
         #wins.append(str(wins)) 
        losses = each['losses']
          #losses.append(str(losses)) 
        #type.append(str(type)) 

    winpercent = float((wins / losses)/2)
    finalrank = tier + ' ' + rank
    iconend = iconstart + str(profileicon) + '.png'






    embed = discord.Embed(title='User Found!',description=namefinished, color=3488062)
    embed.set_thumbnail(url=iconend)
    embed.add_field(name="Level", value= level, inline=True)
    embed.add_field(name="Rank", value= finalrank, inline=True)
    embed.add_field(name="Win%", value=winpercent, inline=True)
    embed.add_field(name="LP", value=points, inline=True)
    embed.add_field(name="Wins", value=wins, inline=True)
    embed.add_field(name="Losses", value=losses, inline=True)
    avatar_url(name="Losses", value=losses, inline=True)

    embed.set_footer(text = "Created by Eryck13",icon_url = icon)
    await ctx.send(embed = embed)

@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands", description="List of the following commands applicable/Tips", color=3488062)
    embed.add_field(name="Names with spaces", value="Use '_' as a replacement of spaces", inline=False)
    embed.add_field(name="How to view summoner profile ", value="!profile", inline=False)
    embed.set_footer(text = "Created by Eryck13",icon_url = icon)
    await ctx.send(embed=embed)

@client.command()
async def Champion(ctx,champion: str):
    champion = ''.join(champion.split())
    url1 = champlink + champion +'.json'
    get3 = requests.get(url1)
    jsonreq3 = json.loads(get3.text) 
    pic = jsonreq3['data'][str(champion)]['id']
    desc = jsonreq3['data'][str(champion)]['title']
    hp = jsonreq3['data'][str(champion)]['stats']['hp']
    hpperlevel = jsonreq3['data'][str(champion)]['stats']['hpperlevel']
    mp = jsonreq3['data'][str(champion)]['stats']['mp']
    mpperlevel = jsonreq3['data'][str(champion)]['stats']['mpperlevel']
    movespeed = jsonreq3['data'][str(champion)]['stats']['movespeed']
    armor = jsonreq3['data'][str(champion)]['stats']['armor']
    armorperlevel = jsonreq3['data'][str(champion)]['stats']['armorperlevel']
    spellblock  =  jsonreq3['data'][str(champion)]['stats']['spellblock']
    spellblockperlevel = jsonreq3['data'][str(champion)]['stats']['spellblockperlevel']
    attackrange =  jsonreq3['data'][str(champion)]['stats']["attackrange"]
    hpregen = jsonreq3['data'][str(champion)]['stats']['hpregen']
    hpregenperlevel =  jsonreq3['data'][str(champion)]['stats']['hpregenperlevel']
    mpregen = jsonreq3['data'][str(champion)]['stats']['mpregen']
    mpregenperlevel =  jsonreq3['data'][str(champion)]['stats']['mpregenperlevel']
    crit = jsonreq3['data'][str(champion)]['stats']['crit']
    critperlevel =  jsonreq3['data'][str(champion)]['stats']['critperlevel']
    attackdamage = jsonreq3['data'][str(champion)]['stats']['attackdamage']
    attackdamageperlevel  = jsonreq3['data'][str(champion)]['stats']['attackdamageperlevel']
    attackspeedoffset = jsonreq3['data'][str(champion)]['stats']['attackspeedoffset']
    attackspeedperlevel  = jsonreq3['data'][str(champion)]['stats']['attackspeedperlevel']

    finalpic = champpicstart + pic + '.png'

    embed = discord.Embed(title=pic, description=desc, color=3488062)
    embed.set_thumbnail(url=finalpic)
    embed.add_field(name="StartingHP", value= hp, inline=True)
    embed.add_field(name="HpPerLvl", value= hpperlevel, inline=True)
    embed.add_field(name="StartMana", value=mp, inline=True)
    embed.add_field(name="MpPerLvl", value=mpperlevel, inline=True)
    embed.add_field(name="StartMovSpeed", value=movespeed, inline=True)
    embed.add_field(name="Start Armor", value=armor, inline=True)
    embed.add_field(name="ArmorPerLvl", value=armorperlevel, inline=True)
    embed.add_field(name="SpellBlock", value=spellblock, inline=True)
    embed.add_field(name="SpellBlockPerLvl", value=spellblockperlevel, inline=True)
    embed.add_field(name="AttackRange", value=attackrange, inline=True)
    embed.add_field(name="HpReGen", value=hpregen, inline=True)
    embed.add_field(name="HpReGenPerLvl", value=hpregenperlevel, inline=True)
    embed.add_field(name="ManaReGen", value=mpregen, inline=True)
    embed.add_field(name="ManaReGenPerLvl", value=mpregenperlevel, inline=True)
    embed.add_field(name="Crit", value=crit, inline=True)
    embed.add_field(name="CritPerLvl", value=critperlevel, inline=True)
    embed.add_field(name="AttackDmg", value=attackdamage, inline=True)
    embed.add_field(name="AttackDmgPerLvl", value=attackdamageperlevel, inline=True)
    embed.add_field(name="AttSpeedOffset", value=attackspeedoffset, inline=True)
    embed.add_field(name="AttSpeedPerLvl", value=attackspeedperlevel, inline=True)
    embed.set_footer(text = "Created by Eryck13",icon_url = icon)
    await ctx.send(embed=embed)
    #avatar_url(name="Losses", value=losses, inline=True)

client.run(token)