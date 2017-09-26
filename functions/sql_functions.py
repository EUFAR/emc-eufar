import logging
from operator import itemgetter

def objectsInit(self):
    logging.debug('sql_functions.py - objectsInit')
    self.logWindow = None
    self.fillInfo = False
    self.out_file_name = None
    self.saved = False
    self.modified = False
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
    self.qv_insitu = 0
    self.qv_insitu_verlay_1 = []
    self.qv_insitu_horlay_1 = []
    self.qv_insitu_horlay_5 = []
    self.qv_insitu_horlay_6 = []
    self.qv_insitu_horlay_7 = []
    self.qv_insitu_horlay_8 = []
    self.qv_insitu_horlay_9 = []
    self.qv_insitu_horlay_10 = []
    self.qv_insitu_horlay_11 = []
    self.qv_insitu_horlay_12 = []
    self.qv_insitu_horlay_13 = []
    self.qv_insitu_horlay_14 = []
    self.qv_insitu_gridlay_1 = []
    self.qv_insitu_gridlay_2 = []
    self.qv_insitu_gridlay_3 = []
    self.qv_insitu_lab_1 = []
    self.qv_insitu_lab_2 = []
    self.qv_insitu_lab_3 = []
    self.qv_insitu_lab_4 = []
    self.qv_insitu_lab_5 = []
    self.qv_insitu_lab_6 = []
    self.qv_insitu_lab_7 = []
    self.qv_insitu_lab_8 = []
    self.qv_insitu_lab_9 = []
    self.qv_insitu_lab_10 = []
    self.qv_insitu_infBut_1 = []
    self.qv_insitu_infBut_2 = []
    self.qv_insitu_infBut_3 = []
    self.qv_insitu_infBut_4 = []
    self.qv_insitu_infBut_5 = []
    self.qv_insitu_line_1 = []
    self.qv_insitu_line_2 = []
    self.qv_insitu_line_3 = []
    self.qv_insitu_line_4 = []
    self.qv_insitu_area_1 = []
    self.qv_insitu_area_2 = []
    self.qv_insitu_round_1 = []
    self.qv_insitu_round_2 = []
    self.qv_insitu_group_1 = []
    self.qv_insitu_check_1 = []
    self.qv_insitu_check_2 = []
    self.qv_insitu_check_3 = []
    self.qv_insitu_check_4 = []
    self.qv_insitu_list_1 = []
    self.qv_insitu_tab_1 = []
    self.qv_insitu_scroll_1 = []
    self.qv_insitu_scroll_2 = []
    self.qv_insitu_area_list = [[],[]]
    self.qv_insitu_line_list = [[],[],[],[]]
    self.qv_insitu_check_list = []
    self.qv_insitu_radio_list = [[]]
    self.qv_insitu_combo_list = [[],[]]
    self.qv_insitu_horlay_15 = []
    self.qv_insitu_lab_11 = []
    self.qv_insitu_list_2 = []
    self.qv_insitu_lab_12 = []
    self.qv_insitu_list_3 = []
    self.qv_insitu_contBut_1 = []
    self.qv_insitu_infBut_6 = []
    self.qv_imagery = 0
    self.qv_imagery_verlay_1 = []
    self.qv_imagery_horlay_1 = []
    self.qv_imagery_horlay_2 = []
    self.qv_imagery_horlay_3 = []
    self.qv_imagery_horlay_4 = []
    self.qv_imagery_horlay_5 = []
    self.qv_imagery_horlay_6 = []
    self.qv_imagery_horlay_7 = []
    self.qv_imagery_horlay_8 = []
    self.qv_imagery_horlay_9 = []
    self.qv_imagery_horlay_10 = []
    self.qv_imagery_horlay_11 = []
    self.qv_imagery_horlay_12 = []
    self.qv_imagery_horlay_13 = []
    self.qv_imagery_horlay_14 = []
    self.qv_imagery_horlay_15 = []
    self.qv_imagery_horlay_16 = []
    self.qv_imagery_horlay_17 = []
    self.qv_imagery_horlay_18 = []
    self.qv_imagery_horlay_19 = []
    self.qv_imagery_horlay_20 = []
    self.qv_imagery_horlay_21 = []
    self.qv_imagery_horlay_22 = []
    self.qv_imagery_horlay_23 = []
    self.qv_imagery_horlay_24 = []
    self.qv_imagery_horlay_25 = []
    self.qv_imagery_horlay_26 = []
    self.qv_imagery_horlay_27 = []
    self.qv_imagery_horlay_28 = []
    self.qv_imagery_horlay_29 = []
    self.qv_imagery_horlay_30 = []
    self.qv_imagery_horlay_31 = []
    self.qv_imagery_horlay_32 = []
    self.qv_imagery_horlay_33 = []
    self.qv_imagery_gridlay_1 = []
    self.qv_imagery_gridlay_2 = []
    self.qv_imagery_gridlay_3 = []
    self.qv_imagery_gridlay_4 = []
    self.qv_imagery_gridlay_5 = []
    self.qv_imagery_gridlay_6 = []
    self.qv_imagery_gridlay_7 = []
    self.qv_imagery_gridlay_8 = []
    self.qv_imagery_infBut_1 = []
    self.qv_imagery_infBut_2 = []
    self.qv_imagery_infBut_3 = []
    self.qv_imagery_infBut_4 = []
    self.qv_imagery_infBut_5 = []
    self.qv_imagery_infBut_6 = []
    self.qv_imagery_infBut_7 = []
    self.qv_imagery_infBut_8 = []
    self.qv_imagery_infBut_9 = []
    self.qv_imagery_infBut_10 = []
    self.qv_imagery_infBut_11 = []
    self.qv_imagery_infBut_12 = []
    self.qv_imagery_infBut_13 = []
    self.qv_imagery_infBut_14 = []
    self.qv_imagery_lab_1 = []
    self.qv_imagery_lab_2 = []
    self.qv_imagery_lab_3 = []
    self.qv_imagery_lab_4 = []
    self.qv_imagery_lab_5 = []
    self.qv_imagery_lab_6 = []
    self.qv_imagery_lab_7 = []
    self.qv_imagery_lab_8 = []
    self.qv_imagery_lab_9 = []
    self.qv_imagery_lab_10 = []
    self.qv_imagery_lab_11 = []
    self.qv_imagery_lab_12 = []
    self.qv_imagery_lab_13 = []
    self.qv_imagery_lab_14 = []
    self.qv_imagery_lab_15 = []
    self.qv_imagery_lab_16 = []
    self.qv_imagery_lab_17 = []
    self.qv_imagery_lab_18 = []
    self.qv_imagery_lab_19 = []
    self.qv_imagery_lab_20 = []
    self.qv_imagery_lab_21 = []
    self.qv_imagery_lab_22 = []
    self.qv_imagery_lab_23 = []
    self.qv_imagery_lab_24 = []
    self.qv_imagery_lab_25 = []
    self.qv_imagery_lab_26 = []
    self.qv_imagery_lab_27 = []
    self.qv_imagery_lab_28 = []
    self.qv_imagery_lab_29 = []
    self.qv_imagery_lab_30 = []
    self.qv_imagery_lab_31 = []
    self.qv_imagery_lab_32 = []
    self.qv_imagery_lab_33 = []
    self.qv_imagery_lab_34 = []
    self.qv_imagery_lab_35 = []
    self.qv_imagery_line_1 = []
    self.qv_imagery_line_2 = []
    self.qv_imagery_line_3 = []
    self.qv_imagery_line_4 = []
    self.qv_imagery_line_5 = []
    self.qv_imagery_line_6 = []
    self.qv_imagery_line_7 = []
    self.qv_imagery_date_1 = []
    self.qv_imagery_date_2 = []
    self.qv_imagery_list_1 = []
    self.qv_imagery_list_2 = []
    self.qv_imagery_check_1 = []
    self.qv_imagery_check_2 = []
    self.qv_imagery_check_3 = []
    self.qv_imagery_check_4 = []
    self.qv_imagery_check_5 = []
    self.qv_imagery_check_6 = []
    self.qv_imagery_check_7 = []
    self.qv_imagery_check_8 = []
    self.qv_imagery_check_9 = []
    self.qv_imagery_check_10 = []
    self.qv_imagery_check_11 = []
    self.qv_imagery_check_12 = []
    self.qv_imagery_check_13 = []
    self.qv_imagery_check_14 = []
    self.qv_imagery_check_15 = []
    self.qv_imagery_check_16 = []
    self.qv_imagery_check_17 = []
    self.qv_imagery_check_18 = []
    self.qv_imagery_check_19 = []
    self.qv_imagery_check_20 = []
    self.qv_imagery_check_21 = []
    self.qv_imagery_check_22 = []
    self.qv_imagery_check_23 = []
    self.qv_imagery_check_24 = []
    self.qv_imagery_check_25 = []
    self.qv_imagery_check_26 = []
    self.qv_imagery_check_27 = []
    self.qv_imagery_check_28 = []
    self.qv_imagery_check_29 = []
    self.qv_imagery_check_30 = []
    self.qv_imagery_check_31 = []
    self.qv_imagery_check_32 = []
    self.qv_imagery_group_1 = []
    self.qv_imagery_group_2 = []
    self.qv_imagery_group_3 = []
    self.qv_imagery_group_4 = []
    self.qv_imagery_group_5 = []
    self.qv_imagery_group_6 = []
    self.qv_imagery_group_7 = []
    self.qv_imagery_group_8 = []
    self.qv_imagery_group_9 = []
    self.qv_imagery_group_10 = []
    self.qv_imagery_group_11 = []
    self.qv_imagery_group_12 = []
    self.qv_imagery_group_13 = []
    self.qv_imagery_group_14 = []
    self.qv_imagery_group_15 = []
    self.qv_imagery_group_16 = []
    self.qv_imagery_tab_1 = []
    self.qv_imagery_scroll_1 = []
    self.qv_imagery_scroll_2 = []
    self.qv_imagery_horlay_34 = []
    self.qv_imagery_lab_36 = []
    self.qv_imagery_list_3 = []
    self.qv_imagery_lab_37 = []
    self.qv_imagery_list_4 = []
    self.qv_imagery_contBut_1 = []
    self.qv_imagery_infBut_15 = []
    self.qv_imagery_line_list = [[],[],[],[], [],[],[]]
    self.qv_imagery_combo_list = [[],[]]
    self.qv_imagery_date_list = [[],[]]
    self.qv_imagery_radio_list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.all_new_del_plus_buttons = []
    self.all_new_inst_rl = []
    self.all_new_inst_rb = []
    self.instrument_list = []
    self.instModel_list = []
    self.instManufacturer_list = []
    self.ai_acft = 0
    self.ai_horlay_2 = []
    self.ai_delbut_2 = []
    self.ai_lab_5 = []
    self.ai_lab_6 = []
    self.ai_lab_7 = []
    self.ai_lab_8 = []
    self.ai_lab_9 = []
    self.ai_lab_10 = []
    self.aircraft_list = []
    
    self.mandatory_line_edit_list = [
        [self.id_resourceTitle_ln, self.id_resourceTitle_lb, "text", 0],
        [self.id_resourceIdent_ln, self.id_resourceIdent_lb, "text", 0],
        [self.id_resourceLocator_ln, self.id_resourceLocator_lb, "text", 0],
        [self.ai_airManufacturer_ln, self.ai_manufacturer_lb, "text", 3],
        [self.ai_airType_ln, self.ai_type_lb, "text", 3],
        [self.ai_airOperator_ln, self.ai_operator_lb, "text", 3],
        [self.ai_airNumber_ln, self.ai_number_lb, "text", 3],
        [self.ai_insName_ln, self.ai_newname_lb, "text", 3],
        [self.ai_insManufacturer_ln, self.ai_newmanufacturer_lb, "text", 3],
        [self.gl_northBound_ln, self.gl_boundingBox_lb, "float", 4],
        [self.gl_westBound_ln, self.gl_boundingBox_lb, "float", 4],
        [self.gl_eastBound_ln, self.gl_boundingBox_lb, "float", 4],
        [self.gl_southBound_ln, self.gl_boundingBox_lb, "float", 4],
        [self.ro_responsibleParty_ln, self.ro_responsibleParty_lb, "text", 8],
        [self.ro_responsibleEmail_ln, self.ro_responsibleEmail_lb, "email", 8],
        [self.mm_contactEmail_ln, self.mm_contactEmail_lb, "email", 9],
        [self.mm_contactName_ln, self.mm_contactName_lb, "text", 9]
        ]
    
    self.mandatory_area_edit_list = [
        [self.id_resourceAbstract_ta, self.id_resourceAbstract_lb, "text", 0],
        [self.au_conditions_ta, self.au_conditions_lb, "text", 7],
        [self.au_limitations_ta, self.au_limitations_lb, "text", 7],
        ]    
        
    self.mandatory_combobox_list = [
        [self.id_resourceType_rl1, self.id_resourceType_lb, 0],
        [self.id_resourceLang_rl2, self.id_resourceLang_lb, 0],
        [self.ai_aircraft_rl1, self.ai_aircraft_lb, 3],
        [self.ai_country_rl, self.ai_country_lb, 3],
        [self.ai_instrument_rl1, self.ai_instrument_lb, 3],
        [self.gl_category_rl1, self.gl_location_lb, 4],
        [self.gl_details_rl2, self.gl_location_lb, 4],
        [self.gl_unit_rl, self.gl_unit_lb, 4],
        [self.ro_responsibleRole_rl1, self.ro_responsibleRole_lb, 8],
        [self.mm_language_rl1, self.mm_language_lb, 9]
        ]
        
    self.mandatory_datebox_list = [
        [self.tr_dateRevision_do2, self.tr_dateRevision_lb, 5],
        [self.tr_dateCreation_do3, self.tr_dateCreation_lb, 5],
        [self.tr_dateStart_do4, self.tr_period_lb, 5],
        [self.tr_dateEnd_do5, self.tr_period_lb, 5],
        [self.mm_date_do1, self.mm_date_lb, 9]
        ]
    
    self.new_operators_aircraft = [
        ['AWI','Basler Turbo Conversions, BT-67','C-GAWI','DE','AWI_Polar5.jpg'],
        ['CNR-ISAFoM','3I / Magnaghi Aeronautica, Sky Arrow 650 TCNS','I-AMMO','IT','ISAFOM_SkyArrow.jpg'],
        ['CNR-IMAA','Partenavia / Vulcanair, P-68 Observer 2','I-OBPC','IT','IMMA_Partenavia.jpg'],
        ['CzechGlobe','Cessna Aircraft Company, C-208 B Grand Caravan','OK-CZG','CZ','CzechGlobe_C208.jpg'],
        ['DLR','Cessna Aircraft Company, C-208 B Grand Caravan','D-FDLR','DE','DLR_C208.jpg'],
        ['DLR','Dassault Aviation, Mystere / Falcon 20 E-5','D-CMET','DE','DLR_Falcon_20.jpg'],
        ['DLR','Dornier Flugzeugwerke, Do 228 - 212','D-CFFU','DE','DLR_Dornier_Do228_D-CFFU.jpg'],
        ['DLR','Dornier Flugzeugwerke, Do 228 - 101','D-CODE','DE','DLR_Dornier_Do228_D-CODE.jpg'],
        ['Enviscope','Learjet / Bombardier Aerospace, 35A','D-CGFD','DE','ENVISCOPE_Learjet_35A.jpg'],
        ['Enviscope','Partenavia / Vulcanair, P-68B','D-GERY','DE','ENVISCOPE_Partenavia.jpg'],
        ['FAAM','BAE Systems, BAe146-301','G-LUXE','GB','FAAM_BAe146.jpg'],
        ['FUB','Cessna Aircraft Company, T207A Turbo Skywagon','D-EAFU','DE','FUB_C_207.jpg'],
        ['INTA','Construcciones Aeronauticas S.A, C-212-200','EC-DTV','ES','CASA_212_AR.jpg'],
        ['INTA','Construcciones Aeronauticas S.A, C-212-200','EC-DUQ','ES','CASA_212_RS.jpg'],
        ['KIT, IMK-IFU','Ultraleichtflug Schmidtler, Enduro','D-MIFU','DE','KIT_ENDURO.jpg'],
        ['NERC','De Havilland Canada, DHC-6 Twin Otter','VP-FAZ','GB','NERC_Twin_Otter_VP-FAZ.jpg'],
        ['NERC','De Havilland Canada, DHC-6 Twin Otter','VP-FBL','GB','NERC_Twin_Otter_VP-FBL.jpg'],
        ['SAFIRE','ATR, ATR42-320','F-HMTO','FR','SAFIRE_ATR42.jpg'],
        ['SAFIRE','Dassault Aviation, Mystere / Falcon 20 GF','F-GBTM','FR','SAFIRE_PIPER_AZTEC.jpg'],
        ['SAFIRE','Piper Aircraft, PA23-250 Aztec','F-BLEB','FR','SAFIRE_FA20.jpg'],
        ['UEDIN','Diamond Aircraft, HK36 TTC ECO Dimona','G-GEOS','GB','UEDIN_HK36.jpg']
        ]
    self.new_operators_aircraft = sorted(self.new_operators_aircraft, key=itemgetter(0,1))
    
    self.new_country_code = {
        'Afghanistan':'AF',
        'Aland Islands':'AX',
        'Albania':'AL',
        'Algeria':'DZ',
        'American Samoa':'AS',
        'Andorra':'AD',
        'Angola':'AO',
        'Anguilla':'AI',
        'Antarctica':'AQ',
        'Antigua And Barbuda':'AG',
        'Argentina':'AR',
        'Armenia':'AM',
        'Aruba':'AW',
        'Australia':'AU',
        'Austria':'AT',
        'Azerbaijan':'AZ',
        'Bahamas':'BS',
        'Bahrain':'BH',
        'Bangladesh':'BD',
        'Barbados':'BB',
        'Belarus':'BY',
        'Belgium':'BE',
        'Belize':'BZ',
        'Benin':'BJ',
        'Bermuda':'BM',
        'Bhutan':'BT',
        'Bolivia':'BO',
        'Bonaire':'BQ',
        'Bosnia And Herzegovina':'BA',
        'Botswana':'BW',
        'Bouvet Island':'BV',
        'Brazil':'BR',
        'British Indian Ocean Territory':'IO',
        'Brunei':'BN',
        'Bulgaria':'BG',
        'Burkina Faso':'BF',
        'Burundi':'BI',
        'Cabo Verde':'CV',
        'Cambodia':'KH',
        'Cameroon':'CM',
        'Canada':'CA',
        'Cayman Islands':'KY',
        'Central African Republic':'CF',
        'Chad':'TD',
        'Chile':'CL',
        'China':'CN',
        'Christmas Island':'CX',
        'Cocos Islands':'CC',
        'Colombia':'CO',
        'Comoros':'KM',
        'Congo, Democratic Republic':'CD',
        'Congo, Republic':'CG',
        'Cook Islands':'CK',
        'Costa Rica':'CR',
        "Cote d'Ivoire":'CI',
        'Croatia':'HR',
        'Cuba':'CU',
        'Curacao':'CW',
        'Cyprus':'CY',
        'Czech Republic':'CZ',
        'Denmark':'DK',
        'Djibouti':'DJ',
        'Dominica':'DM',
        'Dominican Republic':'DO',
        'Ecuador':'EC',
        'Egypt':'EG',
        'El Salvador':'SV',
        'Equatorial Guinea':'GQ',
        'Eritrea':'ER',
        'Estonia':'EE',
        'Ethiopia':'ET',
        'Falkland Islands':'KF',
        'Faroe Islands':'FO',
        'Fiji':'FJ',
        'Finland':'FI',
        'France':'FR',
        'French Guiana':'GF',
        'French Polynesia':'PF',
        'French Southern Territories':'TF',
        'Gabon':'GA',
        'Gambia':'GM',
        'Georgia, Republic':'GE',
        'Germany':'DE',
        'Ghana':'GH',
        'Gibraltar':'GI',
        'Greece':'GR',
        'Greenland':'GL',
        'Grenada':'GD',
        'Guadeloupe':'GP',
        'Guam':'GU',
        'Guatemala':'GT',
        'Guernsey':'GG',
        'Guinea':'GN',
        'Guinea-Bissau':'GW',
        'Guyana':'GY',
        'Haiti':'HT',
        'Heard Island and McDonald':'HM',
        'Holy See':'VA',
        'Honduras':'HN',
        'Hong Kong':'HK',
        'Hungary':'HU',
        'Iceland':'IS',
        'India':'IN',
        'Indonesia':'ID',
        'Iran':'IR',
        'Iraq':'IQ',
        'Ireland':'IE',
        'Isle of Man':'IM',
        'Israel':'IL',
        'Italy':'IT',
        'Jamaica':'JM',
        'Japan':'JP',
        'Jersey':'JE',
        'Jordan':'JO',
        'Kazakhstan':'KZ',
        'Kenya':'KE',
        'Kiribati':'KI',
        "Korea (the Democratic People's Republic of)":'KP',
        'Korea (the Republic of)':'KR',
        'Kuwait':'KW',
        'Kyrgyzstan':'KG',
        "Lao People's Democratic Republic (the)":'LA',
        'Latvia':'LV',
        'Lebanon':'LB',
        'Lesotho':'LS',
        'Liberia':'LR',
        'Libya':'LY',
        'Liechtenstein':'LI',
        'Lithuania':'LT',
        'Luxembourg':'LU',
        'Macao':'MO',
        'Macedonia':'MK',
        'Madagascar':'MG',
        'Malawi':'MW',
        'Malaysia':'MY',
        'Maldives':'MV',
        'Mali':'ML',
        'Malta':'MT',
        'Marshall Islands':'MH',
        'Martinique':'MQ',
        'Mauritania':'MR',
        'Mauritius':'MU',
        'Mayotte':'YT',
        'Mexico':'MX',
        'Micronesia':'FM',
        'Moldova':'MD',
        'Monaco':'MC',
        'Mongolia':'MN',
        'Montenegro':'ME',
        'Montserrat':'MS',
        'Morocco':'MA',
        'Mozambique':'MZ',
        'Myanmar':'MM',
        'Namibia':'NA',
        'Nauru':'NR',
        'Nepal':'NP',
        'Netherlands':'NL',
        'New Caledonia':'NC',
        'New Zealand':'NZ',
        'Nicaragua':'NI',
        'Niger':'NE',
        'Nigeria':'NG',
        'Niue':'NU',
        'Norfolk Island':'NF',
        'Northern Mariana Islands':'MP',
        'Norway':'NO',
        'Oman':'OM',
        'Pakistan':'PK',
        'Palau':'PW',
        'Palestine':'PS',
        'Panama':'PA',
        'Papua New Guinea':'PG',
        'Paraguay':'PY',
        'Peru':'PE',
        'Philippines':'PH',
        'Pitcairn':'PN',
        'Poland':'PL',
        'Portugal':'PT',
        'Puerto Rico':'PR',
        'Qatar':'QA',
        'Reunion':'RE',
        'Romania':'RO',
        'Russia':'RU',
        'Rwanda':'RW',
        'Saint Helena, Ascension and Tristan da Cunha':'SH',
        'Saint Kitts and Nevis':'KN',
        'Saint Lucia':'LC',
        'Saint Martin':'MF',
        'Saint Pierre and Miquelon':'PM',
        'Saint Vincent and the Grenadines':'VC',
        'Samoa':'WS',
        'San Marino':'SM',
        'Sao Tome And Principe':'ST',
        'Saudi Arabia':'SA',
        'Senegal':'SN',
        'Serbia':'RS',
        'Seychelles':'SC',
        'Sierra Leone':'SL',
        'Singapore':'SG',
        'Sint Maarten':'SX',
        'Slovakia':'SK',
        'Slovenia':'SI',
        'Solomon Islands':'SB',
        'Somalia':'SO',
        'South Africa':'ZA',
        'South Georgia and the South Sandwich Island':'GS',
        'South Sudan':'SS',
        'Spain':'ES',
        'Sri Lanka':'LK',
        'Sudan':'SD',
        'Suriname':'SR',
        'Svalbard And Jan Mayen':'SJ',
        'Swaziland':'SZ',
        'Sweden':'SE',
        'Switzerland':'CH',
        'Syria':'SY',
        'Taiwan':'TW',
        'Tajikistan':'TJ',
        'Tanzania':'TZ',
        'Thailand':'TH',
        'Timor-Leste':'TL',
        'Togo':'TG',
        'Tokelau':'TK',
        'Tonga':'TO',
        'Trinidad And Tobago':'TT',
        'Tunisia':'TN',
        'Turkey':'TR',
        'Turkmenistan':'TM',
        'Turks And Caicos Islands':'TC',
        'Tuvalu':'TV',
        'Uganda':'UG',
        'Ukraine':'UA',
        'United Arab Emirates':'AE',
        'United Kingdom':'GB',
        'United States Minor Outlying Islands':'UM',
        'United States of America':'US',
        'Uruguay':'UY',
        'Uzbekistan':'UZ',
        'Vanuatu':'VU',
        'Venezuela':'VE',
        'Vietnam':'VN',
        'Virgin Islands (British)':'VG',
        'Virgin Islands (U.S.)':'VI',
        'Wallis And Futuna':'WF',
        'Western Sahara':'EH',
        'Yemen':'YE',
        'Zambia':'ZM',
        'Zimbabwe':'ZW'}
    
    self.topic_dict = {
        self.cl_topicBiota_ck:'biota',
        self.cl_topicBoundaries_ck:'boundaries',
        self.cl_topicClimatology_ck:'climatologyMeteorologyAtmosphere',
        self.cl_topicEconomy_ck:'economy',
        self.cl_topicElevation_ck:'elevation',
        self.cl_topicEnvironment_ck:'environment',
        self.cl_topicFarming_ck:'farming',
        self.cl_topicInformation_ck:'geoscientificInformation',
        self.cl_topicHealth_ck:'health',
        self.cl_topicImagery_ck:'imageryBaseMapsEarthCover',
        self.cl_topicIntelligence_ck:'intelligenceMilitary',
        self.cl_topicWaters_ck:'inlandWaters',
        self.cl_topicLocation_ck:'location',
        self.cl_topicOceans_ck:'oceans',
        self.cl_topicPlanning_ck:'planningCadastre',
        self.cl_topicSociety_ck:'society',
        self.cl_topicStructure_ck:'structure',
        self.cl_topicTransportation_ck:'transportation',
        self.cl_topicUtilities_ck:'utilitiesCommunication'}
    
    self.language_dict = {
        'Bulgarian':'bul',
        'Czech':'ces',
        'Danish':'dan',
        'Dutch':'dut',
        'English':'eng',
        'Estonian':'est',
        'Finnish':'fin',
        'French':'fre',
        'German':'ger',
        'Greek':'gre',
        'Hungarian':'hun',
        'Irish':'gle',
        'Italian':'ita',
        'Latvian':'lav',
        'Lithuanian':'lit',
        'Maltese':'mlt',
        'Polish':'pol',
        'Portuguese':'por',
        'Romanian':'rum',
        'Slovak':'slo',
        'Slovenian':'slv',
        'Spanish':'spa',
        'Swedish':'swe'}
    
    self.role_dict = {
        'Author':'author',
        'Custodian':'custodian',
        'Distributor':'distributor',
        'Originator':'originator',
        'Owner':'owner',
        'Point of Contact':'pointOfContact',
        'Principal Investigator':'principalInvestigator',
        'Processor':'processor',
        'Publisher':'publisher',
        'Resource Provider':'resourceProvider',
        'User':'user'}
    
    self.unit_dict = {
        'Centimetre(s)':'cm',
        'Decimal degree(s)':'dd',
        'Kilometre(s)':'km',
        'Metre(s)':'m'}
    
    self.ceos_science_keywords = {
        self.kw_agriEngineering_ck:'Agricultural engineering',
        self.kw_agriPlant_ck:'Agricultural plant science',
        self.kw_foodScience_ck:'Food science',
        self.kw_forestScience_ck:'Forest science',
        self.kw_soils_ck:'Soils',
        self.kw_aerosols_ck:'Aerosols',
        self.kw_airQuality_ck:'Air quality',
        self.kw_altitude_ck:'Altitude',
        self.kw_atmChemistry_ck:'Atmospheric chemistry',
        self.kw_atmElectricity_ck:'Atmospheric electricity',
        self.kw_atmPhenomena_ck:'Atmospheric phenomena',
        self.kw_atmPressure_ck:'Atmospheric pressure',
        self.kw_atmRadiation_ck:'Atmospheric radiation',
        self.kw_atmTemperature_ck:'Atmospheric temperature',
        self.kw_atmVapor_ck:'Atmospheric water vapor',
        self.kw_atmWinds_ck:'Atmospheric winds',
        self.kw_clouds_ck:'Clouds',
        self.kw_precipitation_ck:'Precipitation',
        self.kw_ecoDynamics_ck:'Ecological dynamics',
        self.kw_terEcosystems_ck:'Terrestrial ecosystems',
        self.kw_vegetation_ck:'Vegetation',
        self.kw_frozenGround_ck:'Frozen ground',
        self.kw_glaciersIcesheet_ck:'Glaciers / Ice sheet',
        self.kw_seaIce_ck:'Sea ice',
        self.kw_snowIce_ck:'Snow / Ice',
        self.kw_erosionSedimentation_ck:'Erosion / Sedimentation',
        self.kw_geomorphology_ck:'Geomorphology',
        self.kw_landTemperature_ck:'Land temperature',
        self.kw_landCover_ck:'Land use / Land cover',
        self.kw_landscape_ck:'Landscape',
        self.kw_surfaceProperties_ck:'Surface radiative properties',
        self.kw_topography_ck:'Topography',
        self.kw_bathymetry_ck:'Bathymetry / Seafloor topography',
        self.kw_coastalProcesses_ck:'Coastal processes',
        self.kw_marineEnvironment_ck:'Marine environment',
        self.kw_marineGeophysics_ck:'Marine geophysics',
        self.kw_oceanWaves_ck:'Ocean waves',
        self.kw_oceanWinds_ck:'Ocean winds',
        self.kw_seaTopography_ck:'Sea surface topography',
        self.kw_seaTides_ck:'Tides',
        self.kw_waterQuality_ck_2:'Water quality',
        self.kw_geodetics_ck:'Geodetics',
        self.kw_geomagnetism_ck:'Geomagnetism',
        self.kw_geomorphicLandforms_ck:'Geomorphic landforms / processes',
        self.kw_gravity_ck:'Gravity / gravitational field',
        self.kw_gammaRay_ck:'Gamma ray',
        self.kw_irWavelengths_ck:'Infrared wavelengths',
        self.kw_lidar_ck:'LIDAR',
        self.kw_microwave_ck:'Microwave',
        self.kw_radar_ck:'RADAR',
        self.kw_radioWave_ck:'Radio wave',
        self.kw_uvWavelentghs_ck:'Ultraviolet wavelengths',
        self.kw_visWavelentghs_ck:'Visible wavelengths',
        self.kw_xRay_ck:'X-ray',
        self.kw_ionosMagnetos_ck:'Ionosphere / Magnetosphere dynamics',
        self.kw_solarActivity_ck:'Solar activity',
        self.kw_solarFlux_ck:'Solar energetic particle',
        self.kw_solarFlux_ck:'Solar energetic particle properties',
        self.kw_groundWater_ck:'Ground water',
        self.kw_surfaceWater_ck:'Surface water',
        self.kw_waterQuality_ck:'Water quality / chemistry'}
    
    self.emc_continents = [
        'Africa',
        'Antarctica',
        'Asia',
        'Oceania',
        'Europe',
        'North America',
        'South America']
    
    self.emc_oceans = [
        'Atlantic Ocean',
        'Arctic Ocean',
        'Indian Ocean',
        'Pacific Ocean',
        'Southern Ocean']
    
    self.emc_regions = [
        'Arctic Region',
        'Atlantic Ocean Islands',
        'Central Africa',
        'Central America',
        'Central Europe',
        'Eastern Africa',
        'Eastern Asia',
        'Eastern Europe',
        'Indian Ocean Islands',
        'Middle East',
        'North America',
        'Northern Africa',
        'Northern Europe',
        'Pacific Islands',
        'South America',
        'Southcentral Asia',
        'Southern Asia',
        'Southern Europe',
        'Western Africa',
        'Western Asia',
        'Western Europe']
    
    self.instrument_list = [
        ['1.108','Grimm Technologies Inc.'],
        ['1.109','Grimm Technologies Inc.'],
        ['1011C','Buck Research Instruments L.L.C.'],
        ['1201','Rosemount'],
        ['1221','Rosemount'],
        ['2D-C','Particle Measuring Systems'],
        ['2D-P','Particle Measuring Systems'],
        ['2D-S','Stratton Park Engineering Company'],
        ['2D2C','Particle Measuring Systems'],
        ['2DGB2','Particle Measuring Systems'],
        ['3150','ICSensors / Measurement Specialties'],
        ['4PI-SR','METEO-CONSULT'],
        ['5-hole Turbulence Probe','Other'],
        ['858AJ28','Rosemount'],
        ['AA-300','Sperry'],
        ['AADC II','Scintrex Ltd'],
        ['AARP','University of Manchester'],
        ['ADA-100-PDPA','TSI Inc.'],
        ['AE-42','Magee Scientific'],
        ['AE-52 Aethelometer','Magee Scientific'],
        ['AHV16','Thales'],
        ['AHV8','TRT'],
        ['AIMMS-20','Aventech Inc.'],
        ['AIRINS','iXBlue'],
        ['AL5002','Aero-Laser Gmbh'],
        ['AL5003','Aero-Laser Gmbh'],
        ['ALS-450','Leosphere'],
        ['ALS50','Leica Geosystems'],
        ['ARIES','Met Office / ABB Bomem'],
        ['AT4','Javad GNSS Inc.'],
        ['AVAPS','Vaisala'],
        ['Airborne Hyperspectral Scanner','Argon ST'],
        ['Airborne Prism EXperiment','ESA'],
        ['Airborne Thematic Mapper','DLR'],
        ['Airborne Visibility Meter','HSS Inc.'],
        ['Aircraft Systems','Other'],
        ['AisaDUAL','SPECIM'],
        ['AisaEAGLE 1K','SPECIM'],
        ['AisaEAGLE','SPECIM'],
        ['AisaFENIX 1K','SPECIM'],
        ['AisaFENIX','SPECIM'],
        ['AisaOWL','SPECIM'],
        ['B270','Setra Systems'],
        ['BAT','NOAA / Airborne Research Australia'],
        ['BCP','Droplet Measurement Technologies'],
        ['CAPS - LWC','Droplet Measurement Technologies'],
        ['CAPS','Droplet Measurement Technologies'],
        ['CAS Spectrometer','Baumgardner et al., 2001'],
        ['CASI','ITRES Research Ltd'],
        ['CASI-1500i','ITRES Research Ltd'],
        ['CASI-550','ITRES Research Ltd'],
        ['CCN Counter','Droplet Measurement Technologies'],
        ['CCNS4','IGI mbH'],
        ['CDP-2','Droplet Measurement Technologies'],
        ['CEV','INTA'],
        ['CGR-4','Kipp & Zonen'],
        ['CIP','Droplet Measurement Technologies'],
        ['CIP-100','Droplet Measurement Technologies'],
        ['CIP-15','Droplet Measurement Technologies'],
        ['CMP-22','Kipp & Zonen'],
        ['COPAS','University of Mainz'],
        ['CPI','Stratton Park Engineering Company'],
        ['CR-1','Buck Research Instruments L.L.C.'],
        ['CR-2','Buck Research Instruments L.L.C.'],
        ['CRISTA New Frontiers','ForschungsZentrum Juelich'],
        ['CW-QCLAS','Aerodyne Research Inc.'],
        ['Campbell Q7.1','Campbell Scientific'],
        ['Cloud Imaging Probe','Other'],
        ['Counterflow Virtual Impactor','Met Office'],
        ['DEIMOS','Met Office'],
        ['Dewtrak-137','EdgeTech Instruments'],
        ['Dewtrak-200','EdgeTech Instruments'],
        ['dIGIcam K14','IGI mbH'],
        ['E-SAR','DLR'],
        ['ERS microjoule Lidar EMB-ER 1/2','ERS'],
        ['Eppley PS Pyranometer','The Eppley Laboratory Inc.'],
        ['Eppley Pyrgeometer','The Eppley Laboratory Inc.'],
        ['Everest 4000.4ZL','Everest Interscience Inc.'],
        ['F-SAR','DLR'],
        ['FAGE','University of Leeds'],
        ['FLIR M40','FLIR Systems Inc.'],
        ['FLIR SC3000','FLIR Systems Inc.'],
        ['FS2 Relative Humidity','Aerodata GmbH'],
        ['FSSP-100','Particle Measuring Systems'],
        ['FSSP-100ER','Particle Measuring Systems'],
        ['FSSP-300','Particle Measuring Systems'],
        ['FTIR','Midac Inc.'],
        ['FUBISS','Free University of Berlin'],
        ['FUBISS-ASA2','Free University Berlin'],
        ['Filter Sampler','Other'],
        ['Flask Array Sampler','Atmospheric Observing Systems Inc.'],
        ['Flask Sampling System','MetAir'],
        ['Flourescence Water Vapour Sensor','Met Office'],
        ['Formaldehyde Detectors','Other'],
        ['GASCOD-A','FISBAT-CNR'],
        ['GE-1011B','General Eastern'],
        ['GE-1011C','General Eastern'],
        ['GR-DV400','JVC'],
        ['Garmin GPS','Garmin'],
        ['Gyro-4','Javad GNSS Inc.'],
        ['HAGAR','University of Frankfurt'],
        ['HALOX','Forschungszentrum Julich GmbH'],
        ['HMP','Vaisala / Rosemount'],
        ['HMP233','Vaisala'],
        ['HRSC AX','DLR'],
        ['HVPS','Stratton Park Engineering Company'],
        ['High Accuracy INS','SAGEM'],
        ['Hyperspectral Imagery Sensor','DLR'],
        ['HySpecScan','Analytical Spectral Devices Inc.'],
        ['IR Gas analyzer','Edinburgh Sensors'],
        ['IR/UV Line Scanner','OPTIMARE Systems GmbH'],
        ['IRCAM','Jenoptik AG'],
        ['IS-2','Interspect Ltd.'],
        ['IS-3','Interspect Ltd.'],
        ['IS-4','Interspect Ltd.'],
        ['IS2+','Interspect Ltd.'],
        ['Ice Nucleus Counter','University of Manchester'],
        ['J-W LWC','Johnson-Williams'],
        ['JO1D / JNO2 Photometer','Unknown'],
        ['KA-131','Bendix King'],
        ['KT-15','Heitronics Infrarot Messtechnik'],
        ['King Probe','Particle Measuring Systems'],
        ['Kistler 3 axes accelerometers','Kistler Instrumente AG'],
        ['LASAIR-5295','Particle Measurement Systems'],
        ['LD90','Riegl Laser Measurement Systems GmbH'],
        ['LGR 907','Los Gatos Research Inc.'],
        ['LGR DLT100','Los Gatos Research Inc.'],
        ['LI-COR 6262','LI-COR'],
        ['LI-COR 7500','LI-COR'],
        ['LI-COR Pyranometer','LI-COR'],
        ['LI-COR Quantum Sensor','LI-COR'],
        ['LMS-Q280','Riegl Laser Measurement Systems GmbH'],
        ['LMS-Q560','Riegl Laser Measurement Systems GmbH'],
        ['LMS-Q680i','Riegl Laser Measurement Systems GmbH'],
        ['LTC 0600','Philipps'],
        ['LTN 90-100','Litton'],
        ['Lasernav YG1761B','Honeywell'],
        ['Lyman-alpha HMS-2','Buck Research Instruments L.L.C.'],
        ['Lyman-alpha L-5','Buck Research Instruments L.L.C.'],
        ['MARSS','Met Office'],
        ['MS4100','Duncantech'],
        ['MetAir NOxTOy','MetAir AG'],
        ['Meteorological Sensor Package','DLR'],
        ['Mobile Flux Platform','IBIMET CNR'],
        ['NO CLD','DLR'],
        ['Nevzorov IVO-2a','Sky Tech Research Inc.'],
        ['Nevzorov','Sky Tech Research Inc.'],
        ['OAP-200X','Particle Measuring Systems'],
        ['OAP-230X','Particle Measuring Systems'],
        ['OAP-230Y','Particle Measuring Systems'],
        ['OEM4-G2','NovAtel Inc.'],
        ['ORAC','University of Leeds'],
        ['Others','Other'],
        ['Ozone Lidar EXperiment','DLR'],
        ['Ozone Monitor 202','2B Technologies'],
        ['Ozone Monitor','2B Technologies'],
        ['PAN GC','Ai Qualitek Ltd'],
        ['PCASP-100X','Droplet Measurement Technologies'],
        ['PCASP-SPP200','Droplet Measurement Technologies'],
        ['PELICAN','ONERA'],
        ['PERCA','University of Leceister'],
        ['POS AV 510','Applanix'],
        ['POSAV-410','Applanix'],
        ['PRT 6','Barnes'],
        ['PSAP','Radiance Research Inc.'],
        ['PSI-O3','Paul Scherrer Institut'],
        ['PT','Rosemount'],
        ['PT100','Rosemount'],
        ['PT102AL','Rosemount'],
        ['PT102BL','Rosemount'],
        ['PT102BW','Rosemount'],
        ['PT102DB1 AG','Rosemount'],
        ['PT102E2 AL','Rosemount'],
        ['PT102E4 AL','Rosemount'],
        ['PT50','Rosemount'],
        ['PT500','Rosemount'],
        ['PTR-MS','University of East Anglia'],
        ['PVM-100','Gerber Scientific Inc.'],
        ['Peroxide Detectors','Other'],
        ['Pitot Probe','Other'],
        ['Polifemo M21','SUPERELECTRIC s.r.l.'],
        ['Portable Lidar System','University of Munich'],
        ['R4903','Met One Instruments'],
        ['RALI','LATMOS'],
        ['RALI','LATMOS'],
        ['RCD105','Leica-Geosystems'],
        ['RDR-4B','Honeywell'],
        ['RMK A 30/23','Zeiss'],
        ['RMK A','Zeiss'],
        ['RR-0150','RadianceResearch'],
        ['RT3102','Oxford Technical Solutions'],
        ['Radar Echo Sounding System','AWI'],
        ['S-5002','Sistemas Instalaciones Redes S.A.'],
        ['S-5006','Sistemas Instalaciones Redes S.A.'],
        ['S-5012','Sistemas Instalaciones Redes S.A.'],
        ['S3000','Michell Instruments GmbH'],
        ['S56','Micro-g LaCoste'],
        ['SA 41M','Environment S.A.'],
        ['SETHI','ONERA'],
        ['SFIM 3 axes accelerometers','SFIM'],
        ['SID-2','University of Hertfordshire'],
        ['SIELETERS','ONERA'],
        ['SIOUX','DLR'],
        ['SMPS','Grimm Technologies Inc.'],
        ['SP-2','Droplet Measurement Technologies'],
        ['SPEC Hawkeye','Stratton Park Engineering Company'],
        ['SWS','Met Office'],
        ['Solent HS','Gill Instruments Ltd'],
        ['Solent HS-100','Gill Instruments Ltd'],
        ['Solent HS-50','Gill Instruments Ltd'],
        ['Sony Video Camera','Sony'],
        ['Sundstrand 3 axes accelerometers','Sundstrand'],
        ['TABI320','ITRES Research Ltd'],
        ['TAFTS','Imperial College London'],
        ['TASI-600','ITRES Research Ltd'],
        ['TDLAS','Imperial College London'],
        ['TDLAS','National Physical Laboratory'],
        ['TECO 42C','ThermoScientific'],
        ['TECO 42C','ThermoScientific'],
        ['TECO 42S','ThermoScientific'],
        ['TECO 43C','ThermoScientific'],
        ['TECO 48','ThermoScientific'],
        ['TECO 48CS','ThermoScientific'],
        ['TECO 49PS','ThermoScientific'],
        ['TECO 49S','ThermoScientific'],
        ['TOF-AMS','Aerodyne Research Inc.'],
        ['TP3-S','Meteolabor AG'],
        ['TS9260','NEC Corporation'],
        ['TSI-3007','TSI Inc.'],
        ['TSI-3010','TSI Inc.'],
        ['TSI-3022','TSI Inc.'],
        ['TSI-3025','TSI Inc.'],
        ['TSI-3563','TSI Inc.'],
        ['TSI-3776','TSI Inc.'],
        ['TSI-3786','TSI Inc.'],
        ['Total Water Content','Met Office'],
        ['Trimble 2101','Trimble Navigation'],
        ['Trimble 4000 SSI','Trimble Navigation'],
        ['Trimble TNL 2000','Trimble Navigation'],
        ['UHSAS-A','Droplet Measurement Technologies'],
        ['ULISS 45i','SAGEM'],
        ['ULS','Laser Technology Inc.'],
        ['UMP40','Sextant'],
        ['VACC','University of Leeds'],
        ['VIS Line Scanner','OPTIMARE Systems GmbH'],
        ['VIS/NIR Spectrometer ','Other'],
        ['VOC GC','Airmotec AG'],
        ['Video Camera','Other'],
        ['WIND','DLR / CNRS / INSU'],
        ['WVSS-II','SpectraSensors Inc.'],
        ['Walz UV Pyranometer','Heinz Walz Company'],
        ['Whole Air Sampling System','University of York'],
        ['XR5','Navstar Electronics']]
    
    self.window_messages = {
        "infoButton_1":"<p>Available in the EUFAR TA application form (<b>Project title</b>), this i"
         + "s a characteristic and often unique name identifying the resource.</p><p><u>Example:</u> Our"
         + " Small Project.</p>",
        "infoButton_2":"<p>This is a brief narrative summary of the content of the resource. It is ava"
         + "ilable in the EUFAR TA application form (<b>Scientific problems being addressed by the expe"
         + "riments to be performed</b>).</p><p><u>Example:</u> SMALLPROJECT is a small project. Its go"
         + "al is to explain what to do and what to write.</p>",
        "infoButton_3":"<p>This is the type of resource being described by the metadata, and can be ei"
         + "ther dataset or series.</p><p><u>Example:</u> Dataset.</p>",
        "infoButton_4":"<p>The resource locator defines the link(s) to the resource and/or the link to"
         + " additional information about the resource. For EUFAR projects, it is automatically filled "
         + "in with the link to the EUFAR database.</p><p><u>Example:</u> http://browse.ceda.ac.uk/brow"
         + "se/badc/eu far/docs/00eufararchive contents.html</p>",
        "infoButton_5":"<p hyphens='auto'>This element uniquely identifying the project and it is gene"
         + "rally formed with mandatory and/or optional string codes. In a EUFAR project, it is availab"
         + "le in the EUFAR TA application form (<b>Project acronym</b>).</p><p><u>Example:</u> SMALLPR"
         + "OJECT",
        "infoButton_6":"<p>The language(s) used within the resource. In a EUFAR project, English is al"
         + "ways selected and should not be changed. </p><p><u>Example:</u> English.</p>",
        "infoButton_7":"<p>The topic category is a high-level classification scheme to facilitate the "
         + "grouping and topic-based search of available spatial data resources. This item corresponds "
         + "to the Main <b>Scientific Field / specific discipline</b> in the EUFAR Ta application form."
         + "</p><p><u>Example:</u> Environment.</p>",
        "infoButton_8":"<p>The keyword value is a commonly used word to describe the subject. The keyw"
         + "ord scheme is from NASA/Global Change Master Directory (GCMD) Earth Science Keywords.</p><p"
         + "><u>Example:</u> Forest science, Aerosols, Clouds.</p>",
        "infoButton_9":"<p>The selection of an aircraft can help to improve storage and queries in a d"
         + "atabase. Please select here the aircraft used to acquire and prepare the actual data and me"
         + "tadata, and click on the '+' button to add it to the list. It's possible to add multiple ai"
         + "rcraft.<p><u>Example:</u> AWI - POLAR 5.</p>",
        "infoButton_10":"<p>The selection of an instrument, or multiple instruments, can help to impro"
         + "ve storage and queries in a database. Please select here the instrument(s) used to acquire "
         + "and prepare the actual data and metadata, and click on the '+' icon to add it into the list"
         + ".</p><p><u>Example:</u> APEX.</p>",
        "infoButton_11":"<p>This is the name of the formal location covered by the dataset. It is avai"
         + "lable in the EUFAR TA application form.</p><p><u>Example:</u> Countries / France.</p>",
        "infoButton_12":"<p>This is the extent of the resource in the geographic space, given as a bou"
         + "nding box. The bounding box shall be expressed with westbound and eastbound longitudes in d"
         + "ecimal degree (-180.00 to 180.00) and southbound and northbound latitudes in decimal degree"
         + " (-90.00 to 90.00), with a precision of two decimals.</p><p><u>Example:</u> for a bounding "
         + "box above United Kingdom (58.65°N / -11.80°W and 50.69°N / 2.32°E)</p><p align='center'>58."
         + "65</p><p align='center'>-11.80 &nbsp;&nbsp;&nbsp;&nbsp; 2.32</p><p align='center'>50.69</p>",
        "infoButton_13":"<p>Each spatial resolution is either an equivalent scale OR a ground sample d"
         + "istance. When two equivalent scales or two ground sample distances are expressed, the spati"
         + "al resolution is an interval bounded by these two values. It is only mandatory if an equiva"
         + "lent scale or a resolution distance can be specified.</p><p><u>Example:</u> a dataset with "
         + "a spatial resolution of 0.25°x0.25° -> 0.25 / Decimal degree (dd).</p>",
        "infoButton_14":"<p>This is the date of publication of the resource. In a EUFAR project, the d"
         + "ate of entry into EUFAR database (N8-DB) should be used and set <b>before</b> the current d"
         + "ate.</p><p><u>Example:</u> 2015/07/12.</p>",
        "infoButton_15":"<p>This is the date of last revision of the resource if available. In a EUFAR"
         + " project, it is automatically created by the EUFAR database (date stamp).</p>",
        "infoButton_16":"<p>This is the date of creation of the resource. In a EUFAR project, the date"
         + " should be set to the date of data processing.</p><p><u>Example:</u> 2015/07/11.</p>",
        "infoButton_17":"<p>The temporal extent defines the time period covered by the data acquisitio"
         + "n. It can be composed of multiple phases if necessary.</p><p><u>Example:</u></p>&nbsp;&nbsp"
         + ";&nbsp;&nbsp; 2015/07/01 - 2015/07/03<br> &nbsp;&nbsp;&nbsp;&nbsp; 2015/07/05 - 2015/07/07<"
         + "/p>",
        "infoButton_18":"<p>This metadata element defines the conditions for access and use of spatial"
         + " data sets. In a EUFAR project, this element has already been filled in in agreement with t"
         + "he EUFAR Consortium Agreement.</p>",
        "infoButton_19":"<p>This metadata element defines the limitations for public access to spatial"
         + " data sets and the reason for that. In a EUFAR project, this element has already been fille"
         + "d in in agreement with the EUFAR Consortium Agreement.</p>",
        "infoButton_20":"<p>This is the description of the organisation responsible for the production"
         + " of the resource. The description shall include the name of the organisation.</p><p><u>Exam"
         + "ple:</u> SAFIRE</p>",
        "infoButton_21":"<p>This is the email of the point of contact.</p><p><u>Example:</u> john.doe@"
         + "email.com.</p>",
        "infoButton_22":"<p>This is the role of the responsible organisation. In a EUFAR project, the "
         + "value is <b>Point of Contact</b>.</p><p><u>Example:</u> Point of Contact.</p>",
        "infoButton_23":"<p>The date which specifies when the metadata record was created or updated.<"
         + "/p><p><u>Example:</u> 2015/07/14.</p>",
        "infoButton_24":"<p>This is the language in which the metadata elements are expressed. In a EU"
         + "FAR project, English is always selected and should not be changed.</p><p><u>Example:</u> En"
         + "glish.</p>",
        "infoButton_25":"<p>This is the name and the contact e-mail of the party responsible for the m"
         + "etadata.</p><p><u>Example:</u> SAFIRE or John Doe</p>",
        "infoButton_26":"<p>This is a statement on process history and/or overall quality of the spati"
         + "al data set. The user has to fill in the requested fields. Once it has been done, EMC will "
         + "format the inputs as free text to conform to INSPIRE standard.</p>",
        "infoButton_27":"<p>Those items are a link to the description of all procedures, constants and"
         + " materials applied to raw digital data for calibration purpose. A free text description is "
         + "also accepted for each item if necessary.</p><p><u>Example:</u> <b>http://www.operator.com/"
         + "path/pa th2/document_to_explain_procedures.html</b> or <b>We proceed this way and this way "
         + "to calibrate the instrument / The calibration constants come from this book and this public"
         + "ation</b>.</p>",
        "infoButton_28":"<p>Once the data has been processed, the final output format. Multiple entrie"
         + "s are possible. If 'Other' is selected for free text, the characters ';', '|' and '/' are p"
         + "rohibited.</p><p><u>Example:</u> NetCDF.</p>",
        "infoButton_29":"<p>The Quality and Validity section needs a brief description, or a link to t"
         + "he document, of the operator's standard procedures explaining the quality-control flagging "
         + "applied to individual data points.</p><p><u>Example:</u> <b>http://www.operator.com/path/p "
         + "ath2/document_to_explain_flagging.html</b> or <b>Each point has a certain number of flag to"
         + " say if the measurement is allright or not</b>.</p>",
        "infoButton_30":"<p>What are the empirical assumptions, made when processing the data ? Please"
         + " give references if possible.</p><p><u>Example:</u> aerosol refractive index, ice crystal b"
         + "ulk density.</p>",
        "infoButton_31":"<p>In case of issues with the sensor calibration, it is important to track ba"
         + "ck the calibration cycle.</p>",
        "infoButton_32":"<p>The setting up of the spectral mode can be changed with some sensor system"
         + "s.</p>",
        "infoButton_33":"<p>As basic processing information, it is important to know if the DC was alr"
         + "eady corrected, or if this has to be done before all subsequent information retrieval.</p>",
        "infoButton_34":"<p>Some data Quality Indicators can be assigned to single pixels and can ther"
         + "efore provided as Quality Layers in a spatial dataset.</p>",
        "infoButton_35":"<p>This mask includes all pixels for which corrections where carried out in o"
         + "ne or more bands.</p>",
        "infoButton_36":"<p>All pixels where defects were detected, but which were not corrected, are "
         + "included in this bad pixel mask.</p>",
        "infoButton_37":"<p>Saturation occurs when the sensed and amplified signal exceeds the dynamic"
         + " range of the detector.</p>",
        "infoButton_38":"<p>The quality of pixels, spatially or spectrally neighbouring a saturated pi"
         + "xel, can be reduced for sensor designs based on frame-transfer CCDs (e.g., AISA Eagle). Thu"
         + "s these pixels are detected and included in a separate mask.</p>",
        "infoButton_39":"<p>Position information might include data gaps, errors and increased uncerta"
         + "inties related to the reception of a small number of GPS satellites, or rapid changes in ca"
         + "se of turbulent flight conditions. When geocoding, the corresponding scan lines might have "
         + "an error or an increased uncertainty in geo-location.</p>",
        "infoButton_40":"<p>In certain cases, the parameters required for an accurate atmospheric corr"
         + "ection cannot be estimated for all pixels in an image. Such critical pixels should be flagg"
         + "ed.</p>",
        "infoButton_41":"<p>One of the limiting factors, regarding processing quality, is the accuracy"
         + " and spatial resolution of the DEM. Therefore one can expect an increased uncertainty where"
         + "ver the terrain is rough. Thus the local variability of the terrain height is calculated in"
         + " a <b>moving window</b> approach, and critical areas are detected and flagged in this quali"
         + "ty layer.</p>",
        "infoButton_42":"<p>In addition to the increased DEM uncertainty in rough terrain, areas with "
         + "high slope values and/or unfavourable local illumination (large solar zenith angles) are li"
         + "kely affected by an increased uncertainty for the terrain correction.</p>",
        "infoButton_43":"<p>Regarding the strength of the BRDF effect and the related accuracy of BRDF"
         + " correction, critical conditions should be addressed. The strength of the BRDF effect is a "
         + "function of viewing / illumination geometry, terrain as well as land cover. Therefore stron"
         + "gly affected areas can be detected based on these parameters and are subsequently flagged.<"
         + "/p>",
        "infoButton_44":"Each form has to be linked to an instrument. All instruments selected in the "
         + "'Aircraft and Instrument' section will be displayed here.<p>Use the list on the left to sel"
         + "ect an instrument.</p>",
        "infoButton_45":"With the tab controls, you have the possibility to copy/paste any information"
         + " entered in the current form to a new form or another existing form."}

