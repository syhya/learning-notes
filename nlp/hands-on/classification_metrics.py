"""
accuracy, recall, precision, f1 scores。
"""
import torch
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt


def get_metrics(y_true, y_pred):
    n = len(y_true)
    tp  = ((y_true == 1) & (y_pred == 1)).sum().item()
    tn = ((y_true == 0) & (y_pred == 0)).sum().item()
    fp = ((y_true == 0) & (y_pred == 1)).sum().item()
    fn = ((y_true == 1) & (y_pred == 0)).sum().item()
    print(tp, tn, fp, fn, n)

    accuracy = (tp + tn) / n
    if tp + fn > 0:
        recall = tp / (tp + fn)
    else:
        recall = 0
    if tp + fp > 0:
        precision = tp / (tp + fp)
    else:
        precision =0
    if precision == precision == 0:
        f1 = 0
    else:
        f1 = 2 * recall  * precision / (recall + precision)
    print(accuracy, recall, precision, f1)


def visualize_roc(y_true, y_pred):
    # Calculate AUC
    auc_score = roc_auc_score(y_true, y_pred)

    # Calculate ROC Curve
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)

    # Plot ROC Curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f"AUC = {auc_score:.2f}")
    plt.plot([0, 1], [0, 1], linestyle='--', color='grey', label="Random Guess")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend(loc="lower right")
    plt.show()

    print(auc_score)

if __name__ == "__main__":

    y_true = torch.tensor([0, 1, 1, 0, 1])
    y_pred = torch.tensor([0, 1, 1, 1, 0])
    auc_score = get_metrics(y_true, y_pred)
    visualize_roc(y_true, y_pred)


