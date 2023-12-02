from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont

app = QApplication([])
window = QWidget()
window2 = QWidget()

window.setWindowTitle("Health")
window2.setWindowTitle("Test")
font = QFont("Arial", 18, QFont.Bold)

def button_handler():
    window2.show()

label = QLabel("Welcome to the Health Status Detection Program(HSDP)!")
label2 = QLabel("This program does smart stuff that I don't understand so trust the program, not me. You will be doing a series of activities that totally aren't randomly picked on spinthewheel.com which might do something? I'm not the expert, the progam is.")
button = QPushButton("Start")
name = QLabel("Full Name:")
ledit = QLineEdit("Full Name")


vlayout = QVBoxLayout()
vlayout2 = QVBoxLayout()

vlayout.addWidget(label,  alignment=Qt.AlignLeft)
vlayout.addWidget(label2,  alignment=Qt.AlignLeft)
vlayout.addWidget(button,  alignment=Qt.AlignCenter)

window.setLayout(vlayout)

button.clicked.connect(button_handler)

window.resize(1000,400)

window2.hide()
window.show()
app.exec_()