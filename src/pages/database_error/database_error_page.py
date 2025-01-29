from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os


# print(os.path.join(os.getcwd(), 'data', 'images'))

class DatabaseErrorPage(QWidget):
    def __init__(self):
        super().__init__()

        # Основной вертикальный layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Текст ошибки
        error_label = QLabel("Нет подключения к базе данных")
        error_label.setAlignment(Qt.AlignCenter)
        error_label.setStyleSheet("font-size: 26px")
        main_layout.addWidget(error_label)
        main_layout.addSpacing(20)

        # Добавляем иконку
        icon_label = QLabel()
        icon_path = os.path.join(os.getcwd(), 'data', 'images', 'error-icon.png')
        pixmap = QPixmap(icon_path)
        scaled_pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(scaled_pixmap)
        icon_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(icon_label)
        main_layout.addSpacing(20)

        # Горизонтальный layout для кнопок
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        # Кнопки действий
        install_el_ac_btn = QPushButton("Установить El-Ac")
        install_el_ac_btn.setStyleSheet("padding: 10px 20px;")
        button_layout.addWidget(install_el_ac_btn)

        set_cfg_ini_path_btn = QPushButton("Указать Config.ini")
        set_cfg_ini_path_btn.setStyleSheet("padding: 10px 20px;")
        button_layout.addWidget(set_cfg_ini_path_btn)

        retry_btn = QPushButton("Обновить")
        retry_btn.setStyleSheet("padding: 10px 20px;")
        button_layout.addWidget(retry_btn)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)


