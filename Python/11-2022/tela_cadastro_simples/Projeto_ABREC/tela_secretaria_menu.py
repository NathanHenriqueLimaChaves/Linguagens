import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QMenu, QMessageBox, QPushButton, QProxyStyle
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont


class Ui_form_secretaria_menu(object):
    def setupUi(self, form_secretaria_menu):
        form_secretaria_menu.setObjectName("form_secretaria_menu")
        form_secretaria_menu.resize(1440, 822)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form_secretaria_menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_barra_lateral = QtWidgets.QFrame(form_secretaria_menu)
        self.frame_barra_lateral.setStyleSheet(
            "background-color: rgb(227, 59, 78);")
        self.frame_barra_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_barra_lateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_barra_lateral.setObjectName("frame_barra_lateral")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_barra_lateral)
        self.gridLayout.setContentsMargins(-1, 30, -1, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label_recebe_nome = QtWidgets.QLabel(self.frame_barra_lateral)
        self.label_recebe_nome.setStyleSheet("font: 20pt \"Abel\";\n"
                                             "color: #ffffff;")
        self.label_recebe_nome.setAlignment(
            QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_recebe_nome.setObjectName("label_recebe_nome")
        self.gridLayout.addWidget(self.label_recebe_nome, 1, 0, 1, 1)
        self.label_recebe_foto = QtWidgets.QLabel(self.frame_barra_lateral)
        self.label_recebe_foto.setText("")
        self.label_recebe_foto.setPixmap(QtGui.QPixmap(
            "Imagens/foto_perfil_teste-modified.png"))
        self.label_recebe_foto.setScaledContents(False)
        self.label_recebe_foto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_recebe_foto.setObjectName("label_recebe_foto")
        self.gridLayout.addWidget(self.label_recebe_foto, 0, 0, 1, 1)
        self.pushButton_sair = QtWidgets.QPushButton(self.frame_barra_lateral)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_sair.sizePolicy().hasHeightForWidth())
        self.pushButton_sair.setSizePolicy(sizePolicy)
        self.pushButton_sair.setMinimumSize(QtCore.QSize(140, 45))
        self.pushButton_sair.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
                                           "    text-align: center;\n"
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
        icon.addPixmap(QtGui.QPixmap("Imagens/icone_botao_salvar.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sair.setIcon(icon)
        self.pushButton_sair.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_sair.setDefault(False)
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.gridLayout.addWidget(self.pushButton_sair, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 2)
        self.horizontalLayout.addWidget(self.frame_barra_lateral)
        self.frame_2 = QtWidgets.QFrame(form_secretaria_menu)
        self.frame_2.setStyleSheet("background-color: rgb(249, 217, 221);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(150, 25, 150, 25)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_menu_agenda_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_menu_agenda_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_menu_agenda_2.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_agenda_2.setSizePolicy(sizePolicy)
        self.pushButton_menu_agenda_2.setMinimumSize(QtCore.QSize(0, 170))
        font = QtGui.QFont()
        font.setFamily("Six Caps")
        font.setPointSize(80)
        self.pushButton_menu_agenda_2.setFont(font)
        self.pushButton_menu_agenda_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_menu_agenda_2.setStyleSheet("QPushButton {\n"
                                                    "    border: none;\n"
                                                    "    color:  rgb(236, 132, 156);\n"
                                                    "    background-color: rgb(255, 232, 226);\n"
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
            "Imagens/icone_botao_agenda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_agenda_2.setIcon(icon1)
        self.pushButton_menu_agenda_2.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_menu_agenda_2.setObjectName("pushButton_menu_agenda_2")
        self.verticalLayout.addWidget(self.pushButton_menu_agenda_2)
        self.pushButton_menu_cadastrar_eventos = QtWidgets.QPushButton(
            self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_menu_cadastrar_eventos.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_cadastrar_eventos.setSizePolicy(sizePolicy)
        self.pushButton_menu_cadastrar_eventos.setMinimumSize(
            QtCore.QSize(0, 170))
        font = QtGui.QFont()
        font.setFamily("Six Caps")
        font.setPointSize(80)
        self.pushButton_menu_cadastrar_eventos.setFont(font)
        self.pushButton_menu_cadastrar_eventos.setLayoutDirection(
            QtCore.Qt.RightToLeft)
        self.pushButton_menu_cadastrar_eventos.setStyleSheet("QPushButton {\n"
                                                             "    border: none;\n"
                                                             "    color:  rgb(236, 132, 156);\n"
                                                             "    background-color: rgb(255, 232, 226);\n"
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
            "Imagens/icone_botao_cadastrar_evento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_cadastrar_eventos.setIcon(icon2)
        self.pushButton_menu_cadastrar_eventos.setIconSize(
            QtCore.QSize(120, 120))
        self.pushButton_menu_cadastrar_eventos.setObjectName(
            "pushButton_menu_cadastrar_eventos")
        self.verticalLayout.addWidget(self.pushButton_menu_cadastrar_eventos)
        self.pushButton_menu_relatorios = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_menu_relatorios.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_relatorios.setSizePolicy(sizePolicy)
        self.pushButton_menu_relatorios.setMinimumSize(QtCore.QSize(0, 170))
        font = QtGui.QFont()
        font.setFamily("Six Caps")
        font.setPointSize(80)
        self.pushButton_menu_relatorios.setFont(font)
        self.pushButton_menu_relatorios.setLayoutDirection(
            QtCore.Qt.RightToLeft)
        self.pushButton_menu_relatorios.setStyleSheet("QPushButton {\n"
                                                      "    border: none;\n"
                                                      "    color:  rgb(236, 132, 156);\n"
                                                      "    background-color: rgb(255, 232, 226);\n"
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
            "Imagens/icone_botao_relatorios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_relatorios.setIcon(icon3)
        self.pushButton_menu_relatorios.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_menu_relatorios.setObjectName(
            "pushButton_menu_relatorios")
        self.verticalLayout.addWidget(self.pushButton_menu_relatorios)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)

        self.retranslateUi(form_secretaria_menu)
        QtCore.QMetaObject.connectSlotsByName(form_secretaria_menu)

    def retranslateUi(self, form_secretaria_menu):
        _translate = QtCore.QCoreApplication.translate
        form_secretaria_menu.setWindowTitle(
            _translate("form_secretaria_menu", "Form"))
        self.label_recebe_nome.setText(
            _translate("form_secretaria_menu", "Olá, <b> SAMANTHA </b>"))
        self.pushButton_sair.setText(
            _translate("form_secretaria_menu", "SAIR"))
        self.pushButton_menu_agenda_2.setText(
            _translate("form_secretaria_menu", "AGENDA"))
        self.pushButton_menu_cadastrar_eventos.setText(
            _translate("form_secretaria_menu", "CADASTRAR EVENTO"))
        self.pushButton_menu_relatorios.setText(
            _translate("form_secretaria_menu", "RELATÓRIOS"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QWidget()
    ui = Ui_form_secretaria_menu()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec())
