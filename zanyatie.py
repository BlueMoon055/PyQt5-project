from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QListWidget
def click():
    a_text = int(a_edit.text())
    h_text = int(h_edit.text())
    s_text = a_text * h_text
    print(s_text)
    s.setText('s='+str(s_text))

def exit():
    main_win.close()

app = QApplication([]) #создание объекта-приложения
main_win = QWidget() #создание объекта-окна
main_win.resize(700, 400) #задать размеры окна
main_win.setWindowTitle('список дел') #задать название окну
main_win.show() #сделать объект-окно видимым
list_left = QListWidget()
list_right = QListWidget()

tasks_text = QLabel('список дел:')
delete_all_left = QPushButton('удалить все')
delete_all_right = QPushButton('удалить все')
delete1_left = QPushButton('удалить выбранную заметку')
delete1_right = QPushButton('удалить выбранную заметку')
new_task_text = QLabel('новое дело:')
add = QPushButton('добавить')
n2 = QPushButton('переместить в сделано')
list_of_tasks = QPushButton('переместить  в список дел')
done = QLabel('сделано:')
tasks_text_edit = QLineEdit()
new_edit = QLineEdit()
done_edit = QLineEdit()

main_line = QHBoxLayout() #создание горизонтальной направляющей линиии(главная)
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()


v_line1.addWidget(n1, alignment=Qt.AlignCenter) #добавление виджета на линию
v_line1.addWidget(n1_edit, alignment=Qt.AlignCenter)
h_line2 = QHBoxLayout()
h_line2.addWidget(h, alignment=Qt.AlignCenter)
h_line2.addWidget(h_edit, alignment=Qt.AlignCenter)
h_line3 = QHBoxLayout()
h_line3.addWidget(button1, alignment=Qt.AlignCenter)
h_line3.addWidget(button2, alignment=Qt.AlignCenter)
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addWidget(s, alignment=Qt.AlignCenter)
v_line.addLayout(h_line3)

main_win.setLayout(v_line) #загрузка заполненной линии на окно приложения

button1.clicked.connect(click)
button2.clicked.connect(exit)

app.exec_() #оставлять приложение активным