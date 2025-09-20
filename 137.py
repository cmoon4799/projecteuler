from algos import is_square

res = 0
i = 1
while True:
    if is_square(5 * i**2 + 2 * i + 1):
        res += 1
        print(res, i)
    if res == 15:
        break
    i += 1
