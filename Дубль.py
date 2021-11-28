#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
def game():
#= = = == = = = == = = = КОД ИГРЫ = = = == = = = == = = =#
    randint1 = random.randint(1,9)
    randint2 = random.randint(1,9)
    randint3 = random.randint(1,9)
    randint4 = random.randint(1,9)
    g = input("Вам выпало "+str(randint1) +", "+str(randint2) +", "+str(randint3) +", "+str(randint4) +". ")
    if g == "Ок!":
        if int(randint1) == int(randint2) or int(randint2) == int(randint3) or int(randint3) == int(randint4) or int(randint2) == int(randint4) or int(randint1) == int(randint4):
            print("Вы победили!")
        if int(randint1) != int(randint2) and int(randint2) != int(randint3) and int(randint3) != int(randint4) and int(randint2) != int(randint4) and int(randint1) != int(randint4):
            print("Вы проиграли!")
#= = = == = = = == = = = ИГРАТЬ СНОВА = = = == = = = == = = =#
        agane = input("Играть снова? ")
        if agane == "Да!":
            game()
        if agane == "Нет!":
            print("Вы вышли из игры.")
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = = == = = = == = = =#
start = input("Начать игру в дубль? ")
if start == "Да!":
    game()
if start == "Нет!":
     print("Вы вышли из игры")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =#
