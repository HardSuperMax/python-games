#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
def game():
    player = input("Выберите 1 - камень, 2 - ножницы или 3 - бумагу: ")
    computer = random.randint(1,3)
    print(computer)
#= = = == = = = == = = = КОД ИГРЫ = = = == = = = == = = =#
    if int(player) == 1 and int(computer) == 2:
        print("Вы победили!")
    if int(computer) == 1 and int(player) == 2:
        print("Я победил!")
    if int(player) == 3 and int(computer) == 1:
        print("Вы победили!")
    if int(computer) == 3 and int(player) == 1:
        print("Я победил!")
    if int(player) == 2 and int(computer) == 3:
        print("Вы победили!")
    if int(computer) == 2 and int(player) == 3:
        print("Я победил!")
    if int(player) == 1 and int(computer) == 1:
        print("Ничья!")
    if int(player) == 2 and int(computer) == 2:
        print("Ничья!")
    if int(player) == 3 and int(computer) == 3:
        print("Ничья")
#= = = == = = = == = = = ИГРАТЬ СНОВА = = = == = = = == = = =#
    agane = input("Играть снова? ")
    if agane == "Да!":
        game()
    if agane == "Нет!":
        print("Вы вышли из игры.")
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = = == = = = == = = =#
start = input("Начать игру в камень, ножницы, бумага? ")
if start == "Да!":
    game()
if start == "Нет!":
    print("Вы вышли из игры.")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =#
