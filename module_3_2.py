flag_1 = True
flag_2 = True

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" in recipient and sender:
        flag_1 = True
    else:
        flag_1 = False
    for i in [".com",".ru",".net"]:
        if i in recipient and sender:
            flag_2 = True
        else:
            flag_2 = False

        if flag_1 == True and flag_2 == True:
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
            elif sender != "university.help@gmail.com":
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")
            elif sender == recipient:
                print("Нельзя отправить письмо самому себе!")
            else:
                print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
            return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
