import sys


name_list = ["Вася", "Маша", "Петя", "Валера"]


i = 0
while True:
    if name_list[i] == "Валера":
        print("Валера найден")
        break
    else:
        print(name_list[i])
    i = i + 1


