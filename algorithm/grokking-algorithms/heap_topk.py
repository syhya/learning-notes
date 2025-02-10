# 构建小根堆
def sift(li ,low, high):
    """
    :param li:列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根结点
    j = 2*i+1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j+1 <= high and li[j+1] < li[j]:
            j = j+1  # j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j    # 往下看一层
            j = 2*i+1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def took(li, k):
    # 1.建堆
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 2.遍历
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 3.出数
    for i in range(k-1, -1, -1):
        # i指向当前堆的最后一个元素
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap

li = [i for i in range(10)]
import random
random.shuffle(li)
print(li)
print(took(li, 4))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(took(nums, k))





