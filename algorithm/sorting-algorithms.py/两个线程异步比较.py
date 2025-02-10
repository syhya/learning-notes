import time
from concurrent.futures import ThreadPoolExecutor
from calculation_time import cal_time
from flask import Flask, request
import random
import copy

executor = ThreadPoolExecutor(2)
app = Flask(__name__)


nums = list(range(10000))
random.shuffle(nums)

nums_1 = copy.deepcopy(nums)
nums_2 = copy.deepcopy(nums)


@cal_time
def bubble_sort(nums):
    for i in range(len(nums)-1):
        flag = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = True
        if not flag:
            return


def partition(nums, left, right):
    p = nums[left]
    while left < right:
        while left < right and nums[right] >= p:  # 从右边找比p小的数
            right -= 1      # 往左走一位
        nums[left] = nums[right]    # 把右边的值放到左边空位上
        while left <right and nums[left] <= p:
            left += 1
        nums[right] = nums[left]  # 把左边的值放到右边空位上
    nums[left] = p  # 重点；把p归位到left和right相遇的位置
    return left


def _quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        _quick_sort(nums, left, mid-1)
        _quick_sort(nums, mid+1, right)


@cal_time
def quick_sort(nums):
    _quick_sort(nums, 0, len(nums)-1)



# 模拟耗时任务
def run_job(name):
    # 推迟执行的秒数
    time.sleep(0)
    bubble_sort(nums_2)
    print(time.ctime())
    print("冒泡排序2完成了")
    return

# @app.route("/task")
# def run_task():
#     """
#     同步执行
#     """
#     name = request.args.get("name")
#     run_job(name=name)
#     return {"ret": "ok"}


@app.route("/async_task")
def run_async_task():
    """
    异步执行
    """
    name = request.args.get("name")
    executor.submit(run_job, name=name)
    bubble_sort(nums_1)
    #quick_sort(nums_1)
    print(time.ctime())
    print("冒泡排序1完成了")
    return "冒泡排序1完成了"


if __name__ == '__main__':
    app.run(debug=True)