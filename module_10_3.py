import threading
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            chislo1 = random.randint(50, 500)
            self.balance += chislo1
            print(f"Пополнение: {chislo1}. Баланс: {self.balance}\n")
        if self.balance >= 500 and self.lock.locked() == True:
            self.lock.release()
        time.sleep(0.001)

    def take(self):
        for i in range(100):
            chislo2 = random.randint(50, 500)
            print(f"Запрос на {chislo2}\n")
            if chislo2 <= self.balance:
                self.balance -= chislo2
                print(f"Снятие: {chislo2}. Баланс: {self.balance}\n")
            else:
                print("Запрос отклонён, недостаточно средств")
        self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')