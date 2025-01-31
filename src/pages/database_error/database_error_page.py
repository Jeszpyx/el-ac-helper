from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
import os
import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget
from db_manager import db_manager
from settings import update_settings, settings

if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.getcwd()

class DatabaseErrorPage(QWidget):
    refresh_page_signal = Signal()

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
        icon_path = os.path.join(base_path, 'data', 'images', 'error-icon.png')
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
        install_el_ac_btn.clicked.connect(self.install_el_ac)
        button_layout.addWidget(install_el_ac_btn)

        set_cfg_ini_path_btn = QPushButton("Указать Config.ini")
        set_cfg_ini_path_btn.clicked.connect(self.pick_file)
        set_cfg_ini_path_btn.setStyleSheet("padding: 10px 20px;")
        button_layout.addWidget(set_cfg_ini_path_btn)

        retry_btn = QPushButton("Обновить")
        retry_btn.setStyleSheet("padding: 10px 20px;")
        retry_btn.clicked.connect(self.refresh_page)
        button_layout.addWidget(retry_btn)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)



    def install_el_ac(self, e):
        el_ac_exe_path = os.path.join(base_path, 'data', 'installers', 'El-Ac-FB3.exe')
        os.popen(el_ac_exe_path)

    def pick_file(self):
        config_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Выберите файл Config.ini", 
            "", 
            "Файл конфигурации (Config.ini config.ini)"
        )
        if not config_path:
            return
        try:
            db_path = db_manager.get_db_path_from_config_ini(config_path)
            db_manager.try_connect_to_db(db_path)
            if not db_manager.db_connection:
                return
            update_settings("is_default_path", False)
            update_settings("config_ini_custom_path", config_path)
            self.refresh_page()
        except:
            return

    def refresh_page(self):
        print('ref page')
        self.refresh_page_signal.emit()