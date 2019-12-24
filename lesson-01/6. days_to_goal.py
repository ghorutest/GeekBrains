distance = int(input('Километров в 1-й день:\n'))
goal_distance = int(input('Введите целевую дистанцию:\n'))
goal = False
day = 1

while not goal:
    day += 1
    distance *= 1.1
    print (f"День: {day} дистанция: {distance:0.2f} км")
    if distance > goal_distance:
        goal = True
        print (f"Цель достигнута на: {day} день")
