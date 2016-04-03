# -*- coding: utf-8 -*-

# 説明 {{{
'''
  モデル用のモジュール
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


class Employee(object):
    '''
      社員情報モデル
    '''
    def __init__(self, id_=None, employee_id, password, employee_name, affiliation_groups, managerial_positions,
                 mail_addresses, skills, sales_employees):

        self.id                   = id_
        self.employee_id          = employee_id
        self.password             = password
        self.employee_name        = employee_name
        self.affiliation_groups   = affiliation_groups
        self.managerial_positions = managerial_positions
        self.mail_addresses       = mail_addresses
        self.skills               = skills
        self.sales_employees      = sales_employees

# 後処理 {{{
# }}}

