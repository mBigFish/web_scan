# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(556, 415)
        self.verticalLayout_3 = QVBoxLayout(widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.excel_input_edit = QLineEdit(self.groupBox)
        self.excel_input_edit.setObjectName(u"excel_input_edit")

        self.horizontalLayout.addWidget(self.excel_input_edit)

        self.excel_select_btn = QPushButton(self.groupBox)
        self.excel_select_btn.setObjectName(u"excel_select_btn")

        self.horizontalLayout.addWidget(self.excel_select_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.operation_status_edit = QTextEdit(self.groupBox_3)
        self.operation_status_edit.setObjectName(u"operation_status_edit")
        self.operation_status_edit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.operation_status_edit)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_btn = QPushButton(widget)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_2.addWidget(self.start_btn)

        self.exit_btn = QPushButton(widget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.horizontalLayout_2.addWidget(self.exit_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u7f51\u7ad9\u68c0\u6d4b\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("widget", u"\u8bbe\u7f6e", None))
        self.excel_select_btn.setText(QCoreApplication.translate("widget", u"\u9009\u62e9\u8868\u683c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("widget", u"\u8fd0\u884c\u60c5\u51b5", None))
        self.start_btn.setText(QCoreApplication.translate("widget", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.exit_btn.setText(QCoreApplication.translate("widget", u"\u9000\u51fa\u7a0b\u5e8f", None))
    # retranslateUi

