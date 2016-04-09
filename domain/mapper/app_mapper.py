# -*- coding: utf-8 -*-

# 説明 {{{
'''
'''
# }}}

# 標準モジュールのインポート {{{
import sys
import os
import json
import logging
# }}}

# サードパーティーモジュールのインポート {{{
# }}}

# 独自モジュールのインポート {{{
from core.constant.app_const       import View, Message, Session, Form, Path, EndPoint, Logging
from core.util.app_util            import CommonUtil
from service.app_service           import app
from model.app_model               import Employee
from persistence.entity.app_entity import EmployeeEntity
# }}}

# 前処理 {{{
# }}}


class EmployeeMapper(object):
    '''
      EmployeeオブジェクトとEmployeeEntityオブジェクトをマッピングするマッパークラス
    '''
    logger = logging.getLogger(Logging.LOGGER_EXAMPLE) # ロガー

    @classmethod
    def select(cls, session, **kwargs):
        cls.logger.info('EmployeeMapper.select()開始')
        emp_list_from_db = session.query(EmployeeEntity).filter_by(**kwargs).all()

        #logger.debug(u'DBから取得したデータ : %s' % CommonUtil.get_json_for_sqlalchemy(emp_list_from_db))
        logger.debug(u'DBから取得したデータ : %s' % ", ".join([repr(x) for x in emp_list_from_db]))

        emp_list = []
        for emp_from_db in emp_list_from_db:
            emp_list.append(
                Employee(
                    emp_from_db.id,
                    emp_from_db.employee_id,
                    emp_from_db.password,
                    emp_from_db.employee_name,
                    emp_from_db.affiliation_groups,
                    emp_from_db.managerial_positions,
                    emp_from_db.mail_addresses,
                    emp_from_db.skills,
                    emp_from_db.sales_employees
                )
            )
        return emp_list

    @classmethod
    def insert(cls, user):
        session = cls.get_session()
        addresses = [
            AddressRecord(address=address)
            for address in user.addresses
        ]
        emp_from_db = UserRecord(
            name=user.name,
            age=user.age,
            addresses=addresses,
        )
        session.add(emp_from_db)
        return emp_from_db.id


    @classmethod
    def delete(cls, user):
        session = cls.get_session()
        emp_from_db = session.query(UserRecord).filter_by(id=user.id).first()
        session.delete(emp_from_db)

# 後処理 {{{
# }}}


