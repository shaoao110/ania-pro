from db.sqlMapper import SqlMapper
import logging
logger = logging.getLogger()

class Binduser():

    sqlMapper = SqlMapper()

    def bind(self,userid,name) -> str:
        sqlMapper = SqlMapper()

        try:
            # 获取用户td2信息
            userinfo = sqlMapper.getTd2UserByUserId(userid)
        except Exception as e:
            logger.error(e)
            return '用户td2信息获取异常，请联系管理员！'

        try:
            td2name = ''
            if('td2name' in userinfo):
              td2name = userinfo['td2name']
            logger.info("Old Data : " + str(td2name))

            td2name = name
            logger.info("New Data : " + str(td2name))

            sqlMapper.updateTd2nameByUserId(userid,name)
            return '绑定成功！您的全境封锁2游戏ID为: <' + name + '> ！'
        except Exception as e:
            logger.error(e)
            return '用户信息保存异常，请联系管理员！'