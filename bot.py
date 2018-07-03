import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import os

bot = discord.Client()
bot_prefix="."
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready() :
    print("Bot çevrimiçi!")
    print("İsim : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print(str(len(bot.servers)) + " tane serverda çalışıyor!")
    print(str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!")
    await bot.change_presence(game=discord.Game(name='RickTVPUBG çalışıyor!'))

@bot.command(pass_context=True)
async def reklam(ctx) :
    await bot.say("www.twitch.tv/RickTVPUBG izle knk")
    
@bot.command(pass_context=True)
async def csgo(ctx) :
    await bot.say("CSGO Serverimizin IPsi : 185.78.86.156:27015")
    
@bot.command(pass_context=True)
async def steam(ctx) :
    await bot.say("https://steamcommunity.com/id/rickandmortyrick")
 
@bot.command(pass_context=True)
async def youtube(ctx) :
    await bot.say("https://www.youtube.com/c/LargeFX")

@bot.command(pass_context=True)
async def a(ctx, member:discord.Member):
    urll = ["https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif" , 
            "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif" ,
           "https://78.media.tumblr.com/680b69563aceba3df48b4483d007bce3/tumblr_mxre7hEX4h1sc1kfto1_500.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name )
    embed.set_image(url=random.choice(urll))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def sil (ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context=True)
async def s (ctx):
    mgs = ctx.message.content.split("1")
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.channel , mgs)    

@bot.command(pass_context=True)
async def sik(ctx, member:discord.Member) :
   urll = ["https://static.hentai-gifs.com/upload/20160703/19/36972/1.gif" , 
   "https://78.media.tumblr.com/931125762652e49075f26f954049c0da/tumblr_msvseafYc01sflbiso1_1280.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-sexe-hentai.gif" , 
   "https://78.media.tumblr.com/3acd627d51c3484deb5a1349dba15f61/tumblr_nerlc5vPvU1u3p95io1_500.gif" , 
   "https://68.media.tumblr.com/37320d7ba87cc087713cd5f42ceff0fa/tumblr_ok06xwuKen1v2hfg0o1_500.gif" ,
   "https://78.media.tumblr.com/188f0818225d5f1c579a0eb5010b0c90/tumblr_o5498914Dp1ugdh13o1_500.gif" , 
   "https://78.media.tumblr.com/852fc9eff5caf44be79e92295676fbd1/tumblr_o549fohYOD1ugdh13o8_540.gif" ,
   "https://78.media.tumblr.com/54a670815a39bde673bdaaa35f08a88d/tumblr_o548wwiAhn1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/65b0296ed9d5e12e79ac1c02c4502b63/tumblr_o548y9hptR1ugdh13o1_500.gif" , 
   "https://78.media.tumblr.com/916f8497317b49edb5802fa6aa411f47/tumblr_o5492gX7Ir1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/de046b1380f663bf05d4833de2ec8078/tumblr_o54939bHby1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/9cdba610e7f393539718c12a010c12c1/tumblr_o5493vuIAk1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/5a030c57050ce1bcaa4c5efc116ad27a/tumblr_o5496dmxSS1ugdh13o1_500.gif" ,]
   embed = discord.Embed(title=ctx.message.author.name + " seni sikiyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sev(ctx, member:discord.Member) :
   urll = ["https://media1.tenor.com/images/73a746bada06751716d3173fbb9e6864/tenor.gif" , 
   "https://media1.tenor.com/images/a4a2b1eaa47fd0d8d0951433bc59ab9a/tenor.gif" , 
   "https://media.giphy.com/media/K1InqndmlQDE4/giphy.gif" , 
   "https://i.pinimg.com/originals/2c/6e/4b/2c6e4bb81e44fe1a0b8c599f292e2be5.gif" , 
   "https://i.pinimg.com/originals/b6/9a/79/b69a790c15ebdc4a4bf9c16aa6dec786.gif" , 
   "https://media.giphy.com/media/lq72vRtxJtpgQ/giphy.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni seviyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sarıl(ctx, member:discord.Member) :
   urll = ["https://78.media.tumblr.com/2fe074ad467af41a8230b8d9d8e322f1/tumblr_omvj49wYnq1v8tshbo1_500.gif" , 
   "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif" , 
   "https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif" , 
   "https://media.giphy.com/media/3bqtLDeiDtwhq/giphy.gif" , 
   "https://78.media.tumblr.com/b4655e26f615a0e2081b9a6c90076539/tumblr_n13pt9SV4p1r45wgho2_500.gif" , 
   "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif" , 
   "https://i.gifer.com/B7bp.gif",
   "https://cdn.discordapp.com/attachments/357958080224559105/451687910090211338/171021_8687.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)


@bot.command(pass_context=True)
async def developer(ctx, member:discord.Member) :
   urll = ["https://media1.tenor.com/images/73a746bada06751716d3173fbb9e6864/tenor.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni seviyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def ahkmd(ctx, member:discord.Member) :
   embed = discord.Embed(title=ctx.message.author.name + " senin anana hükmediyor " + member.name)
   await bot.say(embed = embed)



@bot.command(pass_context=True)
async def soyle(ctx):
    msg = ctx.message.content.split("1")
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.channel, msg)
    print(ctx.message.author.name, msg)




bot.run(os.environ.get('token'))
