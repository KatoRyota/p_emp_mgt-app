# -*- coding: utf-8 -*-

# 説明 {{{
'''
  アプリケーションのルートディレクトリで以下のコマンドを実行するとテーブルが作成されます。

    python persistence/app_persistence.py
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
from persistence.entity.app_entity import EmployeeEntity
from model.app_model               import Employee
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
        logger.info('EmployeeMapper.select()開始')
        emp_list_from_db = session.query(EmployeeEntity).filter_by(**kwargs).all()

        #logger.debug(u'DBから取得したデータ : %s' % CommonUtil.get_json_for_sqlalchemy(emp_list_from_db))
        logger.debug(u'DBから取得したデータ : %s' % ", ".join([repr(x) for x in emp_list_from_db]))

        emp_list = []
        for emp_from_db in emp_list_from_db:
            emp_list.append(
                Employee(
                    id_=emp_from_db.id,
                    employee_id=emp_from_db.employee_id,
                    password=emp_from_db.password,
                    employee_name=emp_from_db.employee_name,
                    affiliation_groups=emp_from_db.affiliation_groups,
                    managerial_positions=emp_from_db.managerial_positions,
                    mail_addresses=emp_from_db.mail_addresses,
                    skills=emp_from_db.skills,
                    sales_employees=emp_from_db.sales_employees
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


