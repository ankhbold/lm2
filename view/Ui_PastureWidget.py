# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work\LAND_MANAGER\lm2\view\PastureWidget.ui'
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

class Ui_PastureWidget(object):
    def setupUi(self, PastureWidget):
        PastureWidget.setObjectName(_fromUtf8("PastureWidget"))
        PastureWidget.resize(415, 711)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PastureWidget.sizePolicy().hasHeightForWidth())
        PastureWidget.setSizePolicy(sizePolicy)
        PastureWidget.setMinimumSize(QtCore.QSize(415, 620))
        PastureWidget.setMaximumSize(QtCore.QSize(415, 524287))
        PastureWidget.setBaseSize(QtCore.QSize(415, 665))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 411, 650))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 550))
        self.scrollArea.setMaximumSize(QtCore.QSize(435, 650))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -33, 419, 664))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 386, 600))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 600))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.pasture_tab = QtGui.QWidget()
        self.pasture_tab.setObjectName(_fromUtf8("pasture_tab"))
        self.groupBox_18 = QtGui.QGroupBox(self.pasture_tab)
        self.groupBox_18.setGeometry(QtCore.QRect(5, 30, 371, 277))
        self.groupBox_18.setAutoFillBackground(False)
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.pasture_parcel_id_edit = QtGui.QLineEdit(self.groupBox_18)
        self.pasture_parcel_id_edit.setGeometry(QtCore.QRect(190, 29, 170, 20))
        self.pasture_parcel_id_edit.setObjectName(_fromUtf8("pasture_parcel_id_edit"))
        self.member_name_edit = QtGui.QLineEdit(self.groupBox_18)
        self.member_name_edit.setGeometry(QtCore.QRect(10, 188, 170, 20))
        self.member_name_edit.setObjectName(_fromUtf8("member_name_edit"))
        self.member_register_edit = QtGui.QLineEdit(self.groupBox_18)
        self.member_register_edit.setGeometry(QtCore.QRect(10, 150, 170, 20))
        self.member_register_edit.setObjectName(_fromUtf8("member_register_edit"))
        self.pasture_contract_no_edit = QtGui.QLineEdit(self.groupBox_18)
        self.pasture_contract_no_edit.setGeometry(QtCore.QRect(190, 188, 170, 20))
        self.pasture_contract_no_edit.setObjectName(_fromUtf8("pasture_contract_no_edit"))
        self.pasture_app_no_edit = QtGui.QLineEdit(self.groupBox_18)
        self.pasture_app_no_edit.setGeometry(QtCore.QRect(190, 150, 170, 20))
        self.pasture_app_no_edit.setObjectName(_fromUtf8("pasture_app_no_edit"))
        self.label_62 = QtGui.QLabel(self.groupBox_18)
        self.label_62.setGeometry(QtCore.QRect(190, 11, 170, 16))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.label_64 = QtGui.QLabel(self.groupBox_18)
        self.label_64.setGeometry(QtCore.QRect(10, 171, 170, 17))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.label_65 = QtGui.QLabel(self.groupBox_18)
        self.label_65.setGeometry(QtCore.QRect(10, 132, 170, 17))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.label_66 = QtGui.QLabel(self.groupBox_18)
        self.label_66.setGeometry(QtCore.QRect(190, 132, 170, 17))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.label_67 = QtGui.QLabel(self.groupBox_18)
        self.label_67.setGeometry(QtCore.QRect(190, 171, 170, 17))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.pasture_app_date_edit = QtGui.QDateEdit(self.groupBox_18)
        self.pasture_app_date_edit.setEnabled(False)
        self.pasture_app_date_edit.setGeometry(QtCore.QRect(190, 215, 91, 21))
        self.pasture_app_date_edit.setCalendarPopup(True)
        self.pasture_app_date_edit.setObjectName(_fromUtf8("pasture_app_date_edit"))
        self.pasture_clear_button = QtGui.QPushButton(self.groupBox_18)
        self.pasture_clear_button.setGeometry(QtCore.QRect(204, 245, 75, 23))
        self.pasture_clear_button.setObjectName(_fromUtf8("pasture_clear_button"))
        self.pasture_find_button = QtGui.QPushButton(self.groupBox_18)
        self.pasture_find_button.setGeometry(QtCore.QRect(290, 245, 75, 23))
        self.pasture_find_button.setDefault(True)
        self.pasture_find_button.setObjectName(_fromUtf8("pasture_find_button"))
        self.pasture_date_cbox = QtGui.QCheckBox(self.groupBox_18)
        self.pasture_date_cbox.setGeometry(QtCore.QRect(12, 216, 171, 20))
        self.pasture_date_cbox.setObjectName(_fromUtf8("pasture_date_cbox"))
        self.pasture_results_label = QtGui.QLabel(self.groupBox_18)
        self.pasture_results_label.setGeometry(QtCore.QRect(10, 247, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pasture_results_label.setFont(font)
        self.pasture_results_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pasture_results_label.setObjectName(_fromUtf8("pasture_results_label"))
        self.label_68 = QtGui.QLabel(self.groupBox_18)
        self.label_68.setGeometry(QtCore.QRect(10, 10, 170, 17))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.pasture_group_cbox = QtGui.QComboBox(self.groupBox_18)
        self.pasture_group_cbox.setGeometry(QtCore.QRect(10, 28, 171, 22))
        self.pasture_group_cbox.setObjectName(_fromUtf8("pasture_group_cbox"))
        self.label_69 = QtGui.QLabel(self.groupBox_18)
        self.label_69.setGeometry(QtCore.QRect(10, 51, 170, 17))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.pasture_landuse_cbox = QtGui.QComboBox(self.groupBox_18)
        self.pasture_landuse_cbox.setGeometry(QtCore.QRect(10, 69, 351, 22))
        self.pasture_landuse_cbox.setObjectName(_fromUtf8("pasture_landuse_cbox"))
        self.pasture_type_cbox = QtGui.QComboBox(self.groupBox_18)
        self.pasture_type_cbox.setGeometry(QtCore.QRect(10, 108, 351, 22))
        self.pasture_type_cbox.setObjectName(_fromUtf8("pasture_type_cbox"))
        self.label_70 = QtGui.QLabel(self.groupBox_18)
        self.label_70.setGeometry(QtCore.QRect(10, 90, 170, 17))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.groupBox_19 = QtGui.QGroupBox(self.pasture_tab)
        self.groupBox_19.setGeometry(QtCore.QRect(6, 305, 371, 241))
        self.groupBox_19.setObjectName(_fromUtf8("groupBox_19"))
        self.pasture_results_twidget = QtGui.QTableWidget(self.groupBox_19)
        self.pasture_results_twidget.setGeometry(QtCore.QRect(5, 20, 361, 155))
        self.pasture_results_twidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.pasture_results_twidget.setObjectName(_fromUtf8("pasture_results_twidget"))
        self.pasture_results_twidget.setColumnCount(0)
        self.pasture_results_twidget.setRowCount(0)
        self.pasture_contract_view_button = QtGui.QPushButton(self.groupBox_19)
        self.pasture_contract_view_button.setGeometry(QtCore.QRect(266, 183, 101, 23))
        self.pasture_contract_view_button.setObjectName(_fromUtf8("pasture_contract_view_button"))
        self.pasture_app_view_button = QtGui.QPushButton(self.groupBox_19)
        self.pasture_app_view_button.setGeometry(QtCore.QRect(130, 183, 111, 23))
        self.pasture_app_view_button.setObjectName(_fromUtf8("pasture_app_view_button"))
        self.pasture_layer_view_button = QtGui.QPushButton(self.groupBox_19)
        self.pasture_layer_view_button.setGeometry(QtCore.QRect(5, 183, 101, 23))
        self.pasture_layer_view_button.setObjectName(_fromUtf8("pasture_layer_view_button"))
        self.error_label = QtGui.QLabel(self.groupBox_19)
        self.error_label.setGeometry(QtCore.QRect(10, 213, 351, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet(_fromUtf8("QLabel {color : red;}\n"
"font: 75 14pt \"Helvetica\";"))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.pug_register_button = QtGui.QPushButton(self.pasture_tab)
        self.pug_register_button.setGeometry(QtCore.QRect(4, 6, 121, 23))
        self.pug_register_button.setObjectName(_fromUtf8("pug_register_button"))
        self.pasture_app_add_button = QtGui.QPushButton(self.pasture_tab)
        self.pasture_app_add_button.setGeometry(QtCore.QRect(141, 6, 111, 23))
        self.pasture_app_add_button.setObjectName(_fromUtf8("pasture_app_add_button"))
        self.draft_decision_button = QtGui.QPushButton(self.pasture_tab)
        self.draft_decision_button.setGeometry(QtCore.QRect(265, 6, 111, 23))
        self.draft_decision_button.setObjectName(_fromUtf8("draft_decision_button"))
        self.tabWidget.addTab(self.pasture_tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.monitoring_load_button = QtGui.QPushButton(self.tab_2)
        self.monitoring_load_button.setGeometry(QtCore.QRect(5, 5, 101, 23))
        self.monitoring_load_button.setObjectName(_fromUtf8("monitoring_load_button"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 30, 381, 541))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_21 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_21.setGeometry(QtCore.QRect(3, 198, 371, 315))
        self.groupBox_21.setObjectName(_fromUtf8("groupBox_21"))
        self.error_label_2 = QtGui.QLabel(self.groupBox_21)
        self.error_label_2.setGeometry(QtCore.QRect(10, 240, 351, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error_label_2.setFont(font)
        self.error_label_2.setStyleSheet(_fromUtf8("QLabel {color : red;}\n"
"font: 75 14pt \"Helvetica\";"))
        self.error_label_2.setText(_fromUtf8(""))
        self.error_label_2.setWordWrap(True)
        self.error_label_2.setObjectName(_fromUtf8("error_label_2"))
        self.points_results_twidget = QtGui.QTableWidget(self.groupBox_21)
        self.points_results_twidget.setGeometry(QtCore.QRect(4, 14, 361, 150))
        self.points_results_twidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.points_results_twidget.setObjectName(_fromUtf8("points_results_twidget"))
        self.points_results_twidget.setColumnCount(0)
        self.points_results_twidget.setRowCount(0)
        self.label_5 = QtGui.QLabel(self.groupBox_21)
        self.label_5.setGeometry(QtCore.QRect(256, 170, 110, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.avg_unelgee_edit = QtGui.QLineEdit(self.groupBox_21)
        self.avg_unelgee_edit.setGeometry(QtCore.QRect(256, 190, 110, 20))
        self.avg_unelgee_edit.setReadOnly(True)
        self.avg_unelgee_edit.setObjectName(_fromUtf8("avg_unelgee_edit"))
        self.label_3 = QtGui.QLabel(self.groupBox_21)
        self.label_3.setGeometry(QtCore.QRect(6, 170, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.avg_d3_edit = QtGui.QLineEdit(self.groupBox_21)
        self.avg_d3_edit.setGeometry(QtCore.QRect(3, 190, 110, 20))
        self.avg_d3_edit.setReadOnly(True)
        self.avg_d3_edit.setObjectName(_fromUtf8("avg_d3_edit"))
        self.label_4 = QtGui.QLabel(self.groupBox_21)
        self.label_4.setGeometry(QtCore.QRect(131, 170, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.avg_sheep_unit_edit = QtGui.QLineEdit(self.groupBox_21)
        self.avg_sheep_unit_edit.setGeometry(QtCore.QRect(130, 190, 110, 20))
        self.avg_sheep_unit_edit.setReadOnly(True)
        self.avg_sheep_unit_edit.setObjectName(_fromUtf8("avg_sheep_unit_edit"))
        self.avg_value_save_button = QtGui.QPushButton(self.groupBox_21)
        self.avg_value_save_button.setEnabled(False)
        self.avg_value_save_button.setGeometry(QtCore.QRect(290, 215, 75, 23))
        self.avg_value_save_button.setObjectName(_fromUtf8("avg_value_save_button"))
        self.point_results_label = QtGui.QLabel(self.tab_3)
        self.point_results_label.setGeometry(QtCore.QRect(7, 182, 146, 16))
        self.point_results_label.setText(_fromUtf8(""))
        self.point_results_label.setObjectName(_fromUtf8("point_results_label"))
        self.groupBox_20 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_20.setGeometry(QtCore.QRect(2, -2, 371, 182))
        self.groupBox_20.setAutoFillBackground(False)
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.point_find_button = QtGui.QPushButton(self.groupBox_20)
        self.point_find_button.setEnabled(False)
        self.point_find_button.setGeometry(QtCore.QRect(280, 148, 75, 23))
        self.point_find_button.setDefault(True)
        self.point_find_button.setObjectName(_fromUtf8("point_find_button"))
        self.label_75 = QtGui.QLabel(self.groupBox_20)
        self.label_75.setGeometry(QtCore.QRect(10, 10, 170, 17))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.daats_level_cbox = QtGui.QComboBox(self.groupBox_20)
        self.daats_level_cbox.setEnabled(False)
        self.daats_level_cbox.setGeometry(QtCore.QRect(10, 28, 171, 22))
        self.daats_level_cbox.setObjectName(_fromUtf8("daats_level_cbox"))
        self.label_76 = QtGui.QLabel(self.groupBox_20)
        self.label_76.setGeometry(QtCore.QRect(10, 51, 170, 17))
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.aimag_cbox = QtGui.QComboBox(self.groupBox_20)
        self.aimag_cbox.setEnabled(False)
        self.aimag_cbox.setGeometry(QtCore.QRect(10, 69, 171, 22))
        self.aimag_cbox.setObjectName(_fromUtf8("aimag_cbox"))
        self.soum_cbox = QtGui.QComboBox(self.groupBox_20)
        self.soum_cbox.setEnabled(False)
        self.soum_cbox.setGeometry(QtCore.QRect(190, 69, 171, 22))
        self.soum_cbox.setObjectName(_fromUtf8("soum_cbox"))
        self.label_78 = QtGui.QLabel(self.groupBox_20)
        self.label_78.setGeometry(QtCore.QRect(190, 51, 170, 17))
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.label_79 = QtGui.QLabel(self.groupBox_20)
        self.label_79.setGeometry(QtCore.QRect(190, 90, 170, 17))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.bag_cbox = QtGui.QComboBox(self.groupBox_20)
        self.bag_cbox.setEnabled(False)
        self.bag_cbox.setGeometry(QtCore.QRect(10, 108, 171, 22))
        self.bag_cbox.setObjectName(_fromUtf8("bag_cbox"))
        self.pug_cbox = QtGui.QComboBox(self.groupBox_20)
        self.pug_cbox.setEnabled(False)
        self.pug_cbox.setGeometry(QtCore.QRect(190, 108, 171, 22))
        self.pug_cbox.setObjectName(_fromUtf8("pug_cbox"))
        self.label_77 = QtGui.QLabel(self.groupBox_20)
        self.label_77.setGeometry(QtCore.QRect(10, 90, 170, 17))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.pug_parcel_cbox = QtGui.QComboBox(self.groupBox_20)
        self.pug_parcel_cbox.setEnabled(False)
        self.pug_parcel_cbox.setGeometry(QtCore.QRect(10, 148, 171, 22))
        self.pug_parcel_cbox.setObjectName(_fromUtf8("pug_parcel_cbox"))
        self.label_81 = QtGui.QLabel(self.groupBox_20)
        self.label_81.setGeometry(QtCore.QRect(10, 130, 170, 17))
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.daats_level_chbox = QtGui.QCheckBox(self.groupBox_20)
        self.daats_level_chbox.setGeometry(QtCore.QRect(190, 30, 171, 17))
        self.daats_level_chbox.setObjectName(_fromUtf8("daats_level_chbox"))
        self.daats_year_sbox = QtGui.QSpinBox(self.groupBox_20)
        self.daats_year_sbox.setGeometry(QtCore.QRect(190, 149, 68, 20))
        self.daats_year_sbox.setMaximum(2200)
        self.daats_year_sbox.setProperty("value", 2017)
        self.daats_year_sbox.setObjectName(_fromUtf8("daats_year_sbox"))
        self.label_51 = QtGui.QLabel(self.tab_3)
        self.label_51.setGeometry(QtCore.QRect(157, 182, 211, 16))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_22 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_22.setGeometry(QtCore.QRect(3, 170, 371, 315))
        self.groupBox_22.setObjectName(_fromUtf8("groupBox_22"))
        self.error_label_3 = QtGui.QLabel(self.groupBox_22)
        self.error_label_3.setGeometry(QtCore.QRect(10, 240, 351, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error_label_3.setFont(font)
        self.error_label_3.setStyleSheet(_fromUtf8("QLabel {color : red;}\n"
"font: 75 14pt \"Helvetica\";"))
        self.error_label_3.setText(_fromUtf8(""))
        self.error_label_3.setWordWrap(True)
        self.error_label_3.setObjectName(_fromUtf8("error_label_3"))
        self.reserve_points_results_twidget = QtGui.QTableWidget(self.groupBox_22)
        self.reserve_points_results_twidget.setGeometry(QtCore.QRect(4, 14, 361, 150))
        self.reserve_points_results_twidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.reserve_points_results_twidget.setObjectName(_fromUtf8("reserve_points_results_twidget"))
        self.reserve_points_results_twidget.setColumnCount(0)
        self.reserve_points_results_twidget.setRowCount(0)
        self.label_6 = QtGui.QLabel(self.groupBox_22)
        self.label_6.setGeometry(QtCore.QRect(256, 170, 110, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.reserve_avg_unelgee_edit = QtGui.QLineEdit(self.groupBox_22)
        self.reserve_avg_unelgee_edit.setGeometry(QtCore.QRect(256, 190, 110, 20))
        self.reserve_avg_unelgee_edit.setReadOnly(True)
        self.reserve_avg_unelgee_edit.setObjectName(_fromUtf8("reserve_avg_unelgee_edit"))
        self.label_7 = QtGui.QLabel(self.groupBox_22)
        self.label_7.setGeometry(QtCore.QRect(6, 170, 121, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.reserve_avg_d3_edit = QtGui.QLineEdit(self.groupBox_22)
        self.reserve_avg_d3_edit.setGeometry(QtCore.QRect(3, 190, 110, 20))
        self.reserve_avg_d3_edit.setReadOnly(True)
        self.reserve_avg_d3_edit.setObjectName(_fromUtf8("reserve_avg_d3_edit"))
        self.label_8 = QtGui.QLabel(self.groupBox_22)
        self.label_8.setGeometry(QtCore.QRect(131, 170, 121, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.reserve_avg_sheep_unit_edit = QtGui.QLineEdit(self.groupBox_22)
        self.reserve_avg_sheep_unit_edit.setGeometry(QtCore.QRect(130, 190, 110, 20))
        self.reserve_avg_sheep_unit_edit.setReadOnly(True)
        self.reserve_avg_sheep_unit_edit.setObjectName(_fromUtf8("reserve_avg_sheep_unit_edit"))
        self.reserve_avg_value_save_button = QtGui.QPushButton(self.groupBox_22)
        self.reserve_avg_value_save_button.setEnabled(False)
        self.reserve_avg_value_save_button.setGeometry(QtCore.QRect(290, 215, 75, 23))
        self.reserve_avg_value_save_button.setObjectName(_fromUtf8("reserve_avg_value_save_button"))
        self.reserve_point_results_label = QtGui.QLabel(self.tab_4)
        self.reserve_point_results_label.setGeometry(QtCore.QRect(7, 150, 146, 16))
        self.reserve_point_results_label.setText(_fromUtf8(""))
        self.reserve_point_results_label.setObjectName(_fromUtf8("reserve_point_results_label"))
        self.groupBox_23 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_23.setGeometry(QtCore.QRect(2, -2, 371, 151))
        self.groupBox_23.setAutoFillBackground(False)
        self.groupBox_23.setObjectName(_fromUtf8("groupBox_23"))
        self.reserve_point_find_button = QtGui.QPushButton(self.groupBox_23)
        self.reserve_point_find_button.setEnabled(False)
        self.reserve_point_find_button.setGeometry(QtCore.QRect(280, 110, 75, 23))
        self.reserve_point_find_button.setDefault(True)
        self.reserve_point_find_button.setObjectName(_fromUtf8("reserve_point_find_button"))
        self.label_80 = QtGui.QLabel(self.groupBox_23)
        self.label_80.setGeometry(QtCore.QRect(10, 50, 170, 17))
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.reserve_zone_cbox = QtGui.QComboBox(self.groupBox_23)
        self.reserve_zone_cbox.setEnabled(False)
        self.reserve_zone_cbox.setGeometry(QtCore.QRect(10, 68, 171, 22))
        self.reserve_zone_cbox.setObjectName(_fromUtf8("reserve_zone_cbox"))
        self.label_82 = QtGui.QLabel(self.groupBox_23)
        self.label_82.setGeometry(QtCore.QRect(10, 91, 170, 17))
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.reserve_parcel_cbox = QtGui.QComboBox(self.groupBox_23)
        self.reserve_parcel_cbox.setEnabled(False)
        self.reserve_parcel_cbox.setGeometry(QtCore.QRect(10, 109, 171, 22))
        self.reserve_parcel_cbox.setObjectName(_fromUtf8("reserve_parcel_cbox"))
        self.reserve_daats_chbox = QtGui.QCheckBox(self.groupBox_23)
        self.reserve_daats_chbox.setGeometry(QtCore.QRect(190, 30, 171, 17))
        self.reserve_daats_chbox.setObjectName(_fromUtf8("reserve_daats_chbox"))
        self.reserver_daats_year_sbox = QtGui.QSpinBox(self.groupBox_23)
        self.reserver_daats_year_sbox.setGeometry(QtCore.QRect(190, 111, 68, 20))
        self.reserver_daats_year_sbox.setMaximum(2200)
        self.reserver_daats_year_sbox.setProperty("value", 2017)
        self.reserver_daats_year_sbox.setObjectName(_fromUtf8("reserver_daats_year_sbox"))
        self.reserve_daats_level_cbox = QtGui.QComboBox(self.groupBox_23)
        self.reserve_daats_level_cbox.setEnabled(False)
        self.reserve_daats_level_cbox.setGeometry(QtCore.QRect(10, 28, 171, 22))
        self.reserve_daats_level_cbox.setObjectName(_fromUtf8("reserve_daats_level_cbox"))
        self.label_83 = QtGui.QLabel(self.groupBox_23)
        self.label_83.setGeometry(QtCore.QRect(10, 10, 170, 17))
        self.label_83.setObjectName(_fromUtf8("label_83"))
        self.label_52 = QtGui.QLabel(self.tab_4)
        self.label_52.setGeometry(QtCore.QRect(157, 150, 211, 16))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.settings_button = QtGui.QPushButton(self.tab)
        self.settings_button.setGeometry(QtCore.QRect(40, 30, 131, 23))
        self.settings_button.setObjectName(_fromUtf8("settings_button"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.working_l1_cbox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.working_l1_cbox.setGeometry(QtCore.QRect(205, 5, 191, 26))
        self.working_l1_cbox.setObjectName(_fromUtf8("working_l1_cbox"))
        self.working_l2_cbox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.working_l2_cbox.setGeometry(QtCore.QRect(205, 30, 191, 26))
        self.working_l2_cbox.setObjectName(_fromUtf8("working_l2_cbox"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 10, 186, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(20, 35, 191, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        PastureWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(PastureWidget)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PastureWidget)
        PastureWidget.setTabOrder(self.working_l1_cbox, self.working_l2_cbox)
        PastureWidget.setTabOrder(self.working_l2_cbox, self.tabWidget)
        PastureWidget.setTabOrder(self.tabWidget, self.scrollArea)

    def retranslateUi(self, PastureWidget):
        PastureWidget.setWindowTitle(_translate("PastureWidget", "Selection / Filter", None))
        self.groupBox_18.setTitle(_translate("PastureWidget", "Criteria", None))
        self.label_62.setText(_translate("PastureWidget", "Parcel ID", None))
        self.label_64.setText(_translate("PastureWidget", "Member Name", None))
        self.label_65.setText(_translate("PastureWidget", "Group member register", None))
        self.label_66.setText(_translate("PastureWidget", "Application No", None))
        self.label_67.setText(_translate("PastureWidget", "Contract No", None))
        self.pasture_app_date_edit.setDisplayFormat(_translate("PastureWidget", "yyyy-MM-dd", None))
        self.pasture_clear_button.setText(_translate("PastureWidget", "Clear", None))
        self.pasture_find_button.setText(_translate("PastureWidget", "Find", None))
        self.pasture_date_cbox.setText(_translate("PastureWidget", "Application Date", None))
        self.pasture_results_label.setText(_translate("PastureWidget", "Results:", None))
        self.label_68.setText(_translate("PastureWidget", "Pasture Group", None))
        self.label_69.setText(_translate("PastureWidget", "Land use type", None))
        self.label_70.setText(_translate("PastureWidget", "Pasture type", None))
        self.groupBox_19.setTitle(_translate("PastureWidget", "Results", None))
        self.pasture_contract_view_button.setText(_translate("PastureWidget", "View Contract", None))
        self.pasture_app_view_button.setText(_translate("PastureWidget", "View App", None))
        self.pasture_layer_view_button.setText(_translate("PastureWidget", "Layer View/ Hide", None))
        self.pug_register_button.setText(_translate("PastureWidget", "Group Register/ View", None))
        self.pasture_app_add_button.setText(_translate("PastureWidget", "Application Add", None))
        self.draft_decision_button.setText(_translate("PastureWidget", "Draft/ Decision", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pasture_tab), _translate("PastureWidget", "Pasture(PUA)", None))
        self.monitoring_load_button.setText(_translate("PastureWidget", "Load Monitoring", None))
        self.groupBox_21.setTitle(_translate("PastureWidget", "Results", None))
        self.label_5.setText(_translate("PastureWidget", "Үнэлгээ", None))
        self.label_3.setText(_translate("PastureWidget", "D3(Боломжит Даац)", None))
        self.label_4.setText(_translate("PastureWidget", "Бэлчээр байгаа ХТ", None))
        self.avg_value_save_button.setText(_translate("PastureWidget", "Save", None))
        self.groupBox_20.setTitle(_translate("PastureWidget", "Criteria", None))
        self.point_find_button.setText(_translate("PastureWidget", "Find", None))
        self.label_75.setText(_translate("PastureWidget", "Daats Level", None))
        self.label_76.setText(_translate("PastureWidget", "Aimag", None))
        self.label_78.setText(_translate("PastureWidget", "Soum", None))
        self.label_79.setText(_translate("PastureWidget", "PUG", None))
        self.label_77.setText(_translate("PastureWidget", "Bag", None))
        self.label_81.setText(_translate("PastureWidget", "PUG Parcel", None))
        self.daats_level_chbox.setText(_translate("PastureWidget", "Is daats level", None))
        self.label_51.setText(_translate("PastureWidget", "Боломжит ХТ- Одоо байгаа ХТ = Үнэлгээ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("PastureWidget", "Pasture", None))
        self.groupBox_22.setTitle(_translate("PastureWidget", "Results", None))
        self.label_6.setText(_translate("PastureWidget", "Үнэлгээ", None))
        self.label_7.setText(_translate("PastureWidget", "D3(Боломжит Даац)", None))
        self.label_8.setText(_translate("PastureWidget", "Бэлчээр байгаа ХТ", None))
        self.reserve_avg_value_save_button.setText(_translate("PastureWidget", "Save", None))
        self.groupBox_23.setTitle(_translate("PastureWidget", "Criteria", None))
        self.reserve_point_find_button.setText(_translate("PastureWidget", "Find", None))
        self.label_80.setText(_translate("PastureWidget", "Reserve Location", None))
        self.label_82.setText(_translate("PastureWidget", "Reserve Parcel", None))
        self.reserve_daats_chbox.setText(_translate("PastureWidget", "Is daats level", None))
        self.label_83.setText(_translate("PastureWidget", "Daats Level", None))
        self.label_52.setText(_translate("PastureWidget", "Боломжит ХТ- Одоо байгаа ХТ = Үнэлгээ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("PastureWidget", "Reserve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PastureWidget", "Monitoring", None))
        self.settings_button.setText(_translate("PastureWidget", "Settings Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PastureWidget", "Settings", None))
        self.label.setText(_translate("PastureWidget", "Working Aimag / Duureg", None))
        self.label_2.setText(_translate("PastureWidget", "Working Soum", None))

