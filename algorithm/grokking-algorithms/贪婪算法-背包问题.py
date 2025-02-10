#  背包问题

#假设山洞中有n种宝物，每种宝物有一定重量w和相应的价值v，
# 毛驴运载能力 一种宝物只能拿一样，宝物可分割。怎样才能使毛驴运走宝物的价值最大呢？


def bag(datas):
    donkey = 30 # 毛驴运载能力
    get_price = 0 # 获取的总价值
    for i in range(len(datas)):
        price = datas[i][1] / datas[i][0]
        datas[i].append(price)

    datas.sort(key=lambda data: data[2], reverse=True)  # 按性价比排序
    # 按性价比从大到小选取宝物，直到达到毛驴的运载能力
    for data in datas:
        if data[0] <= donkey:
            get_price += data[1]
            donkey -= data[0]
        else:
            get_price += data[2]*donkey
            break
    print("总价值：",get_price)







if __name__ == "__main__":
    # datas中每个元素代表一个古董，每个列表第一个元素代表古董重量，第二个元素代表古董价值
    datas = [
        [4, 3], [2, 8], [9, 18], [5, 6],
        [5, 8], [8, 20], [5, 5], [4, 6],
        [5, 7], [5, 15]
        ]
    bag(datas)
