import time
import multiprocessing as mp

def calc_square(num, q):
    for n in num:
        q.put(n*n)


if __name__ == "__main__":
    arr = [4, 7, 5, 7]
    q = mp.Queue()

    p1 = mp.Process(target = calc_square, args = (arr, q))
    t = time.time()
    p1.start()

    p1.join()

    while not q.empty():
        print(q.get())

    print(f"Done in: {time.time() - t} seconds")