from khl.card import CardMessage, Card, Module, Element, Types
import json

class Build():
    def getBuild(self, name) -> CardMessage:
        with open('build/buildconfig/' + name + '.json', 'r', encoding='utf-8') as f:
            obj = json.load(f,strict=False)
        buildname = obj['buildname']
        #主题 0-红 1-黄 2-蓝
        buildtype = obj['buildtype']
        title = None
        col = None
        if buildtype == 0:
          title = Element.Button(buildname, 'RED', theme=Types.Theme.DANGER)
          col = "FF0000"
        elif buildtype == 1:
          title = Element.Button(buildname, 'RED', theme=Types.Theme.WARNING)
          col = "FF9900"
        elif buildtype == 2:
          title = Element.Button(buildname, 'RED', theme=Types.Theme.INFO)
          col = "6699ff"
        else:
          title = Element.Button(buildname, 'RED', theme=Types.Theme.INFO)
          col = "6699ff"

        #面具
        mask = "```js\n品牌名称：" + obj['mask']['name']
        mask += "\n核心属性：" + obj['mask']['core']
        mask += "\n属性：" + obj['mask']['attribute1']
        if obj['mask']['attribute2'] != '':
            mask += "\n属性：" + obj['mask']['attribute2']
        mask += "\n插件：" + obj['mask']['plugin1']
        if obj['mask']['plugin2'] != '':
            mask += "\n插件：" + obj['mask']['plugin2']
        mask += "\n```"

         #手套
        gloves = "```js\n品牌名称：" + obj['gloves']['name']
        gloves += "\n核心属性：" + obj['gloves']['core']
        gloves += "\n属性：" + obj['gloves']['attribute1']
        if obj['gloves']['attribute2'] != '':
            gloves += "\n属性：" + obj['gloves']['attribute2']
        gloves += "\n插件：" + obj['gloves']['plugin1']
        gloves += "\n```"

        #枪套
        holster = "```js\n品牌名称：" + obj['holster']['name']
        holster += "\n核心属性：" + obj['holster']['core']
        holster += "\n属性：" + obj['holster']['attribute1']
        if obj['holster']['attribute2'] != '':
            holster += "\n属性：" + obj['holster']['attribute2']
        holster += "\n插件：" + obj['holster']['plugin1']
        holster += "\n```"

        #护膝
        kneecap = "```js\n品牌名称：" + obj['kneecap']['name']
        kneecap += "\n核心属性：" + obj['kneecap']['core']
        kneecap += "\n属性：" + obj['kneecap']['attribute1']
        if obj['kneecap']['attribute2'] != '':
            kneecap += "\n属性：" + obj['kneecap']['attribute2']
        kneecap += "\n插件：" + obj['kneecap']['plugin1']
        kneecap += "\n```"

        #背心
        vest = "```js\n品牌名称：" + obj['vest']['name']
        vest += "\n核心属性：" + obj['vest']['core']
        vest += "\n属性：" + obj['vest']['attribute1']
        if obj['vest']['attribute2'] != '':
            vest += "\n属性：" + obj['vest']['attribute2']
        vest += "\n插件：" + obj['vest']['plugin1']
        vest += "\n天赋：" + obj['vest']['talent']
        vest += "\n```"

        #背包
        knapsack = "```js\n品牌名称：" + obj['knapsack']['name']
        knapsack += "\n核心属性：" + obj['knapsack']['core']
        knapsack += "\n属性：" + obj['knapsack']['attribute1']
        if obj['knapsack']['attribute2'] != '':
            knapsack += "\n属性：" + obj['knapsack']['attribute2']
        knapsack += "\n插件：" + obj['knapsack']['plugin1']
        knapsack += "\n天赋：" + obj['knapsack']['talent']
        knapsack += "\n```"

        #武器
        weapon = "```js\n名称：" + obj['weapon']['desc'] + "\n```"

        c = Card(color=col)
        c.append(
            Module.ActionGroup(title))
        #c.append(Module.Context('已被浏览' + str(db['build.viewtime'][name]) + '次'))
        c.append(Module.Section('| 面具'))
        c.append(Module.Section({"type":"kmarkdown","content":mask}))
        c.append(Module.Section('| 背包'))
        c.append(Module.Section({"type":"kmarkdown","content":knapsack}))
        c.append(Module.Section('| 背心'))
        c.append(Module.Section({"type":"kmarkdown","content":vest}))
        c.append(Module.Section('| 手套'))
        c.append(Module.Section({"type":"kmarkdown","content":gloves}))
        c.append(Module.Section('| 枪套'))
        c.append(Module.Section({"type":"kmarkdown","content":holster}))
        c.append(Module.Section('| 护膝'))
        c.append(Module.Section({"type":"kmarkdown","content":kneecap}))
        c.append(Module.Section('| 武器'))
        c.append(Module.Section({"type":"kmarkdown","content":weapon}))
        cm = CardMessage(c)
        return cm
