#!/usr/bin/env python3
"""Compute a compact binary-classification metric set from prediction CSV.

Required columns: y_true, y_score
Optional column: y_pred (otherwise threshold y_score at --threshold)
"""
import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, balanced_accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, average_precision_score, confusion_matrix,
    brier_score_loss
)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--csv', required=True)
    p.add_argument('--threshold', type=float, default=0.5)
    args = p.parse_args()

    df = pd.read_csv(args.csv)
    for col in ['y_true','y_score']:
        if col not in df.columns:
            raise SystemExit(f"Missing required column: {col}")

    y = df['y_true'].astype(int).to_numpy()
    s = df['y_score'].astype(float).to_numpy()
    pred = df['y_pred'].astype(int).to_numpy() if 'y_pred' in df.columns else (s >= args.threshold).astype(int)

    labels = np.unique(y)
    if not set(labels).issubset({0,1}) or len(labels) != 2:
        raise SystemExit('This template expects binary y_true labels encoded as 0/1.')

    tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0,1]).ravel()
    specificity = tn / (tn + fp) if (tn + fp) else float('nan')

    out = {
        'n': len(y),
        'accuracy': accuracy_score(y, pred),
        'balanced_accuracy': balanced_accuracy_score(y, pred),
        'sensitivity_recall': recall_score(y, pred, zero_division=0),
        'specificity': specificity,
        'precision': precision_score(y, pred, zero_division=0),
        'f1': f1_score(y, pred, zero_division=0),
        'roc_auc': roc_auc_score(y, s),
        'pr_auc_average_precision': average_precision_score(y, s),
        'brier_score': brier_score_loss(y, s),
        'tn': int(tn), 'fp': int(fp), 'fn': int(fn), 'tp': int(tp),
    }
    for k,v in out.items():
        if isinstance(v, float):
            print(f"{k}: {v:.4f}")
        else:
            print(f"{k}: {v}")


if __name__ == '__main__':
    main()
