from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

app = QApplication([])

# Головне вікно
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('хахахахахахахахах')

# Початкові дані
images = ['q.jpg', 'w.jpg', 'e.jpg', 'r.jpg','t.jpg', 'y.jpg', 'u.jpg', 'i.jpg','o.jpg','p.jpg','a.jpg', 's.jpg','']  # Список зображень
current_image_index = 0

# Зображення
label_p = QLabel('')
pixmapimage = QPixmap(images[current_image_index])
pixmapimage = pixmapimage.scaled(400, 400, Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.setStyleSheet("border: 2px solid black;")  # Рамка для зображення

# Основний текст
label = QLabel('шось')
label.setStyleSheet("font-size: 20px; font-weight: bold; color: green;")
label.hide()

# Додатковий текст
extra_label = QLabel('поїхали')
extra_label.setStyleSheet("font-size: 14px; color: blue;")
extra_label.hide()

# Кнопки
button_show = QPushButton('далі')
button_show.setStyleSheet("font-size: 16px; padding: 10px; background-color: lightblue;")

button_reset = QPushButton('Скинутися')
button_reset.setStyleSheet("font-size: 16px; padding: 10px; background-color: lightcoral;")
button_reset.hide()

# Розмітка
w = QVBoxLayout()
w.addWidget(label_p, alignment=Qt.AlignCenter)
w.addWidget(label, alignment=Qt.AlignCenter)
w.addWidget(extra_label, alignment=Qt.AlignCenter)
w.addWidget(button_show)
w.addWidget(button_reset)
win.setLayout(w)

# Функції
def show_boat():
    global current_image_index

    # Показати текст
    label.show()
    extra_label.show()

    # Змінити текст у головному лейблі
    label.setText("Давай дивитися")

    # Змінити картинку
    current_image_index = (current_image_index + 1) % len(images)
    new_pixmap = QPixmap(images[current_image_index])
    new_pixmap = new_pixmap.scaled(500, 500, Qt.KeepAspectRatio)
    label_p.setPixmap(new_pixmap)

    # Змінити стиль кнопки
    button_show.setText("ахахахахаха")
    button_show.setStyleSheet("background-color: lightgreen;")

    # Показати кнопку "Скинути"
    button_reset.show()

def reset_scene():
    global current_image_index

    # Приховати текст
    label.hide()
    extra_label.hide()

    # Повернути початкове зображення
    current_image_index = 0
    pixmapimage = QPixmap(images[current_image_index])
    pixmapimage = pixmapimage.scaled(400, 400, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)

    # Відновити стиль кнопки
    button_show.setText("шо я натикав")
    button_show.setStyleSheet("background-color: lightblue;")

    # Приховати кнопку "Скинути"
    button_reset.hide()

# Підключення кнопок
button_show.clicked.connect(show_boat)
button_reset.clicked.connect(reset_scene)

win.show()
app.exec_()
