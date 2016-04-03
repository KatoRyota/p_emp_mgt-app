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
from core.constant.app_const  import View, Message, Session, Form, Path, EndPoint, Logging
from core.util.app_util       import CommonUtil
from domain.mapper.app_mapper import EmployeeMapper
# }}}

# 前処理 {{{
# }}}

class EmployeeIndex(object):
    '''
      社員一覧を表示するクラス
    '''
    logger = logging.getLogger(Logging.LOGGER_EXAMPLE) # ロガー

    def __init__(self):
        pass

    def _get_emp_list(request):
        session = None
        try:
            # データベースの接続情報を取得。
            #engine = create_engine(config.get('data_source', 'dsn'), echo=True, encoding='utf-8', convert_unicode=True)
            engine = create_engine(app.config['DATA_SOURCE_DSN'], echo=app.config['DB_ECHO'],
                                   encoding=app.config['DB_ENCODING'], convert_unicode=app.config['DB_CONVERT_UNICODE'])
            # セッションはスレッドローカルにする
            Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
            session = Session()
            emp_list = EmployeeMapper.select(session)
            session.commit()
            return emp_list
        except Exception as e:
            logger.error(e)
            session.rollback()
            raise
        finally:
            session.close()

    def execute(self, request):
        logger.info(u'社員一覧表示機能の処理開始')
        try:
            # 社員一覧情報を取得
            return render_template(View.INDEX, data=self._get_emp_list(request)) # 社員一覧画面表示
        except Exception as e:
            logger.error(e)
            return render_template(View.SYSTEM_ERROR, data=None) # システムエラー画面表示

# 後処理 {{{
# }}}


