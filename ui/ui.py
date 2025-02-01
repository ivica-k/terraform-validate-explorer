# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(833, 500)
        MainWindow.setMinimumSize(QSize(400, 500))
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        icon = QIcon(QIcon.fromTheme(u"document-open"))
        self.action_open.setIcon(icon)
        self.action_open.setIconVisibleInMenu(True)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon1 = QIcon(QIcon.fromTheme(u"help-about"))
        self.action_about.setIcon(icon1)
        self.action_about.setIconVisibleInMenu(True)
        self.action_reload = QAction(MainWindow)
        self.action_reload.setObjectName(u"action_reload")
        icon2 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.action_reload.setIcon(icon2)
        self.action_reload.setIconVisibleInMenu(True)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.action_quit.setCheckable(False)
        icon3 = QIcon(QIcon.fromTheme(u"window-close"))
        self.action_quit.setIcon(icon3)
        self.action_quit.setIconVisibleInMenu(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_filter = QLineEdit(self.centralwidget)
        self.line_filter.setObjectName(u"line_filter")
        self.line_filter.setEnabled(False)
        self.line_filter.setMaxLength(255)

        self.horizontalLayout.addWidget(self.line_filter)

        self.combo_search_type = QComboBox(self.centralwidget)
        self.combo_search_type.setObjectName(u"combo_search_type")
        self.combo_search_type.setEnabled(False)

        self.horizontalLayout.addWidget(self.combo_search_type)

        self.check_unique = QCheckBox(self.centralwidget)
        self.check_unique.setObjectName(u"check_unique")
        self.check_unique.setEnabled(False)

        self.horizontalLayout.addWidget(self.check_unique)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.treeWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 833, 37))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolbar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_reload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_about)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.toolbar.addAction(self.action_open)
        self.toolbar.addAction(self.action_reload)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_about)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_quit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Terraform validate explorer", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_reload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
#if QT_CONFIG(tooltip)
        self.action_reload.setToolTip(QCoreApplication.translate("MainWindow", u"Reload the contents of the currently opened file.", None))
#endif // QT_CONFIG(tooltip)
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.line_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter resource name or address", None))
        self.check_unique.setText(QCoreApplication.translate("MainWindow", u"Only unique", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

