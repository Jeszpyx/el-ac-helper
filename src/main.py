import locale

def resetlocale(category=locale.LC_ALL):
    locale.setlocale(category, locale.getdefaultlocale()[0])
locale.resetlocale = resetlocale

from pages.database_error.database_error_page import DatabaseErrorPage
from pages.menu.menu_page import MenuPage
from PySide6.QtWidgets import (
    QApplication, QMainWindow
)
from PySide6.QtWidgets import (
    QApplication, QStackedWidget, QMainWindow
)
from db_manager import db_manager



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Помощник El-Ac")
        self.resize(800, 600)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Создаем страницы
        self.main_page = MenuPage()
        self.error_page = DatabaseErrorPage()

        # Добавляем страницы в стек
        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.error_page)

        self.error_page.refresh_page_signal.connect(self.switch_to_menu_page)

        self.switch_to_menu_page()
        
    def switch_to_menu_page(self):
        if db_manager.db_connection is None: 
            self.stack.setCurrentWidget(self.error_page) 
        else:
            self.stack.setCurrentWidget(self.main_page)


if __name__ == '__main__':
    # Создаем экземпляр QApplication
    app = QApplication([])
    # Создаем экземпляр главного окна
    window = MainWindow()
    # Показываем главное окно
    window.show()

    # Запускаем основной цикл событий
    app.exec()