from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QListWidget

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
v_line1 = QVBoxLayout() #создание вертикальной линии
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

v_line1.addWidget(tasks_text, alignment=Qt.AlignCenter) #добавление виджета на линию
v_line1.addWidget(list_left, alignment=Qt.AlignCenter)
h_line1.addWidget(delete_all_left, alignment=Qt.AlignCenter)
h_line1.addWidget(delete1_left, alignment=Qt.AlignCenter)
v_line1.addLayout(h_line1)
v_line1.addWidget(new_task_text, alignment=Qt.AlignCenter)
v_line1.addWidget(new_edit, alignment=Qt.AlignCenter)
v_line1.addWidget(add, alignment=Qt.AlignCenter)

v_line2.addWidget(n2, alignment=Qt.AlignCenter)
v_line2.addWidget(list_of_tasks, alignment=Qt.AlignCenter)

v_line3.addWidget(done, alignment=Qt.AlignCenter)
v_line3.addWidget(list_right, alignment=Qt.AlignCenter)
h_line2.addWidget(delete_all_right, alignment=Qt.AlignCenter)
h_line2.addWidget(delete1_right, alignment=Qt.AlignCenter)
v_line3.addLayout(h_line2)

main_line.addLayout(v_line1)
main_line.addLayout(v_line2)
main_line.addLayout(v_line3)

main_win.setLayout(main_line) #загрузка заполненной линии на окно приложения

app.exec_() #оставлять приложение активным