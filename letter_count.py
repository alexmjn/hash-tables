from collections import Counter

def print_letter_counts(s):
    counter = Counter()
    for letter in s:
        if letter >= 'a' and letter <= 'z':
            counter[letter.lower()] += 1

    counter = sorted([(v, k) for k, v in counter.items()], reverse=True)

    for pair in counter:
        print(f'Count: {pair[1]}, letter: {pair[0]}')

print(print_letter_counts("the quick brown fox jumps over the lazy dog"))
