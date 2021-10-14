nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(word):
    word_lower = ''.join(word).lower()
    if word in nums:
        print(nums[word])
    elif word_lower in nums:
        print(nums[word_lower].title())
    else:
        print(None)


num_translate_adv(str(input()))
