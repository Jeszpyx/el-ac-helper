import locale

def resetlocale(category=locale.LC_ALL):
    locale.setlocale(category, locale.getdefaultlocale()[0])
locale.resetlocale = resetlocale


from PySide6.QtWidgets import (
    QApplication, QMainWindow
)
from fdb import connect, Connection
from typing import Optional
from settings import settings
import os

default_db_path = 'C:\\Electra\\El-Ac\\Global.fdb'
default_config_ini_path = 'C:\\Electra\\El-Ac\\Config.ini'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_connection: Optional[Connection] = self.init_db_connection()

        self.setWindowTitle("Помощник El-Ac")
        self.resize(800, 600)
    
    def try_connect_to_db(self, path_to_db: str) -> bool:
        try:
            self.db_connection = connect(
                host='localhost',
                database=path_to_db,
                user='sysdba',
                password='masterkey',
                charset='WIN1251'
            )
            print("Подключение успешно!")
            return True
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            return False
        
    def get_db_path_from_config_ini(self, path_to_config_ini: str) -> str | None:
        try:
            config_exists: bool = os.path.isfile(path_to_config_ini)
            if not config_exists:
                return None
            db_path = None
            with open(path_to_config_ini, "r") as file:
                lines = file.readlines()
                for l in lines:
                    if l.startswith("GlobalDB"):
                        db_path = l.split("=").pop().strip()
                        return db_path
        except Exception as e:
            print(f"get_db_path_from_config_ini: {e}")
            return None
        finally:
            file.close()
    
    def init_db_connection(self):
        try:
            if settings['is_default_path']:
                self.try_connect_to_db(default_db_path)
            else:
                db_path = self.get_db_path_from_config_ini(settings['config_ini_custom_path'])
                self.try_connect_to_db(db_path)
        except Exception as e:
            print(f'init_db_connection error -> {e}')
            self.db_connection = None

    
    def close_db_connection(self):
        if self.db_connection:
            self.db_connection.close()

        


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = MainWindow()
        window.show()

        app.exec()
    except Exception as e:
        print(e)
    finally:
        window.close_db_connection()

# import locale
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
# )
# from PySide6.QtGui import QPixmap, QIcon
# from PySide6.QtCore import Qt
# from fdb import connect, Connection
# from typing import Optional
# import os

# # Локальная фиксация проблемы с resetlocale
# def resetlocale(category=locale.LC_ALL):
#     locale.setlocale(category, locale.getdefaultlocale()[0])
# locale.resetlocale = resetlocale

# # Константы путей
# DEFAULT_DB_PATH = 'C:\\Electra\\El-Ac\\Global.fdb'
# DEFAULT_CONFIG_INI_PATH = 'C:\\Electra\\El-Ac\\Config.ini'


# # --- DatabaseManager ---
# class DatabaseManager:
#     def __init__(self, default_path: str = DEFAULT_DB_PATH, config_path: str = DEFAULT_CONFIG_INI_PATH):
#         self.connection: Optional[Connection] = None
#         self.default_path = default_path
#         self.config_path = config_path

#     def connect(self, path_to_db: Optional[str] = None) -> bool:
#         try:
#             db_path = path_to_db or self._get_db_path_from_config() or self.default_path
#             self.connection = connect(
#                 host='localhost',
#                 database=db_path,
#                 user='sysdba',
#                 password='masterkey',
#                 charset='WIN1251'
#             )
#             print("Подключение к базе данных успешно!")
#             return True
#         except Exception as e:
#             print(f"Ошибка подключения к базе данных: {e}")
#             return False

#     def close_connection(self):
#         if self.connection:
#             self.connection.close()
#             print("Соединение с базой данных закрыто.")

#     def _get_db_path_from_config(self) -> Optional[str]:
#         try:
#             if not os.path.isfile(self.config_path):
#                 return None
#             with open(self.config_path, "r") as file:
#                 for line in file:
#                     if line.startswith("GlobalDB"):
#                         return line.split("=").pop().strip()
#         except Exception as e:
#             print(f"Ошибка чтения файла конфигурации: {e}")
#             return None

# # --- MainWindow ---
# class MainWindow(QMainWindow):
#     def __init__(self, db_manager: DatabaseManager):
#         super().__init__()
#         self.db_manager = db_manager
#         self.setWindowTitle("Помощник El-Ac")
#         self.resize(800, 600)

#         # Попытка подключения к базе данных
#         if not self.db_manager.connect():
#             self._show_error("Ошибка подключения к базе данных")
#         else:
#             self._setup_ui()

#     def _setup_ui(self):
#         """
#         Настраивает пользовательский интерфейс, если подключение к БД успешно.
#         """
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Текст по центру
#         label = QLabel("Соединение с базой данных установлено.")
#         label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(label)

#         # Кнопка для завершения работы
#         close_button = QPushButton("Закрыть")
#         close_button.clicked.connect(self.close)
#         layout.addWidget(close_button)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def _show_error(self, message: str):
#         """
#         Отображение сообщения об ошибке.
#         """
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         label = QLabel(message)
#         label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(label)

#         close_button = QPushButton("Закрыть")
#         close_button.clicked.connect(self.close)
#         layout.addWidget(close_button)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def closeEvent(self, event):
#         """
#         Обработчик закрытия приложения.
#         """
#         self.db_manager.close_connection()
#         super().closeEvent(event)


# # --- Запуск приложения ---
# if __name__ == "__main__":
#     try:
#         app = QApplication([])

#         # Создаём экземпляр DatabaseManager
#         db_manager = DatabaseManager()

#         # Передаём его в MainWindow
#         window = MainWindow(db_manager)
#         window.show()

#         app.exec()
#     except Exception as e:
#         print(f"Ошибка: {e}")
