# -*- coding: utf-8 -*-

import sqlite3 as lite
from PyQt4 import QtCore, QtGui
import logging

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def objectsInit(self):
    self.logWindow = None
    self.qv_roleBox = 0
    self.gl_roleBox = 0
    self.au_wn_1 = 0
    self.au_wn_lim_ta = []
    self.au_wn_2 = 0
    self.au_wn_con_ta = []
    self.mm_pofc = 0
    self.mm_horlay_1 = []
    self.mm_verlay_1 = []
    self.mm_horlay_2 = []
    self.mm_line_1 = []
    self.mm_lab_1 = []
    self.mm_conName_ln = []
    self.mm_conEmail_1 = []
    self.mm_infBut_1 = []
    self.mm_lab_2 = []
    self.mm_conName_2 = []
    self.mm_conEmail_ln = []
    self.mm_infBut_2 = []
    self.tr_tpex = 0
    self.tr_horlay_1 = []
    self.tr_lab_1 = []
    self.tr_spIt_1 = []
    self.tr_dtSt_1 = []
    self.tr_spIt_2 = []
    self.tr_dtEd_1 = []
    self.tr_infBut_1 = []
    self.ro_roPy = 0
    self.ro_verlay_1 = []
    self.ro_line_1 = []
    self.ro_horlay_1 = []
    self.ro_lab_1 = []
    self.ro_rlPy_ln = []
    self.ro_infBut_1 = []
    self.ro_horlay_2 = []
    self.ro_lab_2 = []
    self.ro_rlEm_ln = []
    self.ro_infBut_2 = []
    self.ro_horlay_3 = []
    self.ro_lab_3 = []
    self.ro_rlRl_ln = []
    self.ro_infBut_3 = []
    self.cf_cfSp = 0
    self.cf_verlay_1 = []
    self.cf_line_1 = []
    self.cf_horlay_1 = []
    self.cf_lab_1 = []
    self.cf_spec_ln = []
    self.cf_infBut_1 = []
    self.cf_horlay_2 = []
    self.cf_lab_2 = []
    self.cf_dtPu_1 = []
    self.cf_infBut_2 = []
    self.cf_horlay_3 = []
    self.cf_lab_3 = []
    self.cf_dtTy_1 = []
    self.cf_infBut_3 = []
    self.cf_horlay_4 = []
    self.cf_lab_4 = []
    self.cf_dtDg_1 = []
    self.cf_infBut_4 = []
    self.kw_list_1 = []
    self.kw_cnVc = 0
    self.kw_lsLs_1 = []
    self.kw_verlay_1 = []
    self.kw_line_1 = []
    self.kw_verlay_2 = []
    self.kw_horlay_1 = []
    self.kw_lab_1 = []
    self.kw_nam_ln = []
    self.kw_infBut_1 = []
    self.kw_horlay_2 = []
    self.kw_lab_2 = []
    self.kw_dat_1 = []
    self.kw_infBut_2 = []
    self.kw_horlay_3 = []
    self.kw_lab_3 = []
    self.kw_tpRl_1 = []
    self.kw_infBut_3 = []
    self.kw_horlay_4 = []
    self.kw_lab_4 = []
    self.kw_frame_1 = []
    self.kw_lay_1 = []
    self.kw_horlay_5 = []
    self.kw_kwls_1 = []
    self.kw_verlay_3 = []
    self.kw_plsBut_1 = []
    self.kw_delBut_1 = []
    self.kw_infBut_4 = []
    self.ai_inst = 0
    self.ai_verlay_1 = []
    self.ai_line_1 = []
    self.ai_horlay_1 = []
    self.ai_verlay_2 = []
    self.ai_horlay_2 = []
    self.ai_lab_1 = []
    self.ai_inst_rl1 = []
    self.ai_lab_2 = []
    self.ai_lab_3 = []
    self.ai_inst_rl2 = []
    self.ai_horlay_3 = []
    self.ai_lab_4 = []
    self.ai_lab_5 = []
    self.ai_lab_6 = []
    self.ai_inst_rl3 = []
    self.ai_inst_rl4 = []
    self.ai_lab_7 = []
    self.ai_horlay_4 = []
    self.ai_lab_8 = []
    self.ai_inst_rb1 = []
    self.ai_inst_rb2 = []
    self.ai_inst_ln3 = []
    self.ai_inst_ln4 = []
    self.instDomain = []
    self.ai_frm_fr1 = []
    self.ai_wdgt_wg1 = []
    self.ai_horlay_5 = []
    self.all_new_del_plus_buttons = []
    self.all_new_inst_rl = []
    self.all_new_inst_rb = []
    self.fillInfo = False
    self.out_file_name = None
    self.saved = False
    self.modified = False


def sql_valueRead(self, table, column, value):
    cur = self.db.cursor()
    sql = 'SELECT * FROM ' + table + ' WHERE ' + column + '=?'
    query = cur.execute(sql, [(unicode(value))]).fetchall()
    return query
