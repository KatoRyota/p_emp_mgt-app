# -*- coding: utf-8 -*-

# 説明 {{{
'''
  アプリケーションのルートディレクトリで以下のコマンドを実行するとテーブルが作成されます。
  カレントディレクトリにsqliteのファイルが作成されます。

    cd ${アプリのルートディレクトリ}
    python tool/table_create.py
'''
# }}}

# 標準モジュールのインポート {{{
import sys
import os
import json
import logging
import logging.config
# }}}

# サードパーティーモジュールのインポート {{{
from sqlalchemy import create_engine
# }}}

# 独自モジュールのインポート {{{
APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..'
sys.path.append(APP_ROOT_DIR)
#sys.path.append(APP_ROOT_DIR + '/core')
#sys.path.append(APP_ROOT_DIR + '/domain')
#sys.path.append(APP_ROOT_DIR + '/model')
#sys.path.append(APP_ROOT_DIR + '/persistence')
#sys.path.append(APP_ROOT_DIR + '/service')

from p_emp_mgt_app.core.configuration.app_conf   import Dev, Stg, Prod
from p_emp_mgt_app.core.constant.app_const       import View, Message, Session, Form, Path, EndPoint, Logging
from p_emp_mgt_app.core.util.app_util            import CommonUtil
from p_emp_mgt_app.persistence.entity.app_entity import Base
# }}}

# 前処理 {{{
try:
    conf = Dev

    logging.config.fileConfig(Logging.CONF_FILE) # ロギングライブラリ読込
    logger = logging.getLogger(Logging.LOGGER_EXAMPLE) # ロガー
except Exception as e:
    logger.exception(e)
    exit()
# }}}


#--------------------------------------------------------------------------------
# TODO : 本スクリプトを実行してテーブル作成してみる。きっと、もう動くはず。
#--------------------------------------------------------------------------------

try:
    # データベースとのコネクションを取得
    engine = create_engine(conf.DATA_SOURCE_DSN, echo=conf.DB_ECHO, encoding=conf.DB_ENCODING,
                           convert_unicode=conf.DB_CONVERT_UNICODE)
    # データベース, テーブル作成
    Base.metadata.create_all(bind=engine, checkfirst=False)
except Exception as e:
    logger.exception(e)
    exit()

# 後処理 {{{
# }}}
