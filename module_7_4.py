team1_num = int(input("team1_num = "))
team2_num = int(input("team2_num = "))
score_1 = int(input("score_1 = "))
score_2 = int(input("score_2 = "))
team1_time = float(input("team1_time = "))
tasks_total = int(input("tasks_total = "))
time_avg = float(input("time_avg = "))
challenge_result = str(input("challenge_result = "))

print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

print("Команда Волшебники данных решила задач: {} ".format(score_2))
print("Волшебники данных решили задачи за {} с!".format(team1_time))

print(f"Команды решили {score_1} и {score_2} задач")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
