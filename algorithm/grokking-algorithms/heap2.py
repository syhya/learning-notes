import heapq  # q->queue 优先队列
import random

li = list(range(100))
random.shuffle(li)

print(li)
heapq.heapify(li)  # 建堆
print(li)

for i in range(len(li)):
    print(heapq.heappop(li), end=',')

