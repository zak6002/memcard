from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication , QWidget ,
        QHBoxLayout , QVBoxLayout ,
        QGroupBox , QRadioButton ,  
        QPushButton , QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
 
# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result , alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct , alignment = Qt.AlignHCenter,stretch = 2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question , alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK , stretch = 2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1 , stretch = 2)
layout_card.addLayout(layout_line2 , stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3 , stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
b = 0
def next_question():
    global b
    window.question += 1
    b += 1
    if window.question >= len(question_list):
        window.question = 0
        shuffle(question_list)
    q = question_list[window.question]
    ask(q)

def show_correct(res):
    if b == 10:
        lb_Result.setText('Правильные ответы:' + str(a))
    else:
        lb_Result.setText(res)
    show_result()
a = 0
def test():
    global a, b
    if answers[0].isChecked():
        show_correct('Верно!')
        a += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')


def click_OK():
    if btn_OK.text() == 'Ответить':
        test()
    else:
        next_question()

q = Question('Государственный язык Бразилии', 'Португальский','Бразильский','Испанский','Итальянский')
question_list = []
question_list.append(q)
question_list.append(Question('1000 - 7', '993', '998', '4', '21'))
question_list.append(Question('15 + 1', '16', '4', '160', '10'))
shuffle(question_list)
btn_OK.clicked.connect(click_OK)
window = QWidget()
window.question = -1
window.setLayout(layout_card)
next_question()
window.setWindowTitle('Карта памяти')
window.show()

app.exec()