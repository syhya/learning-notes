# Overview of NLP Tasks

## Part-of-Speech (POS) Tagging
- Annotate each word in a sentence with a part-of-speech (e.g., verb, adjective, noun)

## Word Segmentation
- Applicable for Chinese

## Parsing
- **Constituency Parsing**
- **Dependency Parsing**

## Coreference Resolution（指代消解）
- Identify which words refer to the same entity

## Summarization
- **Extractive Summarization**
- **Abstractive Summarization**

## Machine Translation
- Unsupervised machine translation is a critical research direction

## Grammar Error Correction

## Sentiment Classification
- **Input:** Sequence
- **Output:** Class

## Stance Detection（立场检测）

## Veracity Prediction

## Natural Language Inference (NLI)（自然语言推理）

## Search Engine

## Question Answering (QA)

## Dialogue（对话）
1. **Chatting**
2. **Task-oriented（任务导向）**
   - Natural Language Generation (NLG)
   - Policy & State Tracker

## Natural Language Understanding (NLU)
- **Intent Classification**
- **Slot Filling**

## Knowledge Graph
1. **Extract Entity**
2. **Extract Relation**

## Named Entity Recognition (NER)

## Relation Extraction

## General Language Understanding Evaluation (GLUE)
- **SuperGLUE**
- **DecaNLP**

## BERT
- **Pre-train**
- Represent each token by an embedding vector

### Contextualized Word Embedding

### ALBERT

## How to Fine-Tune
- **Fine-Tune Methods:**
  - Adaptor
  - Weighted Features

# 学习向量和矩阵运算

- **重点是矩阵乘法，理解数据在模型中的表示方式。**
- **Python** 用 `numpy`，**R** 用 `matrix`。
- 掌握偏导和梯度
- 了解函数变化率，重点是梯度的计算和意义。
- 简单学习线性回归
  - 只需掌握核心概念，不深入公式推导。
- 了解损失函数（MSE）。
- 理解模型优化的核心思想
  - **牢记：损失函数的最小值对应模型的最优权重。**
- 理解梯度下降的核心原理
  - **牢记：梯度的反方向是函数下降最快的方向。**
- 掌握梯度下降优化算法
  - **死记硬背公式：下一次权重 = 当前权重 - 学习率 * 当前梯度**
- 学习决策树和随机森林
  - 理解决策树的基本概念，熟悉熵的计算。
- 理解训练集、验证集、测试集的用途。
- 逻辑回归和交叉熵
  - 了解逻辑回归的作用及其损失函数（交叉熵）。
- 深度学习核心概念
  - **牢记：深度学习通过梯度下降求解损失函数得到权重。**