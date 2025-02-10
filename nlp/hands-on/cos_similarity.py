"""
numpy or pytroch: Implement a function to calculate cosine similarity 
between vector A and vector B.
"""
import numpy as np
import torch
from sklearn.metrics.pairwise import cosine_similarity

def l2_norm(x):
    if isinstance(x, torch.Tensor):
        # L2 by torch
        return torch.sqrt(torch.sum(x ** 2)).item()
    else:
        # L2 by numpy
        return np.sqrt(np.sum(x ** 2))

def cos_similarity_numpy(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    print(norm_v1)
    print(l2_norm(v1))
    norm_v2 = np.linalg.norm(v2)
    cos = dot_product / (norm_v1 * norm_v2)
    return cos

def cos_similarity_torch(v1, v2):
    dot_product = torch.dot(v1, v2)
    norm_v1 = torch.norm(v1)
    print(l2_norm(v1))
    norm_v2 = torch.norm(v2)
    cos = dot_product / (norm_v1 * norm_v2)
    return cos


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(cos_similarity_numpy(arr1, arr2))

tensor1 = torch.tensor(arr1, dtype=torch.float16)
tensor2 = torch.tensor(arr2, dtype=torch.float16)
print(tensor1)
print(cos_similarity_torch(tensor1, tensor2))

print(cosine_similarity(tensor1.reshape(1, -1), tensor2.reshape(1, -1)))
