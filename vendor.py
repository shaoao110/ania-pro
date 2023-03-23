from khl.card import CardMessage, Card, Module, Element
import requests
import json
import logging
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

class Vendor():
    def getGear(self,start) -> CardMessage:
        path = "https://rubenalamina.mx/division/gear.json";
        res = requests.get(url=path)
        total = 0;
        page = "1";
        if(start > 0):
            page = "2"
        object = json.loads(str(res.text))
        c = Card(Module.Header('周商装备('+page+'/2):'),color="FFCCFF")
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
            item += "\n属性1：" + gear['attribute1'].split(">")[-1]
            item += "\n属性2：" + gear['attribute2'].split(">")[-1]
            item += "\n属性3：" + gear['attribute3'].split(">")[-1]
            item += "\n天赋：" + gear['talent']
            item += "\n```"
            c.append(Module.Section({"type":"kmarkdown","content":item}))
        cm = CardMessage(c)
        return cm

    def getMods(self) -> CardMessage:
        path = "https://rubenalamina.mx/division/mods.json";
        res = requests.get(url=path)
        object = json.loads(str(res.text))
        c = Card(Module.Header('周商插件:'),color="FFCCFF")
        c.append(Module.Context('翻译工作进行中'))
        for gear in object:
            vendorEn = gear['vendor']
            if vendorEn in trans_vendor:
                vendorEn = trans_vendor[vendorEn]
            item = "```js\n插件名称：" + gear['name']
            item += "\n商人：" + vendorEn

            mattrEn = gear['attributes'].split(">")[-1].strip()
            mattrList = mattrEn.split(" ",1)
            if mattrList[-1] in trans_modattr:
                mattrEn = mattrList[0] + " " + trans_modattr[mattrList[-1]]
            item += "\n属性：" + mattrEn
            item += "\n```"
            c.append(Module.Section({"type":"kmarkdown","content":item}))
        cm = CardMessage(c)
        return cm