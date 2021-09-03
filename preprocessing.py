from collections import defaultdict, Counter


def get_trigram(path):
    with open(path, 'r', encoding='utf-8') as file:
        corpus = file.read().split()
    corpus_to_pair = [(corpus[i], corpus[i + 1], corpus[i + 2])
                      for i in range(len(corpus) - 2)]

    result = defaultdict(list)
    for head_1, head_2, tail_ in corpus_to_pair:
        head_ = f'{head_1} {head_2}'
        result[head_].append(tail_)

    for head_ in result:
        tails_and_weights = dict(Counter(result[head_]).most_common())
        tails_ = list(tails_and_weights.keys())
        weights_ = list(tails_and_weights.values())
        result.update({head_: (tails_, weights_)})

    return result
