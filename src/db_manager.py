from fdb import connect, Connection
from typing import Optional
from settings import settings
import os

#TODO: refactor default path
default_db_path = 'C:\\Electra\\El-Ac\\Globaыl.fdb'
default_config_ini_path = 'C:\\Electra\\El-Ac\\Config.ini'

class DbManager():
    def __init__(self):
        self.db_connection: Optional[Connection] = None
        self.init_db_connection()
        
    
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

db_manager = DbManager()