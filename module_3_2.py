a = 0

def send_email(message, recipient, sender = "university.help@gmail.com", a = None):
    for i in recipient:
        if i == "@":
            a += 1
        elif i == ".com":
            a += 1
        elif i == ".ru":
            a += 1
        elif i == ".net":
            a += 1
        if a == 0 or a == 1:
            print("Невозможно отправить письмо с адреса" <sender> "на адрес" <recipient>)
        else:
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")
            if sender == recipient:
                print("Нельзя отправить письмо самому себе!")
            return
        return
    return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
