from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(quantity, bool):
    joke = []
    while len(joke) < quantity <= 5:
        if bool:
            joke.append(
                f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        else:
            joke.append(
                f'{nouns.pop(nouns.index(choice(nouns)))} {adverbs.pop(adverbs.index(choice(adverbs)))} {adjectives.pop(adjectives.index(choice(adjectives)))}')
    print(joke)


get_jokes(5, False)
