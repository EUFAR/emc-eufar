# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


def objectsInit(self):
    self.logWindow = None
    self.gl_roleBox = 0
    self.ai_otherAircraft = 0
    self.au_wn_1 = 0
    self.au_wn_lim_ta = []
    self.au_horlay_1 = []
    self.au_delBut_1 = []
    self.au_wn_2 = 0
    self.au_wn_con_ta = []
    self.au_horlay_2 = []
    self.au_delBut_2 = []
    self.mm_pofc = 0
    self.mm_horlay_1 = []
    self.mm_verlay_1 = []
    self.mm_verlay_2 = []
    self.mm_horlay_2 = []
    self.mm_horlay_3 = []
    self.mm_line_1 = []
    self.mm_lab_1 = []
    self.mm_conName_ln = []
    self.mm_conEmail_1 = []
    self.mm_infBut_1 = []
    self.mm_lab_2 = []
    self.mm_conName_2 = []
    self.mm_conEmail_ln = []
    self.mm_infBut_2 = []
    self.mm_delBut = []
    self.tr_tpex = 0
    self.tr_horlay_1 = []
    self.tr_lab_1 = []
    self.tr_spIt_1 = []
    self.tr_dtSt_1 = []
    self.tr_spIt_2 = []
    self.tr_dtEd_1 = []
    self.tr_infBut_1 = []
    self.tr_delBut = []
    self.ro_roPy = 0
    self.ro_delBut = []
    self.ro_verlay_2 = []
    self.ro_grilay_1 = []
    self.ro_line_1 = []
    self.ro_lab_1 = []
    self.ro_rlPy_ln = []
    self.ro_infBut_1 = []
    self.ro_lab_2 = []
    self.ro_rlEm_ln = []
    self.ro_infBut_2 = []
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
    self.ai_inst = 0
    self.ai_horlay = []
    self.ai_delbut = []
    self.ai_lab_1 = []
    self.ai_lab_2 = []
    self.ai_lab_3 = []
    self.ai_lab_4 = []
    self.all_new_del_plus_buttons = []
    self.all_new_inst_rl = []
    self.all_new_inst_rb = []
    self.instrument_list = []
    self.instModel_list = []
    self.instManufacturer_list = []
    cur = self.db.cursor()
    query1 = cur.execute("SELECT Model FROM instrumentsInformations").fetchall()
    query2 = cur.execute("SELECT Manufacturer FROM instrumentsInformations").fetchall()
    for i in range(0,len(query1)):
        self.instrument_list.append(query2[i][0] + " - " + query1[i][0])
    self.instrument_list.sort()
    for i in range(0,len(self.instrument_list)):
        if i == 0:
            self.ai_instrument_rl1.addItem("Make a choice...")
            self.ai_instrument_rl1.addItem("Other...")
        self.ai_instrument_rl1.addItem(self.instrument_list[i])
    self.fillInfo = False
    self.out_file_name = None
    self.saved = False
    self.modified = False

def sql_valueRead(self, table, column, value):
    cur = self.db.cursor()
    sql = 'SELECT * FROM ' + table + ' WHERE ' + column + '=?'
    query = cur.execute(sql, [(value)]).fetchall()
    return query
