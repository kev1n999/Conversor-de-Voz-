import os 
import sys 
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon 
from gtts import gTTS 
from playsound import playsound

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        
        self.window = uic.loadUi("./layout/lay.ui")
        self.Langs = uic.loadUi("./layout/langs.ui")
        self.window.setFixedSize(300, 340)
        self.window.setWindowTitle("Conversor de Voz")
        self.window.setWindowIcon(QIcon("./icon/icon.jpg"))
        self.window.lineEdit.setPlaceholderText("Insira o texto para converter para voz")
        self.window.lineEdit_2.setPlaceholderText("     Idioma")

        self.Langs.setFixedSize(500, 340)
        self.Langs.setWindowTitle("Idiomas disponíveis")

        self.window.show()
        self.window.pushButton_2.clicked.connect(self.quit)
        
        self.window.pushButton.clicked.connect(self.convert)
        self.window.pushButton_3.clicked.connect(self.start)
        self.window.pushButton_4.clicked.connect(self.langs)
        self.window.pushButton_5.clicked.connect(self.clear)

        self.textbrowser = self.window.textBrowser
    
    def langs(self):    
        self.Langs.show()

    def convert(self):
        try:
            voice = gTTS(text=self.window.lineEdit.text(), lang=self.window.lineEdit_2.text())

            voice.save("text.mp3")
            self.textbrowser.append(f"\nArquivo salvo como 'text.mp3' em:\n{os.getcwd()}\\text.mp3")
        except ValueError:
            self.textbrowser.append("\nErro: Idioma inválido, para ver a lista de idiomas disponíveis, clique no botão idiomas;")
        except AssertionError:
            self.textbrowser.append("\nErro: Você não inseriu nenhum texto;")

    def start(self):
        if not "text.mp3" in os.listdir():  
            self.textbrowser.append("\nErro: Você não iniciou nenhuma conversão válida;")
        else:
            try:
                playsound(f"{os.getcwd()}\\text.mp3")
            except Exception as err:
                self.textbrowser.append(f"Ocorreu um erro: {err}")

    def clear(self):
        self.textbrowser.clear()

if __name__ == "__main__":
    app = App()
    sys.exit(app.exec_())
