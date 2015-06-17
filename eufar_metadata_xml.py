# -*- coding: utf-8 -*-

NAMESPACE_URI1 = "http://www.isotc211.org/2005/gmd"
NAMESPACE_URI2 = "http://www.isotc211.org/2005/gco"
NAMESPACE_URI3 = "http://www.opengis.net/gml"
NAMESPACE_URI4 = "http://www.w3.org/2001/XMLSchema-instance"
NAMESPACE_URI5 = "http://www.isotc211.org/2005/srv"
NAMESPACE_URI6 = "http://www.w3.org/1999/xlink"

import datetime
import xml.dom.minidom
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QDate
from PyQt4.QtGui import QCheckBox
from functions import button_functions
from functions.sql_functions import sql_valueRead
from functions.button_functions import gl_categoryRolebox_changed
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QRadioButton
from functions.button_functions import ai_aircraftRolebox_changed


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


def create_eufar_xml(self, out_file_name):
    doc = xml.dom.minidom.Document()
    doc_root = add_element(doc, "gmd:MD_Metadata", doc)
    doc_root.setAttribute("xmlns:gmd", NAMESPACE_URI1)
    doc_root.setAttribute("xmlns:gco", NAMESPACE_URI2)
    doc_root.setAttribute("xmlns:gml", NAMESPACE_URI3)
    doc_root.setAttribute("xmlns:xsi", NAMESPACE_URI4)   
    doc_root.setAttribute("xmlns:srv", NAMESPACE_URI5)    
    doc_root.setAttribute("xmlns:xlink", NAMESPACE_URI6)  


    ############################
    # Identification Info
    ############################
	# Citation
	########################
    identificationIdent1 = add_element(doc, "gmd:identificationInfo", doc_root)
    dataIdent1MD = add_element(doc, "gmd:MD_DataIdentification", identificationIdent1)
    citationIdent1 = add_element(doc, "gmd:citation", dataIdent1MD)
    citationIdent1CI = add_element(doc, "gmd:CI_Citation", citationIdent1)
    titleIdent1 = add_element(doc, "gmd:title", citationIdent1CI)
    add_element(doc, "gco:CharacterString", titleIdent1, self.id_resourceTitle_ln.text())
    identifierIdent1 = add_element(doc, "gmd:identifier", citationIdent1CI)
    identifierIdent1RS = add_element(doc, "gmd:RS_Identifier", identifierIdent1)
    codeIdent = add_element(doc, "gmd:code", identifierIdent1RS)
    add_element(doc, "gco:CharacterString", codeIdent, self.id_resourceIdent_ln.text())
    dateIdent1 = add_element(doc, "gmd:date", citationIdent1CI)
    dateIdent1CI = add_element(doc, "gmd:CI_Date", dateIdent1)
    dateIdent2 = add_element(doc, "gmd:date", dateIdent1CI)
    add_element(doc, "gco:Date", dateIdent2, self.tr_datePublication_do1.date().toString(Qt.ISODate))
    dateTypeIdent1 = add_element(doc, "gmd:dateType", dateIdent1CI)
    dateTypeCodeIdent1CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent1, "publication")
    dateTypeCodeIdent1CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode")
    dateTypeCodeIdent1CI.setAttribute("codeListValue","publication")
    dateIdent3 = add_element(doc, "gmd:date", citationIdent1CI)
    dateIdent2CI = add_element(doc, "gmd:CI_Date", dateIdent3)
    dateIdent4 = add_element(doc, "gmd:date", dateIdent2CI)
    add_element(doc, "gco:Date", dateIdent4, self.tr_dateRevision_do2.date().toString(Qt.ISODate))
    dateTypeIdent2 = add_element(doc, "gmd:dateType", dateIdent2CI)
    dateTypeCodeIdent2CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent2, "revision")
    dateTypeCodeIdent2CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode")
    dateTypeCodeIdent2CI.setAttribute("codeListValue","revision")
    dateIdent5 = add_element(doc, "gmd:date", citationIdent1CI)
    dateIdent3CI = add_element(doc, "gmd:CI_Date", dateIdent5)
    dateIdent6 = add_element(doc, "gmd:date", dateIdent3CI)
    add_element(doc, "gco:Date", dateIdent6, self.tr_dateCreation_do3.date().toString(Qt.ISODate))
    dateTypeIdent3 = add_element(doc, "gmd:dateType", dateIdent3CI)
    dateTypeCodeIdent3CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent3, "creation")
    dateTypeCodeIdent3CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode")
    dateTypeCodeIdent3CI.setAttribute("codeListValue","creation")

	########################
	# Abstract
	######################## 
    abstractIdent = add_element(doc, "gmd:abstract", dataIdent1MD)
    add_element(doc, "gco:CharacterString", abstractIdent, self.id_resourceAbstract_ta.toPlainText())

	#######################
	# Topics
	#######################
    all_check_boxes = self.findChildren(QCheckBox)
    for check_box in all_check_boxes:
	if check_box.objectName()[0:3] == "cl_" and check_box.isChecked():
	    query = sql_valueRead(self, 'topics', 'Text', check_box.text())
	    topicIdent = add_element(doc, "gmd:topicCategory", dataIdent1MD)
	    add_element(doc, "gmd:MD_TopicCategoryCode", topicIdent, query[0][1])

	#######################
	# Keywords
	#######################
    descriptiveKeywordIdent1 = add_element(doc, "gmd:descriptiveKeywords", dataIdent1MD)
    keywordIdent1MD = add_element(doc, "gmd:MD_Keywords", descriptiveKeywordIdent1)
    for check_box in all_check_boxes:
	if check_box.objectName()[0:3] == "kw_" and check_box.isChecked():
	    query = sql_valueRead(self, 'scienceKeywords', 'Labels', check_box.objectName())
	    keywordIdent1 = add_element(doc, "gmd:keyword", keywordIdent1MD)
	    add_element(doc, "gco:CharacterString", keywordIdent1, query[0][1])
    thesaurusKeywordIdent1 = add_element(doc, "gmd:thesaurusName", keywordIdent1MD)
    citationKeywordIdent1CI = add_element(doc, "gmd:CI_Citation", thesaurusKeywordIdent1)
    titleKeywordIdent1 = add_element(doc, "gmd:title", citationKeywordIdent1CI)
    add_element(doc, "gco:CharacterString", titleKeywordIdent1, "NASA/Global Change Master Directory (GCMD) Earth Science Keywords. Version 8.0.0.0.0")
    dateIdent7 = add_element(doc, "gmd:date", citationKeywordIdent1CI)
    dateIdent4CI = add_element(doc, "gmd:CI_Date", dateIdent7)
    dateIdent8 = add_element(doc, "gmd:date", dateIdent4CI)
    add_element(doc, "gco:Date", dateIdent8, "2015-02-20")
    dateTypeIdent4 = add_element(doc, "gmd:dateType", dateIdent4CI)
    dateTypeCodeIdent4CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent4, "revision")
    dateTypeCodeIdent4CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode")
    dateTypeCodeIdent4CI.setAttribute("codeListValue", "revision")

	#######################
	# Location Extent
	#######################
    extentIdent1 = add_element(doc, "gmd:extent", dataIdent1MD)
    extentIdent1EX = add_element(doc, "gmd:EX_Extent", extentIdent1)
    extentDescription = add_element(doc, "gmd:description", extentIdent1EX)
    add_element(doc, "gco:CharacterString", extentDescription, self.gl_details_rl2.currentText())
    geographicIdent1 = add_element(doc, "gmd:geographicElement", extentIdent1EX)
    geographicIdent1EX = add_element(doc, "gmd:EX_GeographicBoundingBox", geographicIdent1)
    westBoundIdent = add_element(doc, "gmd:westBoundLongitude", geographicIdent1EX)
    add_element(doc, "gco:Decimal", westBoundIdent, self.gl_westBound_ln.text())
    eastBoundIdent = add_element(doc, "gmd:eastBoundLongitude", geographicIdent1EX)
    add_element(doc, "gco:Decimal", eastBoundIdent, self.gl_eastBound_ln.text())
    northBoundIdent = add_element(doc, "gmd:northBoundLatitude", geographicIdent1EX)
    add_element(doc, "gco:Decimal", northBoundIdent, self.gl_northBound_ln.text())
    southBoundIdent = add_element(doc, "gmd:southBoundLatitude", geographicIdent1EX)
    add_element(doc, "gco:Decimal", southBoundIdent, self.gl_southBound_ln.text())
    
	#######################
	# Temporal Extent
	#######################
    temporalIdent1 = add_element(doc, "gmd:temporalElement", extentIdent1EX)
    temporalIdent1EX = add_element(doc, "gmd:EX_TemporalExtent", temporalIdent1)
    extentIdent3 = add_element(doc, "gmd:extent", temporalIdent1EX)
    periodIdent1 = add_element(doc, "gml:TimePeriod", extentIdent3)
    periodIdent1.setAttribute("gml:id","extent0") 
    add_element(doc, "gml:beginPosition", periodIdent1, self.tr_dateStart_do4.date().toString(Qt.ISODate))
    add_element(doc, "gml:endPosition", periodIdent1, self.tr_dateEnd_do5.date().toString(Qt.ISODate))
    if self.tr_tpex > 0:
	i = 0
	for item in self.tr_dtSt_1:
	    temporalIdent1 = add_element(doc, "gmd:temporalElement", extentIdent1EX)
	    temporalIdent1EX = add_element(doc, "gmd:EX_TemporalExtent", temporalIdent1)
	    extentIdent3 = add_element(doc, "gmd:extent", temporalIdent1EX)
	    periodIdent1 = add_element(doc, "gml:TimePeriod", extentIdent3)
	    periodIdent1.setAttribute("gml:id","extent" + str(i + 1))
	    add_element(doc, "gml:beginPosition", periodIdent1, self.tr_dtSt_1[i].date().toString(Qt.ISODate))
	    add_element(doc, "gml:endPosition", periodIdent1, self.tr_dtEd_1[i].date().toString(Qt.ISODate))
	    i += 1
   
	#######################
	# Spatial Resolution
	#######################
    resolutionIdent1 = add_element(doc, "gmd:spatialResolution", dataIdent1MD)
    resolutionIdent1MD = add_element(doc, "gmd:MD_Resolution", resolutionIdent1)
    if self.gl_resolution_rl1.currentText() == 'Distance':
	distanceIdent1 = add_element(doc, "gmd:distance", resolutionIdent1MD)
	distanceIdent2 = add_element(doc, "gco:Distance", distanceIdent1, self.gl_resolution_ln.text())
	distanceIdent2.setAttribute("uom",self.gl_unit_ln.text())
    elif self.gl_resolution_rl1.currentText() == 'Scale':
	scaleIdent1 = add_element(doc, "gmd:equivalentScale", resolutionIdent1MD)
	fractionIdent1MD = add_element(doc, "gmd:MD_RepresentativeFraction", scaleIdent1)
	denominatorIdent1 = add_element(doc, "gmd:denominator", fractionIdent1MD)
	add_element(doc, "gco:Integer", denominatorIdent1, self.gl_resolution_ln.text())
   
	########################
	# Language
	######################## 
    query = sql_valueRead(self, 'languageRole', 'Id', self.id_resourceLang_rl2.currentText())
    languageIdent = add_element(doc, "gmd:language", dataIdent1MD)
    languageIdent2 = add_element(doc, "gmd:LanguageCode", languageIdent, query[0][1])
    languageIdent2.setAttribute("codeList", "http://www.loc.gov/standards/iso639-2/")
    languageIdent2.setAttribute("codeListValue", query[0][1])
    
	#######################
	# Resource Constraints
	#######################
    constraintIdent1 = add_element(doc, "gmd:resourceConstraints", dataIdent1MD)
    constraintIdent1MD = add_element(doc, "gmd:MD_Constraints", constraintIdent1)
    useIdent1 = add_element(doc, "gmd:useLimitation", constraintIdent1MD)
    add_element(doc, "gco:CharacterString", useIdent1, self.au_conditions_ta.toPlainText())
    if self.au_wn_2 > 0:
	i = 0
	for item in self.au_wn_con_ta:
	    useIdent1 = add_element(doc, "gmd:useLimitation", constraintIdent1MD)
	    add_element(doc, "gco:CharacterString", useIdent1, self.au_wn_con_ta[i].toPlainText())
	    i += 1
    constraintIdent2 = add_element(doc, "gmd:resourceConstraints", dataIdent1MD)
    legalIdent1MD = add_element(doc, "gmd:MD_LegalConstraints", constraintIdent2)
    accessIdent1 = add_element(doc, "gmd:accessConstraints", legalIdent1MD)
    restrictionIdent1MD = add_element(doc, "gmd:MD_RestrictionCode", accessIdent1, "otherRestrictions")
    restrictionIdent1MD.setAttribute("codeList","http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_RestrictionCode")
    restrictionIdent1MD.setAttribute("codeListValue","otherRestrictions")
    accessIdent2 = add_element(doc, "gmd:otherConstraints", legalIdent1MD)
    add_element(doc, "gco:CharacterString", accessIdent2, self.au_limitations_ta.toPlainText())
    if self.au_wn_1 > 0:
	i = 0
	for item in self.au_wn_lim_ta:
	    accessIdent2 = add_element(doc, "gmd:otherConstraints", legalIdent1MD)
	    add_element(doc, "gco:CharacterString", accessIdent2, self.au_wn_lim_ta[i].toPlainText())
	    i += 1

	#######################
	# Resource Contacts
	#######################
    contactIdent1 = add_element(doc, "gmd:pointOfContact", dataIdent1MD)
    responsibleIdent1CI = add_element(doc, "gmd:CI_ResponsibleParty", contactIdent1)
    organisationIdent1 = add_element(doc, "gmd:organisationName", responsibleIdent1CI)
    add_element(doc, "gco:CharacterString", organisationIdent1, self.ro_responsibleParty_ln.text())
    contactIdent2 = add_element(doc, "gmd:contactInfo", responsibleIdent1CI)
    responsibleIdent2CI = add_element(doc, "gmd:CI_Contact", contactIdent2)
    addressIdent1 = add_element(doc, "gmd:address", responsibleIdent2CI)
    addressIdent1CI = add_element(doc, "gmd:CI_Address", addressIdent1)
    emailIdent1 = add_element(doc, "gmd:electronicMailAddress", addressIdent1CI)
    add_element(doc, "gco:CharacterString", emailIdent1, self.ro_responsibleEmail_ln.text())
    roleIdent1 = add_element(doc, "gmd:role", responsibleIdent1CI)
    query = sql_valueRead(self, 'languageRole', 'Id', self.ro_responsibleRole_rl1.currentText())
    roleCodeIdent1 = add_element(doc, "gmd:CI_RoleCode", roleIdent1, query[0][1])
    roleCodeIdent1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode")
    roleCodeIdent1.setAttribute("codeListValue", query[0][1])
    if self.ro_roPy > 0:
	i = 0
	for item in self.ro_rlPy_ln:
	    contactIdent1 = add_element(doc, "gmd:pointOfContact", dataIdent1MD)
	    responsibleIdent1CI = add_element(doc, "gmd:CI_ResponsibleParty", contactIdent1)
	    organisationIdent1 = add_element(doc, "gmd:organisationName", responsibleIdent1CI)
	    add_element(doc, "gco:CharacterString", organisationIdent1, self.ro_rlPy_ln[i].text())
	    contactIdent2 = add_element(doc, "gmd:contactInfo", responsibleIdent1CI)
	    responsibleIdent2CI = add_element(doc, "gmd:CI_Contact", contactIdent2)
	    addressIdent1 = add_element(doc, "gmd:address", responsibleIdent2CI)
	    addressIdent1CI = add_element(doc, "gmd:CI_Address", addressIdent1)
	    emailIdent1 = add_element(doc, "gmd:electronicMailAddress", addressIdent1CI)
	    add_element(doc, "gco:CharacterString", emailIdent1, self.ro_rlEm_ln[i].text())
	    roleIdent1 = add_element(doc, "gmd:role", responsibleIdent1CI)
	    query = sql_valueRead(self, 'languageRole', 'Id', self.ro_rlRl_ln[i].currentText())
	    roleCodeIdent1 = add_element(doc, "gmd:CI_RoleCode", roleIdent1, query[0][1])
	    roleCodeIdent1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode")
	    roleCodeIdent1.setAttribute("codeListValue", query[0][1])
	    i += 1
    
    
    ############################
    # Hierarchy Level
    ############################
    hierarchyLevel1 = add_element(doc, "gmd:hierarchyLevel", doc_root)
    scopeLevel1MD = add_element(doc, "gmd:MD_ScopeCode", hierarchyLevel1, self.id_resourceType_rl1.currentText().toLower())
    scopeLevel1MD.setAttribute("codeList","http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ScopeCode")
    scopeLevel1MD.setAttribute("codeListValue", self.id_resourceType_rl1.currentText().toLower())
    
    
    ############################
    # Distribution Info
    ############################
    distributionInfo1 = add_element(doc, "gmd:distributionInfo", doc_root)
    distributionInfo1MD = add_element(doc, "gmd:MD_Distribution", distributionInfo1)
    transferInfo1 = add_element(doc, "gmd:transferOptions", distributionInfo1MD)
    transferInfo1MD = add_element(doc, "gmd:MD_DigitalTransferOptions", transferInfo1)
    onlineInfo1 = add_element(doc, "gmd:onLine", transferInfo1MD)
    onlineInfo1CI = add_element(doc, "gmd:CI_OnlineResource", onlineInfo1)
    linkageInfo1 = add_element(doc, "gmd:linkage", onlineInfo1CI)
    add_element(doc, "gmd:URL", linkageInfo1, self.id_resourceLocator_ln.text())
    
    
    ############################
    # Language Info
    ############################
    query = sql_valueRead(self, 'languageRole', 'Id', self.mm_language_rl1.currentText())
    languageInfo1 = add_element(doc, "gmd:language", doc_root)
    languageInfo2 = add_element(doc, "gmd:LanguageCode", languageInfo1, query[0][1])
    languageInfo2.setAttribute("codeList","http://www.loc.gov/standards/iso639-2/")
    languageInfo2.setAttribute("codeListValue", query[0][1])


    ############################
    # Data Quality
    ############################
    qualityInfo1 = add_element(doc, "gmd:dataQualityInfo", doc_root)
    dataQuality1DQ = add_element(doc, "gmd:DQ_DataQuality", qualityInfo1)
    lineageQuality1 = add_element(doc, "gmd:lineage", dataQuality1DQ)
    lineageQuality1LI = add_element(doc, "gmd:LI_Lineage", lineageQuality1)
    statementQuality1 = add_element(doc, "gmd:statement", lineageQuality1LI)
    add_element(doc, "gco:CharacterString", statementQuality1, "validated")
    reportQuality1 = add_element(doc, "gmd:report", dataQuality1DQ)
    domainConsistency1DQ = add_element(doc, "gmd:DQ_DomainConsistency", reportQuality1)
    resultQuality1 = add_element(doc, "gmd:result", domainConsistency1DQ)
    conformanceResult1DQ = add_element(doc, "gmd:DQ_ConformanceResult", resultQuality1)
    specificationQuality1 = add_element(doc, "gmd:specification", conformanceResult1DQ)
    citationQuality1CI = add_element(doc, "gmd:CI_Citation", specificationQuality1)
    titleQuality1 = add_element(doc, "gmd:title", citationQuality1CI)
    add_element(doc, "gco:CharacterString", titleQuality1, "COMMISSION REGULATION (EC) No 1205/2008 of 3 December 2008 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards metadata")
    dateQuality1 = add_element(doc, "gmd:date", citationQuality1CI)
    dateQuality1CI = add_element(doc, "gmd:CI_Date", dateQuality1)
    dateQuality2 = add_element(doc, "gmd:date", dateQuality1CI)
    add_element(doc, "gco:Date", dateQuality2, "2008-12-04")
    dateType1 = add_element(doc, "gmd:dateType", dateQuality1CI)
    dateTypeCode1 = add_element(doc, "gmd:CI_DateTypeCode", dateType1, "publication")
    dateTypeCode1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode")
    dateTypeCode1.setAttribute("codeListValue", "publication")
    passQuality1 = add_element(doc, "gmd:pass", conformanceResult1DQ)
    add_element(doc, "gco:Boolean", passQuality1, "True")


    ############################
    # Aircraft and Instruments
    ############################
    query = sql_valueRead(self, 'languageRole', 'Id', self.ai_label_9.text())
    acquisitionInfo1 = add_element(doc, "gmd:acquisitionInfo", doc_root)
    aircraftInfo1 = add_element(doc, "gmd:platformInfo", acquisitionInfo1)
    aircraftInfo1AI = add_element(doc, "gmd:PI_PlatformInfo", aircraftInfo1)
    aircraftManufacturer = add_element(doc, "gmd:PlatformManufacturer", aircraftInfo1AI)
    add_element(doc, "gco:CharacterString", aircraftManufacturer, self.ai_label_7.text())
    aircraftType = add_element(doc, "gmd:platformType", aircraftInfo1AI)
    add_element(doc, "gco:CharacterString", aircraftType, self.ai_label_8.text())
    aircraftOperator = add_element(doc, "gmd:platformOperator", aircraftInfo1AI)
    if query:
	add_element(doc, "gco:CharacterString", aircraftOperator, query[0][1])
    else:
	add_element(doc, "gco:CharacterString", aircraftOperator, "")
    aircraftRegistration = add_element(doc, "gmd:platformRegistration", aircraftInfo1AI)
    add_element(doc, "gco:CharacterString", aircraftRegistration, self.ai_label_11.text())
	    

    ############################
    # Contact Info
    ############################
    contactContact1 = add_element(doc, "gmd:contact", doc_root)
    responsiblePartyInfo1CI = add_element(doc, "gmd:CI_ResponsibleParty", contactContact1)
    nameContact1 = add_element(doc, "gmd:organisationName", responsiblePartyInfo1CI)
    add_element(doc, "gco:CharacterString", nameContact1, self.mm_contactName_ln.text())
    infoContact1 = add_element(doc, "gmd:contactInfo", responsiblePartyInfo1CI)
    infoContact1CI = add_element(doc, "gmd:CI_Contact", infoContact1)
    addressContact1 = add_element(doc, "gmd:address", infoContact1CI)
    addressContact1CI = add_element(doc, "gmd:CI_Address", addressContact1)
    emailContact1 = add_element(doc, "gmd:electronicMailAddress", addressContact1CI)
    add_element(doc, "gco:CharacterString", emailContact1, self.mm_contactEmail_ln.text())
    roleContact1 = add_element(doc, "gmd:role", responsiblePartyInfo1CI)
    roleCodeContact1 = add_element(doc, "gmd:CI_RoleCode", roleContact1, "pointOfContact")
    roleCodeContact1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode")
    roleCodeContact1.setAttribute("codeListValue", "pointOfContact")
    if self.mm_pofc > 0:
	i = 0
	for item in self.mm_conName_ln:
	    contactContact1 = add_element(doc, "gmd:contact", doc_root)
	    responsiblePartyInfo1CI = add_element(doc, "gmd:CI_ResponsibleParty", contactContact1)
	    nameContact1 = add_element(doc, "gmd:organisationName", responsiblePartyInfo1CI)
	    add_element(doc, "gco:CharacterString", nameContact1, self.mm_conName_ln[i].text())
	    infoContact1 = add_element(doc, "gmd:contactInfo", responsiblePartyInfo1CI)
	    infoContact1CI = add_element(doc, "gmd:CI_Contact", infoContact1)
	    addressContact1 = add_element(doc, "gmd:address", infoContact1CI)
	    addressContact1CI = add_element(doc, "gmd:CI_Address", addressContact1)
	    emailContact1 = add_element(doc, "gmd:electronicMailAddress", addressContact1CI)
	    add_element(doc, "gco:CharacterString", emailContact1, self.mm_conEmail_ln[i].text())
	    roleContact1 = add_element(doc, "gmd:role", responsiblePartyInfo1CI)
	    roleCodeContact1 = add_element(doc, "gmd:CI_RoleCode", roleContact1, "pointOfContact")
	    roleCodeContact1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode")
	    roleCodeContact1.setAttribute("codeListValue", "pointOfContact")
	    i += 1


    ############################
    # Metadata Date
    ############################
    dateStamp1 = add_element(doc, "gmd:dateStamp", doc_root)
    add_element(doc, "gco:Date", dateStamp1, self.mm_date_do1.date().toString(Qt.ISODate))

   
    ############################
    # File Creation
    ############################
    f = open(out_file_name, 'w')
    f.write(doc.toprettyxml(encoding='UTF-8'))
    f.close()
    self.saved = True
    self.modified = False


def read_eufar_xml(self, in_file_name):
    currentIndex = self.toolBox.currentIndex()
    f = open(in_file_name, 'r')
    doc = xml.dom.minidom.parse(f)


    ############################
    # Identification Info
    ############################
	# Citation
	########################
    doc_root = get_element(doc, "gmd:MD_Metadata")
    identificationIdent1 = get_element(doc_root, "gmd:identificationInfo")
    dataIdent1MD = get_element(identificationIdent1, "gmd:MD_DataIdentification")
    citationIdent1 = get_element(dataIdent1MD, "gmd:citation")
    citationIdent1CI = get_element(citationIdent1, "gmd:CI_Citation")
    titleIdent1 = get_element(citationIdent1CI, "gmd:title")
    set_text_value(self.id_resourceTitle_ln, titleIdent1, "gco:CharacterString")
    identifierIdent1 = get_element(citationIdent1CI, "gmd:identifier")
    identifierIdent1RS = get_element(identifierIdent1, "gmd:RS_Identifier")
    codeIdent = get_element(identifierIdent1RS, "gmd:code")
    set_text_value(self.id_resourceIdent_ln, codeIdent, "gco:CharacterString")
    dateIdent1 = get_element(citationIdent1CI, "gmd:date")
    dateIdent1CI = get_element(dateIdent1, "gmd:CI_Date")
    dateIdent2 = get_element(dateIdent1CI, "gmd:date")
    nodes = citationIdent1CI.getElementsByTagName("gmd:CI_Date")
    elements = []
    for node in nodes:
	tmp1 = get_element(node, "gmd:date")
	elements.append(get_element_value(tmp1, "gco:Date"))
    self.tr_datePublication_do1.setDate(QDate.fromString(elements[0], Qt.ISODate))
    self.tr_dateRevision_do2.setDate(QDate.fromString(elements[1], Qt.ISODate))
    self.tr_dateCreation_do3.setDate(QDate.fromString(elements[2], Qt.ISODate))
    
	########################
	# Abstract
	########################
    abstractIdent = get_element(dataIdent1MD, "gmd:abstract")
    set_plainText_value(self.id_resourceAbstract_ta, abstractIdent, "gco:CharacterString")
    
	#######################
	# Topics
	#######################
    all_check_boxes = self.findChildren(QCheckBox)
    for widget in all_check_boxes:
	if widget.objectName()[0:3] == "cl_":
	    for nodes in doc.getElementsByTagName("gmd:topicCategory"):
		node = get_element_value(nodes, "gmd:MD_TopicCategoryCode")
		query = sql_valueRead(self, 'topics', 'Value', node)
		if query[0][0] == widget.text():
		    widget.setChecked(True)

	#######################
	# Temporal Extent
	#######################
    self.toolBox.setCurrentIndex(5)
    nodes = doc_root.getElementsByTagName("gml:TimePeriod")
    starts = []
    ends = []
    for node in nodes:
	starts.append(get_element_value(node, "gml:beginPosition"))
	ends.append(get_element_value(node, "gml:endPosition"))
    self.tr_dateStart_do4.setDate(QDate.fromString(starts[0], Qt.ISODate))
    self.tr_dateEnd_do5.setDate(QDate.fromString(ends[0], Qt.ISODate))
    if len(nodes) > 1:
	i = 0
	for node in nodes[:-1]:
	    button_functions.plusButton_3_clicked(self)
	    self.tr_dtSt_1[i].setDate(QDate.fromString(starts[i + 1], Qt.ISODate))
	    self.tr_dtEd_1[i].setDate(QDate.fromString(ends[i + 1], Qt.ISODate))
	    i += 1

	#######################
	# Resource Constraints
	#######################
    self.toolBox.setCurrentIndex(7)
    nodes = doc_root.getElementsByTagName("gmd:useLimitation")
    set_plainText_value(self.au_conditions_ta, nodes[0], "gco:CharacterString")
    if len(nodes) > 1:
	i = 0
	for node in nodes[1:]:
	    button_functions.plusButton_5_clicked(self)
	    set_plainText_value(self.au_wn_con_ta[i], nodes[i + 1], "gco:CharacterString")
	    i += 1
    nodes = doc_root.getElementsByTagName("gmd:otherConstraints")
    set_plainText_value(self.au_limitations_ta, nodes[0], "gco:CharacterString")
    if len(nodes) > 1:
	i = 0
	for node in nodes[1:]:
	    button_functions.plusButton_6_clicked(self)
	    set_plainText_value(self.au_wn_lim_ta[i], nodes[i + 1], "gco:CharacterString")
	    i += 1

	#######################
	# Resource Contacts
	#######################
    self.toolBox.setCurrentIndex(8)
    nodes = doc_root.getElementsByTagName("gmd:pointOfContact")
    responsibleIdent1CI = get_element(nodes[0], "gmd:CI_ResponsibleParty")
    organisationIdent1 = get_element(responsibleIdent1CI, "gmd:organisationName")
    set_text_value(self.ro_responsibleParty_ln, organisationIdent1, "gco:CharacterString")
    contactIdent2 = get_element(responsibleIdent1CI, "gmd:contactInfo", )
    responsibleIdent2CI = get_element(contactIdent2, "gmd:CI_Contact", )
    addressIdent1 = get_element(responsibleIdent2CI, "gmd:address", )
    addressIdent1CI = get_element(addressIdent1, "gmd:CI_Address", )
    emailIdent1 = get_element(addressIdent1CI, "gmd:electronicMailAddress", )
    set_text_value(self.ro_responsibleEmail_ln, emailIdent1, "gco:CharacterString")
    roleIdent1 = get_element(responsibleIdent1CI, "gmd:role", )
    combo_text = get_element_value(roleIdent1, "gmd:CI_RoleCode")
    query = sql_valueRead(self, 'languageRole', 'Short', combo_text)
    self.ro_responsibleRole_rl1.setCurrentIndex(self.ro_responsibleRole_rl1.findText(query[0][0]))
    if len(nodes) > 1:
	i = 0
	for node in nodes[1:]:
	    button_functions.plusButton_7_clicked(self)
	    responsibleIdent1CI = get_element(nodes[i + 1], "gmd:CI_ResponsibleParty")
	    organisationIdent1 = get_element(responsibleIdent1CI, "gmd:organisationName")
	    set_text_value(self.ro_rlPy_ln[i], organisationIdent1, "gco:CharacterString")
	    contactIdent2 = get_element(responsibleIdent1CI, "gmd:contactInfo", )
	    responsibleIdent2CI = get_element(contactIdent2, "gmd:CI_Contact", )
	    addressIdent1 = get_element(responsibleIdent2CI, "gmd:address", )
	    addressIdent1CI = get_element(addressIdent1, "gmd:CI_Address", )
	    emailIdent1 = get_element(addressIdent1CI, "gmd:electronicMailAddress", )
	    set_text_value(self.ro_rlEm_ln[i], emailIdent1, "gco:CharacterString")
	    roleIdent1 = get_element(responsibleIdent1CI, "gmd:role", )
	    combo_text = get_element_value(roleIdent1, "gmd:CI_RoleCode")
	    query = sql_valueRead(self, 'languageRole', 'Short', combo_text)
	    self.ro_rlRl_ln[i].setCurrentIndex(self.ro_rlRl_ln[i].findText(query[0][0]))
	    i += 1
	    
	#######################
	# Keywords
	#######################
    descriptiveKeywordIdent1 = get_element(dataIdent1MD, "gmd:descriptiveKeywords")
    keywordIdent1MD = get_element(descriptiveKeywordIdent1, "gmd:MD_Keywords")
    for widget in all_check_boxes:
	if widget.objectName()[0:3] == "kw_":
	    query = sql_valueRead(self, 'scienceKeywords', 'Labels', widget.objectName())
	    if query:
		for nodes in keywordIdent1MD.getElementsByTagName("gmd:keyword"):
		    node = get_element_value(nodes, "gco:CharacterString")
		    if query[0][1] == node:
			widget.setChecked(True)

	#######################
	# Location Extent
	#######################
    extentIdent1 = get_element(dataIdent1MD, "gmd:extent")
    extentIdent1EX = get_element(extentIdent1, "gmd:EX_Extent")
    extentDescription = get_element(extentIdent1EX, "gmd:description")
    combo_text = get_element_value(extentDescription, "gco:CharacterString")
    query = sql_valueRead(self, 'emcLocations', 'Detail', combo_text)
    self.gl_category_rl1.setCurrentIndex(self.gl_category_rl1.findText(query[0][0]))
    gl_categoryRolebox_changed(self)
    self.gl_details_rl2.setCurrentIndex(self.gl_details_rl2.findText(query[0][1]))
    geographicIdent1 = get_element(extentIdent1EX, "gmd:geographicElement")
    geographicIdent1EX = get_element(geographicIdent1, "gmd:EX_GeographicBoundingBox")
    westBoundIdent = get_element(geographicIdent1EX, "gmd:westBoundLongitude")
    set_text_value(self.gl_westBound_ln, westBoundIdent, "gco:Decimal")
    eastBoundIdent = get_element(geographicIdent1EX, "gmd:eastBoundLongitude")
    set_text_value(self.gl_eastBound_ln, eastBoundIdent, "gco:Decimal")
    northBoundIdent = get_element(geographicIdent1EX, "gmd:northBoundLatitude")
    set_text_value(self.gl_northBound_ln, northBoundIdent, "gco:Decimal")
    southBoundIdent = get_element(geographicIdent1EX, "gmd:southBoundLatitude")
    set_text_value(self.gl_southBound_ln, southBoundIdent, "gco:Decimal")
    
  
	#######################
	# Spatial Resolution
	#######################
    resolutionIdent1 = get_element(dataIdent1MD, "gmd:spatialResolution")
    resolutionIdent1MD = get_element(resolutionIdent1, "gmd:MD_Resolution")
    test = resolutionIdent1MD.getElementsByTagName("gmd:equivalentScale")
    if test:
	self.gl_resolution_rl1.setCurrentIndex(self.gl_resolution_rl1.findText("Scale"))
	button_functions.gl_rolebox_changed(self)
	distscaleIdent1 = get_element(resolutionIdent1MD, "gmd:equivalentScale")
	fractionIdent1MD = get_element(distscaleIdent1, "gmd:MD_RepresentativeFraction")
	denominatorIdent1 = get_element(fractionIdent1MD, "gmd:denominator")
	set_text_value(self.gl_resolution_ln, denominatorIdent1, "gco:Integer")
    else:
	self.gl_resolution_rl1.setCurrentIndex(self.gl_resolution_rl1.findText("Distance"))
	button_functions.gl_rolebox_changed(self)
	distscaleIdent1 = get_element(resolutionIdent1MD, "gmd:distance")
	set_text_value(self.gl_resolution_ln, distscaleIdent1, "gco:Distance")
	tmp = distscaleIdent1.getElementsByTagName("gco:Distance")
	distanceIdent2 = tmp[0]
	distAttr = distanceIdent2.attributes["uom"]
	self.gl_unit_ln.setText(distAttr.value)

	########################
	# Language
	######################## 
    nodes = doc_root.getElementsByTagName("gmd:language")
    combo_text = get_element_value(nodes[0], "gmd:LanguageCode")
    query = sql_valueRead(self, 'languageRole', 'Short', combo_text)
    self.id_resourceLang_rl2.setCurrentIndex(self.id_resourceLang_rl2.findText(query[0][0]))


    ############################
    # Hierarchy Level
    ############################
    hierarchyLevel = get_element(doc_root, "gmd:hierarchyLevel")
    combo_text = get_element_value(hierarchyLevel, "gmd:MD_ScopeCode")
    self.id_resourceType_rl1.setCurrentIndex(self.id_resourceType_rl1.findText(combo_text.title()))
    

    ############################
    # Distribution Info
    ############################
    distributionInfo1 = get_element(doc_root, "gmd:distributionInfo")
    distributionInfo1MD = get_element(distributionInfo1, "gmd:MD_Distribution")
    transferInfo1 = get_element(distributionInfo1MD, "gmd:transferOptions")
    transferInfo1MD = get_element(transferInfo1, "gmd:MD_DigitalTransferOptions")
    onlineInfo1 = get_element(transferInfo1MD, "gmd:onLine")
    onlineInfo1CI = get_element(onlineInfo1, "gmd:CI_OnlineResource")
    linkageInfo1 = get_element(onlineInfo1CI, "gmd:linkage")
    set_text_value(self.id_resourceLocator_ln, linkageInfo1, "gmd:URL")
    
   
    ############################
    # Language Info
    ############################
    nodes = doc_root.getElementsByTagName("gmd:language")
    combo_text = get_element_value(nodes[1], "gmd:LanguageCode")
    query = sql_valueRead(self, 'languageRole', 'Short', combo_text)
    self.mm_language_rl1.setCurrentIndex(self.mm_language_rl1.findText(query[0][0]))
    
  
    ############################
    # Contact Info
    ############################
    self.toolBox.setCurrentIndex(9)
    nodes = doc_root.getElementsByTagName("gmd:contact")
    responsiblePartyInfo1CI = get_element(nodes[0], "gmd:CI_ResponsibleParty")
    nameContact1 = get_element(responsiblePartyInfo1CI, "gmd:organisationName")
    set_text_value(self.mm_contactName_ln, nameContact1, "gco:CharacterString")
    infoContact1 = get_element(responsiblePartyInfo1CI, "gmd:contactInfo")
    infoContact1CI = get_element(infoContact1, "gmd:CI_Contact")
    addressContact1 = get_element(infoContact1CI, "gmd:address")
    addressContact1CI = get_element(addressContact1, "gmd:CI_Address")
    emailContact1 = get_element(addressContact1CI, "gmd:electronicMailAddress")
    set_text_value(self.mm_contactEmail_ln, emailContact1, "gco:CharacterString")
    if len(nodes) > 1:
	i = 0
	for node in nodes[1:]:
	    button_functions.plusButton_8_clicked(self)
	    responsiblePartyInfo1CI = get_element(nodes[i + 1], "gmd:CI_ResponsibleParty")
	    nameContact1 = get_element(responsiblePartyInfo1CI, "gmd:organisationName")
	    set_text_value(self.mm_conName_ln[i], nameContact1, "gco:CharacterString")
	    infoContact1 = get_element(responsiblePartyInfo1CI, "gmd:contactInfo")
	    infoContact1CI = get_element(infoContact1, "gmd:CI_Contact")
	    addressContact1 = get_element(infoContact1CI, "gmd:address")
	    addressContact1CI = get_element(addressContact1, "gmd:CI_Address")
	    emailContact1 = get_element(addressContact1CI, "gmd:electronicMailAddress")
	    set_text_value(self.mm_conEmail_ln[i], emailContact1, "gco:CharacterString")
	    i += 1
  

    ############################
    # Data Quality
    ############################
    qualityInfo1 = get_element(doc_root, "gmd:dataQualityInfo")
    dataQuality1DQ = get_element(qualityInfo1, "gmd:DQ_DataQuality")
    lineageQuality1 = get_element(dataQuality1DQ, "gmd:lineage")
    lineageQuality1LI = get_element(lineageQuality1, "gmd:LI_Lineage")
    statementQuality1 = get_element(lineageQuality1LI, "gmd:statement")
    #set_plainText_value(self.qv_lineage_ta, statementQuality1, "gco:CharacterString")


    ############################
    # Aircraft and Instruments
    ############################
    self.toolBox.setCurrentIndex(3)
    acquisitionInfo1 = get_element(doc_root, "gmd:acquisitionInfo")
    aircraftInfo1 = get_element(acquisitionInfo1, "gmd:platformInfo")
    aircraftInfo11AI = get_element(aircraftInfo1, "gmd:PI_PlatformInfo")
    aircraftRegistration = get_element(aircraftInfo11AI, "gmd:platformRegistration")
    areg = get_element_value(aircraftRegistration, "gco:CharacterString")
    if areg:
	query = sql_valueRead(self, "aircraftInformations", "Code", unicode(areg))
	self.ai_aircraft_rl1.setCurrentIndex(self.ai_aircraft_rl1.findText(query[0][0]))
	ai_aircraftRolebox_changed(self)

  
    ############################
    # Metadata Date
    ############################
    dateStamp1 = get_element(doc_root, "gmd:dateStamp")
    date = get_element_value(dateStamp1, "gco:Date")
    self.mm_date_do1.setDate(QDate.fromString(date, Qt.ISODate))

    self.toolBox.setCurrentIndex(currentIndex)


def get_element(parent, element_name):
    return parent.getElementsByTagName(element_name)[0]


def get_element_value(parent, element_name):
    elements = parent.getElementsByTagName(element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()


def set_text_value(text_widget, parent, element_name):
    node_data = get_element_value(parent, element_name)
    if node_data:
        text_widget.setText(node_data)


def set_plainText_value(text_widget, parent, element_name):
    node_data = get_element_value(parent, element_name)
    if node_data:
        text_widget.setPlainText(node_data)


def add_element(doc, element_name, parent, value=None):
    new_element = doc.createElement(element_name)
    if value:
        new_text = doc.createTextNode(unicode(value))
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element