import pyodbc
import pyttsx3
import datetime

class DatabaseHandler:
    def __init__(self, db_path):
        self.conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
             (
                ID AUTOINCREMENT PRIMARY KEY,
                UserInput TEXT,
                Timestamp DATETIME,
            )
        ''')
        self.conn.commit()

    def insert_user_input(self, user_input):
        timestamp = datetime.datetime.now()
        self.cursor.execute('''
            INSERT INTO UserInputs (UserInput, Timestamp)
            VALUES (?, ?)
        ''', (user_input, timestamp))
        self.conn.commit()

    def get_input_history(self):
        self.cursor.execute('SELECT UserInput, Timestamp FROM UserInputs ORDER BY Timestamp DESC')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
