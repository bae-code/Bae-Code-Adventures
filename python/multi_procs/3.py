import threading
import time
import random

count = 0

def worker(name):
    global count
    
    for i in range(100):
        current = count
        
        # 1. 확률을 10%로 확 줄입니다. (대부분은 정상적으로 달림)
        if random.random() < 0.1:
            # 2. sleep(0)은 '순서 양보'입니다. 
            # 딜레이는 없지만 문맥 전환(Context Switch)을 유발합니다.
            # 가끔은 아주 조금(0.0001초) 쉬어서 '뒤쳐지는 놈'을 만듭니다.
            if random.random() < 0.5:
                time.sleep(0) 
            else:
                time.sleep(0.0001)
        
        count = current + 1

if __name__ == "__main__":

    for attempt in range(1, 6):
        count = 0
        threads = []
        
        for i in range(4):
            t = threading.Thread(target=worker, args=(f"T{i}",))
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
            
        print(f"[{attempt}회차] 결과: {count}")