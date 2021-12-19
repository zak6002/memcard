import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()
win.setWindowTitle('Easy Editor')
win.resize(700, 500)

lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_bw = QPushButton('Ч/Б')
btn_sharp = QPushButton('Резкость')
btn_flip = QPushButton('Зеркало')
lw_files = QListWidget()

row = QHBoxLayout()
main_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_sharp)
row.addWidget(btn_flip)
row.addWidget(btn_bw)

col2.addWidget(lb_image)
col2.addLayout(row)
main_layout.addLayout(col1, 1)
main_layout.addLayout(col2, 4)

workdir = ''

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result

def showFilenamesList():
    chooseWorkdir()
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

win.setLayout(main_layout)
win.show()
app.exec_()