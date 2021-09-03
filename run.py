from model import create_sentence
from preprocessing import get_trigram
import random
import re


def run():
    random.seed()
    # while True:
    input_ = input()
    # if input_ == "exit":
    #     break
    if re.match(r'.*corpus.txt', input_):
        try:
            trigrams = get_trigram(input_)
            for i in range(10):
                print(create_sentence(trigrams))
        except FileNotFoundError as e:
            print(f"{e.__class__.__name__}!!"
                  f"File not found at {input_}. Make sure the file "
                  "has not been deleted or moved.")
    else:
        try:
            pass
        except Exception as e:
            print(e.__class__.__name__)
            pass
