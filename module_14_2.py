import sqlite3

connection = sqlite3.connect("not_telegram2.db")
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

cursor.execute(" DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()