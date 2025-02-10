 we do a pass forward through a model’s layers⁠(opens in a new window) to compute an output for each training example in a batch of data. 

 Then another pass proceeds backward⁠(opens in a new window) through the layers, propagating how much each parameter affects the final output by computing a gradient⁠(opens in a new window) with respect to each parameter



 Various parallelism techniques slice this training process across different dimensions, including:

Data parallelism—run different subsets of the batch on different GPUs;
Pipeline parallelism—run different layers of the model on different GPUs;
Tensor parallelism—break up the math for a single operation such as a matrix multiplication to be split across GPUs;
Mixture-of-Experts—process each example by only a fraction of each layer.


Data parallelism：

That being said, there are strategies to increase the effective RAM available to your GPU, such as temporarily offloading parameters to CPU memory between usages.

