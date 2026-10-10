# 🧠 PD Computational Neuroimaging Review

## Companion repository for
### *Advances in Computational Neuroimaging for Parkinson’s Disease: Models, Multimodal Learning, Validation, and Clinical Translation*

**Authors:** Muhammad Zubair and Malika Bendenchache  
**Manuscript year:** 2026  
**Status:** Companion repository for the review manuscript. Add the final journal citation and DOI after publication.

---

## 📖 About this repository

This repository is designed as a practical companion to our state-of-the-art review on computational neuroimaging for Parkinson’s disease (PD). The review does not treat the imaging modality, computational model, validation design, explainability, and clinical translation as separate topics. Instead, it follows the complete pathway:

> **Neuroimaging signal → computational representation → learning model → multimodal integration → validation → explanation → clinical translation**

The repository provides readers with a concise roadmap of the review, curated PD neuroimaging data resources, software/tool links, representative studies, and lightweight reproducibility scripts for subject-level splitting and binary-classification evaluation.

> **Clinical-use disclaimer:** This repository is for research and education. It is not a diagnostic device and does not provide clinical recommendations.

---

## 🔍 What the review covers

The review spans:

- **Neuroimaging modalities:** structural MRI, diffusion MRI/DTI, functional MRI, nigral-sensitive and neuromelanin MRI, QSM/SWI, DAT-SPECT, and PET.
- **Computational representations:** raw 3D volumes, parametric maps, regional/radiomic features, tracer-uptake measures, and structural/functional brain networks.
- **Model evolution:** handcrafted features, conventional machine learning, CNNs, 3D deep learning, graph neural networks, attention mechanisms, Transformers, contrastive learning, self-supervised learning, foundation-model strategies, and distributed learning.
- **Multimodal learning:** anatomical–microstructural, structure–function, MRI–PET/SPECT, imaging–clinical, graph-based, attention-based, contrastive, and cross-modal representations.
- **Reliability:** dataset size, class distribution, site/scanner bias, harmonization, leakage, cross-validation, external testing, shortcut learning, and generalization.
- **Explainability:** LIME, LRP, Grad-CAM, SmoothGrad, SHAP, graph explainers, attention-based interpretation, uncertainty, and neurobiological plausibility.
- **Clinical translation:** differential diagnosis, prodromal/early disease, prognosis, staging, uncertainty-aware decision support, prospective multicenter validation, and human–AI collaboration.

---

## ❓ Research questions

| RQ | Question | Review section |
|---|---|---|
| **RQ1** | How does the biological information provided by different neuroimaging modalities influence computational representation and model design for PD? | Section II |
| **RQ2** | How have computational methods for PD neuroimaging evolved, and what has been gained from increasing model complexity? | Section III |
| **RQ3** | How is information from multiple neuroimaging modalities integrated, and when does multimodal learning provide meaningful advantages? | Section IV |
| **RQ4** | How reliable and generalizable are reported computational PD neuroimaging results? | Section V |
| **RQ5** | To what extent are model predictions explainable and neurobiologically plausible? | Section VI |
| **RQ6** | What evidence is required to translate computational neuroimaging models into clinically useful decision-support systems? | Section VII |

A more detailed section-to-RQ map is available in [`resources/paper-roadmap.md`](resources/paper-roadmap.md).

---

## 🧭 Visual roadmap

### 1. From neuroimaging signal to computational representation

![Neuroimaging to computational representation](assets/figure1_neuroimaging_to_representation.png)

### 2. Evolution of computational PD neuroimaging

![Evolution of computational PD neuroimaging](assets/figure2_computational_evolution.png)

### 3. Evidence hierarchy for clinical translation

![Evidence hierarchy for clinical translation](assets/figure3_clinical_translation_evidence_hierarchy.png)

> These figures were extracted from the authors' manuscript draft for use in this companion repository. After publication, verify the journal's figure-reuse policy before keeping manuscript figures in a public repository.

---

## 📚 Data resources for PD neuroimaging

| Resource | PD relevance | Modalities / data | Access |
|---|---|---|---|
| **PPMI** | Major longitudinal PD/prodromal research cohort | MRI, DAT imaging, clinical, biomarkers, genetics, sensor data | Registration + data-use agreement |
| **NINDS PDBP** | PD and related-disorder research resource | Imaging, clinical, genetic and biomarker data | Researcher account / controlled access |
| **OpenNeuro ds001907** | Public PD vs healthy-aging dataset | Anatomy, resting/task fMRI, DTI; repeated sessions | Public BIDS dataset |
| **ENIGMA-PD** | Large international multicenter collaboration | Structural MRI, DTI, fMRI and harmonized analyses | Consortium/collaborative access |

See [`resources/datasets.md`](resources/datasets.md) and [`data/dataset_catalog.csv`](data/dataset_catalog.csv) for details.

---

## 🧰 Useful open-source tools

The review spans several stages of the neuroimaging pipeline. We therefore curate tools by purpose rather than by model family:

- **Data standards & I/O:** BIDS Validator, NiBabel, DataLad
- **Registration / preprocessing:** ANTs, FSL, fMRIPrep
- **Diffusion MRI:** MRtrix3, DIPY
- **Functional MRI:** Nilearn
- **Radiomics:** PyRadiomics
- **Deep learning:** MONAI, TorchIO, PyTorch
- **Graph learning:** PyTorch Geometric
- **Harmonization:** neuroCombat / ComBat-based workflows
- **Explainability:** Captum, SHAP
- **Evaluation:** scikit-learn + repository scripts

See [`resources/software-tools.md`](resources/software-tools.md).

---

## ✅ Reproducibility and validation checklist

The repository includes a practical checklist derived from the methodological issues emphasized in the review. At minimum, PD neuroimaging studies should document:

- subject-level splitting;
- separation of longitudinal visits and multimodal scans from the same participant;
- training-only fitting of normalization, feature selection and harmonization;
- class distribution and clinically relevant metrics;
- repeated/nested cross-validation where appropriate;
- an untouched holdout test set;
- external or site-held-out evaluation whenever possible;
- scanner/site subgroup analysis;
- probability calibration and uncertainty reporting;
- XAI faithfulness/stability checks rather than visual heatmaps alone;
- clinically meaningful targets beyond only PD vs healthy controls.

Full checklist: [`resources/validation-checklist.md`](resources/validation-checklist.md)

---

## 🧪 Lightweight reproducibility utilities

### Check for subject leakage across data splits

```bash
python scripts/check_subject_splits.py \
  --csv your_split_file.csv \
  --subject-col subject_id \
  --split-col split \
  --site-col site
```

### Compute binary classification metrics

Input CSV columns: `y_true`, `y_score`, and optionally `y_pred`.

```bash
python scripts/classification_metrics.py --csv predictions.csv
```

Install the small Python dependency set with:

```bash
pip install -r requirements.txt
```

These scripts are intentionally simple templates. They do **not** reproduce any specific study in the review.

---

## 📊 Representative studies

A machine-readable table of representative studies highlighted across the review is provided in:

- [`data/representative_studies.csv`](data/representative_studies.csv)

It is organized by modality, computational approach, clinical task, and the reason each study is methodologically relevant.

---

## 📑 Citation

If you use this repository or its curated resources, please cite the associated review article. Until the final bibliographic record is available, use the following temporary citation and update it after publication:

```bibtex
@article{zubair2026pdneuroimaging,
  title   = {Advances in Computational Neuroimaging for Parkinson's Disease: Models, Multimodal Learning, Validation, and Clinical Translation},
  author  = {Zubair, Muhammad and Bendenchache, Malika},
  year    = {2026},
  note    = {Review manuscript; update journal, volume, pages and DOI after publication}
}
```

GitHub also reads [`CITATION.cff`](CITATION.cff) and can expose a **Cite this repository** button automatically.

---

## 🤝 Contributing

Suggestions for datasets, open-source implementations, benchmarking protocols, or newly published PD neuroimaging studies are welcome. Please follow [`CONTRIBUTING.md`](CONTRIBUTING.md) and do not upload patient-level clinical or imaging data to this repository.

---

## ⚖️ Data, image and licensing note

This repository does **not** redistribute PPMI, PDBP, ENIGMA-PD, or other controlled-access participant data. Users must obtain data directly from the original providers and comply with their data-use agreements.

No repository-wide open-source license has been selected in this starter package. Before making the repository public, the authors should choose an appropriate license for code/resources and confirm journal/publisher permissions for manuscript figures.

---

## 🔗 Suggested repository name

`PD-Computational-Neuroimaging-Review`

Suggested GitHub description:

> Companion resources for a review of computational neuroimaging in Parkinson’s disease: modalities, representation learning, multimodal fusion, validation, explainability, and clinical translation.
