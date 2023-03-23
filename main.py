from khl import Bot, Message, MessageTypes, EventTypes, Event,ChannelTypes
from khl.card import CardMessage, Card, Module, Element
from khl.command.rule import Rule
from logging.handlers import TimedRotatingFileHandler
from datetime import timedelta, datetime
from build.builds import BuildList
from db.sqlMapper import SqlMapper
from image_comm import ImageServe
from binduser import Binduser
from signin import Signin
from menu import Menu
from vendor import Vendor

import logging
import json
import requests

# init base configuration
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
# load living room
with open('config/livingroom.json', 'r', encoding='utf-8') as f:
    livingroom = json.load(f)

# init Bot
bot = Bot(token=config['token'])

sqlMapper = SqlMapper()
# register build handler
build = BuildList(bot)
# register image handler
imageServe = ImageServe(bot)
# vendor handler
vendorTool = Vendor()

# log setting
new_formatter = '[%(levelname)s]%(asctime)s:%(msecs)s#>[%(funcName)s]:%(lineno)s  %(message)s'
logging.StreamHandler()
logging.basicConfig(level='DEBUG')
fmt = logging.Formatter(new_formatter)
log_handel = TimedRotatingFileHandler('./log/ania.log', when='D', backupCount=15)
log_handel.setFormatter(fmt)
# init logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handel)

async def reqFrontLogger(msg:Message):
    cont = "Channel:" + msg.target_id + " | Command request:" + msg.content + " | userid:" +  msg.author.id + " | userName:" + msg.author.username + '#' + msg.author.identify_num + " | time:" + (datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(cont)
    chan = await bot.client.fetch_public_channel("7678231813152563")
    await bot.client.send(chan, cont)

def getLivingRoom(obj):
    item = {
        "type": "section",
        "text": {
            "type": "plain-text",
            "content": obj['name']
        },
        "mode": "right",
        "accessory": {
            "type": "button",
            "theme": "primary",
            "value": obj['url'],
            "click": "link",
            "text": {
                "type": "plain-text",
                "content": "进入直播间"
            }
        }
    }
    return item

# set playing game
@bot.on_startup
async def on_startup(bot:Bot):
    # game_id : int
    await bot.client.update_playing_game(config['td2gameid'])
    logger.info("TheDivision2 Robot Ania Started")
    logger.info("Set Playing Game：The Division 2")

# show Ania base info
@bot.command(regex=r'/ania-pro')
async def showInfo(msg: Message):
    await reqFrontLogger(msg)
    info = await bot.client.fetch_me()
    c = Card(Module.Header('Robot Ania-pro (ONLINE)'), color='#5A3BD7')
    c.append(Module.Context('version: ' + config['version']))
    c.append(Module.Context('comment: ' + config['comment']))
    c.append(Module.Divider())
    c.append(Module.Section('id: \t\t\t\t' + info.id)) # id
    c.append(Module.Section('username: \t\t' + info.username))  # 用户名
    c.append(Module.Section('nickname: \t\t' + info.nickname + '#' + info.identify_num))  # 备注名#身份编号
    c.append(Module.Section('online: \t\t\t' + '在线' if info.online else '离线')) # 是否在线
    c.append(Module.Section('status: \t\t\t' + ('被封禁' if str(info.status) == '10' else '正常'))) # 状态
    cm = CardMessage(c)
    await msg.reply(cm)

# show th2 menu
@bot.command(regex=r'/菜单|/cd|/menu|menu|/\?')
async def menu(msg: Message):
    await reqFrontLogger(msg)
    channel = await bot.client.fetch_public_channel(msg.target_id)
    if channel.guild_id == config["pla_guild_id"]:
        await msg.reply(Menu().getMenu("1"))
    if channel.guild_id == config["tieba_guild_id"]:
        await msg.reply(Menu().getMenu("2"))

# cronjob
@bot.task.add_cron(hour="8",timezone="Asia/Shanghai")
async def cronjob():
    c = Card(Module.Header('Ania小广播 :loudspeaker:'),color="FFCCFF")
    c.append(Module.Context('在聊天框输入快捷指令即可触发Ania的功能哦~'))
    # 全火输出
    c.append(Module.Divider())
    c.append(Module.Section({"type":"kmarkdown","content":"本次语音频道全面消杀已完成~"}))
    c.append(Module.Section({"type":"kmarkdown","content":"欢迎加入PLA大家庭，请详细阅读本频道置顶消息，如您需要帮助请@ShaoaoQAQ，本频道ID为`29278287`，以下是Ania为您提供的快捷指令"}))
    c.append(Module.Section({"type":"kmarkdown","content":"重要通知：Ania公开测试版已停止服务，Ania正式版已上线，继承测试版用户数据，因功能调试Raid武器查询功能暂时下线"}))
    c.append(Module.Section({"type":"kmarkdown","content":"1、Ania功能菜单（全部功能快捷指令）：`/cd`"}))
    c.append(Module.Section({"type":"kmarkdown","content":"2、战队名片（如需加战队请查看）：`/pla`"}))
    c.append(Module.Section({"type":"kmarkdown","content":"3、配装表：`/pz` 萌新推荐配装指南：`/map`"}))
    c.append(Module.Divider())
    c.append(Module.Context('Ania版本号: ' + config['version']))
    cm = CardMessage(c)
    channel = await bot.client.fetch_public_channel(config['public_channel_id'])
    await bot.client.send(channel,cm)

# show td2 pve buildList
@bot.command(regex=r'/pz|配装|/配装')
async def builds(msg: Message):
    await reqFrontLogger(msg)
    zp = BuildList(None)
    c = zp.getList()
    await msg.reply(c)

# show td2 pvp buildList
@bot.command(regex=r'/pvp')
async def pvpbuilds(msg: Message):
    await reqFrontLogger(msg)
    zp = BuildList(None)
    c = zp.getPvp()
    await msg.reply(c)

# query td2 server status
@bot.command(regex=r'/服务器|服务器|/server')
async def serverStatus(msg: Message):
    await reqFrontLogger(msg)
    url = config['td2-instance-status-url']
    res = requests.get(url=url)
    object = json.loads(str(res.text))
    logger.info(str(res.text))
    c = Card()
    for i in object:
        c.append(Module.Section('--  ' + i['Name']))
        c.append(Module.Section('实例ID：\t\t' + i['AppID ']))
        c.append(Module.Section('平台：\t\t' + i['Platform']))
        c.append(Module.Section('实例状态：\t' + ('在线' if i['Status'] == 'Online' else '离线')))
        c.append(Module.Divider())
    cm = CardMessage(c)
    await msg.reply(cm)

# show clan card
@bot.command(regex=r'/zd|/pla')
async def pla(msg: Message):
    await reqFrontLogger(msg)
    c = Card(Module.Header('[PLA]战队卡片'), color='#ff9900')
    c.append(Module.Divider())
    c.append(Module.Section({"type":"kmarkdown","content":"主队队名：`CPLASFOFCHINA`  (入队要求手表2000级)"}))
    c.append(Module.Section({"type":"kmarkdown","content":"二队队名：`Peanut Agents`  (无要求)"}))
    c.append(Module.Section({"type":"kmarkdown","content":"QQ群号：`136932781`"}))
    c.append(Module.Section({"type":"kmarkdown","content":"KOOK语音频道ID：`29278287`"}))
    c.append(Module.Section({"type":"kmarkdown","content":"开挂、速成玩家请勿入队，谢谢合作！入队审核，其他咨询(met)1595665465(met)"}))
    cm = CardMessage(c)
    await msg.reply(cm)

# query td2 character data
@bot.command(name='查询')
async def find(msg: Message, name):
    await reqFrontLogger(msg)
    c = Card(Module.Header('数据查询'), color='#5A3BD7')
    c.append(Module.Section({"type":"kmarkdown","content":"[查看玩家" + name +"生涯数据报告](https://tracker.gg/division-2/profile/uplay/" + name + "/overview)"}))
    cm = CardMessage(c)
    await msg.reply(cm)

# list livingroom
@bot.command(regex=r'/直播|直播|/zb')
async def liveroom(msg: Message):
    await reqFrontLogger(msg)
    c = Card(Module.Header('直播间导航'), color='#99FF00')
    c.append(Module.Divider())
    for room in livingroom:
        c.append(getLivingRoom(room))
    cm = CardMessage(c)
    await msg.reply(cm)

# reno
@bot.command(regex=r'/reno|/Reno')
async def reno(msg: Message):
    await reqFrontLogger(msg)
    c = Card(Module.Header('Reno必出驯鹰人仪式'), color='#5A3BD7')
    c.append(Module.Divider())
    c.append(Module.Section({"type":"kmarkdown","content":"1、飞机入口处背对箱子放空手枪子弹"}))
    c.append(Module.Section({"type":"kmarkdown","content":"2、复苏蜂窝放在飞机机舱与上坡的连接处"}))
    c.append(Module.Section({"type":"kmarkdown","content":"3、蓄力EMP的同时往箱子走，注意，蓄满EMP自动释放"}))
    c.append(Module.Section({"type":"kmarkdown","content":"4、向斜上方开一枪手枪"}))
    c.append(Module.Section({"type":"kmarkdown","content":"5、开箱"}))
    cm = CardMessage(c)
    await msg.reply(cm)

@bot.command(regex=r'整个活.+', rules={Rule.is_bot_mentioned(bot)})
async def hulue(msg: Message):
    await reqFrontLogger(msg)
    channel = await bot.fetch_public_channel(msg.target_id)
    await bot.client.send(channel, '草！走！忽略！ ጿ ኈ ቼ ዽ ጿ')

@bot.command(regex=r'您好.+|请问.+|谢谢.+|麻烦了.+|辛苦您.+|辛苦了.+|抱歉.+|不好意思.+|欢迎.+')
async def jiecao(msg: Message):
    await msg.add_reaction("❤")
    now = (datetime.now())
    ti = now.strftime("%Y%m%d")
    userinfo = sqlMapper.getUserInfoByUserId(msg.author_id)
    if userinfo['jiecaoDate'] == None or userinfo['jiecaoDate'] != ti:
        userinfo['jiecao'] += 1
        userinfo['jiecaoLimit'] = 1
        userinfo['jiecaoDate'] = ti
        sqlMapper.updateUserInfo(userinfo)
        logger.info("New Data : " + str(userinfo))
        await msg.add_reaction("🎉")
    else:
        if userinfo['jiecaoLimit'] < 5:
            userinfo['jiecao'] += 1
            userinfo['jiecaoLimit'] += 1
            sqlMapper.updateUserInfo(userinfo)
            logger.info("New Data : " + str(userinfo))
            await msg.add_reaction("🎉")

# reno
@bot.command(regex=r'/节操')
async def chajiecao(msg: Message):
    userinfo = sqlMapper.getUserInfoByUserId(msg.author_id)
    if userinfo['jiecao'] == 0:
        await msg.reply('你没有节操……')
    else:
        item = {
            "type": "section",
            "text": {
                "type": "plain-text",
                "content": '🎉你的节操值：' + str(userinfo['jiecao'])
            },
            "mode": "right",
            "accessory": {
                "type": "button",
                "theme": "primary",
                "value": "buy1card",
                "click": "return-val",
                "text": {
                    "type": "plain-text",
                    "content": "兑换1张免断签卡(-35节操)"
                }
            }
        }
        c = Card()
        c.append(item)
        await msg.reply(CardMessage(c))

# pay for jiecao
@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def handleBtnClick(b: Bot, event: Event):
    if event.body['value'] == 'buy1card':
        userinfo = sqlMapper.getUserInfoByUserId(event.body['user_id'])
        signinfo = sqlMapper.getSigninByUserId(event.body['user_id'])
        user = await bot.client.fetch_user(event.body['user_id'])
        if userinfo['jiecao'] >= 35:
            userinfo['jiecao'] -= 35
            sqlMapper.updateUserInfo(userinfo)
            logger.info("User New Data : " + str(userinfo))
            signinfo['prop'] += 1
            sqlMapper.updateSigninByUserId(signinfo)
            logger.info("Signin New Data : " + str(signinfo))
            await user.send("兑换成功啦,现在有" + str(signinfo['prop']) + '张免断签卡和' + str(userinfo['jiecao']) + '节操！')
        else:
            await user.send("歪歪歪，你的节操余额不足~")

# td2 vendor main
@bot.command(regex='/周商|/zs')
async def zhoushang0(msg: Message):
    c = Card(Module.Header('周商查询:'),color="FFCCFF")
    c.append(Module.Section({"type":"kmarkdown","content":"1、周商装备：`/zs zb` `/周商 装备`"}))
    c.append(Module.Section({"type":"kmarkdown","content":"2、周商武器：`/zs wq` `/周商 武器`"}))
    c.append(Module.Section({"type":"kmarkdown","content":"3、周商插件：`/zs cj` `/周商 插件`"}))
    cm = CardMessage(c)
    await msg.reply(cm)
    
# td2 vendor
@bot.command(regex='/周商.+|/zs.+')
async def zhoushang(msg: Message):
    await reqFrontLogger(msg)
    content = msg.content.split(' ')
    if content[1] == "装备" or content[1] == "zb":
        await msg.reply(vendorTool.getGear(0))
        await msg.reply(vendorTool.getGear(20))
    if content[1] == "武器" or content[1] == "wq":
        await msg.reply(vendorTool.getWeapons(0))
        await msg.reply(vendorTool.getWeapons(20))
    if content[1] == "插件" or content[1] == "cj":
        await msg.reply(vendorTool.getMods())

# apply test role
@bot.command(regex=r'申请测试资格.+', rules={Rule.is_bot_mentioned(bot)})
async def getRole1(msg: Message):
    await reqFrontLogger(msg)
    guild = await bot.client.fetch_guild(msg.guild.id)
    user = await bot.client.fetch_user(msg.author_id)
    await guild.grant_role(user, config['test-role-id'])
    await msg.reply('添加权限成功，处理中，请稍后查看！')

# download logfile
@bot.command(name='log')
async def logfile(msg: Message):
    await reqFrontLogger(msg)
    url = await bot.client.create_asset('./doc/log.txt')
    await msg.reply(url, type=MessageTypes.TEXT)

# bind td2 character
@bot.command(name='绑定')
async def bind(msg: Message, name):
    await reqFrontLogger(msg)
    print('userid: ' + msg.author.id)
    await msg.reply(Binduser().bind(msg.author.id, name))

# show td2name
@bot.command(regex=r'/id|/名片')
async def nameCard(msg: Message):
    await reqFrontLogger(msg)
    td2name = sqlMapper.getTd2nameByUserId(msg.author.id)
    #未绑定提醒
    if (td2name == ''):
        await msg.reply('请先使用 /绑定<空格><游戏角色名> 进行绑定！')
        return
    c = Card(Module.Header('游戏邀请'), color='#33FFFF')
    c.append(Module.Divider())
    c.append(Module.Section({"type": "kmarkdown","content": "我的全境封锁2游戏ID为 `" + td2name + "`"}))
    c.append(Module.Section('复制如下内容，在游戏内聊天框中输入后，按回车进入我的队伍'))
    c.append(Module.Section({"type": "kmarkdown","content": "`/join " + td2name + "`"}))
    cm = CardMessage(c)
    await msg.reply(cm)

# signin
@bot.command(regex=r'/qd|/签到|签到')
async def sign(msg: Message):
    await reqFrontLogger(msg)
    guild = await bot.client.fetch_guild(msg.guild.id)
    user = await bot.client.fetch_user(msg.author_id)
    guildUser = await guild.fetch_user(msg.author_id)
    logger.info('guildUser.roles:'+str(guildUser.roles))
    notice,total,consecutive,prop = Signin().sign(msg.author.id,bot).split('|')
    if int(consecutive) == config['dtygk-role-days']:
        if int(config['dtygk-role-id']) not in guildUser.roles:
            await guild.grant_role(user, config['dtygk-role-id'])
            notice += '，恭喜您获得荣誉称号：< 洞庭有归客 >'
    if int(consecutive) < config['dtygk-role-days']:
        if int(config['dtygk-role-id']) not in guildUser.roles:
            days = config['dtygk-role-days']-int(consecutive)
            notice += '，距离获得< 洞庭有归客 >称号还需连续签到' + str(days) + '天'
    if int(total) == config['xxfgr-role-days']:
        if int(config['xxfgr-role-id']) not in guildUser.roles:
            await guild.grant_role(user, config['xxfgr-role-id'])
            notice += '，恭喜您获得荣誉称号：< 潇湘逢故人 >'
    if int(total) < config['xxfgr-role-days']:
        if int(config['xxfgr-role-id']) not in guildUser.roles:
            days = config['xxfgr-role-days']-int(total)
            notice += '，距离获得< 潇湘逢故人 >称号还需累计签到' + str(days) + '天'
    await msg.reply('@' + msg.author.nickname + notice)

# auto signin
@bot.on_event(EventTypes.JOINED_CHANNEL)
async def auto_signin(b: Bot, event: Event):
    if event.body['channel_id'] == config['auto_sign_channel_id']:
        channel = await b.client.fetch_public_channel(config['public_channel_id'])
        guild = await bot.client.fetch_guild(config['guild_id'])
        user = await bot.client.fetch_user(event.body['user_id'])
        guildUser = await guild.fetch_user(event.body['user_id'])
        notice,total,consecutive,prop = Signin().sign(event.body['user_id'],bot).split('|')
        if int(consecutive) == config['dtygk-role-days']:
            if int(config['dtygk-role-id']) not in guildUser.roles:
                await guild.grant_role(user, config['dtygk-role-id'])
        if int(total) == config['xxfgr-role-days']:
            if int(config['xxfgr-role-id']) not in guildUser.roles:
                await guild.grant_role(user, config['xxfgr-role-id'])
        userinfo = sqlMapper.getUserInfoByUserId(event.body['user_id'])
        if userinfo['welword'] != '':
            await bot.client.send(channel,user.nickname + userinfo['welword'] + notice,type=MessageTypes.KMD)
        else:
            await bot.client.send(channel,user.nickname + "来咯~" + notice,type=MessageTypes.KMD)
    if event.body['channel_id'] == '1753876426908171':
        guild = await bot.client.fetch_guild(config['guild_id'])
        user = await bot.client.fetch_user(event.body['user_id'])
        channelname = user.username + ' 的自习室'
        voiceChannel = await bot.client.create_voice_channel(channelname,guild,'1269596120540644',1,2)
        await voiceChannel.move_user(user.id)

# auto delete room
@bot.on_event(EventTypes.EXITED_CHANNEL)
async def auto_delete_channel(b: Bot, event: Event):
    channel = await bot.client.fetch_public_channel(event.body['channel_id'])
    if('的自习室' in channel.name):
        await bot.client.delete_channel(channel)

# set welcome words
@bot.command(name='welcome')
async def welcome(msg: Message, word):
    await reqFrontLogger(msg)
    userinfo = sqlMapper.getUserInfoByUserId(msg.author_id)
    userinfo['welword'] = word
    sqlMapper.updateUserInfo(userinfo)
    logger.info("New Data : " + str(userinfo))
    await msg.reply('设置成功')


@bot.command(regex=r'打开控制台')
async def find(msg: Message):
    await reqFrontLogger(msg)
    c = Card()
    c.append(Module.Section({"type":"kmarkdown","content":"[控制台](https://ecs.console.aliyun.com/vnc/index.htm?instanceId=i-rj9gjdatfp304idf90wx&regionId=us-west-1&instanceName=launch-advisor-20221214)"}))
    cm = CardMessage(c)
    await msg.reply(cm)

# chat with chatgpt
@bot.command(regex=r'/gpt.+')
async def gpt(msg: Message):
    await reqFrontLogger(msg)
    url = 'https://api.openai.com/v1/chat/completions'

    mo = "gpt-3.5-turbo-0301"
    me = [{"role": "user","content": msg.content.split(' ',1)[1]}]
    data = {"model":mo,"messages":me}
    logger.info("Data : " + str(data))

    headers = {'Content-Type':'application/json','Authorization':'Bearer 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'}

    response = requests.post(url,json=data,headers=headers)
    r = json.loads(response.content.decode('utf-8'))
    await msg.reply('[gpt-3.5-turbo-0301] : ' + r['choices'][0]['message']['content'])

# generate image by ai
# @bot.command(regex=r'/gimg.+')
# async def gptimg(msg: Message):
#     await reqFrontLogger(msg)
#     url = 'https://api.openai.com/v1/images/generations'
#     m = msg.content.split(' ',2)
#     size = m[1]
#     prompt = m[2]
#     data = {"prompt":prompt,"size":size,"n":1}
#     logger.info("Data : " + str(data))
#     headers = {'Content-Type':'application/json','Authorization':'Bearer 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'}

#     response = requests.post(url,json=data,headers=headers)
#     r = json.loads(response.content.decode('utf-8'))
#     if "error" in r:
#         await msg.reply(r['error']['message'])
#     else:
#         u = r['data'][0]['url']
#         await msg.reply('[查看AI生成结果](' + u + ')', type=MessageTypes.KMD)

# calculator
@bot.command(name='计算')
async def calculate(msg: Message, expression):
    await reqFrontLogger(msg)
    try:
        result = eval(expression.replace('x', '*'))
        await msg.reply(f'{expression} = {result}')
    except:
        await msg.reply('表达式有误，请重新输入！')


bot.run()

