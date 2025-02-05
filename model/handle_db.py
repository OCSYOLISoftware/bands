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

    def delete(self, username: str):
        """Eliminar un usuario por su nombre de usuario."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()  # Confirmar la transacción
        conn.close()  # Cerrar la conexión después de la eliminación

    def __del__(self):
        """Cerrar la conexión al final, si es necesario."""
        # No necesitamos cerrar la conexión aquí, ya que la cerramos después de cada operación
        pass


    # ------------------------- MÉTODOS PARA BANDAS ------------------------- #

    def get_all_bands(self):
        """Obtener todas las bandas de la base de datos."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bands")
        data = cur.fetchall()
        conn.close()
        return data

    def get_band(self, band_name):
        """Obtener una banda por su nombre."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bands WHERE name = ?", (band_name,))
        data = cur.fetchone()
        conn.close()
        return data

    def insert_band(self, data_band):
        """Insertar una nueva banda en la base de datos."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO bands (name, record_label_id) VALUES (?, ?)",
                    (data_band['name'], data_band['record_label_id']))
        conn.commit()
        conn.close()

    def delete_band(self, band_name):
        """Eliminar una banda por su nombre."""
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM bands WHERE name = ?", (band_name,))
        conn.commit()
        conn.close()

    # ------------------------- MÉTODOS PARA Recod Label ------------------------- #
    def get_all_record_labels(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM record_labels")  # Asegúrate de que la tabla se llame correctamente
        labels = cur.fetchall()
        conn.close()
        return labels  # Devuelve una lista de tuplas (id, name)

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