# -*- coding: utf-8 -*-

# 説明 {{{
'''
  DBのデータを格納するモジュール

'''
# }}}

# 標準モジュールのインポート {{{
import sys
import os
import json
import logging
# }}}

# サードパーティーモジュールのインポート {{{
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
# }}}

# 独自モジュールのインポート {{{
# }}}

# 前処理 {{{
Base = declarative_base()
# }}}


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


# 後処理 {{{
# }}}

