import time
import multiprocessing as mp

def calc_square(num, result):
    for idx, n in enumerate(num):
        result[idx] = n*n


if __name__ == "__main__":
    arr = [4, 7, 5, 7]
    result = mp.Array('i', 4)

    p1 = mp.Process(target = calc_square, args = (arr, result))
    t = time.time()
    p1.start()

    p1.join()

    print(f"Result: {result[:]}")
    print(f"Done in: {time.time() - t} seconds")