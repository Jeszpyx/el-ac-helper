from PySide6.QtWidgets import (
     QVBoxLayout,QPushButton, QWidget, QStackedWidget, QMainWindow
)
from PySide6.QtCore import Qt

class MenuPage(QWidget):
    def __init__(self):
        super().__init__()

        # Основной вертикальный layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Центрируем все по вертикали

        # Добавляем растяжение сверху
        layout.addStretch()

        # Создаем 6 кнопок
        self.button1 = QPushButton("Страница 1")
        self.button2 = QPushButton("Страница 2")
        self.button3 = QPushButton("Страница 3")
        self.button4 = QPushButton("Страница 4")
        self.button5 = QPushButton("Страница 5")
        self.button6 = QPushButton("Страница 6")

        # Увеличиваем шрифт кнопок
        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;  /* Размер шрифта */
                padding: 10px 20px;  /* Внешние отступы */
            }
        """)

        # Добавляем кнопки в layout
        layout.addWidget(self.button1)
        layout.addStretch()  # Растяжение между кнопками
        layout.addWidget(self.button2)
        layout.addStretch()
        layout.addWidget(self.button3)
        layout.addStretch()
        layout.addWidget(self.button4)
        layout.addStretch()
        layout.addWidget(self.button5)
        layout.addStretch()
        layout.addWidget(self.button6)

        # Добавляем растяжение снизу
        layout.addStretch()

        # Применяем layout к виджету
        self.setLayout(layout)