# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 22:02:23 2025

@author: USER
"""

from sklearn.metrics import precision_recall_fscore_support, mean_squared_error
import math
def evaluate_triples(pred_triples, gt_triples):
    # treat triples as strings
    pred_set = set([tuple(t) for t in pred_triples])
    gt_set = set([tuple(t) for t in gt_triples])
    tp = len(pred_set & gt_set)
    precision = tp / len(pred_set) if pred_set else 0.0
    recall = tp / len(gt_set) if gt_set else 0.0
    f1 = (2*precision*recall/(precision+recall)) if (precision+recall)>0 else 0.0
    return {"precision":precision, "recall":recall, "f1":f1}

def evaluate_personality(pred, gt):
    # pred and gt are dicts mapping trait->score
    y_pred = [pred[t] for t in sorted(gt)]
    y_true = [gt[t] for t in sorted(gt)]
    mse = mean_squared_error(y_true, y_pred)
    rmse = math.sqrt(mse)
    return {"rmse": rmse}