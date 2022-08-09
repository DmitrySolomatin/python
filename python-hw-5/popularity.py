def popularity(text: str):
    lower_text = text.lower()
    array_words = lower_text.split(' ')
    words_count = dict(array_words)
    for word in array_words:
        if word in words_count:
            words_count [word] += 1
        else:
            words_count [word] = 1

def get_second_key(item):
    return item[1]

def get_first_key(item):
    return item[0]

sort_by_word = sorted(words_count.item(), key=lambda item: item[0])

sort_by_popularity = sorted(sort_by_word, key=get_second_key, reverse = True)

sorted_words = list(map(get_first_key, sort_by_popularity))

# return sorted_words


# popularity'app(le kiwi pineapple kiwi apple kiwi') -> ['kiwi', 'apple', 'pineapple']
# popularity('aPPle pine Apple kiwi Apple kiwi') -> ['apple', 'kiwi', 'pine']
# popularity('aPPle pine Apple kiwi Apple kiwi') -> ['apple', 'kiwi', 'pine']
# popularity('aab aaa aac aab aac aaa x') -> ['aaa', 'aab', 'aac', 'x']