# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work\LAND_MANAGER\lm2\view\SentToGovernorDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_SentToGovernorDialog(object):
    def setupUi(self, SentToGovernorDialog):
        SentToGovernorDialog.setObjectName(_fromUtf8("SentToGovernorDialog"))
        SentToGovernorDialog.resize(840, 582)
        SentToGovernorDialog.setMinimumSize(QtCore.QSize(840, 582))
        SentToGovernorDialog.setMaximumSize(QtCore.QSize(840, 700))
        self.line = QtGui.QFrame(SentToGovernorDialog)
        self.line.setGeometry(QtCore.QRect(0, 20, 856, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(SentToGovernorDialog)
        self.line_2.setGeometry(QtCore.QRect(0, 578, 833, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.close_button = QtGui.QPushButton(SentToGovernorDialog)
        self.close_button.setGeometry(QtCore.QRect(760, 550, 75, 23))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.label_12 = QtGui.QLabel(SentToGovernorDialog)
        self.label_12.setGeometry(QtCore.QRect(7, 2, 161, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.help_button = QtGui.QPushButton(SentToGovernorDialog)
        self.help_button.setGeometry(QtCore.QRect(680, 551, 75, 23))
        self.help_button.setObjectName(_fromUtf8("help_button"))
        self.tabWidget = QtGui.QTabWidget(SentToGovernorDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 834, 271))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_20 = QtGui.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(11, 1, 321, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.drafts_edit = QtGui.QLineEdit(self.tab)
        self.drafts_edit.setGeometry(QtCore.QRect(6, 21, 231, 20))
        self.drafts_edit.setReadOnly(True)
        self.drafts_edit.setObjectName(_fromUtf8("drafts_edit"))
        self.drafts_twidget = QtGui.QTableWidget(self.tab)
        self.drafts_twidget.setGeometry(QtCore.QRect(6, 50, 329, 190))
        self.drafts_twidget.setObjectName(_fromUtf8("drafts_twidget"))
        self.drafts_twidget.setColumnCount(1)
        self.drafts_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.drafts_twidget.setHorizontalHeaderItem(0, item)
        self.drafts_twidget.horizontalHeader().setDefaultSectionSize(328)
        self.select_app_count = QtGui.QLabel(self.tab)
        self.select_app_count.setGeometry(QtCore.QRect(697, -1, 31, 20))
        self.select_app_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.select_app_count.setObjectName(_fromUtf8("select_app_count"))
        self.app_count_lbl = QtGui.QLabel(self.tab)
        self.app_count_lbl.setGeometry(QtCore.QRect(731, -1, 31, 20))
        self.app_count_lbl.setObjectName(_fromUtf8("app_count_lbl"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(342, 138, 481, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(221, 17, 191, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.draft_no_edit = QtGui.QLineEdit(self.groupBox)
        self.draft_no_edit.setGeometry(QtCore.QRect(19, 35, 90, 20))
        self.draft_no_edit.setObjectName(_fromUtf8("draft_no_edit"))
        self.doc_print_button = QtGui.QPushButton(self.groupBox)
        self.doc_print_button.setGeometry(QtCore.QRect(380, 70, 92, 23))
        self.doc_print_button.setObjectName(_fromUtf8("doc_print_button"))
        self.decision_level_cbox = QtGui.QComboBox(self.groupBox)
        self.decision_level_cbox.setGeometry(QtCore.QRect(220, 35, 251, 22))
        self.decision_level_cbox.setObjectName(_fromUtf8("decision_level_cbox"))
        self.sent_to_governor_button = QtGui.QPushButton(self.groupBox)
        self.sent_to_governor_button.setGeometry(QtCore.QRect(120, 70, 141, 23))
        self.sent_to_governor_button.setObjectName(_fromUtf8("sent_to_governor_button"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(115, 17, 91, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.draft_print_button = QtGui.QPushButton(self.groupBox)
        self.draft_print_button.setGeometry(QtCore.QRect(270, 70, 101, 23))
        self.draft_print_button.setObjectName(_fromUtf8("draft_print_button"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 17, 101, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.draft_date = QtGui.QDateEdit(self.groupBox)
        self.draft_date.setGeometry(QtCore.QRect(115, 35, 90, 22))
        self.draft_date.setCalendarPopup(True)
        self.draft_date.setObjectName(_fromUtf8("draft_date"))
        self.new_group_box = QtGui.QGroupBox(self.tab)
        self.new_group_box.setGeometry(QtCore.QRect(343, 16, 480, 122))
        self.new_group_box.setObjectName(_fromUtf8("new_group_box"))
        self.search_button = QtGui.QPushButton(self.new_group_box)
        self.search_button.setGeometry(QtCore.QRect(340, 78, 132, 23))
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.begin_date = QtGui.QDateEdit(self.new_group_box)
        self.begin_date.setGeometry(QtCore.QRect(20, 35, 90, 22))
        self.begin_date.setCalendarPopup(True)
        self.begin_date.setObjectName(_fromUtf8("begin_date"))
        self.end_date = QtGui.QDateEdit(self.new_group_box)
        self.end_date.setGeometry(QtCore.QRect(20, 78, 90, 22))
        self.end_date.setCalendarPopup(True)
        self.end_date.setObjectName(_fromUtf8("end_date"))
        self.app_type_cbox = QtGui.QComboBox(self.new_group_box)
        self.app_type_cbox.setGeometry(QtCore.QRect(130, 35, 341, 22))
        self.app_type_cbox.setObjectName(_fromUtf8("app_type_cbox"))
        self.label_6 = QtGui.QLabel(self.new_group_box)
        self.label_6.setGeometry(QtCore.QRect(20, 17, 96, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.new_group_box)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_11 = QtGui.QLabel(self.new_group_box)
        self.label_11.setGeometry(QtCore.QRect(130, 17, 226, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.officer_cbox = QtGui.QComboBox(self.new_group_box)
        self.officer_cbox.setGeometry(QtCore.QRect(130, 78, 195, 22))
        self.officer_cbox.setObjectName(_fromUtf8("officer_cbox"))
        self.label_17 = QtGui.QLabel(self.new_group_box)
        self.label_17.setGeometry(QtCore.QRect(130, 60, 226, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(561, 1, 131, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.drafts_path_button = QtGui.QPushButton(self.tab)
        self.drafts_path_button.setGeometry(QtCore.QRect(245, 20, 91, 23))
        self.drafts_path_button.setObjectName(_fromUtf8("drafts_path_button"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.drafts_twidget_2 = QtGui.QTableWidget(self.tab_2)
        self.drafts_twidget_2.setGeometry(QtCore.QRect(6, 50, 329, 190))
        self.drafts_twidget_2.setObjectName(_fromUtf8("drafts_twidget_2"))
        self.drafts_twidget_2.setColumnCount(1)
        self.drafts_twidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.drafts_twidget_2.setHorizontalHeaderItem(0, item)
        self.drafts_twidget_2.horizontalHeader().setDefaultSectionSize(328)
        self.draft_group_box_2 = QtGui.QGroupBox(self.tab_2)
        self.draft_group_box_2.setGeometry(QtCore.QRect(345, 47, 477, 71))
        self.draft_group_box_2.setObjectName(_fromUtf8("draft_group_box_2"))
        self.decision_number_edit = QtGui.QLineEdit(self.draft_group_box_2)
        self.decision_number_edit.setGeometry(QtCore.QRect(10, 37, 195, 20))
        self.decision_number_edit.setObjectName(_fromUtf8("decision_number_edit"))
        self.label_30 = QtGui.QLabel(self.draft_group_box_2)
        self.label_30.setGeometry(QtCore.QRect(7, 17, 201, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.draft_group_box_2)
        self.label_31.setGeometry(QtCore.QRect(220, 17, 151, 15))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.decision_date = QtGui.QDateEdit(self.draft_group_box_2)
        self.decision_date.setGeometry(QtCore.QRect(220, 37, 90, 22))
        self.decision_date.setCalendarPopup(True)
        self.decision_date.setObjectName(_fromUtf8("decision_date"))
        self.change_button = QtGui.QPushButton(self.draft_group_box_2)
        self.change_button.setGeometry(QtCore.QRect(330, 36, 141, 24))
        self.change_button.setObjectName(_fromUtf8("change_button"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(345, 126, 475, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_29 = QtGui.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(10, 16, 321, 20))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.decision_save_edit = QtGui.QLineEdit(self.groupBox_2)
        self.decision_save_edit.setGeometry(QtCore.QRect(10, 40, 299, 20))
        self.decision_save_edit.setReadOnly(True)
        self.decision_save_edit.setObjectName(_fromUtf8("decision_save_edit"))
        self.decision_save_button = QtGui.QPushButton(self.groupBox_2)
        self.decision_save_button.setGeometry(QtCore.QRect(328, 39, 140, 23))
        self.decision_save_button.setObjectName(_fromUtf8("decision_save_button"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_18 = QtGui.QLabel(SentToGovernorDialog)
        self.label_18.setGeometry(QtCore.QRect(16, 298, 251, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.draft_detail_twidget = QtGui.QTableWidget(SentToGovernorDialog)
        self.draft_detail_twidget.setGeometry(QtCore.QRect(7, 320, 824, 216))
        self.draft_detail_twidget.setDragEnabled(True)
        self.draft_detail_twidget.setAlternatingRowColors(True)
        self.draft_detail_twidget.setObjectName(_fromUtf8("draft_detail_twidget"))
        self.draft_detail_twidget.setColumnCount(13)
        self.draft_detail_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.draft_detail_twidget.setHorizontalHeaderItem(12, item)
        self.draft_detail_twidget.verticalHeader().setCascadingSectionResizes(True)
        self.draft_detail_twidget.verticalHeader().setDefaultSectionSize(30)
        self.draft_detail_twidget.verticalHeader().setMinimumSectionSize(19)
        self.draft_detail_twidget.verticalHeader().setSortIndicatorShown(True)
        self.draft_detail_twidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(SentToGovernorDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SentToGovernorDialog)

    def retranslateUi(self, SentToGovernorDialog):
        SentToGovernorDialog.setWindowTitle(_translate("SentToGovernorDialog", "Dialog", None))
        self.close_button.setText(_translate("SentToGovernorDialog", "Close", None))
        self.label_12.setText(_translate("SentToGovernorDialog", "Sent To Governor", None))
        self.help_button.setText(_translate("SentToGovernorDialog", "?", None))
        self.label_20.setText(_translate("SentToGovernorDialog", "Drafts path", None))
        item = self.drafts_twidget.horizontalHeaderItem(0)
        item.setText(_translate("SentToGovernorDialog", "File Name", None))
        self.select_app_count.setText(_translate("SentToGovernorDialog", "TextLabel", None))
        self.app_count_lbl.setText(_translate("SentToGovernorDialog", "TextLabel", None))
        self.groupBox.setTitle(_translate("SentToGovernorDialog", "Draft Value", None))
        self.label_15.setText(_translate("SentToGovernorDialog", "Decision Level", None))
        self.doc_print_button.setText(_translate("SentToGovernorDialog", "Doc Print", None))
        self.sent_to_governor_button.setText(_translate("SentToGovernorDialog", "Sent to governor", None))
        self.label_14.setText(_translate("SentToGovernorDialog", "Draft Date", None))
        self.draft_print_button.setText(_translate("SentToGovernorDialog", "Draft Print", None))
        self.label_13.setText(_translate("SentToGovernorDialog", "Draft No", None))
        self.draft_date.setDisplayFormat(_translate("SentToGovernorDialog", "yyyy-MM-dd", None))
        self.new_group_box.setTitle(_translate("SentToGovernorDialog", "Application Search", None))
        self.search_button.setText(_translate("SentToGovernorDialog", "Search", None))
        self.begin_date.setDisplayFormat(_translate("SentToGovernorDialog", "yyyy-MM-dd", None))
        self.end_date.setDisplayFormat(_translate("SentToGovernorDialog", "yyyy-MM-dd", None))
        self.label_6.setText(_translate("SentToGovernorDialog", "Begin Date", None))
        self.label_7.setText(_translate("SentToGovernorDialog", "End Date", None))
        self.label_11.setText(_translate("SentToGovernorDialog", "Application Type", None))
        self.label_17.setText(_translate("SentToGovernorDialog", "Officer name", None))
        self.label_16.setText(_translate("SentToGovernorDialog", "Application Count:", None))
        self.drafts_path_button.setText(_translate("SentToGovernorDialog", "Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SentToGovernorDialog", "Decision Draft", None))
        item = self.drafts_twidget_2.horizontalHeaderItem(0)
        item.setText(_translate("SentToGovernorDialog", "File Name", None))
        self.draft_group_box_2.setTitle(_translate("SentToGovernorDialog", "Decision Value", None))
        self.label_30.setText(_translate("SentToGovernorDialog", "Decision Number", None))
        self.label_31.setText(_translate("SentToGovernorDialog", "Decision Date", None))
        self.decision_date.setDisplayFormat(_translate("SentToGovernorDialog", "yyyy-MM-dd", None))
        self.change_button.setText(_translate("SentToGovernorDialog", "change", None))
        self.groupBox_2.setTitle(_translate("SentToGovernorDialog", "Save Decision", None))
        self.label_29.setText(_translate("SentToGovernorDialog", "Decision save path:", None))
        self.decision_save_button.setText(_translate("SentToGovernorDialog", "Decision Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SentToGovernorDialog", "Recieved Decision", None))
        self.label_18.setText(_translate("SentToGovernorDialog", "Application List", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(0)
        item.setText(_translate("SentToGovernorDialog", "Surname/Company Name", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(1)
        item.setText(_translate("SentToGovernorDialog", "First Name", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(2)
        item.setText(_translate("SentToGovernorDialog", "Person Id", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(3)
        item.setText(_translate("SentToGovernorDialog", "Application No", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(4)
        item.setText(_translate("SentToGovernorDialog", "Parcel No", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(5)
        item.setText(_translate("SentToGovernorDialog", "Address", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(6)
        item.setText(_translate("SentToGovernorDialog", "Area [m2]", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(7)
        item.setText(_translate("SentToGovernorDialog", "Land Use Type", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(8)
        item.setText(_translate("SentToGovernorDialog", "Decision No", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(9)
        item.setText(_translate("SentToGovernorDialog", "Decision Date", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(10)
        item.setText(_translate("SentToGovernorDialog", "Decision Level", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(11)
        item.setText(_translate("SentToGovernorDialog", "Decision Result", None))
        item = self.draft_detail_twidget.horizontalHeaderItem(12)
        item.setText(_translate("SentToGovernorDialog", "Duration", None))

