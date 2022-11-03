from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 600)
        MainWindow.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(10, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nome.setFont(font)
        self.label_nome.setObjectName("label_nome")
        self.line_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nome.setGeometry(QtCore.QRect(80, 25, 281, 25))
        self.line_nome.setAutoFillBackground(False)
        self.line_nome.setObjectName("line_nome")
        self.label_idade = QtWidgets.QLabel(self.centralwidget)
        self.label_idade.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_idade.setFont(font)
        self.label_idade.setObjectName("label_idade")
        self.line_idade = QtWidgets.QLineEdit(self.centralwidget)
        self.line_idade.setGeometry(QtCore.QRect(80, 60, 71, 25))
        self.line_idade.setAutoFillBackground(False)
        self.line_idade.setObjectName("line_idade")
        self.label_cpf = QtWidgets.QLabel(self.centralwidget)
        self.label_cpf.setGeometry(QtCore.QRect(160, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_cpf.setFont(font)
        self.label_cpf.setObjectName("label_cpf")
        self.line_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.line_cpf.setGeometry(QtCore.QRect(210, 60, 151, 25))
        self.line_cpf.setAutoFillBackground(False)
        self.line_cpf.setObjectName("line_cpf")
        self.label_rua = QtWidgets.QLabel(self.centralwidget)
        self.label_rua.setGeometry(QtCore.QRect(10, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rua.setFont(font)
        self.label_rua.setObjectName("label_rua")
        self.line_rua = QtWidgets.QLineEdit(self.centralwidget)
        self.line_rua.setGeometry(QtCore.QRect(60, 100, 301, 25))
        self.line_rua.setAutoFillBackground(False)
        self.line_rua.setObjectName("line_rua")
        self.label_bairro = QtWidgets.QLabel(self.centralwidget)
        self.label_bairro.setGeometry(QtCore.QRect(10, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_bairro.setFont(font)
        self.label_bairro.setObjectName("label_bairro")
        self.line_bairro = QtWidgets.QLineEdit(self.centralwidget)
        self.line_bairro.setGeometry(QtCore.QRect(10, 160, 351, 25))
        self.line_bairro.setAutoFillBackground(False)
        self.line_bairro.setObjectName("line_bairro")
        self.label_numero = QtWidgets.QLabel(self.centralwidget)
        self.label_numero.setGeometry(QtCore.QRect(10, 190, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_numero.setFont(font)
        self.label_numero.setObjectName("label_numero")
        self.line_numero = QtWidgets.QLineEdit(self.centralwidget)
        self.line_numero.setGeometry(QtCore.QRect(50, 190, 91, 25))
        self.line_numero.setAutoFillBackground(False)
        self.line_numero.setObjectName("line_numero")
        self.label_cep = QtWidgets.QLabel(self.centralwidget)
        self.label_cep.setGeometry(QtCore.QRect(150, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_cep.setFont(font)
        self.label_cep.setObjectName("label_cep")
        self.line_cep = QtWidgets.QLineEdit(self.centralwidget)
        self.line_cep.setGeometry(QtCore.QRect(200, 190, 161, 25))
        self.line_cep.setAutoFillBackground(False)
        self.line_cep.setObjectName("line_cep")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 250, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_questionario = QtWidgets.QLabel(self.centralwidget)
        self.label_questionario.setGeometry(QtCore.QRect(130, 240, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_questionario.setFont(font)
        self.label_questionario.setObjectName("label_questionario")
        self.label_pergunta_filho = QtWidgets.QLabel(self.centralwidget)
        self.label_pergunta_filho.setGeometry(QtCore.QRect(10, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pergunta_filho.setFont(font)
        self.label_pergunta_filho.setObjectName("label_pergunta_filho")
        self.radioButton_filho_sim = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_filho_sim.setGeometry(QtCore.QRect(120, 280, 51, 17))
        self.radioButton_filho_sim.setObjectName("radioButton_filho_sim")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_filho_sim)
        self.radioButton_filho_nao = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_filho_nao.setGeometry(QtCore.QRect(170, 280, 51, 17))
        self.radioButton_filho_nao.setObjectName("radioButton_filho_nao")
        self.buttonGroup_2.addButton(self.radioButton_filho_nao)
        self.label_pergunta_mora = QtWidgets.QLabel(self.centralwidget)
        self.label_pergunta_mora.setGeometry(QtCore.QRect(10, 310, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pergunta_mora.setFont(font)
        self.label_pergunta_mora.setObjectName("label_pergunta_mora")
        self.radioButton_mora_sim = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_mora_sim.setGeometry(QtCore.QRect(130, 310, 51, 17))
        self.radioButton_mora_sim.setObjectName("radioButton_mora_sim")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_mora_sim)
        self.radioButton_mora_nao = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_mora_nao.setGeometry(QtCore.QRect(180, 310, 51, 17))
        self.radioButton_mora_nao.setObjectName("radioButton_mora_nao")
        self.buttonGroup.addButton(self.radioButton_mora_nao)
        self.label_pergunta_doenca = QtWidgets.QLabel(self.centralwidget)
        self.label_pergunta_doenca.setGeometry(QtCore.QRect(10, 340, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pergunta_doenca.setFont(font)
        self.label_pergunta_doenca.setObjectName("label_pergunta_doenca")
        self.radioButton_doenca_sim = QtWidgets.QRadioButton(
            self.centralwidget)
        self.radioButton_doenca_sim.setGeometry(QtCore.QRect(10, 360, 51, 17))
        self.radioButton_doenca_sim.setObjectName("radioButton_doenca_sim")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_doenca_sim)
        self.radioButton_doenca_nao = QtWidgets.QRadioButton(
            self.centralwidget)
        self.radioButton_doenca_nao.setGeometry(QtCore.QRect(10, 380, 51, 17))
        self.radioButton_doenca_nao.setObjectName("radioButton_doenca_nao")
        self.buttonGroup_3.addButton(self.radioButton_doenca_nao)
        self.label_pergunta_estado = QtWidgets.QLabel(self.centralwidget)
        self.label_pergunta_estado.setGeometry(QtCore.QRect(10, 410, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pergunta_estado.setFont(font)
        self.label_pergunta_estado.setObjectName("label_pergunta_estado")
        self.comboBox_pergunta_estado = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pergunta_estado.setGeometry(
            QtCore.QRect(180, 410, 69, 22))
        self.comboBox_pergunta_estado.setObjectName("comboBox_pergunta_estado")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.comboBox_pergunta_estado.addItem("")
        self.pushButton_sair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sair.setGeometry(QtCore.QRect(50, 520, 111, 51))
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setGeometry(QtCore.QRect(230, 520, 111, 51))
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_sair.clicked.connect(MainWindow.close)  # type: ignore
        self.pushButton_salvar.clicked.connect(self.salvar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "                                       Cadastro"))
        self.label_nome.setText(_translate("MainWindow", "NOME:"))
        self.label_idade.setText(_translate("MainWindow", "IDADE:"))
        self.label_cpf.setText(_translate("MainWindow", "CPF:"))
        self.label_rua.setText(_translate("MainWindow", "RUA:"))
        self.label_bairro.setText(_translate("MainWindow", "BAIRRO:"))
        self.label_numero.setText(_translate("MainWindow", "Nº:"))
        self.label_cep.setText(_translate("MainWindow", "CEP:"))
        self.label_questionario.setText(
            _translate("MainWindow", "QUESTIONÁRIO"))
        self.label_pergunta_filho.setText(
            _translate("MainWindow", "Possui filho(s)?"))
        self.radioButton_filho_sim.setText(_translate("MainWindow", "SIM"))
        self.radioButton_filho_nao.setText(_translate("MainWindow", "NÃO"))
        self.label_pergunta_mora.setText(
            _translate("MainWindow", "Mora sozinho(a)?"))
        self.radioButton_mora_sim.setText(_translate("MainWindow", "SIM"))
        self.radioButton_mora_nao.setText(_translate("MainWindow", "NÃO"))
        self.label_pergunta_doenca.setText(_translate(
            "MainWindow", "Possui alguma doença crônica?"))
        self.radioButton_doenca_sim.setText(_translate("MainWindow", "SIM"))
        self.radioButton_doenca_nao.setText(_translate("MainWindow", "NÃO"))
        self.label_pergunta_estado.setText(
            _translate("MainWindow", "Nasceu em qual estado?"))
        self.comboBox_pergunta_estado.setItemText(
            0, _translate("MainWindow", "Selecione"))
        self.comboBox_pergunta_estado.setItemText(
            1, _translate("MainWindow", "AC"))
        self.comboBox_pergunta_estado.setItemText(
            2, _translate("MainWindow", "AL"))
        self.comboBox_pergunta_estado.setItemText(
            3, _translate("MainWindow", "AP"))
        self.comboBox_pergunta_estado.setItemText(
            4, _translate("MainWindow", "AM"))
        self.comboBox_pergunta_estado.setItemText(
            5, _translate("MainWindow", "BA"))
        self.comboBox_pergunta_estado.setItemText(
            6, _translate("MainWindow", "CE"))
        self.comboBox_pergunta_estado.setItemText(
            7, _translate("MainWindow", "DF"))
        self.comboBox_pergunta_estado.setItemText(
            8, _translate("MainWindow", "ES"))
        self.comboBox_pergunta_estado.setItemText(
            9, _translate("MainWindow", "GO"))
        self.comboBox_pergunta_estado.setItemText(
            10, _translate("MainWindow", "MA"))
        self.comboBox_pergunta_estado.setItemText(
            11, _translate("MainWindow", "MT"))
        self.comboBox_pergunta_estado.setItemText(
            12, _translate("MainWindow", "MS"))
        self.comboBox_pergunta_estado.setItemText(
            13, _translate("MainWindow", "MG"))
        self.comboBox_pergunta_estado.setItemText(
            14, _translate("MainWindow", "PA"))
        self.comboBox_pergunta_estado.setItemText(
            15, _translate("MainWindow", "PB"))
        self.comboBox_pergunta_estado.setItemText(
            16, _translate("MainWindow", "PR"))
        self.comboBox_pergunta_estado.setItemText(
            17, _translate("MainWindow", "PE"))
        self.comboBox_pergunta_estado.setItemText(
            18, _translate("MainWindow", "PI"))
        self.comboBox_pergunta_estado.setItemText(
            19, _translate("MainWindow", "RJ"))
        self.comboBox_pergunta_estado.setItemText(
            20, _translate("MainWindow", "RN"))
        self.comboBox_pergunta_estado.setItemText(
            21, _translate("MainWindow", "RS"))
        self.comboBox_pergunta_estado.setItemText(
            22, _translate("MainWindow", "RO"))
        self.comboBox_pergunta_estado.setItemText(
            23, _translate("MainWindow", "RR"))
        self.comboBox_pergunta_estado.setItemText(
            24, _translate("MainWindow", "SC"))
        self.comboBox_pergunta_estado.setItemText(
            25, _translate("MainWindow", "SP"))
        self.comboBox_pergunta_estado.setItemText(
            26, _translate("MainWindow", "SE"))
        self.comboBox_pergunta_estado.setItemText(
            27, _translate("MainWindow", "TO"))
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))

    def salvar(self):
        nome = self.line_nome.text()
        idade = self.line_idade.text()
        cpf = self.line_cpf.text()
        rua = self.line_rua.text()
        bairro = self.line_bairro.text()
        numero = self.line_numero.text()
        cep = self.line_cep.text()
        filho = ''
        if (self.radioButton_filho_sim.isChecked()):
            filho = 'filhos: sim'
        elif (self.radioButton_filho_nao.isChecked()):
            filho = 'filhos: não'
        mora = ''
        if (self.radioButton_mora_sim.isChecked()):
            mora = 'sozinho: sim'
        elif (self.radioButton_mora_nao.isChecked()):
            mora = 'sozinho: não'
        doenca = ''
        if (self.radioButton_doenca_sim.isChecked()):
            doenca = 'doença: sim'
        elif (self.radioButton_doenca_nao.isChecked()):
            doenca = 'doença: não'
        estado = self.comboBox_pergunta_estado.currentText()

        with open("dados.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(nome+",")
            arquivo.write(idade+",")
            arquivo.write(cpf+",")
            arquivo.write(rua+",")
            arquivo.write(bairro+",")
            arquivo.write(numero+",")
            arquivo.write(cep+",")
            arquivo.write(filho+",")
            arquivo.write(mora+",")
            arquivo.write(doenca+",")
            arquivo.write(estado+"\n")

        self.msg = QMessageBox()
        # Set the information icon
        self.msg.setIcon(QMessageBox.Information)
        # Set the main message
        self.msg.setText(f"DADOS SALVOS COM SUCESSO!")
        # Set the title of the window
        self.msg.setWindowTitle("SUCESSO!!!")
        # Display the message box
        self.msg.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec())
