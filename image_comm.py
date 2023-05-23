from khl import Bot,Message,MessageTypes
from datetime import timedelta, datetime
import logging
import json

logger = logging.getLogger()

# init base configuration
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

async def reqFrontLogger(msg:Message,bot:Bot):
    cont = "Channel:" + msg.target_id + " | Command request:" + msg.content + " | userid:" +  msg.author.id + " | userName:" + msg.author.username + '#' + msg.author.identify_num + " | time:" + (datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(cont)
    chan = await bot.client.fetch_public_channel(config['command-log-channel-id'])
    await bot.client.send(chan, cont)

class ImageServe():
    def __init__(self, bot):
        if bot != None:
            # 待丰富
            @bot.command(name='奇特武器')
            async def exoticwp(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/exoticweapon.png')
                await msg.reply(url, type=MessageTypes.IMG)

            @bot.command(name='奇特装备')
            async def exotic(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/exotic.png')
                await msg.reply(url, type=MessageTypes.IMG)

            @bot.command(name='强化')
            async def material(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/material.png')
                await msg.reply(url, type=MessageTypes.IMG)

            @bot.command(name='材料')
            async def cailiao(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/cailiao.jpg')
                await msg.reply(url, type=MessageTypes.IMG)

            # 显示配装列表
            @bot.command(regex=r'/map|路线图')
            async def buildmap(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/map.png')
                await msg.reply(url, type=MessageTypes.IMG)

            # 技能增伤
            @bot.command(name='技能')
            async def jineng(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/jineng.png')
                await msg.reply(url, type=MessageTypes.IMG)

            # 突击步枪性能排行
            @bot.command(name='ar')
            async def arrank(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/arrank.png')
                await msg.reply(url, type=MessageTypes.IMG)

            # 赛季日历
            @bot.command(regex=r'/rl|日历|赛季日历')
            async def calane(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/calander_season11.png')
                await msg.reply(url, type=MessageTypes.IMG)

            # 赛季日历
            @bot.command(regex=r'/jy|活动经验')
            async def extable(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/extable.png')
                await msg.reply(url, type=MessageTypes.IMG)

            # 暗区
            @bot.command(regex=r'/aq|暗区')
            async def anqu(msg: Message):
                await reqFrontLogger(msg,bot)
                url1 = await bot.client.create_asset('./img/xianqu.png')
                url2 = await bot.client.create_asset('./img/nananqu.png')
                url3 = await bot.client.create_asset('./img/donganqu.png')
                await msg.reply(url1, type=MessageTypes.IMG)
                await msg.reply(url2, type=MessageTypes.IMG)
                await msg.reply(url3, type=MessageTypes.IMG)

            # 套装
            @bot.command(regex=r'/tz')
            async def taozhuang(msg: Message):
                await reqFrontLogger(msg,bot)
                url1 = await bot.client.create_asset('./img/taozhuang1.jpg')
                url2 = await bot.client.create_asset('./img/taozhuang2.jpg')
                url3 = await bot.client.create_asset('./img/taozhuang3.jpg')
                await msg.reply(url1, type=MessageTypes.IMG)
                await msg.reply(url2, type=MessageTypes.IMG)
                await msg.reply(url3, type=MessageTypes.IMG)

            # 装备天赋强度
            @bot.command(name='装备天赋')
            async def abtalent(msg: Message):
                await reqFrontLogger(msg,bot)
                url = await bot.client.create_asset('./img/abtalent.png')
                await msg.reply(url, type=MessageTypes.IMG)