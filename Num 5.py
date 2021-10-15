from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(quantity):
    joke = []
    while len(joke) < quantity:
        joke.append(
            f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    print(joke)


get_jokes(5)
