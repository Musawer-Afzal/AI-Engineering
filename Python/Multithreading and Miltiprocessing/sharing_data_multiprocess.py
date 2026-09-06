import time
import multiprocessing as mp

def calc_square(num, result, v):
    v.value = 86.53 # We are actually assigning the value here in this process
    for idx, n in enumerate(num):
        result[idx] = n*n


if __name__ == "__main__":
    arr = [4, 7, 5, 7]
    result = mp.Array('i', 4)
    v = mp.Value('d', 0.0) # We are intentionally leaving the value as 0

    p1 = mp.Process(target = calc_square, args = (arr, result, v))
    t = time.time()
    p1.start()

    p1.join()

    # The Value will be available at the main/Parent Process
    print(f"Result: {result[:]}\nValue: {v.value}")
    print(f"Done in: {time.time() - t} seconds")