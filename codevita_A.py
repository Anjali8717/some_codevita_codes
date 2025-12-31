import sys
from typing import List, Tuple
Event = Tuple[int, int]

def max_chairs_needed() -> int:
    input = sys.stdin.read
    data = input().split()

    idx = 0 
    N = int(data[idx])
    idx += 1

    orders: List[Tuple[int, int, int]] = []

    for i in range(N):
        A = int(data[idx])
        P = int(data[idx + 1])
        V = int(data[idx + 2])
        orders.append((A, P, V))
        idx +=3

    orders.sort(key=lambda x: (x[2], x[0], x[1]))


    events: List[Event] = []
    cur_time = 0 

    for arrival, pack, vip in orders:
        start_serve = max(cur_time, arrival)

        finish = start_serve + pack

        if start_serve > arrival:

            events.append((arrival, 0))

            events.append((start_serve, 1))

            cur_time = finish

        if not events:
            return 0 
        
        events.sort()

        for _, orig_idx in events:
            print(orig_idx)

        return 0 
    
if __name__ == "__main__":
    max_chairs_needed()
    