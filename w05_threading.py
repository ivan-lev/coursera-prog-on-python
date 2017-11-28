from threading import Thread

def f(name):
    print('Hello', name)

th = Thread(target = f, args = ('Ivan',))
th.start()
th.join()



from concurrent.futures import ThreadPoolExecutor, as_completed

def func(a):
    return a * a

with ThreadPoolExecutor(max_workers = 3) as pool:
    results = [pool.submit(func, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
    
