from khl.card import CardMessage, Card, Module, Element, Types
# 功能菜单
class Menu():
  def getMenu(self,type) -> CardMessage:
    func = ""
    comm = ""
    menutype = []
    remark = []
    if type == "1":
        menutype = menuCommands
        remark = 'PLA战队频道专用菜单'
    if type == "2":
        menutype = menuCommands2
        remark = '全境封锁系列语音频道定制菜单'
    for record in menutype:
        func += record['func'] + "\n"
        comm += record['comm'] + "\n"
    c = Card()
    c = Card(Module.Header('阿妮亚功能菜单'), color='#FFCC00')
    c.append(Module.Context(remark))
    c.append(Module.Divider())
    c.append(
        Module.Section({
            "type":"paragraph",
            "cols":2,
            "fields": [{
                "type": "kmarkdown",
                "content": "**功能**\n" + func
            }, {
                "type": "kmarkdown",
                "content": "**快捷指令**\n" + comm
            }]
        }))
    cm = CardMessage(c) 
    return cm

#PLA专用菜单
menuCommands = [
  {
    "func":"功能菜单",
    "comm":"/cd 或 /menu"
  },{
    "func":"签到",
    "comm":"/qd"
  },{
    "func":"战队名片",
    "comm":"/zd 或 /pla"
  },{
    "func":"战队Raid武器查询",
    "comm":"/td2raid ?"
  },{
    "func":"每周商人查询",
    "comm":"/zs 或 /周商"
  },{
    "func":"萌新配装路线图",
    "comm":"/map"
  },{
    "func":"PVE配装表",
    "comm":"/pz"
  },{
    "func":"突击步枪性能排名",
    "comm":"/ar"
  },{
    "func":"装备天赋增伤强度",
    "comm":"/装备天赋"
  },{
    "func":"奇特武器",
    "comm":"/奇特武器"
  },{
    "func":"奇特装备",
    "comm":"/奇特装备"
  },{
    "func":"套装效果",
    "comm":"/tz"
  },{
    "func":"强化材料查询",
    "comm":"/强化"
  },{
    "func":"优化材料来源",
    "comm":"/材料"
  },{
    "func":"技能增伤机制",
    "comm":"/技能"
  },{
    "func":"白区活动经验",
    "comm":"/jy 或 活动经验"
  },{
    "func":"服务器状态",
    "comm":"/server"
  },{
    "func":"绑定游戏角色",
    "comm":"/绑定<空格><游戏角色名>"
  },{
    "func":"发送游戏邀请",
    "comm":"/id 或 /名片"
  },{
    "func":"查询玩家数据",
    "comm":"/查询<空格><游戏角色名>"
  },{
    "func":"掠夺站武器记录",
    "comm":"/raid"
  },{
    "func":"赛季日历",
    "comm":"/rl 或 日历 或 赛季日历"
  },{
    "func":"暗区箱子地图",
    "comm":"/aq 或 暗区"
  }
]
#全境封锁系列语音频道定制菜单
menuCommands2 = [
  {
    "func":"功能菜单",
    "comm":"/cd 或 /menu"
  },{
    "func":"签到",
    "comm":"/qd"
  },{
    "func":"每周商人查询",
    "comm":"/zs 或 /周商"
  },{
    "func":"萌新配装路线图",
    "comm":"/map"
  },{
    "func":"PVE配装表",
    "comm":"/pz"
  },{
    "func":"突击步枪性能排名",
    "comm":"/ar"
  },{
    "func":"装备天赋增伤强度",
    "comm":"/装备天赋"
  },{
    "func":"奇特武器",
    "comm":"/奇特武器"
  },{
    "func":"奇特装备",
    "comm":"/奇特装备"
  },{
    "func":"套装效果",
    "comm":"/tz"
  },{
    "func":"强化材料查询",
    "comm":"/强化"
  },{
    "func":"优化材料来源",
    "comm":"/材料"
  },{
    "func":"技能增伤机制",
    "comm":"/技能"
  },{
    "func":"白区活动经验",
    "comm":"/jy 或 活动经验"
  },{
    "func":"服务器状态",
    "comm":"/server"
  },{
    "func":"绑定游戏角色",
    "comm":"/绑定<空格><游戏角色名>"
  },{
    "func":"发送游戏邀请",
    "comm":"/id 或 /名片"
  },{
    "func":"查询玩家数据",
    "comm":"/查询<空格><游戏角色名>"
  },{
    "func":"赛季日历",
    "comm":"/rl 或 日历 或 赛季日历"
  },{
    "func":"暗区箱子地图",
    "comm":"/aq 或 暗区"
  }
]