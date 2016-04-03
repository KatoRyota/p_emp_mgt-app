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
import ConfigParser
# }}}

# サードパーティーモジュールのインポート {{{
from sqlalchemy import create_engine, Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, relation, sessionmaker
# }}}

# 独自モジュールのインポート {{{
from app_util import CommonUtil
# }}}

# 前処理 {{{
Base = declarative_base()
# }}}




#---------------------------------------------------------------------
# TODO : このモジュールは使用しないようにしたい。
#        それぞれのクラスを分割して別ファイルに切り出したい。
#---------------------------------------------------------------------




class BaseEntity(object):
    '''
      エンティティクラス共通の親クラス
    '''
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        items = [
                  '{key}={value}'.format(key=key, value=value)
                  for key, value in self.__dict__.items() if not key.startswith('_')
                ]

        return '<{cls_name}: {attrs}>'.format(cls_name=self.__class__.__name__, attrs=', '.join(items),)


class EmployeeEntity(Base, BaseEntity):
    '''
     社員エンティティクラス
    '''
    __tablename__ = 'employees' # テーブル名
    employee_id = Column(String(255), nullable=False) # 社員ID
    password = Column(String(255), nullable=False) # ログインパスワード
    employee_name = Column(String(255), nullable=False) # 社員名 (氏名)
    affiliation_groups = Column(String(255)) # 所属グループ
    managerial_positions = Column(String(255)) # 役職
    mail_addresses = Column(String(255)) # メールアドレス
    skills = Column(String(255)) # スキルセット
    sales_employees = Column(String(255)) # 担当営業


class Employee(object):
    '''
      ユーザー (社員) ドメインクラス
    '''
    def __init__(self, employee_id, password, employee_name, affiliation_groups, managerial_position,
                 mail_address, id_=None):
        self.id = id_
        self.employee_id = user_id
        self.password = password
        self.employee_name = employee_name
        self.affiliation_groups = affiliation_groups
        self.managerial_positions = managerial_positions
        self.mail_addresses = mail_addresses


class EmployeeMapper(object):
    '''
      EmployeeオブジェクトとEmployeeEntityオブジェクトをマッピングするマッパークラス
    '''
    # ロガー
    logger = logging.getLogger('logExample')

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
    def delete(cls, user):
        session = cls.get_session()
        emp_from_db = session.query(UserRecord).filter_by(id=user.id).first()
        session.delete(emp_from_db)

# 後処理 {{{
# }}}
