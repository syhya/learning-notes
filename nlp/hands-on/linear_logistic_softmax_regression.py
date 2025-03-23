import torch
import torch.nn as nn

"""
- **线性回归**：回归问题，输出连续数值
  - 定义了参数 `weights` 和 `bias`。
  - 前向传播为线性组合：\( y = xW + b \)。
  - 损失函数使用均方误差 (MSE)。
"""
class LinearRegression(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        # (input_dim, output_dim = 1)
        self.weights = torch.nn.Parameter(torch.randn(input_dim, 1))
        self.bias = torch.nn.Parameter(torch.randn(1))
    
    def forward(self, x):
        # (batch_size, input_dim) @ (input_dim, 1) = (batch_size, 1)
        y = x @ self.weights + self.bias
        return y

    # 均方误差损失函数
    def mse_loss(self, pred, target):
        # 均方误差公式: loss = Σ (pred - target)^2 / batch_size
        loss = torch.mean((pred - target) ** 2)
        return loss

# 测试线性回归
def test_linear_regression():
    # (batch_size=10, input_dim=3)
    x = torch.randn(10, 3)
    y = torch.randn(10, 1)
    linear_model = LinearRegression(input_dim=3)
    preds = linear_model(x)
    print(f"Linear Regression preds: {preds}" )
    loss = linear_model.mse_loss(preds, y)
    print(f"Linear Regression loss: {loss.item()}")


"""
- **逻辑回归**： 二分类问题，输出 0/1 标签的概率。
  - 定义了参数 `weights` 和 `bias`。
  - 前向传播为 sigmoid 激活后的线性组合：\( y = \sigma(xW + b) \)。
  - 损失函数为二元交叉熵损失（binary cross entropy）。
"""
class LogisticRegression(nn.Module):
    def __init__(self, input_dim, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.weights = torch.nn.Parameter(torch.randn(input_dim, 1))
        self.bias = torch.nn.Parameter(torch.randn(1))

    def forward(self, x):
        y = torch.sigmoid(x @ self.weights + self.bias)
        return y
    
    # 自定义二元交叉熵损失函数
    def binary_cross_entropy(self, pred, target):
        # pred: (batch_size, 1), target: (batch_size, 1)，值为0或1
        # 二元交叉熵公式:
        # loss = -[target * log(pred) + (1 - target) * log(1 - pred)] / batch_size
        pred = torch.clip(pred, self.eps, 1 - self.eps) # 防止log(0)
        single_loss = -(target * torch.log(pred) + (1 - target) * torch.log(1 - pred))
        loss = torch.mean(single_loss)
        return loss

# 测试逻辑回归
def test_logistic_regression():
    # (batch_size=10, input_dim=3)
    x = torch.randn(10, 3)

    # val: 0 or 1. size: (batch_size, 1)
    y = torch.randint(low=0, high=2, size=(10, 1)).float()
    logistic_model = LogisticRegression(input_dim=3)
    preds = logistic_model(x)
    print(f"Logistic Regression preds: {preds}")
    loss = logistic_model.binary_cross_entropy(pred=preds, target=y)
    print(f"Logistic Regression loss: {loss.item()}")  
      

"""
- **多分类逻辑回归（Softmax回归）**：多分类问题，输出在多个类别上的概率分布。
  - 定义了参数 `weights` 和 `bias`。
  - 前向传播为 softmax 激活后的线性组合：\( y = \text{softmax}(xW + b) \)。
  - 损失函数使用手写的**多分类交叉熵损失**（cross entropy）。
"""

class SoftmaxRegression(nn.Module):
    def __init__(self, input_dim, num_classes, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.weights = torch.nn.Parameter(torch.randn(input_dim, num_classes))
        self.bias = torch.nn.Parameter(torch.randn(num_classes))
    
    def forward(self, x):
        #(batch_size, input_dim) @ (input_dim, num_classes) = (batch_size, num_classes)
        y = torch.softmax(x @ self.weights + self.bias, dim=-1)
        return y
    
    # 自定义多分类交叉熵损失函数
    def cross_entropy(self, pred, target):
        # pred: (batch_size, num_classes), softmax概率；target: (batch_size, num_classes)，one-hot编码
        # 多分类交叉熵公式:
        # loss = - Σ [target * log(pred)] / batch_size
        pred = torch.clip(pred, self.eps, 1 - self.eps) # 防止log(0)
        single_loss = -(target * torch.log(pred)).sum(dim=-1)
        loss = torch.mean(single_loss)
        return loss

# 测试多分类逻辑回归
def test_softmax_regression():
    # (batch_size=10, input_dim=3)
    x = torch.randn(10, 3)
    # val: 0, 1, 2, 3 
    y_labels = torch.randint(0, 4, (10, ))
    y = torch.nn.functional.one_hot(y_labels, num_classes=4).float()
    print(f"In softmax regression, y is {y}")
    softmax_model = SoftmaxRegression(input_dim=3, num_classes=4)
    preds = softmax_model(x)
    print(f"Softmax Regression preds: {preds}")
    loss = softmax_model.cross_entropy(preds, y)
    print(f"Softmax Regression loss: {loss.item()}")     


if __name__ == "__main__":
  test_linear_regression()
  test_logistic_regression()
  test_softmax_regression()
  
