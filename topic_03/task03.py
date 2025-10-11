d = {'a': 1, 'b': 2}
d.update({'c': 3})
del d['a']
keys = d.keys()
values = d.values()
items = d.items()
d.clear()
print("Keys:", list(keys))
print("Values:", list(values))
print("Items:", list(items))
print("Dictionary after clear:", d)
