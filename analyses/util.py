import numpy as np
import pandas as pd
import scipy.stats


def bootmean(arr, n=1000):
    idx = np.random.randint(0, len(arr), (n, len(arr)))
    means = np.asarray(arr)[idx].mean(axis=1)
    stats = pd.Series(
        np.percentile(means, [2.5, 50, 97.5]),
        index=["lower", "median", "upper"])
    stats["mean"] = arr.mean()
    stats["lerr"] = stats["mean"] - stats["lower"]
    stats["uerr"] = stats["upper"] - stats["mean"]
    return stats


def bootcorr(x, y, n=1000):
    idx = np.random.randint(0, len(x), (n, len(x)))
    x_ = np.asarray(x)
    y_ = np.asarray(y)
    corrs = np.array([scipy.stats.pearsonr(x_[i], y_[i])[0] for i in idx])
    stats = pd.Series(
        np.percentile(corrs, [2.5, 50, 97.5]),
        index=["lower", "median", "upper"])
    stats["corr"] = scipy.stats.pearsonr(x, y)[0]
    return stats


def sigmoid(x, beta):
    return 1.0 / (1 + np.exp(-beta * (x - 0.5)))
