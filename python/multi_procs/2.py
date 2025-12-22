import multiprocessing
import time
import threading

# 전역 변수 (Global Variable)
# 프로세스 세상에서는 이게 '공유'되는 게 아니라 '복사'됩니다.
count = 0

def worker():

    global count
    for _ in range(100):
        count += 1
    
    # 각 프로세스 내부에서는 100이 됩니다.

if __name__ == "__main__":
    procs = []
    
    # 4개의 프로세스 생성
    for _ in range(4):
        p = multiprocessing.Process(target=worker)
        procs.append(p)
        p.start()
        # t = threading.Thread(target=worker)
        # procs.append(t)
        # t.start()


    for p in procs:
        p.join()

    # 기대값: 400 (4명이 100씩 했으니까)
    # 실제값: 0 (메인 프로세스의 count는 아무도 건드리지 않음)
    print(f"Main Process Result: {count}")