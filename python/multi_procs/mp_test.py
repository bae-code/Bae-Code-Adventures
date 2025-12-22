import multiprocessing
import queue
def worker(q:queue.Queue, num: int):
    q.put(num)


if __name__ == "__main__":

    q = multiprocessing.Queue()
    procs = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(q,i))
        procs.append(p)
        p.start()

    for p in procs:
        p.join()


    results = []


    while not q.empty():
        results.append(q.get())

    print(f"After: {results}")