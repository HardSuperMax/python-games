#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
def game():
    player = input("Выберите 1 - камень, 2 - ножницы или 3 - бумагу, 4 - карандаш, 5 - огонь, 6 - вода (цифру): ")
    computer = random.randint(1,6)
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
    if int(player) == 1 and int(computer) == 4: 
        print("Вы победили!")
    if int(computer) == 1 and int(player) == 4: 
        print("Я победил!")
    if int(player) == 1 and int(computer) == 5: 
        print("Вы победили!")
    if int(computer) == 1 and int(player) == 5:
        print("Я победил!")
    if int(player) == 1 and int(computer) == 6: 
        print("Я победил!")
    if int(computer) == 1 and int(player) == 6:
        print("Вы победили!")
    if int(player) == 4 and int(computer) == 4:
        print("Ничья!")
    if int(player) == 5 and int(computer) == 5:
        print("Ничья!")
    if int(player) == 6 and int(computer) == 6:
        print("Ничья!")
    if int(player) == 4 and int(computer) == 6:
        print("Вы победили!")
    if int(computer) == 4 and int(player) == 6:
        print("Я победил!")
    if int(player) == 2 and int(computer) == 4: 
        print("Вы победили!")   
    if int(computer) == 2 and int(player) == 4: 
        print("Я победил!")
    if int(player) == 2 and int(computer) == 5: 
        print("Я победил")
    if int(computer) == 2 and int(player) == 5:
        print("Вы победили!")
    if int(player) == 2 and int(computer) == 6: 
        print("Я победил!")
    if int(computer) == 2 and int(player) == 6: 
        print("Вы победили!")
    if int(player) == 3 and int(computer) == 4: 
        print("Я победил!")
    if int(computer) == 3 and int(player) == 4: 
        print("Вы победили!")
    if int(player) == 3 and int(computer) == 5: 
        print("Я победил!")
    if int(computer) == 3 and int(player) == 5: 
        print("Вы победили!")
    if int(player) == 3 and int(computer) == 6: 
        print("Я победил!")
    if int(computer) == 3 and int(player) == 6: 
        print("Вы победили!")
#= = = == = = = == = = = ИГРАТЬ СНОВА = = = == = = = == = = =#
    agane = input("Играть снова? ('Да' или 'Нет'): ")
    if agane == "Да!" or agane == "Да" or agane == "да":
        game()
    if agane == "Нет!" or agane == "Нет" or agane == "нет":
        print("Вы вышли из игры.")
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = = == = = = == = = =#
start = input("Начать игру в камень, ножницы, бумага? ('Да' или 'Нет'): ")
if start == "Да!" or start == "Да" or start == "да":
    game()
if start == "Нет!" or start == "Нет" or start == "нет":
    print("Вы вышли из игры.")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =# 
