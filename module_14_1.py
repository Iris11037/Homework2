import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute(" DROP TABLE IF EXISTS Users")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)    
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    a = 10 * i
    cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{a}", "1000"))

cursor.execute(" UPDATE Users SET balance = 500 WHERE id % 2 != 0")

cursor.execute(" DELETE FROM Users WHERE (id + 2) % 3 = 0")

cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for i in users:
    print("Имя:", i[0], "|", "Почта:", i[1], "|", "Возраст", i[2], "|", "Баланс:", i[3])

connection.commit()
connection.close()