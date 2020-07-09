import re

def word_count(s, cache):
    """count words in a string and cache the counts"""
    # format string
    s = s.lower()
    pattern = re.compile(r"[^a-zA-Z\'\s]")
    s = re.sub(pattern, "", s)
    s = s.split()

    for word in s:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1

cache = {}

with open("applications/histo/robin.txt", "r") as robin:
    for line in robin:
        word_count(line, cache)

# sort cache
sorted_cache = list(cache.items())
sorted_cache.sort(key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    for word, count in sorted_cache:
        print(f"{word.ljust(20)}{'#'*count}")
