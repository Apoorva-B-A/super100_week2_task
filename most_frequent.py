# beginner3_most_frequent.py

from collections import Counter

def most_frequent(lst):
    if not lst:
        return None
    count = Counter(lst)
    return count.most_common(1)[0][0]

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  # 3
