# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 787)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_futebol = QLabel(self.centralwidget)
        self.label_futebol.setObjectName(u"label_futebol")
        self.label_futebol.setGeometry(QRect(10, 30, 91, 31))
        self.btn_esportes = QPushButton(self.centralwidget)
        self.btn_esportes.setObjectName(u"btn_esportes")
        self.btn_esportes.setGeometry(QRect(230, 30, 94, 32))
        self.btn_novidades = QPushButton(self.centralwidget)
        self.btn_novidades.setObjectName(u"btn_novidades")
        self.btn_novidades.setGeometry(QRect(570, 30, 94, 32))
        self.label_novidades = QLabel(self.centralwidget)
        self.label_novidades.setObjectName(u"label_novidades")
        self.label_novidades.setGeometry(QRect(350, 30, 211, 31))
        self.textNovidades = QTextBrowser(self.centralwidget)
        self.textNovidades.setObjectName(u"textNovidades")
        self.textNovidades.setGeometry(QRect(350, 70, 321, 321))
        self.textEsportes = QTextBrowser(self.centralwidget)
        self.textEsportes.setObjectName(u"textEsportes")
        self.textEsportes.setGeometry(QRect(10, 70, 321, 321))
        self.btn_eletronicos = QPushButton(self.centralwidget)
        self.btn_eletronicos.setObjectName(u"btn_eletronicos")
        self.btn_eletronicos.setGeometry(QRect(910, 30, 94, 32))
        self.textEletronicos = QTextBrowser(self.centralwidget)
        self.textEletronicos.setObjectName(u"textEletronicos")
        self.textEletronicos.setGeometry(QRect(690, 70, 321, 321))
        self.label_eletronicos = QLabel(self.centralwidget)
        self.label_eletronicos.setObjectName(u"label_eletronicos")
        self.label_eletronicos.setGeometry(QRect(690, 30, 211, 31))
        self.label_politicas = QLabel(self.centralwidget)
        self.label_politicas.setObjectName(u"label_politicas")
        self.label_politicas.setGeometry(QRect(10, 400, 91, 31))
        self.btn_politicas = QPushButton(self.centralwidget)
        self.btn_politicas.setObjectName(u"btn_politicas")
        self.btn_politicas.setGeometry(QRect(230, 400, 94, 32))
        self.label_negocios = QLabel(self.centralwidget)
        self.label_negocios.setObjectName(u"label_negocios")
        self.label_negocios.setGeometry(QRect(350, 400, 211, 31))
        self.btn_viagens = QPushButton(self.centralwidget)
        self.btn_viagens.setObjectName(u"btn_viagens")
        self.btn_viagens.setGeometry(QRect(910, 400, 94, 32))
        self.textNegocios = QTextBrowser(self.centralwidget)
        self.textNegocios.setObjectName(u"textNegocios")
        self.textNegocios.setGeometry(QRect(350, 440, 321, 321))
        self.label_viagens = QLabel(self.centralwidget)
        self.label_viagens.setObjectName(u"label_viagens")
        self.label_viagens.setGeometry(QRect(690, 400, 211, 31))
        self.textViagens = QTextBrowser(self.centralwidget)
        self.textViagens.setObjectName(u"textViagens")
        self.textViagens.setGeometry(QRect(690, 440, 321, 321))
        self.btn_negocios = QPushButton(self.centralwidget)
        self.btn_negocios.setObjectName(u"btn_negocios")
        self.btn_negocios.setGeometry(QRect(570, 400, 94, 32))
        self.textPoliticas = QTextBrowser(self.centralwidget)
        self.textPoliticas.setObjectName(u"textPoliticas")
        self.textPoliticas.setGeometry(QRect(10, 440, 321, 321))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_futebol.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Esportes:</span></p></body></html>", None))
        self.btn_esportes.setText(QCoreApplication.translate("MainWindow", u"Inscrever-se", None))
        self.btn_novidades.setText(QCoreApplication.translate("MainWindow", u"Inscrever-se", None))
        self.label_novidades.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Novidades da Internet:</span></p></body></html>", None))
        self.btn_eletronicos.setText(QCoreApplication.translate("MainWindow", u"Inscrever-se", None))
        self.label_eletronicos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Eletr\u00f4nicos:</span></p></body></html>", None))
        self.label_politicas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Pol\u00edticas:</span></p></body></html>", None))
        self.btn_politicas.setText(QCoreApplication.translate("MainWindow", u"Inscrever-se", None))
        self.label_negocios.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Neg\u00f3cios:</span></p></body></html>", None))
        self.btn_viagens.setText(QCoreApplication.translate("MainWindow", u"Inscrever-se", None))
        self.label_viagens.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Viagens:</span></p></body></html>", None))
        self.btn_negocios.setText(QCoreApplication.translate("MainWindow", u"Inscrever-se", None))
    # retranslateUi

