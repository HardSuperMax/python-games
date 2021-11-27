#= = = == = = = == = = = ИМПОРТЫ = = = == = = = == = = =#
import random
import sys
def game():
#= = = == = = = == = = = КОД ИГРЫ = = = == = = = == = = =#
    ok = input("Всего 30 клеток до выигрыша. ")
    if ok == "Ок!":
        first = random.randint(2,2)
        OR = input("Первый начинает "+str(first) +" (1 - вы, 2 - я).")
        if OR == "":
            go = []
            GO = []
            if first == int(1):
                def you():
                    player = input("Ходите! ")
                    if player == "Кидаю...":
                        CUBE = random.randint(1,6)               
                        cube = input("Вам выпало "+str(CUBE) +".")
                        if cube == "":
                            end = input("Вы передвинулись на "+str(CUBE) +".")
                            if end == "":
                                go.append(CUBE)
                                finish = sum(go)
                                big = input("Всего вы передвинулись на "+str(finish) +".")
                                if big == "":
                                    if finish == int(30) or finish > 30:
                                        win = input("Вы победили!")
                                        if win == "":
                                            START = input("Играть снова? ")
                                            if START == "Да!":
                                                game()
                                            if START == "Нет!":
                                                print("Вы вышли из игры.")
                                                sys.exit()
                                    computer = input("Хожу я!")
                                    if computer == "":
                                        CUBEC = random.randint(1,6)
                                        cubec = input("Мне выпало "+str(CUBEC) +".")
                                        if cubec == "":
                                            endc = input("Я передвинулся на "+str(CUBEC) +".")
                                            if endc == "":
                                                GO.append(CUBEC)
                                                finishc = sum(GO)
                                                bigc = input("Всего я передвинулся на "+str(finishc) +".")
                                                if bigc == "":
                                                    if finishc == int(30) or finishc > int(30):
                                                        lose = input("Я победил!")
                                                        if lose == "":
                                                            START = input("Играть снова? ")
                                                            if START == "Да!":
                                                                game()
                                                            if START == "Нет!":
                                                                print("Вы вышли из игры.")
                                                                sys.exit()
                                                    you()
                you()
            if first == int(2):
                def computer():
                    comp = input("Хожу я!")
                    if comp == "":
                        CUBEC = random.randint(1,6)
                        cubec = input("Мне выпало "+str(CUBEC) +".")
                        if cubec == "":
                            endc = input("Я передвинулся на "+str(CUBEC) +".")
                            if endc == "":
                                GO.append(CUBEC)
                                finishc = sum(GO)
                                bigc = input("Всего я передвинулся на "+str(finishc) +".")
                                if bigc == "":
                                    if finishc == int(30) or finishc > int(30):
                                        lose = input("Я победил!")
                                        if lose == "":
                                            START = input("Играть снова? ")
                                            if START == "Да!":
                                                game()
                                            if START == "Нет!":
                                                print("Вы вышли из игры.")
                                                sys.exit()
                                    player = input("Ходите! ")
                                    if player == "Кидаю...":
                                        CUBE = random.randint(1,6)               
                                        cube = input("Вам выпало "+str(CUBE) +".")
                                        if cube == "":
                                            end = input("Вы передвинулись на "+str(CUBE) +".")
                                            if end == "":
                                                go.append(CUBE)
                                                finish = sum(go)
                                                big = input("Всего вы передвинулись на "+str(finish) +".")
                                                if big == "":
                                                    if finish == int(30) or finish > 30:
                                                        win = input("Вы победили!")
                                                        if win == "":
                                                            START = input("Играть снова? ")
                                                            if START == "Да!":
                                                                game()
                                                            if START == "Нет!":
                                                                print("Вы вышли из игры.")
                                                                sys.exit()                                                            
                                                    computer()
                computer()
#= = = == = = = == = = = ПЕРЕМЕННЫЕ = = == = = = == = = =#
start = input("Начать игру-ходилку? ")
if start == "Да!":
    game()
if start == "Нет!":
    print("Вы вышли из игры.")
#= = = == = = = == = = = КОНЕЦ = = = == = = = == = = =#

