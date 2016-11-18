# -*- coding: utf-8 -*-

import xml.dom.minidom
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QCheckBox, QWidget
from functions import button_functions
from functions.sql_functions import sql_valueRead
from functions.button_functions import gl_categoryRolebox_changed
from functions.button_functions import qv_output_other
from functions.button_functions import plusButton_12_clicked
from functions.button_functions import plusButton_11_clicked
from ui.Ui_aboutwindow import Ui_aboutWindow


def create_eufar_xml(self, out_file_name):
    NAMESPACE_URI1 = "http://www.isotc211.org/2005/gmd"
    NAMESPACE_URI2 = "http://www.isotc211.org/2005/gco"
    NAMESPACE_URI3 = "http://www.opengis.net/gml"
    NAMESPACE_URI4 = "http://www.w3.org/2001/XMLSchema-instance"
    NAMESPACE_URI5 = "http://www.isotc211.org/2005/srv"
    NAMESPACE_URI6 = "http://www.w3.org/1999/xlink"
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
    add_element(doc, "gco:Date", dateIdent2, QDate.currentDate().toString(Qt.ISODate))
    dateTypeIdent1 = add_element(doc, "gmd:dateType", dateIdent1CI)
    dateTypeCodeIdent1CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent1, "publication")
    dateTypeCodeIdent1CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableS"
                                      + "tandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodeli"
                                      + "sts.xml#CI_DateTypeCode")
    dateTypeCodeIdent1CI.setAttribute("codeListValue","publication")
    dateIdent3 = add_element(doc, "gmd:date", citationIdent1CI)
    dateIdent2CI = add_element(doc, "gmd:CI_Date", dateIdent3)
    dateIdent4 = add_element(doc, "gmd:date", dateIdent2CI)
    add_element(doc, "gco:Date", dateIdent4, self.tr_dateRevision_do2.date().toString(Qt.ISODate))
    dateTypeIdent2 = add_element(doc, "gmd:dateType", dateIdent2CI)
    dateTypeCodeIdent2CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent2, "revision")
    dateTypeCodeIdent2CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableS"
                                      + "tandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodeli"
                                      + "sts.xml#CI_DateTypeCode")
    dateTypeCodeIdent2CI.setAttribute("codeListValue","revision")
    dateIdent5 = add_element(doc, "gmd:date", citationIdent1CI)
    dateIdent3CI = add_element(doc, "gmd:CI_Date", dateIdent5)
    dateIdent6 = add_element(doc, "gmd:date", dateIdent3CI)
    add_element(doc, "gco:Date", dateIdent6, self.tr_dateCreation_do3.date().toString(Qt.ISODate))
    dateTypeIdent3 = add_element(doc, "gmd:dateType", dateIdent3CI)
    dateTypeCodeIdent3CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent3, "creation")
    dateTypeCodeIdent3CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableS"
                                      + "tandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodeli"
                                      + "sts.xml#CI_DateTypeCode")
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
    add_element(doc, "gco:CharacterString", titleKeywordIdent1, "NASA/Global Change Master Director"
                + "y (GCMD) Earth Science Keywords. Version 8.0.0.0.0")
    dateIdent7 = add_element(doc, "gmd:date", citationKeywordIdent1CI)
    dateIdent4CI = add_element(doc, "gmd:CI_Date", dateIdent7)
    dateIdent8 = add_element(doc, "gmd:date", dateIdent4CI)
    add_element(doc, "gco:Date", dateIdent8, "2015-02-20")
    dateTypeIdent4 = add_element(doc, "gmd:dateType", dateIdent4CI)
    dateTypeCodeIdent4CI = add_element(doc, "gmd:CI_DateTypeCode", dateTypeIdent4, "revision")
    dateTypeCodeIdent4CI.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableS"
                                      + "tandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodeli"
                                      + "sts.xml#CI_DateTypeCode")
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
    add_element(doc, "gml:beginPosition", periodIdent1, self.tr_dateStart_do4.date().
                toString(Qt.ISODate))
    add_element(doc, "gml:endPosition", periodIdent1, self.tr_dateEnd_do5.date().
                toString(Qt.ISODate))
    if self.tr_tpex > 0:
        i = 0
        for item in self.tr_dtSt_1:  # @UnusedVariable
            temporalIdent1 = add_element(doc, "gmd:temporalElement", extentIdent1EX)
            temporalIdent1EX = add_element(doc, "gmd:EX_TemporalExtent", temporalIdent1)
            extentIdent3 = add_element(doc, "gmd:extent", temporalIdent1EX)
            periodIdent1 = add_element(doc, "gml:TimePeriod", extentIdent3)
            periodIdent1.setAttribute("gml:id","extent" + str(i + 1))
            add_element(doc, "gml:beginPosition", periodIdent1, self.tr_dtSt_1[i].date().
                        toString(Qt.ISODate))
            add_element(doc, "gml:endPosition", periodIdent1, self.tr_dtEd_1[i].date().
                        toString(Qt.ISODate))
            i += 1
   
    #######################
    # Spatial Resolution
    #######################
    resolutionIdent1 = add_element(doc, "gmd:spatialResolution", dataIdent1MD)
    resolutionIdent1MD = add_element(doc, "gmd:MD_Resolution", resolutionIdent1)
    if self.gl_resolution_rl1.currentText() == 'Distance':
        distanceIdent1 = add_element(doc, "gmd:distance", resolutionIdent1MD)
        distanceIdent2 = add_element(doc, "gco:Distance", distanceIdent1, self.gl_resolution_ln.
                                     text())
        if self.gl_unit_rl.currentText() == "Make a choice...":
            distanceIdent2.setAttribute("uom", "")
        else:
            query = sql_valueRead(self, 'unit', 'Main', self.gl_unit_rl.currentText())
            distanceIdent2.setAttribute("uom", query[0][1])
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
        for item in self.au_wn_con_ta:  # @UnusedVariable
            useIdent1 = add_element(doc, "gmd:useLimitation", constraintIdent1MD)
            add_element(doc, "gco:CharacterString", useIdent1, self.au_wn_con_ta[i].toPlainText())
            i += 1
    constraintIdent2 = add_element(doc, "gmd:resourceConstraints", dataIdent1MD)
    legalIdent1MD = add_element(doc, "gmd:MD_LegalConstraints", constraintIdent2)
    accessIdent1 = add_element(doc, "gmd:accessConstraints", legalIdent1MD)
    restrictionIdent1MD = add_element(doc, "gmd:MD_RestrictionCode", accessIdent1, "otherRestrictions")
    restrictionIdent1MD.setAttribute("codeList","http://standards.iso.org/ittf/PubliclyAvailableSta"
                                     + "ndards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xm"
                                     + "l#MD_RestrictionCode")
    restrictionIdent1MD.setAttribute("codeListValue","otherRestrictions")
    accessIdent2 = add_element(doc, "gmd:otherConstraints", legalIdent1MD)
    add_element(doc, "gco:CharacterString", accessIdent2, self.au_limitations_ta.toPlainText())
    if self.au_wn_1 > 0:
        i = 0
        for item in self.au_wn_lim_ta:  # @UnusedVariable
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
    roleCodeIdent1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandar"
                                + "ds/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_Role"
                                + "Code")
    roleCodeIdent1.setAttribute("codeListValue", query[0][1])
    if self.ro_roPy > 0:
        i = 0
        for item in self.ro_rlPy_ln:  # @UnusedVariable
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
            roleCodeIdent1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailabl"
                                        + "eStandards/ISO_19139_Schemas/resources/Codelist/gmxCodel"
                                        + "ists.xml#CI_RoleCode")
            roleCodeIdent1.setAttribute("codeListValue", query[0][1])
            i += 1
    
    
    ############################
    # Hierarchy Level
    ############################
    hierarchyLevel1 = add_element(doc, "gmd:hierarchyLevel", doc_root)
    scopeLevel1MD = add_element(doc, "gmd:MD_ScopeCode", hierarchyLevel1, self.id_resourceType_rl1.
                                currentText().lower())
    scopeLevel1MD.setAttribute("codeList","http://standards.iso.org/ittf/PubliclyAvailableStandards"
                               + "/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ScopeCode")
    scopeLevel1MD.setAttribute("codeListValue", self.id_resourceType_rl1.currentText().lower())
    
    
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
    stringBuilder = []
    for i in range(len(self.qv_insitu_tab_1)):
        stringBuilder.append(save_statement_insitu(self, i))
    for i in range(len(self.qv_imagery_tab_1)):
        stringBuilder.append(save_statement_imagery(self, i))
    statement = ''.join(stringBuilder)
    qualityInfo1 = add_element(doc, "gmd:dataQualityInfo", doc_root)
    dataQuality1DQ = add_element(doc, "gmd:DQ_DataQuality", qualityInfo1)
    lineageQuality1 = add_element(doc, "gmd:lineage", dataQuality1DQ)
    lineageQuality1LI = add_element(doc, "gmd:LI_Lineage", lineageQuality1)
    statementQuality1 = add_element(doc, "gmd:statement", lineageQuality1LI)
    '''if self.qv_obsRadio.isChecked() == False and self.qv_insituRadio.isChecked() == False:
        statement = ""
    else:
        statement = self.save_statement()'''
    add_element(doc, "gco:CharacterString", statementQuality1, statement)
    reportQuality1 = add_element(doc, "gmd:report", dataQuality1DQ)
    domainConsistency1DQ = add_element(doc, "gmd:DQ_DomainConsistency", reportQuality1)
    resultQuality1 = add_element(doc, "gmd:result", domainConsistency1DQ)
    conformanceResult1DQ = add_element(doc, "gmd:DQ_ConformanceResult", resultQuality1)
    specificationQuality1 = add_element(doc, "gmd:specification", conformanceResult1DQ)
    citationQuality1CI = add_element(doc, "gmd:CI_Citation", specificationQuality1)
    titleQuality1 = add_element(doc, "gmd:title", citationQuality1CI)
    add_element(doc, "gco:CharacterString", titleQuality1, "COMMISSION REGULATION (EC) No 1205/2008"
                + " of 3 December 2008 implementing Directive 2007/2/EC of the European Parliament "
                + "and of the Council as regards metadata")
    dateQuality1 = add_element(doc, "gmd:date", citationQuality1CI)
    dateQuality1CI = add_element(doc, "gmd:CI_Date", dateQuality1)
    dateQuality2 = add_element(doc, "gmd:date", dateQuality1CI)
    add_element(doc, "gco:Date", dateQuality2, "2008-12-04")
    dateType1 = add_element(doc, "gmd:dateType", dateQuality1CI)
    dateTypeCode1 = add_element(doc, "gmd:CI_DateTypeCode", dateType1, "publication")
    dateTypeCode1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStandard"
                               + "s/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_Dat"
                               + "eTypeCode")
    dateTypeCode1.setAttribute("codeListValue", "publication")
    passQuality1 = add_element(doc, "gmd:pass", conformanceResult1DQ)
    add_element(doc, "gco:Boolean", passQuality1, "True")


    ############################
    # Aircraft and Instruments
    ############################
    acquisitionInfo1 = add_element(doc, "gmd:acquisitionInfo", doc_root)
    for sublist in self.aircraft_list:
        aircraftInfo1 = add_element(doc, "gmd:platformInfo", acquisitionInfo1)
        aircraftInfo1AI = add_element(doc, "gmd:PI_PlatformInfo", aircraftInfo1)
        aircraftManufacturer = add_element(doc, "gmd:platformManufacturer", aircraftInfo1AI)
        add_element(doc, "gco:CharacterString", aircraftManufacturer, sublist[0])
        aircraftType = add_element(doc, "gmd:platformType", aircraftInfo1AI)
        add_element(doc, "gco:CharacterString", aircraftType, sublist[1])
        aircraftOperator = add_element(doc, "gmd:platformOperator", aircraftInfo1AI)
        add_element(doc, "gco:CharacterString", aircraftOperator, sublist[2])
        aircraftCountry = add_element(doc, "gmd:platformCountry", aircraftInfo1AI)
        add_element(doc, "gco:CharacterString", aircraftCountry, sublist[3])
        aircraftRegistration = add_element(doc, "gmd:platformRegistration", aircraftInfo1AI)
        add_element(doc, "gco:CharacterString", aircraftRegistration, sublist[4])
    for i in range(0, len(self.instModel_list)):
            instrumentInfo1 = add_element(doc, "gmd:instrumentInfo", acquisitionInfo1)
            instrumentInfo1II = add_element(doc, "gmd:II_InstrumentInfo", instrumentInfo1)
            instrumentManufacturer = add_element(doc, "gmd:instrumentManufacturer", instrumentInfo1II)
            instrumentType = add_element(doc, "gmd:instrumentType", instrumentInfo1II)
            add_element(doc, "gco:CharacterString", instrumentManufacturer, self.instManufacturer_list[i])
            add_element(doc, "gco:CharacterString", instrumentType, self.instModel_list[i])


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
    roleCodeContact1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvailableStand"
                                  + "ards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_"
                                  + "RoleCode")
    roleCodeContact1.setAttribute("codeListValue", "pointOfContact")
    if self.mm_pofc > 0:
        i = 0
        for item in self.mm_conName_ln:  # @UnusedVariable
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
            roleCodeContact1.setAttribute("codeList", "http://standards.iso.org/ittf/PubliclyAvaila"
                                          + "bleStandards/ISO_19139_Schemas/resources/Codelist/gmxC"
                                          + "odelists.xml#CI_RoleCode")
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
    f = open(out_file_name, 'wb')
    f.write(doc.toprettyxml(indent="    ", encoding="UTF-8"))
    f.close()
    self.saved = True
    self.modified = False


def read_eufar_xml(self, in_file_name):
    currentIndex = self.tabWidget.currentIndex()
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
    nodes = citationIdent1CI.getElementsByTagName("gmd:CI_Date")
    elements = []
    for node in nodes:
        tmp1 = get_element(node, "gmd:date")
        elements.append(get_element_value(tmp1, "gco:Date"))
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
    self.tabWidget.setCurrentIndex(5)
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
    self.tabWidget.setCurrentIndex(7)
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
    self.tabWidget.setCurrentIndex(8)
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
    if combo_text:
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
        distAttr = distanceIdent2.attributes["uom"].value
        query = sql_valueRead(self, 'unit', 'Short', distAttr)
        self.gl_unit_rl.setCurrentIndex(self.gl_unit_rl.findText(query[0][0]))

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
    self.tabWidget.setCurrentIndex(9)
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
    # Aircraft and Instruments
    ############################
    self.tabWidget.setCurrentIndex(3)
    nodes = doc_root.getElementsByTagName("gmd:platformInfo")
    if len(nodes) > 0:
        i = 0
        for i in range(0, len(nodes)):
            aircraftInfo11AI = get_element(nodes[i], "gmd:PI_PlatformInfo")
            aircraftRegistration = get_element(aircraftInfo11AI, "gmd:platformRegistration")
            aircraftManufacturer = get_element(aircraftInfo11AI, "gmd:platformManufacturer")
            aircraftType = get_element(aircraftInfo11AI, "gmd:platformType")
            aircraftOperator = get_element(aircraftInfo11AI, "gmd:platformOperator")
            aircraftCountry = get_element(aircraftInfo11AI, "gmd:platformCountry")
            manufacturer = get_element_value(aircraftManufacturer, "gco:CharacterString")
            aircraft = get_element_value(aircraftType, "gco:CharacterString")
            operator = get_element_value(aircraftOperator, "gco:CharacterString")
            identification = get_element_value(aircraftRegistration, "gco:CharacterString")
            country = get_element_value(aircraftCountry, "gco:CharacterString")
            button_functions.plusButton_10_clicked(self, aircraft, operator, manufacturer, identification, country)
    nodes = doc_root.getElementsByTagName("gmd:instrumentInfo")
    if len(nodes) > 0:
        i = 0
        for i in range(0, len(nodes)):
            instrument1AI = get_element(nodes[i], "gmd:II_InstrumentInfo")
            instrumentManufacturer = get_element(instrument1AI, "gmd:instrumentManufacturer")
            manufacturer = get_element_value(instrumentManufacturer, "gco:CharacterString")
            instrumentModel = get_element(instrument1AI, "gmd:instrumentType")
            model = get_element_value(instrumentModel, "gco:CharacterString")
            button_functions.plusButton_4_clicked(self, manufacturer + " - " + model)
    
    
    ############################
    # Data Quality
    ############################
    old_format = 0
    self.tabWidget.setCurrentIndex(6)
    qualityInfo1 = get_element(doc_root, "gmd:dataQualityInfo")
    dataQuality1DQ = get_element(qualityInfo1, "gmd:DQ_DataQuality")
    lineageQuality1 = get_element(dataQuality1DQ, "gmd:lineage")
    lineageQuality1LI = get_element(lineageQuality1, "gmd:LI_Lineage")
    statementQuality1 = get_element(lineageQuality1LI, "gmd:statement")
    statement = get_element_value(statementQuality1, "gco:CharacterString")
    if statement != "" and statement != None:
        stringList = []
        indexStart = statement.find("[", 0)
        if indexStart != -1:
            indexEnd = statement.find("]", 0)
            stringList.append(statement[indexStart + 1 : indexEnd])
            indexStart += 1
            indexEnd += 1
            while indexStart < len(statement):
                indexStart = statement.find("[", indexStart)
                if indexStart == -1:
                    break
                indexEnd = statement.find("]", indexEnd)
                stringList.append(statement[indexStart + 1 : indexEnd])
                indexStart += 1
                indexEnd += 1
            indexInsitu = 0
            indexImagery = 0
            for string in stringList:
                if "Atmospheric" in string:
                    plusButton_12_clicked(self)
                    read_statement_insitu(self, string, indexInsitu)
                    indexInsitu += 1
                elif "Earth" in string:
                    plusButton_11_clicked(self)
                    read_statement_imagery(self, string, indexImagery)
                    indexImagery += 1
        else:
            old_format = 1
            if "Atmospheric" in statement:
                plusButton_12_clicked(self)
                read_statement_insitu_old(self, statement, 0)
            elif "Earth" in statement:
                plusButton_11_clicked(self)
                read_statement_imagery_old(self, statement, 0)
  
  
    ############################
    # Metadata Date
    ############################
    dateStamp1 = get_element(doc_root, "gmd:dateStamp")
    date = get_element_value(dateStamp1, "gco:Date")
    self.mm_date_do1.setDate(QDate.fromString(date, Qt.ISODate))

    self.tabWidget.setCurrentIndex(currentIndex)
    if old_format == 1:
        self.aboutWindow = MyAbout()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()  # @UnusedVariable
        self.aboutWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()


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
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element

def save_statement_imagery(self, index):
    statement = "[Earth observation/Remote sensing data " + str(index + 1) + "|Instrument: "
    if self.qv_imagery_list_2[index].currentText() == "Make a choice...":
        instrument = ""
    else:
        instrument = str(self.qv_imagery_list_2[index].currentText())
    statement = statement + instrument + "|Name of calibration laboratory: "
    statement = statement + str(self.qv_imagery_line_1[index].text()) + "|Date of radiometric calibration: "
    statement = statement + str(self.qv_imagery_date_1[index].date().toString(Qt.ISODate)) + "|Date of spectral calibration: "
    statement = statement + str(self.qv_imagery_date_2[index].date().toString(Qt.ISODate)) + "|Number of spectral bands: "
    statement = statement + str(self.qv_imagery_line_2[index].text()) + "|Overall heading / fligh direction (dd): "
    statement = statement + str(self.qv_imagery_line_3[index].text()) + "|Overall altitude / average height ASL (m): "
    statement = statement + str(self.qv_imagery_line_4[index].text()) + "|Solar zenith (dd): "
    statement = statement + str(self.qv_imagery_line_5[index].text()) + "|Solar azimuth (dd): "
    statement = statement + str(self.qv_imagery_line_6[index].text()) + "|Report anomalies in data acquisition: "
    statement = statement + str(self.qv_imagery_line_7[index].text()) + "|Processing level: "
    if self.qv_imagery_list_1[index].currentText() == "Make a choice...":
        choice = ""
    else:
        choice = self.qv_imagery_list_1[index].currentText()
    statement = statement + choice + "|Dark current (DC) correction: "
    statement = statement + getAnswer(self.qv_imagery_check_1[index], self.qv_imagery_check_2[index])
    statement = statement + "|Aggregated interpolated pixel mask: "
    statement = statement + getAnswer(self.qv_imagery_check_3[index], self.qv_imagery_check_4[index])
    statement = statement + "|Aggregated bad pixel mask: "
    statement = statement + getAnswer(self.qv_imagery_check_5[index], self.qv_imagery_check_6[index])
    statement = statement + "|Saturated pixels / overflow: "
    statement = statement + getAnswer(self.qv_imagery_check_7[index], self.qv_imagery_check_8[index])
    statement = statement + "|Problems with affected by saturation in spatial/spectral neighbourhood: "
    statement = statement + getAnswer(self.qv_imagery_check_9[index], self.qv_imagery_check_10[index])
    statement = statement + "|Problems with position information / Interpolated position information: "
    statement = statement + getAnswer(self.qv_imagery_check_11[index], self.qv_imagery_check_12[index])
    statement = statement + "|Problems with attitude information / Interpolated attitude information: "
    statement = statement + getAnswer(self.qv_imagery_check_13[index], self.qv_imagery_check_14[index])
    statement = statement + "|Synchronization problems: "
    statement = statement + getAnswer(self.qv_imagery_check_15[index], self.qv_imagery_check_16[index])
    statement = statement + "|Interpolated pixels during geocoding: "
    statement = statement + getAnswer(self.qv_imagery_check_17[index], self.qv_imagery_check_18[index])
    statement = statement + "|Failure of atmospheric correction: "
    statement = statement + getAnswer(self.qv_imagery_check_19[index], self.qv_imagery_check_20[index])
    statement = statement + "|Cloud mask: "
    statement = statement + getAnswer(self.qv_imagery_check_21[index], self.qv_imagery_check_22[index])
    statement = statement + "|Cloud shadow mask: "
    statement = statement + getAnswer(self.qv_imagery_check_23[index], self.qv_imagery_check_24[index])
    statement = statement + "|Haze mask: "
    statement = statement + getAnswer(self.qv_imagery_check_25[index], self.qv_imagery_check_26[index])
    statement = statement + "|Critical terrain correction based on DEM roughness measure: "
    statement = statement + getAnswer(self.qv_imagery_check_27[index], self.qv_imagery_check_28[index])
    statement = statement + "|Critical terrain correction based on slope/local illumination angle: "
    statement = statement + getAnswer(self.qv_imagery_check_29[index], self.qv_imagery_check_30[index])
    statement = statement + "|Critical BRDF geometry based on sun-sensor-terrain geometry: "
    statement = statement + getAnswer(self.qv_imagery_check_31[index], self.qv_imagery_check_32[index])
    statement = statement + "]"
    return statement

def save_statement_insitu(self, index):
    statement = "[Atmospheric/In-situ measurements " + str(index + 1) + "|Instrument: "
    if self.qv_insitu_list_1[index].currentText() == "Make a choice...":
        instrument = ""
    else:
        instrument = str(self.qv_insitu_list_1[index].currentText())
    statement = statement + instrument + "|Link to the procedure's description: "
    statement = statement + str(self.qv_insitu_line_1[index].text()) + "|Source of calibration constants: "
    statement = statement + str(self.qv_insitu_line_2[index].text()) + "|Source of calibration materials: "
    statement = statement + str(self.qv_insitu_line_3[index].text()) + "|Data converted to geophysical units: "
    statement = statement + getAnswer(self.qv_insitu_round_1[index], self.qv_insitu_round_2[index]) + "|Output format: "
    format_list = []
    answer = ""
    if self.qv_insitu_check_1[index].isChecked() == True:
        format_list.append("NetCDF")
    if self.qv_insitu_check_3[index].isChecked() == True:
        format_list.append("HDF")
    if self.qv_insitu_check_2[index].isChecked() == True: 
        format_list.append("NASA/Ames")
    if self.qv_insitu_check_4[index].isChecked() == True: 
        format_list.append("Other/" + self.qv_insitu_line_4[index].text())
    if len(format_list) > 1:
        for item in format_list:
            answer = answer + item + "; "
        answer = answer[:-2]
    elif len(format_list) == 1:
        answer = format_list[0]
    statement = statement + answer + "|Quality-control flagging applied to individual data points: "
    statement = statement + str(self.qv_insitu_area_1[index].toPlainText()) + "|Assumption: "
    statement = statement + str(self.qv_insitu_area_2[index].toPlainText()) + "]"
    return statement

def read_statement_imagery(self, statement, index):
    stringList = []
    indexStart = statement.find(":", 40)
    indexEnd = statement.find("|", 40)
    stringList.append(statement[indexStart + 2 : indexEnd])
    indexStart += 1
    indexEnd += 1
    while indexStart < len(statement):
        indexStart = statement.find(":", indexStart)
        if indexStart == -1:
            break
        indexEnd = statement.find("|", indexEnd)
        if indexEnd == -1:
            stringList.append(statement[indexStart + 2 :])
        else:
            stringList.append(statement[indexStart + 2 : indexEnd])
        indexStart += 1
        indexEnd += 1
    if self.qv_imagery_list_2[index].findText(stringList[0]) == -1:
        self.qv_imagery_list_2[index].setCurrentIndex(0)
    else:
        self.qv_imagery_list_2[index].setCurrentIndex(self.qv_imagery_list_2[index].findText(stringList[0]))
    self.qv_imagery_line_1[index].setText(stringList[1])
    self.qv_imagery_date_1[index].setDate(QDate.fromString(stringList[2], Qt.ISODate))
    self.qv_imagery_date_2[index].setDate(QDate.fromString(stringList[3], Qt.ISODate))
    self.qv_imagery_line_2[index].setText(stringList[4])
    self.qv_imagery_line_3[index].setText(stringList[5])
    self.qv_imagery_line_4[index].setText(stringList[6])
    self.qv_imagery_line_5[index].setText(stringList[7])
    self.qv_imagery_line_6[index].setText(stringList[8])
    self.qv_imagery_line_7[index].setText(stringList[9])
    if self.qv_imagery_list_1[index].findText(stringList[10]) == -1:
        self.qv_imagery_list_1[index].setCurrentIndex(0)
    else:
        self.qv_imagery_list_1[index].setCurrentIndex(self.qv_imagery_list_1[index].findText(stringList[10]))
    pushAnswer(self.qv_imagery_check_1[index], self.qv_imagery_check_2[index], stringList[11])
    pushAnswer(self.qv_imagery_check_3[index], self.qv_imagery_check_4[index], stringList[12])
    pushAnswer(self.qv_imagery_check_5[index], self.qv_imagery_check_6[index], stringList[13])
    pushAnswer(self.qv_imagery_check_7[index], self.qv_imagery_check_8[index], stringList[14])
    pushAnswer(self.qv_imagery_check_9[index], self.qv_imagery_check_10[index], stringList[15])
    pushAnswer(self.qv_imagery_check_11[index], self.qv_imagery_check_12[index], stringList[16])
    pushAnswer(self.qv_imagery_check_13[index], self.qv_imagery_check_14[index], stringList[17])
    pushAnswer(self.qv_imagery_check_15[index], self.qv_imagery_check_16[index], stringList[18])
    pushAnswer(self.qv_imagery_check_17[index], self.qv_imagery_check_18[index], stringList[19])
    pushAnswer(self.qv_imagery_check_19[index], self.qv_imagery_check_20[index], stringList[20])
    pushAnswer(self.qv_imagery_check_21[index], self.qv_imagery_check_22[index], stringList[21])
    pushAnswer(self.qv_imagery_check_23[index], self.qv_imagery_check_24[index], stringList[22])
    pushAnswer(self.qv_imagery_check_25[index], self.qv_imagery_check_26[index], stringList[23])
    pushAnswer(self.qv_imagery_check_27[index], self.qv_imagery_check_28[index], stringList[24])
    pushAnswer(self.qv_imagery_check_29[index], self.qv_imagery_check_30[index], stringList[25])
    pushAnswer(self.qv_imagery_check_31[index], self.qv_imagery_check_32[index], stringList[26])
    
def read_statement_imagery_old(self, statement, index):
    stringList = []
    indexStart = statement.find(":", 40)
    indexEnd = statement.find("|", 40)
    stringList.append(statement[indexStart + 2 : indexEnd])
    indexStart += 1
    indexEnd += 1
    while indexStart < len(statement):
        indexStart = statement.find(":", indexStart)
        if indexStart == -1:
            break
        indexEnd = statement.find("|", indexEnd)
        if indexEnd == -1:
            stringList.append(statement[indexStart + 2 :])
        else:
            stringList.append(statement[indexStart + 2 : indexEnd])
        indexStart += 1
        indexEnd += 1
    self.qv_imagery_line_1[index].setText(stringList[0])
    self.qv_imagery_date_1[index].setDate(QDate.fromString(stringList[1], Qt.ISODate))
    self.qv_imagery_date_2[index].setDate(QDate.fromString(stringList[2], Qt.ISODate))
    self.qv_imagery_line_2[index].setText(stringList[3])
    self.qv_imagery_line_3[index].setText(stringList[4])
    self.qv_imagery_line_4[index].setText(stringList[5])
    self.qv_imagery_line_5[index].setText(stringList[6])
    self.qv_imagery_line_6[index].setText(stringList[7])
    self.qv_imagery_line_7[index].setText(stringList[8])
    if self.qv_imagery_list_1[index].findText(stringList[9]) == -1:
        self.qv_imagery_list_1[index].setCurrentIndex(0)
    else:
        self.qv_imagery_list_1[index].setCurrentIndex(self.qv_imagery_list_1[index].findText(stringList[9]))
    pushAnswer(self.qv_imagery_check_1[index], self.qv_imagery_check_2[index], stringList[10])
    pushAnswer(self.qv_imagery_check_3[index], self.qv_imagery_check_4[index], stringList[11])
    pushAnswer(self.qv_imagery_check_5[index], self.qv_imagery_check_6[index], stringList[12])
    pushAnswer(self.qv_imagery_check_7[index], self.qv_imagery_check_8[index], stringList[13])
    pushAnswer(self.qv_imagery_check_9[index], self.qv_imagery_check_10[index], stringList[14])
    pushAnswer(self.qv_imagery_check_11[index], self.qv_imagery_check_12[index], stringList[15])
    pushAnswer(self.qv_imagery_check_13[index], self.qv_imagery_check_14[index], stringList[16])
    pushAnswer(self.qv_imagery_check_15[index], self.qv_imagery_check_16[index], stringList[17])
    pushAnswer(self.qv_imagery_check_17[index], self.qv_imagery_check_18[index], stringList[18])
    pushAnswer(self.qv_imagery_check_19[index], self.qv_imagery_check_20[index], stringList[19])
    pushAnswer(self.qv_imagery_check_21[index], self.qv_imagery_check_22[index], stringList[20])
    pushAnswer(self.qv_imagery_check_23[index], self.qv_imagery_check_24[index], stringList[21])
    pushAnswer(self.qv_imagery_check_25[index], self.qv_imagery_check_26[index], stringList[22])
    pushAnswer(self.qv_imagery_check_27[index], self.qv_imagery_check_28[index], stringList[23])
    pushAnswer(self.qv_imagery_check_29[index], self.qv_imagery_check_30[index], stringList[24])
    pushAnswer(self.qv_imagery_check_31[index], self.qv_imagery_check_32[index], stringList[25])
    
def read_statement_insitu(self, statement, index):
    stringList = []
    indexStart = statement.find(":", 35)
    indexEnd = statement.find("|", 35)
    stringList.append(statement[indexStart + 2 : indexEnd])
    indexStart += 1
    indexEnd += 1
    while indexStart < len(statement):
        indexStart = statement.find(":", indexStart)
        if indexStart == -1:
            break
        indexEnd = statement.find("|", indexEnd)
        if indexEnd == -1:
            stringList.append(statement[indexStart + 2 :])
        else:
            stringList.append(statement[indexStart + 2 : indexEnd])
        indexStart += 1
        indexEnd += 1  
    if self.qv_insitu_list_1[index].findText(stringList[0]) == -1:
        self.qv_insitu_list_1[index].setCurrentIndex(0)
    else:
        self.qv_insitu_list_1[index].setCurrentIndex(self.qv_insitu_list_1[index].findText(stringList[0]))
    self.qv_insitu_line_1[index].setText(stringList[1])
    self.qv_insitu_line_2[index].setText(stringList[2])
    self.qv_insitu_line_3[index].setText(stringList[3])
    pushAnswer(self.qv_insitu_round_1[index], self.qv_insitu_round_2[index], stringList[4])
    if "NetCDF" in stringList[5]:
        self.qv_insitu_check_1[index].setChecked(True)
    if "HDF" in stringList[5]:
        self.qv_insitu_check_3[index].setChecked(True)
    if "NASA/Ames" in stringList[5]:
        self.qv_insitu_check_2[index].setChecked(True)
    if "Other" in stringList[5]:
        self.qv_insitu_check_4[index].setChecked(True)
        qv_output_other(self, index)
        findOther = stringList[5].find("Other")
        self.qv_insitu_line_4[index].setText(stringList[5][findOther + 6 :])
    self.qv_insitu_area_1[index].setPlainText(stringList[6])
    self.qv_insitu_area_2[index].setPlainText(stringList[7])
    
def read_statement_insitu_old(self, statement, index):
    stringList = []
    indexStart = statement.find(":", 35)
    indexEnd = statement.find("|", 35)
    stringList.append(statement[indexStart + 2 : indexEnd])
    indexStart += 1
    indexEnd += 1
    while indexStart < len(statement):
        indexStart = statement.find(":", indexStart)
        if indexStart == -1:
            break
        indexEnd = statement.find("|", indexEnd)
        if indexEnd == -1:
            stringList.append(statement[indexStart + 2 :])
        else:
            stringList.append(statement[indexStart + 2 : indexEnd])
        indexStart += 1
        indexEnd += 1  
    self.qv_insitu_line_1[index].setText(stringList[0])
    self.qv_insitu_line_2[index].setText(stringList[1])
    self.qv_insitu_line_3[index].setText(stringList[2])
    pushAnswer(self.qv_insitu_round_1[index], self.qv_insitu_round_2[index], stringList[3])
    if "NetCDF" in stringList[4]:
        self.qv_insitu_check_1[index].setChecked(True)
    if "HDF" in stringList[4]:
        self.qv_insitu_check_3[index].setChecked(True)
    if "NASA/Ames" in stringList[4]:
        self.qv_insitu_check_2[index].setChecked(True)
    if "Other" in stringList[4]:
        self.qv_insitu_check_4[index].setChecked(True)
        qv_output_other(self, index)
        findOther = stringList[4].find("Other")
        self.qv_insitu_line_4[index].setText(stringList[4][findOther + 6 :])
    self.qv_insitu_area_1[index].setPlainText(stringList[5])
    self.qv_insitu_area_2[index].setPlainText(stringList[6])

def getAnswer(radioButton1, radioButton2):
    answer = ""
    if radioButton1.isChecked() == True:
        answer = "yes"
    elif radioButton2.isChecked() == True:
        answer = "no"
    return answer

def pushAnswer(radioButton1, radioButton2, answer):
    if answer == "yes":
        radioButton1.setChecked(True)
    elif answer == "no":
        radioButton2.setChecked(True)


class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        aboutText = ("<html><head/><body><p align=justify>The EMC has detected that the Quality and "
                + "Validity section of your XML file has been produced with an old version of the EM"
                + "C. Since the version 1.1.0, the XML code for the Quality and Validity section has"
                + " been replaced to take into account multiple instruments and multiple forms.</p><"
                + "span align=justify>All Quality and Validity data in the XML file have been loaded"
                + " into a new form. In order to convert the old XML code to the new one, <b>after s"
                + "electing an instrument in your Quality and Validity form</b>, please save your do"
                + "cument to a new file.</span>")
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)
        self.aw_okButton.setFocus(True)
        self.aw_label_2.setPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Old Quality & Validity section detected")

    def closeWindow(self):
        self.close()