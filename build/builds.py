from khl.card import CardMessage, Module, Card
from khl import Bot, Message, MessageTypes, EventTypes, Event
from build.getBuild import Build
from datetime import timedelta, datetime
import json
import logging

logger = logging.getLogger()

with open('build/buildmenu.json', 'r', encoding='utf-8') as f:
    menujson = json.load(f)

async def reqFrontLogger(msg:Message,bot:Bot):
    cont = "Channel:" + msg.target_id + " | Command request:" + msg.content + " | userid:" +  msg.author.id + " | userName:" + msg.author.username + '#' + msg.author.identify_num + " | time:" + (datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(cont)
    chan = await bot.client.fetch_public_channel("7678231813152563")
    await bot.client.send(chan, cont)

# 配装表
class BuildList():
    def __init__(self, bot):
        if bot != None:
            # 配装指令
            @bot.command(regex=r'/zp|重炮|极限重炮')
            async def zhongpao(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('zhongpao'))

            @bot.command(regex=r'/qh|全火|金装全火')
            async def quanhuo(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('quanhuo'))

            @bot.command(regex=r'/qh2|全火2|金装全火2')
            async def quanhuo2(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('quanhuo2'))

            @bot.command(regex=r'/fx|芳心|火体芳心')
            async def fangxin(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('fangxin'))

            @bot.command(regex=r'/lr|猎人|追悼猎人')
            async def lierenpen(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('lierenpen'))

            @bot.command(regex=r'/nm|奶妈|未来奶')
            async def weilainai(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('weilainai'))

            @bot.command(regex=r'/rs|日蚀|日蚀控')
            async def rishi(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('rishi'))

            @bot.command(regex=r'/dp|打牌|打牌狙')
            async def dapai(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('dapai'))

            @bot.command(regex=r'/xf|先锋|先锋狙')
            async def xianfeng(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('xianfeng'))

            @bot.command(regex=r'/yhj|氧化剂')
            async def yanghuaji(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('yanghuaji'))

            @bot.command(regex=r'/tf|塔防')
            async def tafang(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('tafang'))

            @bot.command(regex=r'/jf|精防|精防喷子')
            async def jingfang(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('jingfang'))

            @bot.command(regex=r'/tj|探子警戒')
            async def tanzijingjie(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('tanzijingjie'))

            @bot.command(regex=r'/hjer|红甲恶人')
            async def hongjiaeren(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('hongjiaeren'))

            @bot.command(regex=r'/jffx|精防芳心')
            async def jingfangfangxin(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('jingfangfangxin'))

            @bot.command(regex=r'/zl|政令')
            async def zhengling(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('zhengling'))

            @bot.command(regex=r'/zk|中控')
            async def zhongkong(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('zhongkong'))

            @bot.command(regex=r'/tp|谈判')
            async def tanpan(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('tanpan'))

            @bot.command(regex=r'/gx|固线')
            async def guxian(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('guxian'))

            @bot.command(regex=r'/cb|拆板')
            async def chaiban(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('chaiban'))

            @bot.command(regex=r'/wz|王子')
            async def wangzi(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('wangzi'))

            @bot.command(regex=r'/tx|突袭')
            async def tuxi(msg: Message):
                await reqFrontLogger(msg,bot)
                await msg.reply(Build().getBuild('tuxi'))
            
            logger.info("Build Commands Load Success")

    def getList(self) -> CardMessage:
        c = Card(Module.Header('常用配装指南（配装表2.0）'), color='#FFCC00')
        c.append(Module.Section({"type":"kmarkdown","content":"萌新配装推荐路线图请参考指令：`/map`"}))
        c.append(Module.Context('在文字频道发送配装对应指令，Ania会回复你具体配装信息，多个快捷指令任选其一即可'))
        # 全火输出
        c.append(Module.Divider())
        c.append(Module.Section('全火输出(6)'))
        c.append(Module.Context('全部属性致力于提升武器伤害，不关注生存，追求极致的输出能力，但身板很脆，在有队友辅助的情况下是绝对的团队输出核心'))
        c.append(Module.Divider())
        c.append(Module.Section({"type":"kmarkdown","content":"全火探子警戒(推荐)     快捷指令：`/tj` `探子警戒`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"全火突袭(推荐)            快捷指令：`/tx` `突袭`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"谈判专注AR(高群伤)    快捷指令：`/tp` `谈判`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"金装全火AR(三天命)    快捷指令：`/qh` `全火` `金装全火`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"金装全火AR(无天命)    快捷指令：`/qh2` `全火2` `金装全火2`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"打牌猎头狙                 快捷指令：`/dp` `打牌` `打牌狙`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"先锋猎头狙                 快捷指令：`/xf` `先锋` `先锋狙`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"王子手枪盾                 快捷指令：`/wz` `王子`"}))
        # 火体生存
        c.append(Module.Divider())
        c.append(Module.Section('火体生存(4)'))
        c.append(Module.Context('兼顾进攻与防守，往往依靠高阶盾牌和叠加大量的额外装甲抵御敌方的攻击，同时能够打出可观的伤害，是吸引仇恨、保护队友、冲锋陷阵的首选'))
        c.append(Module.Divider())
        c.append(Module.Section({"type":"kmarkdown","content":"猎人追悼天蝎座          快捷指令：`/lr` `猎人` `猎人喷`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"火体芳心                    快捷指令：`/fx` `芳心` `火体芳心`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"精防喷子                    快捷指令：`/jf` `精防` `精防喷子`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"精防芳心                    快捷指令：`/jffx` `精防芳心`"}))
        # 电工塔防
        c.append(Module.Divider())
        c.append(Module.Section('电工塔防(3)'))
        c.append(Module.Context('以技能为主要输出手段，输出手法比较简单，适用于难以露头输出的极端场景或依靠技能的强大火力对敌人形成压制，甚至堵门输出，技能的多样性决定了电工各种场景的高适应性'))
        c.append(Module.Divider())
        c.append(Module.Section({"type":"kmarkdown","content":"波皇塔防                    快捷指令：`/tf` `塔防`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"极限重炮                    快捷指令：`/zp` `重炮` `极限重炮`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"极限氧化剂                 快捷指令：`/yhj` `氧化剂`"}))
        # 辅助增伤
        c.append(Module.Divider())
        c.append(Module.Section('辅助增伤(3)'))
        c.append(Module.Context('为团队队友提供增伤、控场、治疗等辅助手段，是团队不可或缺的一员，一名经验丰富的辅助可以使整个团队战力倍增'))
        c.append(Module.Divider())
        c.append(Module.Section({"type":"kmarkdown","content":"超载未来奶妈              快捷指令：`/nm` `奶妈` `未来奶`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"日蚀火法控制              快捷指令：`/rs` `日蚀` `日蚀控`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"政令极限增伤(推荐)     快捷指令：`/zl` `政令`"}))
        # Raid常用
        c.append(Module.Divider())
        c.append(Module.Section('Raid常用(3)'))
        c.append(Module.Context('Raid机制位常用套装，车头必备，使用场景固定，配装针对性较强'))
        c.append(Module.Divider())
        c.append(Module.Section({"type":"kmarkdown","content":"中控火抗回甲              快捷指令：`/zk` `中控`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"固线干扰脉冲              快捷指令：`/gx` `固线`"}))
        c.append(Module.Section({"type":"kmarkdown","content":"道奇城拆板套              快捷指令：`/cb` `拆板`"}))
        cm = CardMessage(c)
        return cm

    def getPvp(self) -> CardMessage:
        c = Card(Module.Header('PVP配装表'))
        c.append(Module.Section('红甲恶人     \t\t快捷指令：/hjer 红甲恶人'))
        c.append(Module.Section('爆头隐身(反芳心) \t快捷指令：/ys'))
        cm = CardMessage(c)
        return cm
