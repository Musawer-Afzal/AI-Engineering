import time
import multiprocessing as mp

square_result = []
def calc_square(num):
    global square_result
    for n in num:
        print(f"Square: {n ** 2}")
        square_result.append(n**2) 
    print(f"with in Process Result: {square_result}")


# def calc_cube(num):
#     for n in num:
#         time.sleep(3)
#         print(f"Cube: {n ** 3}")


if __name__ == "__main__":
    arr = [4, 7, 5, 7]

    p1 = mp.Process(target = calc_square, args = (arr,))
    # p2 = mp.Process(target = calc_cube, args = (arr,))

    t = time.time()
    p1.start()
    # p2.start()

    p1.join()
    # p2.join()
    print(f"Done in: {time.time() - t} seconds")