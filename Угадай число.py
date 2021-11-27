#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
def game():
    randint = random.randint(1,10)
    player = input("Угадай число. У тебя 3 попытки, а всего еще 10 чисел! ")
#= = = == = = = == = = = КОД ИГРЫ = = = == = = = == = = =#
    if int(player) == int(randint):
        print("Вы победили с первой попытки!")
        agane = input("Играть снова? ")
        if agane == "Да!":
            game()
        if agane == "Нет!":
            print("Вы вышли из игры.")
#= = = == = = = == = = = ИНАЧЕ = = = == = = = == = = =#
    if int(player) != int(randint):
        play = input("Неправильно! Попробуйте еще раз! ")
        if play == "":
            player = input("Угадай число. У вас 2 попытки, а всего еще 9 чисел! ")
            if int(player) == int(randint):
                print("Вы победили со второй попытки!")
                agane = input("Играть снова? ")
                if agane == "Да!":
                    game()
                if agane == "Нет!":
                    print("Вы вышли из игры.")
#= = = == = = = == = = = ИНАЧЕ = = = == = = = == = = =#
            if int(player) != int(randint):
                play = input("Неправильно! Попробуйте последний раз! ")
                if play == "":
                    player = input("Угадай число. У вас последняя попытка, а всего еще 8 чисел! ")
            if int(player) == int(randint):
                print("Вы победили с последней попытки!")
                agane = input("Играть снова? ")
                if agane == "Да!":
                    game()
                if agane == "Нет!":
                    print("Вы вышли из игры.")
#= = = == = = = == = = = ИНАЧЕ = = = == = = = == = = =#
            if int(player) != int(randint):
                print("Вы проиграли!")
                agane = input("Играть снова? ")
                if agane == "Да!":
                    game()
                if agane == "Нет!":
                    print("Вы вышли из игры.")
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = = == = = = == = = =#    
start = input("Начать игру в угадай число? ")
if start == "Да!":
    game()
if start == "Нет!":
    print("Вы вышли из игры.")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =#
