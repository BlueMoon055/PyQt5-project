# импортируем:
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QListWidget
from PyQt5.QtGui import QPixmap, QBrush, QIcon

def delete_1_element_db_done(a, b):
    connection = sqlite3.connect('della.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM my_list WHERE name=? AND ind=?''', (a, b))
    connection.commit()
    connection.close()

def delete_all_from_db_done(a):
    connection = sqlite3.connect('della.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM my_list WHERE ind=?''', (a,))
    connection.commit()
    connection.close()

def move_elements_db(a, b):
    connection = sqlite3.connect('della.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM my_list WHERE name=? AND ind=?''', (a, b))
    if b == 1:
        b = 0
    else:
        b = 1
    cursor.execute('''INSERT INTO my_list (name, ind) VALUES (?, ?)''', (a, b))
    connection.commit()
    connection.close()

def delete_all_from_db(a):
    connection = sqlite3.connect('della.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM my_list WHERE ind=?''', (a,))
    connection.commit()
    connection.close()

def create_db(): #подргузка данных из бд и добавление дел в интерфейс
    connection = sqlite3.connect('della.db') # создание, подключение к бд
    cursor = connection.cursor() # создание оъекта-курсора
    # запрос создаёт новую таблицу my_list с полями name и ind, если она не была создана (name-0, ind-1)
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_list (name TEXT, ind INTEGER)''')
    items = cursor.execute("SELECT name, ind FROM my_list") # посмотреть данные из бд
    for item in items: # проходимся по списку из списков
        if item[1] == 0: # если индекс = 0 (потому что эл-т под номером 1 - индекс)
            list_left.addItem(item[0]) # добавление текста дела в левый список (из столбца name)
        else:
            list_right.addItem(item[0])
    connection.close() # сохранение изменений

def add_to_db(text): #добавление заметки по кнопке в бд
    connection = sqlite3.connect('della.db')  # создание, подключение к бд
    cursor = connection.cursor()  # создание объекта-курсора
    cursor.execute('''INSERT INTO my_list (name, ind) VALUES (?, ?)''', (text, 0))
    connection.commit()  # сохранение изменений
    connection.close()  # сохранение изменений

def delete_from_db(a, b): # a, b - параметры
    connection = sqlite3.connect('della.db')  # создание, подключение к бд
    cursor = connection.cursor()  # создание объекта-курсора
    cursor.execute('''DELETE FROM my_list WHERE name=? AND ind=?''', (a, b))
    connection.commit()
    connection.close()

def add_1(): # функция для кнопки добавить (левый список)
    count = 0
    txt = tasks_text_edit.text() # изменить текст
    for i in range(list_left.count()): #метод count() - количество эл-в списка list_left()
        if txt != list_left.item(i).text(): # если введённый текст не равен элементу списка, то
            count += 1 # счётчик увеличивается на 1
        else:
            break
    if list_left.count() == count: # если количество эл-в левого списка = счётчику, то
        add_to_db(txt) # добавляем в бд
        list_left.addItem(txt) # добавить элемент в список

def delete_all_elements(): # функция для кнопки удалить всё (левый список)
    delete_all_from_db(0)
    list_left.clear() # очистить лист

def delete_1_element(): # функция для кнопки удалить выбранную заметку (левый список)
    delete_from_db(list_left.currentItem().text(), 0) # в скобках аргументы
    list_left.takeItem(list_left.currentRow())  # удаляем выбранный элемент
    list_left.setCurrentRow(-1) # выделить строку под номером -1

def move_element_in_done(): # функция для кнопки переместить в сделано
    a = list_left.currentItem() # выбрать элемент
    if a:
        it_text = a.text() # получаем текст элемента
        move_elements_db(it_text, 0)
        list_left.takeItem(list_left.currentRow()) # удаляем элемент из левого списка
        list_right.addItem(it_text) # добавляем элемент в правый список
        list_left.setCurrentRow(-1) # выделить строку под номером -1

def move_element_in_tasks_list(): # функция для кнопки переместить в список дел
    b = list_right.currentItem() # выбрать элемент
    if b:
        take_text = b.text() # получаем текст элемента
        move_elements_db(take_text, 1)
        list_right.takeItem(list_right.currentRow()) # удаляем элемент из правого списка
        list_left.addItem(take_text) # добавляем элемент в левый список
        list_right.setCurrentRow(-1) # выделить строку под номером -1

def delete_all_elements_done(): # функция для кнопки удалить всё (правый список)
    delete_all_from_db_done(1)
    list_right.clear() # очистить лист

def delete_1_element_done(): # функция для кнопки удалить выбранную заметку (правый список)
    delete_1_element_db_done(list_right.currentItem().text(), 1) # в скобках аргументы
    list_right.takeItem(list_right.currentRow())  # удаляем выбранный элемент
    list_right.setCurrentRow(-1) # выделить строку под номером -1

app = QApplication([]) # создание объекта-приложения
app.setWindowIcon(QIcon("иконка.jpg")) # устанавливаем иконку для приложения
main_win = QWidget() # создание объекта-окна
main_win.resize(700, 400) # задать размеры окна
main_win.setWindowTitle('список дел') # задать название окну
main_win.show() # сделать объект-окно видимым

palette = main_win.palette() # получаем текущую палитру главного окна для изменений
palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('фон.png'))) # устанавливаем фон
main_win.setPalette(palette) # применяем изменённую палитру к окну
main_win.setStyleSheet("QPushButton, QLabel { background-color: pink; }") # устанавливаем розовый цвет для виджетов

# виджеты:
list_left = QListWidget() # создание виджета списка
list_right = QListWidget()
tasks_text = QLabel('список дел:') # создание виджета с текстом
delete_all_left = QPushButton('удалить все') # создание виджета кнопки
delete_all_right = QPushButton('удалить все')
delete1_left = QPushButton('удалить выбранную заметку')
delete1_right = QPushButton('удалить выбранную заметку')
new_task_text = QLabel('новое дело:')
b_add = QPushButton('добавить')
n2 = QPushButton('переместить в сделано')
list_of_tasks = QPushButton('переместить  в список дел')
done = QLabel('сделано:')
tasks_text_edit = QLineEdit() # создание виджета для ввода текста

main_line = QHBoxLayout() # создание горизонтальной направляющей линиии (главная)
v_line1 = QVBoxLayout() # создание вертикальной направляющей линии
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

# добавление виджетов на линии:
v_line1.addWidget(tasks_text, alignment=Qt.AlignCenter)
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

# загружаем линии на главную линию:
main_line.addLayout(v_line1)
main_line.addLayout(v_line2)
main_line.addLayout(v_line3)
main_win.setLayout(main_line) # загрузка заполненной линии на окно приложения

# подключаем кнопки:
b_add.clicked.connect(add_1)
delete_all_left.clicked.connect(delete_all_elements)
delete1_left.clicked.connect(delete_1_element)
n2.clicked.connect(move_element_in_done)
list_of_tasks.clicked.connect(move_element_in_tasks_list)
delete_all_right.clicked.connect(delete_all_elements_done)
delete1_right.clicked.connect(delete_1_element_done)
create_db()

app.exec_() #оставлять приложение активным