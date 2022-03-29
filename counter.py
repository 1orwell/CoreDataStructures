from collections import defaultdict
from collections import Counter

def top_three_letters(word):
    counter = defaultdict(lambda: 0)
    for val in word:
        counter[val] += 1
    sorted_counter = sorted(counter, key=lambda k:counter[k], reverse=True)
    top_three = sorted(counter, key=lambda k:counter[k], reverse=True)[:3]
    result = [(letter, counter[letter]) for letter in top_three]
    print(result)

def top_three_better(word):
    # Well, this is just amazing
    print(Counter(word).most_common(3))

top_three_letters("aadbbbcdeeeeeee")
top_three_better("fdsaffffdsss")
    