# -*- coding: utf-8 -*-

# 説明 {{{
'''
  p_emp_mgt_app (社員管理アプリ)へのリクエストを制御して、domain配下のソースコードに処理を委譲し、
  処理結果をリクエスト元に返します。
'''
# }}}

# 標準モジュールのインポート {{{
import sys
import os
import json
import logging
import logging.config
import optparse
# }}}

# サードパーティーモジュールのインポート {{{
from flask  import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from jinja2 import FileSystemLoader
# }}}

# 独自モジュールのインポート {{{
APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..'
sys.path.append(APP_ROOT_DIR)

from core.constant.app_const import View, Message, Session, Form, Path, EndPoint, Logging
from core.util.app_util      import CommonUtil
from domain.employee_index   import EmployeeIndex
# }}}

# 前処理 {{{
try:
    logging.config.fileConfig(Logging.CONF_FILE) # ロギングライブラリ読込
    logger = logging.getLogger(Logging.LOGGER_EXAMPLE) # ロガー

    # 起動パラメータのパーサー生成
    parser = optparse.OptionParser()
    parser.add_option("-t", "--host", dest="host", help=u"ホスト名を指定して下さい。 ", metavar="HOST", type="string")
    parser.add_option("-p", "--port", dest="port", help=u"ポート番号を指定して下さい。", metavar="PORT", type="int")
    parser.add_option("--debug", dest="debug", help=u"サーバーがデバッグモードで起動します。", action="store_true",
                      default=False)

    # 起動パラメータのパース
    (options, args) = parser.parse_args()

    logger.info(options.host)

    # 起動パラメータ入力チェック
    if options.host is None or not options.host:
        parser.error(u"ホスト名が不正です。")
        parser.print_help()
        exit()

    if options.port is None or not options.port:
        parser.error(u"ポート番号が不正です。")
        parser.print_help()
        exit()

    if options.debug is None or not options.debug:
        logger.info(u"debug mode : no")
    else:
        logger.info(u"debug mode : yes")

    if len(args) != 0:
        parser.error(u"引数は指定できません。")
        parser.print_help()
        exit()

    # アプリケーションのインスタンス
    app = Flask(__name__)
    # 設定ファイルをロード
    app.config.from_object('p_emp_mgt_app.core.configuration.app_conf.Dev')
    # テンプレートの読込みパスを変更
    app.jinja_loader = FileSystemLoader(APP_ROOT_DIR + '/templates')
    # セッション管理用のシークレットキー
    app.secret_key = app.config['SECRET_KEY']
except Exception as e:
    logger.exception(e)
    exit()
# }}}

def auth(func):
    '''
      認証処理
    '''
    def _auth(*args, **kwargs):
        if 'user_auth_key' in session:
            return func(*args, **kwargs) # セッションにユーザー認証キーが存在する場合は正常系処理を実行
        else:
            # それ以外はログイン画面にリダイレクト
            return redirect(url_for('login'))
    return _auth


@app.route(EndPoint.LOGIN['uri'], methods=EndPoint.LOGIN['methods'])
def login():
    '''
      ログイン画面表示
    '''
    return Login().execute(request)


@app.route(EndPoint.LOGOUT['uri'], methods=EndPoint.LOGOUT['methods'])
def logout():
    '''
      ログアウト画面表示
    '''
    return Logout().execute(request)


@app.route(EndPoint.INDEX['uri'], methods=EndPoint.INDEX['methods'])
#@auth
def index():
    '''
      社員一覧表示
    '''
    return EmployeeIndex().execute(request)


# 後処理 {{{
if __name__ == '__main__':
    app.run(host=options.host, port=options.port, debug=options.debug)
# }}}
