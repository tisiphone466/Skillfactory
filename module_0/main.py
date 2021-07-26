

def guess_number(number):
    """Guess the number from 1 to 100"""
    tries_count = 1
    step = 50  # Step of changing predictable number
    predict = step  # Predictable number

    while predict != number:
        tries_count += 1
        step = round(step/2) if step > 1 else step
        predict = predict + step if number > predict else predict - step

    print(f"The number {number} was guessed in {tries_count} tries.")
    return tries_count


def guess_benchmark(guess_number_fn):
    """Guessing number function benchmark"""
    tries = list()
    for number in range(1, 101):
        tries.append(guess_number_fn(number))

    print("On average", sum(tries) / len(tries), "tries")


guess_benchmark(guess_number)
