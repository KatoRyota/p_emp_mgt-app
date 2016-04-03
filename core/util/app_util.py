# -*- coding: utf-8 -*-

# 説明 {{{
'''
  p_emp_mgt-app (社員管理アプリ)共通の関数定義
'''
# }}}

# 標準モジュールのインポート {{{
import sys
import os
import json
import logging
import ConfigParser
import re
import pprint
# }}}

# サードパーティーモジュールのインポート {{{
# }}}

# 独自モジュールのインポート {{{
from app_const import View, Message, Session, Form, Path, EndPoint
# }}}

# 前処理 {{{
# }}}

class CommonUtil(object):
    logger = logging.getLogger('logExample') # ロガー

    @classmethod
    def get_json_for_sqlalchemy(cls, obj_list):
        '''
        SQLAlchemyのレスポンスオブジェクトをJSONに変換して返す
        '''
        try:
            result = []
            if (isinstance(obj_list, list)):
                # 複数オブジェクトの場合
                # オブジェクトリスト分ループして、オブジェクト毎に処理
                for i, obj in enumerate(obj_list):
                    column_obj = {}
                    for column in obj._sa_class_manager.mapper.mapped_table.columns:
                        column_obj[column.name] = getattr(obj, column.name)
                    result.append(column_obj)
            else:
                # 単一オブジェクトの場合
                obj = obj_list
                column_obj = {}
                for column in obj._sa_class_manager.mapper.mapped_table.columns:
                    column_obj[column.name] = getattr(obj, column.name)
                result.append(column_obj)

            return json.dumps(result, ensure_ascii=False, indent=4)
        except Exception as e:
            logger.error(e)
            raise

    @classmethod
    def pp(cls, obj):
        '''
        日本語が含まれてるオブジェクトをユニコードエラーが発生しない形に変換して出力する
        '''
        try:
            pp = pprint.PrettyPrinter(indent=4, width=160)
            obj_str = pp.pformat(obj)
            return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), obj_str)
        except Exception as e:
            logger.error(e)
            raise

    @classmethod
    def get_conf(cls):
        '''
        設定ファイルをパースしてオブジェクトにマッピングして返す
        '''
        try:
            # 設定ファイル
            conf = ConfigParser.SafeConfigParser()
            conf.read(Path.APP_ROOT_DIR + 'core/configuration/app_conf.conf')
            return conf
        except Exception as e:
            logger.error(e)
            raise


# 後処理 {{{
# }}}
