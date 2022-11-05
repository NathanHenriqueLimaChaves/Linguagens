import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QMenu, QMessageBox, QPushButton
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont
from janela1 import *
from janela2 import *
from janela3 import *


class janelaTerciaria (QMainWindow):
    def __init__(self):
        super().__init__()
        self.jan3 = Ui_janelaTerceira()
        self.jan3.setupUi(self)

        with open("dados.txt", "r", encoding='utf-8') as arquivo:
            dados = arquivo.readline()
            respostas = ""
            respostas = dados.split(",")
            print(respostas)


class janelaSecundaria (QMainWindow):
    def __init__(self):
        super().__init__()
        self.jan2 = Ui_janelaSegunda()
        self.jan2.setupUi(self)

        self.j1 = janelaPrimaria()
        self.j3 = janelaTerciaria()

        self.jan2.botaoVoltar.clicked.connect(self.voltar)
        self.jan2.botaoConcluir.clicked.connect(self.enviarJanela3)

    def voltar(self):
        self.j1.show()
        self.hide()

    def enviarJanela3(self):
        rua = self.jan2.inputRua.text()
        num = self.jan2.inputNr.text()
        cep = self.jan2.inputCep.text()
        bairro = self.jan2.inputBairro.text()
        cidade = self.jan2.inputCidade.text()
        estado = self.jan2.inputcomboBoxEstado.currentText()

        with open("dados.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(rua+",")
            arquivo.write(num+",")
            arquivo.write(cep+",")
            arquivo.write(bairro+",")
            arquivo.write(cidade+",")
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

        self.j3.show()
        self.hide()


class janelaPrimaria (QMainWindow):
    def __init__(self):
        super().__init__()
        self.jan1 = Ui_janelaPrimeira()
        self.jan1.setupUi(self)

        self.jan1.botaoEnviar.clicked.connect(self.enviarJanela2)

    def enviarJanela2(self):
        nome = self.jan1.inputNome.text()
        rg = self.jan1.inputRg.text()
        email = self.jan1.inputEmail.text()
        escolaridade = ''
        if (self.jan1.radioButtonFundamental.isChecked()):
            escolaridade = 'Ensino Fundamental'
        elif (self.jan1.radioButtonMedio.isChecked()):
            escolaridade = 'Ensino Médio'
        elif (self.jan1.radioButtonSuperior.isChecked()):
            escolaridade = 'Ensino Superior'
        data_formacao = self.jan1.dataFormacao.text()

        with open("dados.txt", "w", encoding='utf-8') as arquivo:
            arquivo.write(nome+",")
            arquivo.write(rg+",")
            arquivo.write(email+",")
            arquivo.write(escolaridade+",")
            arquivo.write(data_formacao+",")

        self.j2 = janelaSecundaria()

        self.j2.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    arq = janelaPrimaria()
    arq.show()
    sys.exit(app.exec())
