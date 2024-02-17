result = []

def divider(a, b):
    if type(a) == str:
        a = int(a)
    # if a < b:

    if b == 100:
        raise IndexError
    return a / b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8: 4}
except:
    data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
    except NameError:
        kem = key
        res = divider(key, data[kem])
    result.append(res)
print(result)
