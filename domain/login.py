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
from p_emp_mgt_app.core.constant.app_const  import View, Message, Session, Form, Path, EndPoint, Logging
from p_emp_mgt_app.core.util.app_util       import CommonUtil
from p_emp_mgt_app.domain.base_domain       import BaseDomain
from p_emp_mgt_app.domain.mapper.app_mapper import EmployeeMapper
# }}}

# 前処理 {{{
# }}}


class Login(BaseDomain):
    '''
      ログイン処理を行うクラス
    '''
    def __init__(self):
        super(Login, self).__init__()

    def _login(self, request):
        pass

    def _validate(self, request):
        err_msg_list = []
        if not request.form[Form.USER_NAME['name']]:
            err_msg_list.append(Form.USER_NAME['err_msg'])

        if not request.form[Form.PASSWORD['name']]:
            err_msg_list.append(Form.PASSWORD['err_msg'])

        return err_msg_list

    def _select_emp_from_db(self, user_id, password):
        session = None
        try:
            # データベースの接続情報を取得。
            engine = create_engine(config.get('data_source', 'dsn'), echo=True, encoding='utf-8', convert_unicode=True)
            # セッションはスレッドローカルにする
            Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
            session = Session()
            self.logger.debug('user_id : %s, password : %s' % (user_id, password))
            emp_list_from_db = EmployeeMapper.select(session, user_id=user_id, password=password)
            session.commit()
            return emp_list_from_db
        except Exception as e:
            self.logger.exception(e)
            session.rollback()
            raise
        finally:
            session.close()

    def execute(self, request):
        self.logger.info(u'ログイン機能の処理開始')
        try:
            if len(self._validate(request)) > 0:
                # 初期表示の場合はこのブロックに入る
                return render_template(View.LOGIN, data=None) # ログイン画面表示
            else:
                emp_list_from_db = self._select_emp_from_db(request.form[Form.USER_NAME['name']],
                                                              request.form[Form.PASSWORD['name']])
                # レコード数チェック
                if len(emp_list_from_db) == 1:
                    # 単一の社員情報が取得できた場合は正常系
                    # セッションに社員情報をセット
                    self._login()
                    return redirect(url_for('index')) # 社員一覧画面へリダイレクト
                else:
                    # 複数の社員情報が取得できた場合は異常系
                    return render_template(View.LOGIN, data=None) # ログイン画面表示
        except Exception as e:
            self.logger.exception(e)
            return render_template(View.SYSTEM_ERROR, data=None) # システムエラー画面表示


# 後処理 {{{
# }}}
