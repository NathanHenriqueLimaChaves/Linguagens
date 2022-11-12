import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QMenu, QMessageBox, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont
#import resource_rc


class Ui_menu_secretaria(object):
    def setupUi(self, menu_secretaria):
        menu_secretaria.setObjectName("menu_secretaria")
        menu_secretaria.resize(1440, 812)
        menu_secretaria.setLayoutDirection(QtCore.Qt.LeftToRight)
        menu_secretaria.setStyleSheet("background-color: rgb(249, 217, 221);")
        self.barra_lateral = QtWidgets.QFrame(menu_secretaria)
        self.barra_lateral.setGeometry(QtCore.QRect(0, 0, 195, 812))
        self.barra_lateral.setStyleSheet("background-color: rgb(220, 56, 75);")
        self.barra_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_lateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_lateral.setObjectName("barra_lateral")
        self.frame_foto = QtWidgets.QFrame(self.barra_lateral)
        self.frame_foto.setGeometry(QtCore.QRect(35, 42, 125, 125))
        self.frame_foto.setStyleSheet("QFrame{\n"
                                      "    border-radius:60px;\n"
                                      "    background-image: url(Imagens/kisspng-computer-icons-user-profile-profile-ico-5ab03f382d75f4.1216592715214999601862_resized (1).png);\n"
                                      "    background-repeat:no-repeat;\n"
                                      "    background-position:center;\n"
                                      "};")
        self.frame_foto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_foto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_foto.setLineWidth(0)
        self.frame_foto.setObjectName("frame_foto")
        self.label_cumprimento = QtWidgets.QLabel(self.barra_lateral)
        self.label_cumprimento.setGeometry(QtCore.QRect(44, 182, 127, 29))
        self.label_cumprimento.setStyleSheet("font: 20pt \"Abel\";\n"
                                             "color: #ffffff;")
        self.label_cumprimento.setObjectName("label_cumprimento")
        self.pushButton_sair = QtWidgets.QPushButton(self.barra_lateral)
        self.pushButton_sair.setGeometry(QtCore.QRect(28, 722, 140, 45))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_sair.setPalette(palette)
        self.pushButton_sair.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_sair.setStyleSheet("QPushButton {\n"
                                           "    font: 25pt \"Abel\";\n"
                                           "    color: #ffffff;\n"
                                           "    background-color: rgb(255, 54, 54);\n"
                                           "    border-bottom: 3px groove rgb(9, 9, 9);\n"
                                           "    border-radius: 20px;\n"
                                           "    padding: 5px; \n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(220, 56, 75);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "       font: 25pt \"Abel\";\n"
                                           "    color: #ffffff;\n"
                                           "    background-color: rgb(159, 40, 54);\n"
                                           "    border-left: 2px groove rgb(9, 9, 9);\n"
                                           "    border-right: 2px groove rgb(9, 9, 9);\n"
                                           "    border-top: 3px groove rgb(9, 9, 9);\n"
                                           "    border-radius: 20px;\n"
                                           "}\n"
                                           "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/ligar 1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sair.setIcon(icon)
        self.pushButton_sair.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.frame = QtWidgets.QFrame(menu_secretaria)
        self.frame.setGeometry(QtCore.QRect(431, 131, 755, 170))
        self.frame.setStyleSheet("background-color: rgb(255, 232, 226);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_menu_agenda = QtWidgets.QPushButton(self.frame)
        self.pushButton_menu_agenda.setGeometry(QtCore.QRect(0, 0, 755, 170))
        font = QtGui.QFont()
        font.setFamily("Six Caps")
        font.setPointSize(80)
        self.pushButton_menu_agenda.setFont(font)
        self.pushButton_menu_agenda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_menu_agenda.setStyleSheet("QPushButton {\n"
                                                  "    border: none;\n"
                                                  "    color:  rgb(236, 132, 156);\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgb(243, 185, 192);\n"
                                                  "}\n"
                                                  "QPushButton:pressed {\n"
                                                  "    background-color: rgb(243, 185, 192);\n"
                                                  "    border-top: 3px solid rgb(243, 185, 192);\n"
                                                  "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "Imagens/agenda 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_agenda.setIcon(icon1)
        self.pushButton_menu_agenda.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_menu_agenda.setObjectName("pushButton_menu_agenda")
        self.frame_2 = QtWidgets.QFrame(menu_secretaria)
        self.frame_2.setGeometry(QtCore.QRect(431, 321, 755, 170))
        self.frame_2.setStyleSheet("background-color: rgb(255, 232, 226);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_menu_cadastrar_eventos = QtWidgets.QPushButton(
            self.frame_2)
        self.pushButton_menu_cadastrar_eventos.setGeometry(
            QtCore.QRect(0, 0, 755, 170))
        font = QtGui.QFont()
        font.setFamily("Six Caps")
        font.setPointSize(80)
        self.pushButton_menu_cadastrar_eventos.setFont(font)
        self.pushButton_menu_cadastrar_eventos.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.pushButton_menu_cadastrar_eventos.setStyleSheet("QPushButton {\n"
                                                             "    border: none;\n"
                                                             "    color:  rgb(236, 132, 156);\n"
                                                             "}\n"
                                                             "QPushButton:hover {\n"
                                                             "    background-color: rgb(243, 185, 192);\n"
                                                             "}\n"
                                                             "QPushButton:pressed {\n"
                                                             "    background-color: rgb(243, 185, 192);\n"
                                                             "    border-top: 3px solid rgb(243, 185, 192);\n"
                                                             "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "Imagens/festa-de-aniversario 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_cadastrar_eventos.setIcon(icon2)
        self.pushButton_menu_cadastrar_eventos.setIconSize(
            QtCore.QSize(120, 120))
        self.pushButton_menu_cadastrar_eventos.setObjectName(
            "pushButton_menu_cadastrar_eventos")
        self.frame_3 = QtWidgets.QFrame(menu_secretaria)
        self.frame_3.setGeometry(QtCore.QRect(431, 511, 755, 170))
        self.frame_3.setStyleSheet("background-color: rgb(255, 232, 226);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_menu_relatorios = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_menu_relatorios.setGeometry(
            QtCore.QRect(0, 0, 755, 170))
        font = QtGui.QFont()
        font.setFamily("Six Caps")
        font.setPointSize(80)
        self.pushButton_menu_relatorios.setFont(font)
        self.pushButton_menu_relatorios.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.pushButton_menu_relatorios.setStyleSheet("QPushButton {\n"
                                                      "    border: none;\n"
                                                      "    color:  rgb(236, 132, 156);\n"
                                                      "}\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: rgb(243, 185, 192);\n"
                                                      "}\n"
                                                      "QPushButton:pressed {\n"
                                                      "    background-color: rgb(243, 185, 192);\n"
                                                      "    border-top: 3px solid rgb(243, 185, 192);\n"
                                                      "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "Imagens/relatorio-de-negocios 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_relatorios.setIcon(icon3)
        self.pushButton_menu_relatorios.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_menu_relatorios.setObjectName(
            "pushButton_menu_relatorios")

        self.retranslateUi(menu_secretaria)
        QtCore.QMetaObject.connectSlotsByName(menu_secretaria)

    def retranslateUi(self, menu_secretaria):
        _translate = QtCore.QCoreApplication.translate
        menu_secretaria.setWindowTitle(_translate("menu_secretaria", "Form"))
        self.label_cumprimento.setText(_translate("menu_secretaria", "Olá, "))
        self.pushButton_sair.setText(_translate("menu_secretaria", "SAIR"))
        self.pushButton_menu_agenda.setText(
            _translate("menu_secretaria", "AGENDA"))
        self.pushButton_menu_cadastrar_eventos.setText(
            _translate("menu_secretaria", "CADASTRAR EVENTO"))
        self.pushButton_menu_relatorios.setText(
            _translate("menu_secretaria", "RELATÓRIOS"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_menu_secretaria()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec())
