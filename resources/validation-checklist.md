# Validation, robustness and generalization checklist

Use this checklist when designing or reviewing a computational PD neuroimaging study.

## Dataset definition

- [ ] Report the number of **independent subjects**, not only slices/scans.
- [ ] Describe disease stage, clinical phenotype, medication status and diagnostic criteria.
- [ ] Report class distribution and relevant demographic variables.
- [ ] Distinguish PD-vs-control from clinically harder differential-diagnosis tasks.

## Partitioning and leakage control

- [ ] Split at the **subject level**.
- [ ] Keep all visits from one participant in the same partition.
- [ ] Keep all modalities/sequences from one participant in the same partition.
- [ ] Fit normalization, feature selection, PCA and harmonization using training data only.
- [ ] Do not use the final test set for model selection or repeated tuning.

## Internal validation

- [ ] Use stratification only when clinically/statistically appropriate.
- [ ] Prefer repeated or nested CV when tuning many hyperparameters on small datasets.
- [ ] Report variability/confidence intervals, not only one point estimate.

## Generalization

- [ ] Keep an untouched holdout set whenever possible.
- [ ] Add external testing from another center/scanner/population.
- [ ] Consider leave-one-site-out or site-held-out evaluation for multisite data.
- [ ] Report site/scanner subgroup performance.
- [ ] Test clinically meaningful subgroups such as early/prodromal disease when relevant.

## Metrics

- [ ] Accuracy
- [ ] Balanced accuracy for imbalanced tasks
- [ ] Sensitivity / specificity
- [ ] Precision / F1
- [ ] ROC-AUC
- [ ] Precision–recall metrics when class imbalance is substantial
- [ ] Confusion matrix counts
- [ ] Calibration / Brier score when probabilities are used clinically

## Explainability and uncertainty

- [ ] Match XAI method to representation (image, tabular, graph, multimodal).
- [ ] Test explanation stability across runs/folds where possible.
- [ ] Perform perturbation or sanity checks rather than relying only on attractive heatmaps.
- [ ] Evaluate whether explanations are consistent with the biological signal of the modality.
- [ ] Report uncertainty or flag out-of-distribution/ambiguous cases where relevant.

## Clinical translation

- [ ] Define the intended clinical use: screening, second reader, differential diagnosis, prognosis, staging, etc.
- [ ] Compare against strong clinical or imaging baselines.
- [ ] Prefer clinically realistic tasks over only PD-vs-healthy-control classification.
- [ ] Evaluate workflow burden, missing modalities and inference time.
- [ ] For deployment claims, seek prospective multicenter and human–AI impact evaluation.
