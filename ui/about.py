# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_dialog_about(object):
    def setupUi(self, dialog_about):
        if not dialog_about.objectName():
            dialog_about.setObjectName(u"dialog_about")
        dialog_about.resize(398, 192)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_about.sizePolicy().hasHeightForWidth())
        dialog_about.setSizePolicy(sizePolicy)
        dialog_about.setMinimumSize(QSize(398, 192))
        dialog_about.setMaximumSize(QSize(398, 192))
        self.horizontalLayout_3 = QHBoxLayout(dialog_about)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon = QLabel(dialog_about)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setPixmap(QPixmap(u":/icon/icon_64x64.png"))

        self.horizontalLayout.addWidget(self.label_icon)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.label_title = QLabel(dialog_about)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout.addWidget(self.label_title)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_text = QLabel(dialog_about)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setMinimumSize(QSize(300, 0))
        self.label_text.setMaximumSize(QSize(300, 16777215))
        self.label_text.setTextFormat(Qt.TextFormat.RichText)
        self.label_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_text)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_ok = QPushButton(dialog_about)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout_2.addWidget(self.btn_ok)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(dialog_about)

        QMetaObject.connectSlotsByName(dialog_about)
    # setupUi

    def retranslateUi(self, dialog_about):
        dialog_about.setWindowTitle(QCoreApplication.translate("dialog_about", u"About", None))
        self.label_icon.setText("")
        self.label_title.setText(QCoreApplication.translate("dialog_about", u"Terraform validator explorer", None))
        self.label_text.setText(QCoreApplication.translate("dialog_about", u"ABOUT_TEXT_HERE", None))
        self.btn_ok.setText(QCoreApplication.translate("dialog_about", u"OK", None))
    # retranslateUi

