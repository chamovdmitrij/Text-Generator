import random
import re


def is_capital(word_):
    return True if re.match(r'[A-Z]', word_) else False


def is_last(word_):
    return True if re.match(r'[.!?]', word_[-1]) else False


def get_first(trigrams_):
    first_word = random.choice(list(trigrams_.keys()))
    while not (is_capital(first_word.split()[0]) and not is_last(first_word.split()[0])):
        first_word = random.choice(list(trigrams_.keys()))
    return first_word


def create_sentence(trigrams_):
    next_word = get_first(trigrams_)
    chain = next_word.split()
    while True:
        second_word = random.choices(population=trigrams_.get(next_word)[0],
                                     weights=trigrams_.get(next_word)[1])[0]
        chain.append(second_word)
        next_word = f'{chain[-2]} {chain[-1]}'
        if is_last(next_word) and len(chain) >= 5:
            break
    return " ".join(chain)
