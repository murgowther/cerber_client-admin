import psycopg2.extras

class DataBase:
    def __init__(self,db):
        self.__db = db
        self.__cur = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    def get_Zayavki(self):
        try:
            self.__cur.execute(f"SELECT * FROM pc")
            res = self.__cur.fetchall()
            if not res:
                return False

            return res
        except:
            print('Ошибка получения данных из БД')

        return False
    
    def get_all_activ(self):
        try:
            self.__cur.execute(f"SELECT * FROM activity")
            res = self.__cur.fetchall()
            if not res:
                return False

            return res
        
        except Exception as e:
            print(e.message) 

    def get_activ(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM activity WHERE id_pc_activity = '{id}'")
            res = self.__cur.fetchall()
            if not res:
                return False

            return res
        
        except Exception as e:
            print(e.message) 

    def get_secretfiles(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM secret_files WHERE id_pc_secret_files = '{id}'")
            res = self.__cur.fetchall()
            if not res:
                return False

            return res
 	    # для INSERT, UPDATE и DELETE ничего возвращать не нужно
        except Exception as e:
            print(e.message) 

    def get_printers(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM printers WHERE id_pc_printer = '{id}'")
            res = self.__cur.fetchall()
            if not res:
                return False

            return res
 	    # для INSERT, UPDATE и DELETE ничего возвращать не нужно
        except Exception as e:
            print(e.message) 

    def get_usb(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM usb WHERE id_pc_usb = '{id}'")
            res = self.__cur.fetchall()
            if not res:
                return False

            return res
 	    # для INSERT, UPDATE и DELETE ничего возвращать не нужно
        except Exception as e:
            print(e.message) 