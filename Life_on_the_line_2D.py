import time
import random
count = 0
new_world = []
past_world = []
empty_world = []
new_line = []
line = []
world = []
random_world = ["0", "4"]
length = int(input("Введите длину мира -->"))
print("Введите длину мира -->", length)
wide = int(input("Введите ширину мира -->"))
print("Введите ширину мира -->", wide)
generations = int(input("Введите число поколений -->"))
print("Введите число поколений -->", generations)
line = []
for i in range(length):
        for g in range(wide):
            line.append("0")
        empty_world.append(line)
        line = []
word = input("Введите 'Да' для генерации случайного мира. -->")
print("Сгенерировать случайный мир? -->", word)
if word == "Да":
    for i in range(length):
        for g in range(wide):
            line.append(random.choice(random_world))
        world.append(line)
        line = []
else:
    for i in range(length):
        for g in range(wide):
            line = input("Вводите '4' или '0' через пробел.").split(" ")
        world.append(line)
        line = []
for i in range(generations):
    for line_number in range(0, wide):
        for column_number in range(0, length):
            if world[(line_number + 1) % (wide - 1)][(column_number + 1) % (length - 1)] == "4":
                count += 1
            if world[(line_number + 1) % (wide - 1)][column_number - 1] == "4":
                count += 1
            if world[(line_number + 1) % (wide - 1)][column_number] == "4":
                count += 1
            if world[line_number - 1][(column_number + 1) % (length - 1)] == "4":
                count += 1
            if world[line_number - 1][column_number - 1] == "4":
                count += 1
            if world[line_number - 1][column_number] == "4":
                count += 1
            if world[line_number][column_number - 1] == "4":
                count += 1
            if world[line_number][(column_number + 1) % (length - 1)] == "4":
                count += 1
            if world[line_number][column_number] == "4" and (count == 2 or count == 3):
                new_line.append("4")
            elif count == 3:
                new_line.append("4")
            else:
                new_line.append("0")
            count = 0
        new_world.append(new_line)
        new_line = []
    world = new_world.copy()
    new_world = []
    for k in world:
        print(*k)
    time.sleep(0.4)
    if world == empty_world:
        print("Не осталось живых клеток.")
        break
    elif world in past_world:
        print("Конфигурация в очередном поколении в точности повторяет себя же на одном из более ранних поклений.")
        break
    past_world.append(world)
