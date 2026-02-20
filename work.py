from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QListWidget
from PyQt5.QtGui import QPixmap, QBrush, QIcon

def add_1():
    tasks_text_edit.text()
    list_left.addItem(tasks_text_edit.text())

def delete_all_elements():
    list_left.clear()

def delete_1_element():
    #удаляем выбранный элемент из списка
    list_left.currentItem()
    list_left.takeItem(list_left.currentRow())
    list_left.setCurrentRow(-1)

def move_element_in_done():
    a = list_left.currentItem()
    if a:
        it_text = a.text() #получаем текст элемента
        list_left.takeItem(list_left.currentRow()) #удаляем из начального списка
        list_right.addItem(it_text)
        list_left.setCurrentRow(-1)

def move_element_in_tasks_list():
    b = list_right.currentItem()
    if b:
        take_text = b.text()
        list_right.takeItem(list_right.currentRow())
        list_left.addItem(take_text)
        list_right.setCurrentRow(-1)

def delete_all_elements_done():
    list_right.clear()

def delete_1_element_done():
    list_right.currentItem()
    list_right.takeItem(list_right.currentRow())
    list_right.setCurrentRow(-1)

app = QApplication([]) #создание объекта-приложения
app.setWindowIcon(QIcon("иконка.jpg"))
main_win = QWidget() #создание объекта-окна
main_win.resize(700, 400) #задать размеры окна
main_win.setWindowTitle('список дел') #задать название окну
main_win.show() #сделать объект-окно видимым

palette = main_win.palette()
palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('фон.png')))
main_win.setPalette(palette)
main_win.setStyleSheet("QPushButton, QLabel { background-color: pink; }") # Установить розовый цвет для виджетов

# виджеты
list_left = QListWidget()
list_right = QListWidget()
tasks_text = QLabel('список дел:')
delete_all_left = QPushButton('удалить все')
delete_all_right = QPushButton('удалить все')
delete1_left = QPushButton('удалить выбранную заметку')
delete1_right = QPushButton('удалить выбранную заметку')
new_task_text = QLabel('новое дело:')
b_add = QPushButton('добавить')
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
v_line1.addWidget(tasks_text, alignment=Qt.AlignCenter)#добавление виджета на линию
v_line1.addWidget(list_left, alignment=Qt.AlignCenter)
h_line1.addWidget(delete_all_left, alignment=Qt.AlignCenter)
h_line1.addWidget(delete1_left, alignment=Qt.AlignCenter)
v_line1.addLayout(h_line1)
v_line1.addWidget(new_task_text, alignment=Qt.AlignCenter)
v_line1.addWidget(tasks_text_edit, alignment=Qt.AlignCenter)
v_line1.addWidget(b_add, alignment=Qt.AlignCenter)

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

b_add.clicked.connect(add_1)
delete_all_left.clicked.connect(delete_all_elements)
delete1_left.clicked.connect(delete_1_element)
n2.clicked.connect(move_element_in_done)
list_of_tasks.clicked.connect(move_element_in_tasks_list)
delete_all_right.clicked.connect(delete_all_elements_done)
delete1_right.clicked.connect(delete_1_element_done)

app.exec_() #оставлять приложение активным