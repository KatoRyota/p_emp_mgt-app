# -*- coding: utf-8 -*-

# 説明 {{{
'''
  app_service.pyからリクエストを受け取ってメイン処理を行います。
'''
# }}}

# 標準モジュールのインポート {{{
import sys
import os
import json
import logging
# }}}

# サードパーティーモジュールのインポート {{{
from flask          import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from sqlalchemy     import create_engine
from sqlalchemy.orm import scoped_session, relation, sessionmaker
# }}}

# 独自モジュールのインポート {{{
from app_const       import View, Message, Session, Form, Path, EndPoint
from app_util        import CommonUtil
from app_persistence import Employee, EmployeeMapper



from p_emp_mgt_app.core.constant.app_const  import View, Message, Session, Form, Path, EndPoint, Logging
from p_emp_mgt_app.core.util.app_util       import CommonUtil
from p_emp_mgt_app.domain.base_domain       import BaseDomain
# }}}

# 前処理 {{{
# }}}


class Logout(BaseDomain):
    '''
      ログアウト処理を行うクラス
    '''
    def __init__(self):
        super(Logout, self).__init__()

    def _logout():
        # セッション削除 (ユーザー認証キーも削除される)
        session.clear()
        flash('You were logged out')

    def execute(self, request):
        self.logger.info(u'ログアウト機能の処理開始')
        try:
            self._logout() # ログアウト
            return render_template(View.LOGIN, data=None) # ログイン画面表示
        except Exception as e:
            logger.exception(e)
            return render_template(View.SYSTEM_ERROR, data=None) # システムエラー画面表示


# 後処理 {{{
# }}}


