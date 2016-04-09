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

from core.configuration.app_conf   import Dev, Stg, Prod
from core.constant.app_const       import View, Message, Session, Form, Path, EndPoint, Logging
from core.util.app_util            import CommonUtil
from persistence.entity.app_entity import Base
# }}}

# 前処理 {{{
try:
    logging.config.fileConfig(Logging.CONF_FILE) # ロギングライブラリ読込
    logger = logging.getLogger(Logging.LOGGER_EXAMPLE) # ロガー
    conf = Dev
except Exception as e:
    print(repr(e))
    exit()
# }}}

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
