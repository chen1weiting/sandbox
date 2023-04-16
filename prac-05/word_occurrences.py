from typing import Dict, Any


def count_words(text):
    words = text.split()
    counts: dict[Any, int] = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(count_words("text"))
