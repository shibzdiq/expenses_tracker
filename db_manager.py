import sqlite3

class DatabaseManager:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Створює таблицю, якщо її ще не існує"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
        ''')
        self.conn.commit()

    def add_expense(self, date, category, amount, description):
        """Додає новий запис про витрати"""
        self.cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
        ''', (date, category, amount, description))
        self.conn.commit()

    def view_expenses(self):
        """Отримує всі записи про витрати"""
        self.cursor.execute('SELECT * FROM expenses')
        return self.cursor.fetchall()

    def total_expenses(self):
        """Підраховує загальну суму витрат"""
        self.cursor.execute('SELECT SUM(amount) FROM expenses')
        return self.cursor.fetchone()[0]

    def add_test_data(self):
        """Додає тестові дані"""
        test_data = [
            ("2024-12-01", "Продукти", 250.50, "Закупівля на тиждень"),
            ("2024-12-02", "Транспорт", 50.00, "Поїздка на роботу"),
            ("2024-12-03", "Розваги", 120.00, "Кіно та попкорн"),
        ]
        self.cursor.executemany('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
        ''', test_data)
        self.conn.commit()

    def close_connection(self):
        """Закриває з'єднання з базою даних"""
        self.conn.close()
