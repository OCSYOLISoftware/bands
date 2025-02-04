import sqlite3

class HandleDB():
    def __init__(self, db_path="./bands.db"):
        self.db_path = db_path

    def _connect(self):
        """Crear una nueva conexión para cada solicitud."""
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def get_all(self):
        """Obtener todos los usuarios desde la base de datos."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        conn.close()  # Cerrar la conexión después de la consulta
        return data

    def get_only(self, data_user):
        """Obtener un usuario por su nombre de usuario."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (data_user,))
        data = cur.fetchone()
        conn.close()  # Cerrar la conexión después de la consulta
        return data

    def insert(self, data_user):
        """Insertar un nuevo usuario en la base de datos."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (id, firstname, lastname, username, password_user) VALUES (?, ?, ?, ?, ?)",
                    (data_user['id'], data_user['firstname'], data_user['lastname'], data_user['username'], data_user['password_user']))
        conn.commit()  # Confirmar la transacción
        conn.close()  # Cerrar la conexión después de la inserción

    def __del__(self):
        """Cerrar la conexión al final, si es necesario."""
        # No necesitamos cerrar la conexión aquí, ya que la cerramos después de cada operación
        pass

'''
class HandleDB():
    def __init__(self):
        self._con = sqlite3.connect("./bands.db")
        self._cur = self._con.cursor()
        
    def get_all(self):
        data = self._cur.execute("SELECT * FROM users")
        return data.fetchall()
    
    def get_only(self, data_user):
        data = self._cur.execute("Select * FROM users WHERE username = '{}'".format(data_user))
        return data.fetchone()
    
    def insert(self, data_user):
        self._cur.execute("INSERT INTO users  VALUES('{}','{}','{}','{}','{}')".format(
            data_user['id'],
            data_user['firstname'],
            data_user['lastname'],
            data_user['username'],
            data_user['password_user']
        ))
        self._con.commit()
    
    def __del__(self):
        self._con.close()
'''