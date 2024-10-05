#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
def game():
    player = input("Выберите 1 - камень, 2 - ножницы или 3 - бумагу: ")
    computer = random.randint(1,3)
    if int(computer) == int(1):
        print("- Камень")
    if int(computer) == int(2):
        print("- Ножницы")
    if int(computer) == int(3):
        print("- Бумага")
#= = = == = = = == = = = КОД ИГРЫ = = = == = = = == = = =#
    if int(player) == 1 and int(computer) == 2:
        print("- Вы победили!")
    if int(computer) == 1 and int(player) == 2:
        print("- Я победил!")
    if int(player) == 3 and int(computer) == 1:
        print("Вы победили!")
    if int(computer) == 3 and int(player) == 1:
        print("- Я победил!")
    if int(player) == 2 and int(computer) == 3:
        print("- Вы победили!")
    if int(computer) == 2 and int(player) == 3:
        print("- Я победил!")
    if int(player) == 1 and int(computer) == 1:
        print("- Ничья!")
    if int(player) == 2 and int(computer) == 2:
        print("- Ничья!")
    if int(player) == 3 and int(computer) == 3:
        print("- Ничья")
#= = = == = = = == = = = ИГРАТЬ СНОВА = = = == = = = == = = =#
    YES = input("Играть снова? Скажите да если хотите, и нет если не хотите: ")
    if YES == "да":
        game()
    if YES == "нет":
        print("Вы вышли из игры.")
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = = == = = = == = = =#
yes = input("Начать игру в камень, ножницы, бумага? Скажите да если хотите, и нет если не хотите: ")
if yes == "да":
    game()
if yes == "нет":
    print("Вы вышли из игры.")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =#
