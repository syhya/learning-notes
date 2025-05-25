import torch

class MySigmoid(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        # Sigmoid 正向传播计算公式: y = 1 / (1 + exp(-x))
        output = 1 / (1 + torch.exp(-input))
        # 将输出保存下来，以便在反向传播时使用
        ctx.save_for_backward(output)
        return output
    
    @staticmethod
    def backward(ctx, grad_output):
        output, = ctx.saved_tensors
        # Sigmoid 反向传播公式: dL/dx = dL/dy * y * (1 - y)
        grad_input = grad_output * output * (1 - output) 
        return grad_input

# 测试代码
# 并设置 requires_grad=True 以便追踪梯度
x = torch.tensor(data=[1.0, 2.0, 3.0], requires_grad=True)
# 使用自定义的 Sigmoid 操作
y = MySigmoid.apply(x)

# 定义一个简单的损失函数：这里取 y 所有元素之和
loss = y.sum()

# 反向传播，计算 x 的梯度
loss.backward()

print("输入 x:\n", x)
print("Sigmoid 输出 y:\n", y)
print("x 的梯度:\n", x.grad)    
