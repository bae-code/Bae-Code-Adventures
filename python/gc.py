# GC

import gc
import sys

class Node:
    def __init__(self,name):
        self.name = name
        self.link = None

def show_circular():
    # 객체 생성 ( Ref Cnt = 1)
    node_a = Node("A")
    node_b = Node("B")

    print(f"A ref: {sys.getrefcount(node_a)}")
    # 2 출력이 됩니다 ( 변수 선언 + getrefcount 인자)

    # 순환참조 생성
    node_a.link = node_b
    node_b.link = node_a
    print( " 순환참조 작업 후")
    
    # 각 노드 count 는 2 가 됩니다.
    # ? = 변수 node + node_n.link 값으로 참조되어있기때문

    print(f"A ref: {sys.getrefcount(node_a)}")
    
    # 3이 출력 됩니다 ( 변수 + link + 인자 전달)

    # 변수를 삭제합니다.

    del node_a
    del node_b

    print( " 변수 삭제 작업 후 ")

    # 접근 방법은 없지만, 서로 참조로 붙잡고있음
    # 메모리에서 사라지지않고 ref count가 1로 남아있습니다
    # (메모리 누수)

    # 이것을 방지하기위해 가비지 컬렉터 강제 호출
    # (실제로는 파이썬이 주기적으로 함)

    n = gc.collect()

    print(f"GC가 수거한 수 : {n}")

show_circular()