import torch
import torch.nn.functional as F

def cross_entropy_loss(y_true, y_pred, eps=1e-15):
    y_pred = torch.clip(y_pred, min=eps, max=1 - eps)

    batch_size = y_pred.size(0)

    loss = -torch.sum(y_true * torch.log(y_pred)) / batch_size
    return loss


# 假设 batch_size = 2，num_classes = 3
y_true = torch.tensor([[1, 0, 0], [0, 1, 0]], dtype=torch.float32)  # One-hot 编码
y_pred = torch.tensor([[0.9, 0.05, 0.05], [0.1, 0.8, 0.1]], dtype=torch.float32)  # 预测概率


# 计算交叉熵损失
loss = cross_entropy_loss(y_true, y_pred)
print("交叉熵损失：", loss.item())


def generalized_cross_entropy_loss(y_true, y_pred, eps=1e-15):
    """
    计算任意形状张量的交叉熵损失
    参数:
        y_true: 真实标签，形状为 (batch_size, seq_len, hidden_dim)
        y_pred: 预测值（logits），形状为 (batch_size, seq_len, hidden_dim)
    返回:
        平均交叉熵损失
    """
    # 对最后一个维度应用 softmax
    y_pred = F.softmax(y_pred, dim=-1)
    # 防止 log(0)
    y_pred = torch.clip(y_pred, min=eps, max=1 - eps)

    # 对 y_true 进行标准化，使其表示概率分布
    y_true = F.softmax(y_true, dim=-1)
    
    # 计算交叉熵损失
    loss = -torch.sum(y_true * torch.log(y_pred), dim=-1)  # 在最后一个维度求和
    # 计算 batch 的平均损失
    return loss.mean()

# 示例数据
y_true2 = torch.randn(2, 3, 4)  # 随机生成真实值
y_pred2 = torch.randn(2, 3, 4)  # 随机生成预测值

# 计算损失
loss2 = generalized_cross_entropy_loss(y_true2, y_pred2)
print("交叉熵损失：", loss2.item())
