flag_1 = True
flag_2 = True
flag_3 = True
flag_4 = True

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" in recipient:
        flag_1 = True
    else:
        flag_1 = False
    if "@" in sender:
        flag_2 = True
    else:
        flag_2 = False

    for i in [".com",".ru",".net"]:
        if i in recipient:
            flag_3 = True
            break
        else:
            flag_3 = False

    for i in [".com", ".ru", ".net"]:
        if i in sender:
            flag_4 = True
            break
        else:
            flag_4 = False
    if flag_1 == False or flag_2 == False or flag_3  == False or flag_4 == False:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
