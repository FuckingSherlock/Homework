nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(word):
    if word in nums:
        print(nums[word])
    elif str(word).lower() in nums:
        print(nums[str(word).lower()].title())
    else:
        return None


num_translate_adv(input())
