# -*- coding: utf-8 -*-

# 説明 {{{
'''
  p_emp_mgt_app (社員管理アプリ)用の設定モジュール
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
# }}}

# 前処理 {{{
# }}}


class Dev(object):
    DATA_SOURCE_DSN    = 'sqlite:///employee.sqlite3.db'
    SECRET_KEY         = '\x00\x98\xea!\xdb\xbc\x1dp\xe4\x81)\xfeT\xccf\xca\r\x8f\x87$Y\x8aG\xbd'
    DB_ENCODING        = 'utf-8'
    DB_ECHO            = True
    DB_CONVERT_UNICODE = True


class Stg(object):
    DATA_SOURCE_DSN    = 'sqlite:///employee.sqlite3.db'
    SECRET_KEY         = '\x00\x98\xea!\xdb\xbc\x1dp\xe4\x81)\xfeT\xccf\xca\r\x8f\x87$Y\x8aG\xbd'
    DB_ENCODING        = 'utf-8'
    DB_ECHO            = True
    DB_CONVERT_UNICODE = True


class Prod(object):
    DATA_SOURCE_DSN    = 'sqlite:///employee.sqlite3.db'
    SECRET_KEY         = '\x00\x98\xea!\xdb\xbc\x1dp\xe4\x81)\xfeT\xccf\xca\r\x8f\x87$Y\x8aG\xbd'
    DB_ENCODING        = 'utf-8'
    DB_ECHO            = True
    DB_CONVERT_UNICODE = True


# 後処理 {{{
# }}}
