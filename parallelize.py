from multiprocessing import Pool

# expensive operation
def f(x):
    return x ** 2

# use 4 pools
if __name__ == '__main__':
    with Pool(4) as p:
        print(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8]))