# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(791, 628)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
#ifndef Q_OS_MAC
        self.verticalLayout_7.setSpacing(-1)
#endif
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.excel_input_edit = QLineEdit(self.tab)
        self.excel_input_edit.setObjectName(u"excel_input_edit")

        self.horizontalLayout_3.addWidget(self.excel_input_edit)

        self.excel_select_btn = QPushButton(self.tab)
        self.excel_select_btn.setObjectName(u"excel_select_btn")

        self.horizontalLayout_3.addWidget(self.excel_select_btn)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.canshushezhi = QLabel(self.tab)
        self.canshushezhi.setObjectName(u"canshushezhi")

        self.horizontalLayout_7.addWidget(self.canshushezhi)

        self.canshupz = QGroupBox(self.tab)
        self.canshupz.setObjectName(u"canshupz")
        self.horizontalLayout_4 = QHBoxLayout(self.canshupz)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_19 = QLabel(self.canshupz)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.timeout_slider = QSlider(self.canshupz)
        self.timeout_slider.setObjectName(u"timeout_slider")
        self.timeout_slider.setMinimum(1)
        self.timeout_slider.setMaximum(50)
        self.timeout_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.timeout_slider)

        self.timeout_lab = QLabel(self.canshupz)
        self.timeout_lab.setObjectName(u"timeout_lab")

        self.horizontalLayout_21.addWidget(self.timeout_lab)

        self.label_24 = QLabel(self.canshupz)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_21.addWidget(self.label_24)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 2)
        self.horizontalLayout_21.setStretch(2, 1)
        self.horizontalLayout_21.setStretch(3, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_20 = QLabel(self.canshupz)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_22.addWidget(self.label_20)

        self.max_workers_slider = QSlider(self.canshupz)
        self.max_workers_slider.setObjectName(u"max_workers_slider")
        self.max_workers_slider.setMinimum(1000)
        self.max_workers_slider.setMaximum(10000)
        self.max_workers_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_22.addWidget(self.max_workers_slider)

        self.max_workers_lab = QLabel(self.canshupz)
        self.max_workers_lab.setObjectName(u"max_workers_lab")

        self.horizontalLayout_22.addWidget(self.max_workers_lab)

        self.label_22 = QLabel(self.canshupz)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 2)
        self.horizontalLayout_22.setStretch(2, 1)
        self.horizontalLayout_22.setStretch(3, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_18 = QLabel(self.canshupz)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_26.addWidget(self.label_18)

        self.verify_yes_radio_btn = QRadioButton(self.canshupz)
        self.verify_yes_radio_btn.setObjectName(u"verify_yes_radio_btn")

        self.horizontalLayout_26.addWidget(self.verify_yes_radio_btn)

        self.verify_no_radio_btn = QRadioButton(self.canshupz)
        self.verify_no_radio_btn.setObjectName(u"verify_no_radio_btn")

        self.horizontalLayout_26.addWidget(self.verify_no_radio_btn)

        self.label_25 = QLabel(self.canshupz)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_26.addWidget(self.label_25)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_21 = QLabel(self.canshupz)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_28.addWidget(self.label_21)

        self.allow_redirect_yes_btn = QRadioButton(self.canshupz)
        self.allow_redirect_yes_btn.setObjectName(u"allow_redirect_yes_btn")

        self.horizontalLayout_28.addWidget(self.allow_redirect_yes_btn)

        self.allow_redirect_no_btn = QRadioButton(self.canshupz)
        self.allow_redirect_no_btn.setObjectName(u"allow_redirect_no_btn")

        self.horizontalLayout_28.addWidget(self.allow_redirect_no_btn)

        self.label_26 = QLabel(self.canshupz)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_28.addWidget(self.label_26)


        self.verticalLayout_10.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_17 = QLabel(self.canshupz)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_19.addWidget(self.label_17)

        self.api_yes_radio_btn = QRadioButton(self.canshupz)
        self.api_yes_radio_btn.setObjectName(u"api_yes_radio_btn")

        self.horizontalLayout_19.addWidget(self.api_yes_radio_btn)

        self.api_no_radio_btn = QRadioButton(self.canshupz)
        self.api_no_radio_btn.setObjectName(u"api_no_radio_btn")

        self.horizontalLayout_19.addWidget(self.api_no_radio_btn)

        self.label_23 = QLabel(self.canshupz)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_19.addWidget(self.label_23)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.label_37 = QLabel(self.canshupz)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_37)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 1)
        self.verticalLayout_10.setStretch(4, 1)
        self.verticalLayout_10.setStretch(5, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_10)


        self.horizontalLayout_7.addWidget(self.canshupz)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.operation_status_edit = QTextBrowser(self.tab)
        self.operation_status_edit.setObjectName(u"operation_status_edit")

        self.horizontalLayout_2.addWidget(self.operation_status_edit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.progress_bar = QProgressBar(self.tab)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.horizontalLayout.addWidget(self.progress_bar)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_36.addWidget(self.label_29)

        self.checkBox_15 = QCheckBox(self.groupBox)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setCheckable(True)
        self.checkBox_15.setChecked(True)

        self.horizontalLayout_36.addWidget(self.checkBox_15)


        self.verticalLayout.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_30 = QLabel(self.groupBox)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_37.addWidget(self.label_30)

        self.checkBox_16 = QCheckBox(self.groupBox)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setChecked(True)

        self.horizontalLayout_37.addWidget(self.checkBox_16)


        self.verticalLayout.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_38 = QLabel(self.groupBox)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_16.addWidget(self.label_38)

        self.checkBox_20 = QCheckBox(self.groupBox)
        self.checkBox_20.setObjectName(u"checkBox_20")
        self.checkBox_20.setChecked(True)

        self.horizontalLayout_16.addWidget(self.checkBox_20)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_31 = QLabel(self.groupBox)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_38.addWidget(self.label_31)

        self.checkBox_17 = QCheckBox(self.groupBox)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setChecked(True)

        self.horizontalLayout_38.addWidget(self.checkBox_17)


        self.verticalLayout.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_39.addWidget(self.label_33)

        self.checkBox_19 = QCheckBox(self.groupBox)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setChecked(True)

        self.horizontalLayout_39.addWidget(self.checkBox_19)


        self.verticalLayout.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_40.addWidget(self.label_32)

        self.checkBox_18 = QCheckBox(self.groupBox)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setChecked(True)

        self.horizontalLayout_40.addWidget(self.checkBox_18)


        self.verticalLayout.addLayout(self.horizontalLayout_40)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.horizontalLayout_10.addWidget(self.checkBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.horizontalLayout_12.addWidget(self.checkBox_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_13.addWidget(self.label_8)

        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.horizontalLayout_13.addWidget(self.checkBox_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.checkBox_6 = QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setChecked(True)

        self.horizontalLayout_14.addWidget(self.checkBox_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.checkBox_8 = QCheckBox(self.groupBox_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBox_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_29.addWidget(self.label_11)

        self.checkBox_7 = QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setChecked(True)

        self.horizontalLayout_29.addWidget(self.checkBox_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_8.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_30.addWidget(self.label_12)

        self.checkBox_9 = QCheckBox(self.groupBox_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setCheckable(True)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setAutoRepeat(False)

        self.horizontalLayout_30.addWidget(self.checkBox_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_31.addWidget(self.label_13)

        self.checkBox_10 = QCheckBox(self.groupBox_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setChecked(True)

        self.horizontalLayout_31.addWidget(self.checkBox_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_32.addWidget(self.label_14)

        self.checkBox_11 = QCheckBox(self.groupBox_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setCheckable(True)
        self.checkBox_11.setChecked(True)

        self.horizontalLayout_32.addWidget(self.checkBox_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_33.addWidget(self.label_15)

        self.checkBox_12 = QCheckBox(self.groupBox_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setCheckable(True)
        self.checkBox_12.setChecked(True)

        self.horizontalLayout_33.addWidget(self.checkBox_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_34.addWidget(self.label_27)

        self.checkBox_13 = QCheckBox(self.groupBox_2)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setCheckable(True)
        self.checkBox_13.setChecked(True)

        self.horizontalLayout_34.addWidget(self.checkBox_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_35.addWidget(self.label_28)

        self.checkBox_14 = QCheckBox(self.groupBox_2)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setCheckable(True)
        self.checkBox_14.setChecked(True)

        self.horizontalLayout_35.addWidget(self.checkBox_14)


        self.verticalLayout_3.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_8.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_16)

        self.textEdit = QTextEdit(self.groupBox_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.textEdit)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 9)

        self.verticalLayout_11.addLayout(self.verticalLayout_9)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_34 = QLabel(self.groupBox_7)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_9.addWidget(self.label_34)

        self.introduction_use_btn = QPushButton(self.groupBox_7)
        self.introduction_use_btn.setObjectName(u"introduction_use_btn")

        self.horizontalLayout_9.addWidget(self.introduction_use_btn)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_35 = QLabel(self.groupBox_7)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_41.addWidget(self.label_35)

        self.open_source_address_btn = QPushButton(self.groupBox_7)
        self.open_source_address_btn.setObjectName(u"open_source_address_btn")
        self.open_source_address_btn.setCheckable(True)
        self.open_source_address_btn.setChecked(False)

        self.horizontalLayout_41.addWidget(self.open_source_address_btn)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_41)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_17.addWidget(self.label_36)

        self.update_btn = QPushButton(self.groupBox_7)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setEnabled(True)

        self.horizontalLayout_17.addWidget(self.update_btn)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18.setStretch(0, 2)
        self.horizontalLayout_18.setStretch(1, 1)
        self.horizontalLayout_18.setStretch(2, 2)
        self.horizontalLayout_18.setStretch(3, 1)
        self.horizontalLayout_18.setStretch(4, 2)

        self.verticalLayout_4.addWidget(self.groupBox_7)

        self.verticalLayout_4.setStretch(0, 4)
        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.start_btn = QPushButton(Form)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_11.addWidget(self.start_btn)

        self.open_file_btn = QPushButton(Form)
        self.open_file_btn.setObjectName(u"open_file_btn")

        self.horizontalLayout_11.addWidget(self.open_file_btn)

        self.exit_btn = QPushButton(Form)
        self.exit_btn.setObjectName(u"exit_btn")

        self.horizontalLayout_11.addWidget(self.exit_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u6279\u91cf\u68c0\u6d4b\u5de5\u5177", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u672c\u5730\u76ee\u5f55", None))
        self.excel_select_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.canshushezhi.setText(QCoreApplication.translate("Form", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.canshupz.setTitle("")
        self.label_19.setText(QCoreApplication.translate("Form", u"timeout\uff1a", None))
        self.timeout_lab.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"max_workers", None))
        self.max_workers_lab.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u7ebf\u7a0b\u6570", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"verify\uff1a", None))
        self.verify_yes_radio_btn.setText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.verify_no_radio_btn.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u8ba4\u8bc1SSL\u8bc1\u4e66", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"allow_redirects\uff1a", None))
        self.allow_redirect_yes_btn.setText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.allow_redirect_no_btn.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"\u91cd\u5b9a\u5411", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u8c03\u7528\u63a5\u53e3\u529f\u80fd\uff1a", None))
        self.api_yes_radio_btn.setText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.api_no_radio_btn.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u5907\u6848\u4fe1\u606f\u83b7\u53d6", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u53c2\u6570\u82e5\u65e0\u7279\u6b8a\u8981\u6c42\uff0c\u4fdd\u6301\u9ed8\u8ba4\u5373\u53ef\uff0c\u82e5\u8981\u83b7\u53d6\u5173\u4e8e\u5907\u6848\u4fe1\u606f\uff0c\u8bf7\u5f00\u542f\u8c03\u7528\u63a5\u53e3\u529f\u80fd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u65e5\u5fd7", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u8fdb\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u4e3b\u9875\u9762", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u76f4\u63a5\u722c\u53d6", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u60c5\u51b5", None))
        self.checkBox_15.setText("")
        self.label_30.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u6807\u9898", None))
        self.checkBox_16.setText("")
        self.label_38.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u662f\u5426\u8fdd\u6cd5", None))
        self.checkBox_20.setText("")
        self.label_31.setText(QCoreApplication.translate("Form", u"\u72b6\u6001\u7801", None))
        self.checkBox_17.setText("")
        self.label_33.setText(QCoreApplication.translate("Form", u"\u60ac\u6302ICP\u5907\u6848\u53f7", None))
        self.checkBox_19.setText("")
        self.label_32.setText(QCoreApplication.translate("Form", u"\u60ac\u6302\u7f51\u5b89\u5907\u6848\u53f7", None))
        self.checkBox_18.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u8c03\u7528\u63a5\u53e3\u83b7\u53d6ICP\u5907\u6848", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u72b6\u6001", None))
        self.checkBox.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5ba1\u6838\u65f6\u95f4", None))
        self.checkBox_2.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5355\u4f4d\u540d\u79f0", None))
        self.checkBox_3.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5355\u4f4d\u6027\u8d28", None))
        self.checkBox_4.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5907\u6848\u53f7", None))
        self.checkBox_5.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u540d\u79f0", None))
        self.checkBox_6.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u9996\u9875\u5730\u5740", None))
        self.checkBox_8.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u8d1f\u8d23\u4eba", None))
        self.checkBox_7.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8c03\u7528\u63a5\u53e3\u83b7\u53d6\u7f51\u5b89\u5907\u6848", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u72b6\u6001", None))
        self.checkBox_9.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u7c7b\u522b", None))
        self.checkBox_10.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"\u5f00\u529e\u8005\u4e3b\u4f53", None))
        self.checkBox_11.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"\u516c\u5b89\u673a\u5173", None))
        self.checkBox_12.setText("")
        self.label_27.setText(QCoreApplication.translate("Form", u"\u8054\u7f51\u5907\u6848\u65f6\u95f4", None))
        self.checkBox_13.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"\u7f51\u5b89\u5907\u6848\u53f7", None))
        self.checkBox_14.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u76ee\u524d\u529f\u80fd", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u5176\u5b83\u8bbe\u7f6e", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u7f51\u7ad9\u6279\u91cf\u68c0\u6d4b\u5de5\u5177V1.0.2", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">\u672a\u6765\u8ba1\u5212</span></h2>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u6027\u80fd\u4f18\u5316\u4e0e"
                        "\u7a33\u5b9a\u6027\u63d0\u5347</span>\uff1a \u4e0d\u65ad\u4f18\u5316\u722c\u866b\u4ee3\u7801\uff0c<span style=\" font-weight:700;\">\u63d0\u9ad8\u7a0b\u5e8f\u7684\u7a33\u5b9a\u6027\u548c\u6267\u884c\u6548\u7387</span>\uff0c\u786e\u4fdd\u5728\u5904\u7406\u5927\u89c4\u6a21\u6570\u636e\u65f6\u4ecd\u80fd\u4fdd\u6301\u826f\u597d\u7684\u6027\u80fd\u3002</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u7528\u6237\u754c\u9762\u4f18\u5316\u4e0e\u53cb\u597d\u5316</span>\uff1a \u8fdb\u4e00\u6b65\u6539\u8fdb\u56fe\u5f62\u5316\u754c\u9762\uff0c<span style=\" font-weight:700;\">\u5c06\u5957\u7528\u5fb7\u53e4\u62c9\u6a21\u677f</span>\uff0c\u63d0\u5347\u7528\u6237\u4f53\u9a8c\uff0c\u589e\u52a0\u66f4\u591a\u76f4\u89c2\u7684\u64cd\u4f5c\u63d0\u793a\u548c\u53cd\u9988\u4fe1\u606f\uff0c\u4f7f\u5de5\u5177\u66f4\u52a0\u6613\u7528\u3002</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u914d\u7f6e\u9009\u9879</span>\uff1a \u589e\u52a0\u66f4\u591a\u7684\u914d\u7f6e\u9009\u9879\uff0c\u63d0\u4f9b\u66f4\u7075\u6d3b\u7684\u68c0\u6d4b\u65b9\u6848\u3002</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u529f\u80fd\u62d3\u5c55\u4e0e\u5b9a\u5236\u5316</span>\uff1a \u8003\u8651\u6dfb\u52a0\u66f4\u591a\u5b9e\u7528\u7684\u529f\u80fd\u6a21\u5757\uff0c\u6bd4\u5982\u5b9a\u65f6\u4efb\u52a1\u3001\u81ea\u5b9a\u4e49\u89c4\u5219\u7b5b\u9009\u3001\u7ed3\u679c\u5bfc\u51fa\u7b49\uff0c\u4ee5\u6ee1\u8db3\u7528\u6237\u5728\u5b9e\u9645\u5de5\u4f5c\u4e2d\u7684\u591a\u6837\u5316\u9700\u6c42\u3002</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u793e\u533a\u53cd\u9988\u4e0e\u66f4\u65b0</span>\uff1a \u9f13\u52b1"
                        "\u7528\u6237\u63d0\u4f9b\u53cd\u9988\u610f\u89c1\u548c\u5efa\u8bae\uff0c\u53ca\u65f6\u4fee\u590d\u548c\u66f4\u65b0\u5de5\u5177\uff0c\u786e\u4fdd\u5b83\u59cb\u7ec8\u9002\u5e94\u7f51\u7edc\u73af\u5883\u548c\u653f\u7b56\u6cd5\u89c4\u7684\u53d8\u5316</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6dfb\u52a0\u66f4\u591a\u5f02\u5e38\u6216\u8fdd\u6cd5\u7f51\u7ad9\u7684\u8bc6\u522b\u89c4\u5219\u3002</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u589e\u52a0\u65e5\u5fd7\u8bb0\u5f55\uff0c\u65b9\u4fbf\u7528\u6237\u8ddf\u8e2a\u7a0b\u5e8f\u6267\u884c\u8fc7\u7a0b\u3002</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u2014\u2014\u20142024.03.13\uff08fish\uff09</span></p></body></html>", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u4ecb\u7ecd", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u4ecb\u7ecd", None))
        self.introduction_use_btn.setText(QCoreApplication.translate("Form", u"BIGFISH", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u5f00\u6e90\u5730\u5740", None))
        self.open_source_address_btn.setText(QCoreApplication.translate("Form", u"GITHUB", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u66f4\u65b0", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"\u8bf7\u70b9\u51fb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u66f4\u591a\u5173\u4e8e", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.open_file_btn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6587\u4ef6", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u9000\u51fa\u7a0b\u5e8f", None))
    # retranslateUi

