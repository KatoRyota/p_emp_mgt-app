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
# }}}

# 独自モジュールのインポート {{{
from p_emp_mgt_app.core.constant.app_const import View, Message, Session, Form, Path, EndPoint, Logging
from p_emp_mgt_app.core.util.app_util      import CommonUtil
# }}}

# 前処理 {{{
# }}}


class BaseDomain(object):
    logger = logging.getLogger(Logging.LOGGER_EXAMPLE) # ロガー

    def __init__(self):
        pass


# 後処理 {{{
# }}}



