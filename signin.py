from khl import Bot
from datetime import timedelta, datetime
from db.sqlMapper import SqlMapper
import logging
logger = logging.getLogger()

class Signin():

    # 指定key作为计数key
    def sign(self, userid,bot:Bot) -> str:
        sqlMapper = SqlMapper()

        # 获取当前时间日期
        now = (datetime.now())
        ti = now.strftime("%Y-%m-%d")
        tii = now.strftime('%Y-%m-%d %H:%M:%S')
        signinfo = {}
      
        try:
            # 获取用户签到信息
            signinfo = sqlMapper.getSigninByUserId(userid)
        except Exception as e:
            logger.error(e)
            return '`用户信息获取异常，请联系管理员！`'

        try:
            logger.info("Old Data : " + str(signinfo))
            # 获取上次签到时间
            last = signinfo['record']
            lasttime = signinfo['record'].split(' ')[0]
            tempstr = ''
            # 第一次签到
            if signinfo['total'] == 0:
              signinfo['total'] = 1
              signinfo['consecutive'] = 1
              signinfo['record'] = tii
              # 更新数据库
              sqlMapper.updateSigninByUserId(signinfo)
              logger.info("New Data : " + str(signinfo))
              return '`签到成功！已累计签到1天，连续签到1天，感谢您首次在本频道签到！`' + "|1|1|0"
            # 如果上次签到是今天
            if ti == lasttime:
                logger.info("Data No Change")
                tempstr = '|' + str(signinfo['total']) + '|' + str(signinfo['consecutive']) + '|' + str(signinfo['prop'])
                return '`今天您已签到！已累计签到' + str(
                    signinfo['total']) + '天，连续签到' + str(
                        signinfo['consecutive']) + '天，上次签到时间：' + last + '，免断签卡剩余' + str(signinfo['prop']) + '张`' + tempstr
            # 如果上次签到是昨天
            elif (datetime.now() + timedelta(days=-1)).strftime("%Y-%m-%d") == lasttime:
                signinfo['total'] += 1
                signinfo['consecutive'] += 1
                tempstr = '|' + str(signinfo['total']) + '|' + str(signinfo['consecutive']) + '|' + str(signinfo['prop'])
            # 否则是断签
            else:
                if signinfo['prop'] == 0:
                    signinfo['total'] += 1
                    signinfo['consecutive'] = 1
                    tempstr = '|' + str(signinfo['total']) + '|1|0'
                else :
                    signinfo['total'] += 2
                    signinfo['consecutive'] += 2
                    signinfo['prop'] -= 1
                    tempstr = '|' + str(signinfo['total']) + '|' + str(signinfo['consecutive']) + '|' + str(signinfo['prop'])
            signinfo['record'] = tii
            # 更新数据库
            sqlMapper.updateSigninByUserId(signinfo)
            logger.info("New Data : " + str(signinfo))
            return '`签到成功！已累计签到' + str(signinfo['total']) + '天，连续签到' + str(
                signinfo['consecutive']) + '天，上次签到时间：' + last + '，免断签卡剩余' + str(signinfo['prop']) + '张`' + tempstr
        except Exception as e:
            logger.error(e)
            return '`签到异常，请联系管理员！`'
