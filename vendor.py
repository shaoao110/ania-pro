from khl.card import CardMessage, Card, Module, Element
from khl import Bot
import requests
import json
import logging
import xlwt
logger = logging.getLogger()

with open('translation/vendor.json', 'r', encoding='utf-8') as f:
    trans_vendor = json.load(f)
with open('translation/brand.json', 'r', encoding='utf-8') as f:
    trans_brand = json.load(f)
with open('translation/slot.json', 'r', encoding='utf-8') as f:
    trans_slot = json.load(f)
with open('translation/core.json', 'r', encoding='utf-8') as f:
    trans_core = json.load(f)
with open('translation/attribute.json', 'r', encoding='utf-8') as f:
    trans_attr = json.load(f)
with open('translation/geartalent.json', 'r', encoding='utf-8') as f:
    trans_geartalent = json.load(f)
with open('translation/geartype.json', 'r', encoding='utf-8') as f:
    trans_geartype = json.load(f)
with open('translation/modattribute.json', 'r', encoding='utf-8') as f:
    trans_modattr = json.load(f)
with open('translation/skillname.json', 'r', encoding='utf-8') as f:
    trans_skillname = json.load(f)
with open('translation/weapontalent.json', 'r', encoding='utf-8') as f:
    trans_weapontalent = json.load(f)
with open('translation/weaponattr.json', 'r', encoding='utf-8') as f:
    trans_weaponattr = json.load(f)

class Vendor():
    def getGear(self,start) -> CardMessage:
        path = "https://rubenalamina.mx/division/gear.json";
        res = requests.get(url=path)
        total = 0;
        page = "1";
        if(start == 20):
            page = "2"
        if(start == 40):
            page = "3"
        object = json.loads(str(res.text))
        c = Card(Module.Header('周商装备('+page+'/3):'),color="FFCCFF")
        for index in range(len(object)):
            if index < start:
                continue
            if total == 20 :
                break;
            total += 1
            
            gear = object[index]
            item = "```js\n装备名称：" + gear['name'] + " (" + trans_geartype[gear['rarity']] + ")" 
            #商人
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            item += "\n商人：" + vendorEn
            #品牌
            brandEn = gear['brand']
            if brandEn in trans_brand:
                brandEn = trans_brand[brandEn]
            item += "\n品牌：" + brandEn
            #部位
            slotEn = gear['slot']
            if slotEn in trans_slot:
                slotEn = trans_slot[slotEn]
            item += "\n部位：" + slotEn
            #核心属性
            coreEn = gear['core'].split(">")[-1].strip()
            coreList = coreEn.split(" ",1)
            if coreList[-1] in trans_core:
                coreEn = coreList[0] + " " + trans_core[coreList[-1]]
            item += "\n核心属性：" + coreEn
            #属性
            attributes = gear['attributes'].split(" <br/>")
            count = 1
            for attr in attributes:
                attrEn = attr.split(">")[-1].strip()
                attrList = attrEn.split(" ",1)
                if attrList[-1] in trans_attr:
                    attrEn = attrList[0] + " " + trans_attr[attrList[-1]]
                item += "\n属性" + str(count) + "：" + attrEn
                count += 1
            #天赋
            talents = gear['talents'].split(" <br/>")
            count2 = 1
            for tal in talents:
                gtalentEn = tal.split(">")[-1].strip()
                if gtalentEn in trans_geartalent:
                    gtalentEn = trans_geartalent[gtalentEn]
                item += "\n天赋" + str(count2) + "：" + gtalentEn
                count2 += 1
            item += "\n```"
            c.append(Module.Section({"type":"kmarkdown","content":item}))
        cm = CardMessage(c)
        return cm

    def getWeapons(self,start) -> CardMessage:
        path = "https://rubenalamina.mx/division/weapons.json";
        res = requests.get(url=path)
        total = 0;
        page = "1";
        if(start > 0):
            page = "2"
        object = json.loads(str(res.text))
        c = Card(Module.Header('周商武器('+page+'/2):'),color="FFCCFF")
        c.append(Module.Context('翻译工作进行中'))
        for index in range(len(object)):
            if index < start:
                continue
            if total == 20 :
                break;
            total += 1
            
            gear = object[index]
            item = "```js\n武器名称：" + gear['name'] + " (" + trans_geartype[gear['rarity']] + ")" 
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            item += "\n商人：" + vendorEn
            item += "\n白字伤害、射速、弹夹容量：" + str(gear['dmg']) + " | " + str(gear['rpm']) + " | " + str(gear['mag'])
            
            weaponattr1En = gear['attribute1'].split(">")[-1].split(" ",1)
            if weaponattr1En[-1] in trans_weaponattr:
                weaponattr1En[-1] = trans_weaponattr[weaponattr1En[-1]]
            item += "\n属性1：" + weaponattr1En[0] + " " + weaponattr1En[-1]

            weaponattr2En = gear['attribute2'].split(">")[-1].split(" ",1)
            if weaponattr2En[-1] in trans_weaponattr:
                weaponattr2En[-1] = trans_weaponattr[weaponattr2En[-1]]
            item += "\n属性2：" + weaponattr2En[0] + " " + weaponattr2En[-1]

            weaponattr3En = gear['attribute3'].split(">")[-1].split(" ",1)
            if weaponattr3En[-1] in trans_weaponattr:
                weaponattr3En[-1] = trans_weaponattr[weaponattr3En[-1]]
            item += "\n属性3：" + weaponattr3En[0] + " " + weaponattr3En[-1]

            weapontalentEn = gear['talent']
            if weapontalentEn in trans_weapontalent:
                weapontalentEn = trans_weapontalent[weapontalentEn]
            item += "\n天赋：" + weapontalentEn
            item += "\n```"
            c.append(Module.Section({"type":"kmarkdown","content":item}))
        cm = CardMessage(c)
        return cm

    def getMods(self,start) -> CardMessage:
        path = "https://rubenalamina.mx/division/mods.json";
        res = requests.get(url=path)
        total = 0;
        page = "1";
        if(start > 0):
            page = "2"
        object = json.loads(str(res.text))
        c = Card(Module.Header('周商插件('+page+'/2):'),color="FFCCFF")
        c.append(Module.Context('翻译工作进行中'))
        for index in range(len(object)):
            if index < start:
                continue
            if total == 30 :
                break;
            total += 1
            
            gear = object[index]
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            item = "```js\n插件名称：" + gear['name']
            item += "\n商人：" + vendorEn

            skill = ''
            if "<br/>" in gear['attributes']:
                skill = gear['attributes'].split("<br/>")[0].strip()
                if skill in trans_skillname:
                    skill = trans_skillname[skill] + "："
                else:
                    skill = skill + ":"
            mattrEn = gear['attributes'].split(">")[-1].strip()
            mattrList = mattrEn.split(" ",1)
            if mattrList[-1] in trans_modattr:
                mattrEn = mattrList[0] + " " + trans_modattr[mattrList[-1]]
            item += "\n属性：" + skill + mattrEn
            item += "\n```"
            c.append(Module.Section({"type":"kmarkdown","content":item}))
        cm = CardMessage(c)
        return cm

    def getVendorExcel(self) :
        wb = xlwt.Workbook()

        ############################### 导出装备信息 ###############################
        path = "https://rubenalamina.mx/division/gear.json";
        res = requests.get(url=path)
        # 添加一个表
        ws = wb.add_sheet('装备')
        # 设置列宽
        ws.col(0).width = 256*20
        ws.col(1).width = 256*24
        ws.col(2).width = 256*8
        ws.col(3).width = 256*20
        ws.col(4).width = 256*5
        ws.col(5).width = 256*15
        ws.col(6).width = 256*40
        ws.col(7).width = 256*12
        # 表头
        ws.write(0, 0, f'商人')
        ws.write(0, 1, f'装备名称')
        ws.write(0, 2, f'装备类型')
        ws.write(0, 3, f'品牌')
        ws.write(0, 4, f'部位')
        ws.write(0, 5, f'核心属性')
        ws.write(0, 6, f'属性')
        ws.write(0, 7, f'天赋')

        object = json.loads(str(res.text))
        for index in range(len(object)):
            gear = object[index]

            #商人
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            ws.write(index+1, 0, vendorEn)

            #装备名称
            ws.write(index+1, 1, gear['name'])

            #装备类型
            ws.write(index+1, 2, trans_geartype[gear['rarity']])

            #品牌
            brandEn = gear['brand']
            if brandEn in trans_brand:
                brandEn = trans_brand[brandEn]
            ws.write(index+1, 3, brandEn)

            #部位
            slotEn = gear['slot']
            if slotEn in trans_slot:
               slotEn = trans_slot[slotEn]
            ws.write(index+1, 4, slotEn)

            #核心属性
            coreEn = gear['core'].split(">")[-1].strip()
            coreList = coreEn.split(" ",1)
            if coreList[-1] in trans_core:
                coreEn = coreList[0] + " " + trans_core[coreList[-1]]
            ws.write(index+1, 5, coreEn)

            #属性
            attributes = gear['attributes'].split(" <br/>")
            attribute = ""
            for attr in attributes:
                attrEn = attr.split(">")[-1].strip()
                attrList = attrEn.split(" ",1)
                if attrList[-1] in trans_attr:
                    attrEn = attrList[0] + " " + trans_attr[attrList[-1]]
                attribute += attrEn + "\n"
            if attribute != "":    
                attribute = attribute[:-1]
            ws.write(index+1, 6, attribute)
                    
            #天赋
            talents = gear['talents'].split(" <br/>")
            talent = ""
            for tal in talents:
                gtalentEn = tal.split(">")[-1].strip()
                if gtalentEn in trans_geartalent:
                    gtalentEn = trans_geartalent[gtalentEn]
                talent += gtalentEn + "\n"
            if talent != "":
                talent = talent[:-1]
            ws.write(index+1, 7, talent)      
        
        ############################### 导出武器信息 ###############################
        path = "https://rubenalamina.mx/division/weapons.json";
        res = requests.get(url=path)
        # 添加一个表
        ws2 = wb.add_sheet('武器')
        # 设置列宽
        ws2.col(0).width = 256*20
        ws2.col(1).width = 256*36
        ws2.col(2).width = 256*8
        ws2.col(3).width = 256*25
        ws2.col(4).width = 256*25
        ws2.col(5).width = 256*25
        ws2.col(6).width = 256*12
        ws2.col(7).width = 256*8
        ws2.col(8).width = 256*5
        ws2.col(9).width = 256*8
        # 表头
        ws2.write(0, 0, f'商人')
        ws2.write(0, 1, f'武器名称')
        ws2.write(0, 2, f'武器类型')
        ws2.write(0, 3, f'属性1')
        ws2.write(0, 4, f'属性2')
        ws2.write(0, 5, f'属性3')
        ws2.write(0, 6, f'天赋')
        ws2.write(0, 7, f'武器伤害')
        ws2.write(0, 8, f'射速')
        ws2.write(0, 9, f'弹夹容量')

        object = json.loads(str(res.text))
        for index in range(len(object)):
            gear = object[index]

            #商人
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            ws2.write(index+1, 0, vendorEn)

            #武器名称
            ws2.write(index+1, 1, gear['name'])

            #武器类型
            ws2.write(index+1, 2, trans_geartype[gear['rarity']])

            #属性1
            weaponattr1En = gear['attribute1'].split(">")[-1].split(" ",1)
            if weaponattr1En[-1] in trans_weaponattr:
                weaponattr1En[-1] = trans_weaponattr[weaponattr1En[-1]]
            ws2.write(index+1, 3, weaponattr1En[0] + " " + weaponattr1En[-1])

            #属性2
            weaponattr2En = gear['attribute2'].split(">")[-1].split(" ",1)
            if weaponattr2En[-1] in trans_weaponattr:
                weaponattr2En[-1] = trans_weaponattr[weaponattr2En[-1]]
            ws2.write(index+1, 4, weaponattr2En[0] + " " + weaponattr2En[-1])

            #属性3
            weaponattr3En = gear['attribute3'].split(">")[-1].split(" ",1)
            if weaponattr3En[-1] in trans_weaponattr:
                weaponattr3En[-1] = trans_weaponattr[weaponattr3En[-1]]
            ws2.write(index+1, 5, weaponattr3En[0] + " " + weaponattr3En[-1])

            #天赋
            weapontalentEn = gear['talent']
            if weapontalentEn in trans_weapontalent:
                weapontalentEn = trans_weapontalent[weapontalentEn]
            ws2.write(index+1, 6, weapontalentEn)

            #伤害、射速、弹容
            ws2.write(index+1, 7, str(gear['dmg']))
            ws2.write(index+1, 8, str(gear['rpm']))
            ws2.write(index+1, 9, str(gear['mag']))

        ############################### 导出插件信息 ###############################
        path = "https://rubenalamina.mx/division/mods.json";
        res = requests.get(url=path)
        # 添加一个表
        ws3 = wb.add_sheet('插件')
        # 设置列宽
        ws3.col(0).width = 256*20
        ws3.col(1).width = 256*36
        ws3.col(2).width = 256*12
        ws3.col(3).width = 256*20
        # 表头
        ws3.write(0, 0, f'商人')
        ws3.write(0, 1, f'插件名称')
        ws3.write(0, 2, f'插件位置')
        ws3.write(0, 3, f'插件效果')
        
        object = json.loads(str(res.text))
        for index in range(len(object)):
            gear = object[index]

            #商人
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            ws3.write(index+1, 0, vendorEn)

            #插件名称
            ws3.write(index+1, 1, gear['name'])
           
            #插件位置
            skill = ''
            if "<br/>" in gear['attributes']:
                skill = gear['attributes'].split("<br/>")[0].strip()
                if skill in trans_skillname:
                    skill = trans_skillname[skill]
            ws3.write(index+1, 2, skill)

            #插件效果
            mattrEn = gear['attributes'].split(">")[-1].strip()
            mattrList = mattrEn.split(" ",1)
            if mattrList[-1] in trans_modattr:
                mattrEn = mattrList[0] + " " + trans_modattr[mattrList[-1]]
            ws3.write(index+1, 3, mattrEn)
            
        wb.save('./TD2WeeklyVendor.xls')