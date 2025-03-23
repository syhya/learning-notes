import torch

def dropout_pytorch(x, dropout_rate):
    # 生成随机掩码矩阵，并转换为浮点型
    mask = torch.rand(x.shape) > dropout_rate
    print("生成的掩码矩阵:\n", mask)
    
    # 应用掩码，将部分神经元置零
    x_mask = x * mask
    # 缩放输出，保持总和的期望值不变
    output = x_mask / (1 - dropout_rate)
    return output

# 测试代码
x = torch.tensor([[0.5, 0.3], [0.2, 0.8]])
dropout_rate = 0.5
output = dropout_pytorch(x, dropout_rate)
print("输出结果：\n", output)