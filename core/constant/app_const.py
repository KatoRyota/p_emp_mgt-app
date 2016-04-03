# -*- coding: utf-8 -*-

# 説明 {{{
'''
  p_emp_mgt-app (社員管理アプリ)用の定数モジュール
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

class Message(object):
    SUCCESS_001 = {'code' : 'SUCCESS_001', 'message' : u'正常終了'}
    ERROR_001   = {'code' : 'ERROR_001',   'message' : u'アクセストークン不正'}
    ERROR_002   = {'code' : 'ERROR_002',   'message' : u'認証エラー'}
    ERROR_003   = {'code' : 'ERROR_003',   'message' : u'KVSへのデータ登録時に異常発生'}
    ERROR_004   = {'code' : 'ERROR_004',   'message' : u'ユーザー認証キーが存在しません。'}
    ERROR_005   = {'code' : 'ERROR_005',   'message' : u'システムエラー'}
    WARN_001    = {'code' : 'WARN_001',    'message' : u'警告'}


class View(object):
    SYSTEM_ERROR = 'system_error.html'
    INDEX = 'index.html' # 社員一覧画面
    LOGIN = 'login.html' # ログイン画面


class Session(object):
    USER_AUTH_KEY = 'user_auth_key' # ユーザー認証キー

class Form(object):
    USER_NAME = {'name' : 'user_name', 'err_msg' : u'ユーザー名が不正です。'}
    PASSWORD  = {'name' : 'password', 'err_msg' : u'パスワードが不正です。'}


class Path(object):
    APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../..'
    CONF_DIR     = APP_ROOT_DIR + 'core/configuration'


class EndPoint(object):
    LOGIN  = {'uri' : '/p_emp_mgt-app/login',  'methods' : ['GET']}
    LOGOUT = {'uri' : '/p_emp_mgt-app/logout', 'methods' : ['GET']}
    INDEX  = {'uri' : '/p_emp_mgt-app/index',  'methods' : ['GET']}

class Logging(object):
    CONF_FILE      = 'logging.conf'
    LOGGER_EXAMPLE = 'logExample'

# 後処理 {{{
# }}}
