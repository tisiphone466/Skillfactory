

def guessing_game(number):
    print(f"Загадано число от 1 до 100")
    try_count = 1  # счетчик попыток

    step = 50  # шаг изменения предполагаемого числа
    predict = step  # предполагаемое число

    while predict != number:
        try_count += 1  # плюсуем попытку
        step = round(step/2) if step > 1 else step
        predict = predict + step if number > predict else predict - step

        print('predict:', predict, 'step:', step)

    print(f"Вы угадали число {number} за {try_count} попыток.")
    return try_count


def score_game(guessing_game_func):
    tries = list()
    for number in range(1, 101):
        tries.append(guessing_game_func(number))

    print("В среднем", sum(tries) / len(tries), "попыток")


score_game(guessing_game)
