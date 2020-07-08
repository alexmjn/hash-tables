d = {
    'Austni':12,
    "MIchael":22,
    'stff':33
}

type(d.items())

list_items = list(d.items())

print(d.values())

sorted([(v, k) for k, v in d.items()])

# tuple unpacking with list comprehension

list_items.sort(reverse=True, key=lambda x: x[1])
print(list_items)
