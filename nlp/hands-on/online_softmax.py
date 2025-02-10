import torch

def online_softmax(x, dim=-1, batch_size=128):
    """
    Computes softmax in an online manner to reduce memory usage.
    
    Parameters:
        x (torch.Tensor): Input tensor.
        dim (int): The dimension along which to compute the softmax. Default is -1.
        batch_size (int): Size of each batch for online computation.
    
    Returns:
        torch.Tensor: Softmax-transformed tensor with the same shape as the input.
    """
    # Ensure the dimension is positive
    dim = dim if dim >= 0 else x.dim() + dim
    
    # Step 1: Find max values in an online manner
    max_x = torch.amax(x, dim=dim, keepdim=True)
    
    # Initialize softmax result
    result = torch.zeros_like(x)
    
    # Step 2: Online exponentiation and normalization
    exp_sum = torch.zeros_like(max_x)  # To accumulate the sum of exponentials
    for start in range(0, x.size(dim), batch_size):
        # Slicing the data along the target dimension
        end = min(start + batch_size, x.size(dim))
        indices = [slice(None)] * x.dim()
        indices[dim] = slice(start, end)
        
        # Subtract max_x for stability and compute exp
        exp_values = torch.exp(x[tuple(indices)] - max_x)
        result[tuple(indices)] = exp_values
        
        # Accumulate the sum of exponentials
        exp_sum += torch.sum(exp_values, dim=dim, keepdim=True)
    
    # Step 3: Normalize each batch
    result /= exp_sum
    return result


# 测试代码
x = torch.randn(1000, 10000)  # 大张量
result = online_softmax(x, dim=1, batch_size=256)
print(result.shape)  # 确保结果形状正确
print(torch.allclose(torch.sum(result, dim=1), torch.ones(1000), atol=1e-6))  # 每行归一化
