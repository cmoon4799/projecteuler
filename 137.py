from algos import is_square, fibonacci


for k in range(0, 32, 2):
    print(k//2, fibonacci(2*k + 1), ((-1)**k * fibonacci(2*k + 1, 2, 1) - 1)/5)
