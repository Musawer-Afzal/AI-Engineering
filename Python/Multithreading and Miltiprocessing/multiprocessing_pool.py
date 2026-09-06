# Using normal function we are only taking advantage of one core
# def f(n):
#     return n*n

# if __name__ == "__main__":
#     array = [1, 2, 3, 4, 5]
#     result = []
#     for n in array:
#         result.append(f(n))

#     print(result)


# Now lets do the above process using multiprocessing
from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(10000):
        sum += x*x

    return sum


if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000)) # this runs for 100000 * 10000(from the function that we are calling)
    p.close()
    p.join()

    print("Pool Time: ", time.time() - t1, " seconds")

    t2 = time.time()
    result = []
    for x in range(100000): # this also runs for 100000 * 10000(from the function that we are calling)
        result.append(f(x))

    print("Normal Time: ", time.time() - t2, " seconds")


# def f(n):
#     return n*n


# if __name__ == "__main__":
#     p = Pool(processes = 3)
#     result = p.map(f, [1, 2, 3, 4, 5])
#     for n in result:
#         print(n)