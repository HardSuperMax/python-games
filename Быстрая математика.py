#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
def game():
#= = = == = = = == = = = КОД ИГРЫ = = = == = = = == = = =#
    first = random.randint(10,100)
    second = random.randint(10,40)
    simvle = random.randint(1,3)
    if simvle == int(1):
        sumg = input("Решите: "+str(first) +" + "+str(second) +": ")
        if int(sumg) == int(first) + int(second):
            agane = input("Давайте еще! ")
            if agane == "Да!":
                game()
            if agane == "Нет!":
                print("Вы вышли из игры.")
        if int(sumg) != int(first) + int(second):
            lose = input("Неправильно!")
            if lose == "":
                game()
    if simvle == int(2):
        sumg = input("Решите: "+str(first) +" - "+str(second) +": ")
        if int(sumg) == int(first) - int(second):
            agane = input("Давайте еще! ")
            if agane == "Да!":
                game()
            if agane == "Нет!":
                print("Вы вышли из игры.")
        if int(sumg) != int(first) - int(second):
            lose = input("Неправильно!")
            if lose == "":
                game()
    if simvle == int(3):
        second = random.randint(5,15)
        sumg = input("Решите: "+str(first) +" * "+str(second) +": ")
        if int(sumg) == int(first) * int(second):
            agane = input("Давайте еще! ")
            if agane == "Да!":
                game()
            if agane == "Нет!":
                print("Вы вышли из игры.")
        if int(sumg) != int(first) * int(second):
            lose = input("Неправильно!")
            if lose == "":
                game()
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = = == = = = == = = =#
start = input("Начать игру в быструю математику? ")
if start == "Да!":
    game()
if start == "Нет!":
    print("Вы вышли из игры.")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =#
