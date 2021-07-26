

def guessing_game(number):
    print(f"Загадано число от 1 до 100")
    try_count = 1  # счетчик попыток

    step = 50  # шаг изменения предполагаемого числа
    predict = step  # предполагаемое число

    while predict != number:
        try_count += 1  # плюсуем попытку
        if number < predict:
            # print(f"Угадываемое число меньше {predict} ")
            if step//2 > 0:
                step = step//2
            else:
                step = 1
            predict = predict - step

        else:
            # print(f"Угадываемое число больше {predict} ")
            if step//2 > 0:
                step = step//2
            else:
                step = 1
            predict = predict + step

    print(predict)
    print(f"Вы угадали число {number} за {try_count} попыток.")
    return try_count


def score_game(guessing_game_func):
    tries = list()
    for number in range(1, 101):
        tries.append(guessing_game_func(number))

    print("В среднем", sum(tries) / len(tries), "попыток")


score_game(guessing_game)
