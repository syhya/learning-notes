# https://blog.csdn.net/Mr_fengzi/article/details/96427737?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-6.opensearchhbase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-6.opensearchhbase
#  返回装载的古董和装载的装载的古董

def max_ans(nums):
    nums_sort = sorted(nums)
    c = int(input("请输入海盗船所能装载的最大容量："))
    a = 0   #记录装载古董重量
    count = 0    # count记录装载古董数量
    ship = []   #记录装载的古董
    for i in range(len(nums_sort)):
        a += nums_sort[i]
        if a < c:
            ship.append(nums_sort[i])
            count += 1

    print("装载古董的数量:", count)
    print("装载古董:", ship)

if __name__ == "__main__":
    nums = [4, 10, 7, 11, 3, 5, 14, 2]
    max_ans(nums)









