# 🧠 PD Computational Neuroimaging Review

## Companion repository for
### *Advances in Computational Neuroimaging for Parkinson’s Disease: Models, Multimodal Learning, Validation, and Clinical Translation*

**Authors:** Muhammad Zubair and Malika Bendechache  
**Manuscript year:** 2026  
**Status:** Companion repository for the review manuscript. Add the final journal citation and DOI after publication.

---

## 📖 About this repository

This repository is designed as a practical companion to our state-of-the-art review on computational neuroimaging for Parkinson’s disease (PD). The review does not treat the imaging modality, computational model, validation design, explainability, and clinical translation as separate topics. Instead, it follows the complete pathway:

> **Neuroimaging signal → computational representation → learning model → multimodal integration → validation → explanation → clinical translation**

The repository provides readers with a concise roadmap of the review, curated PD neuroimaging data resources, software/tool links, representative studies, and lightweight reproducibility scripts for subject-level splitting and binary-classification evaluation.

> **Clinical-use disclaimer:** This repository is for research and education. It is not a diagnostic device and does not provide clinical recommendations.

---

## 📚 Available Resources

This repository collects practical resources that readers can use to move from the review article to hands-on Parkinson’s disease neuroimaging research. The tables below link directly to major datasets, software libraries, representative studies, and methodological resources discussed across the review.

### 🧠 Public and research-access PD neuroimaging datasets

| Dataset / Resource | Main modalities / data | Typical research use | Access model | Access link |
|---|---|---|---|---|
| **Parkinson’s Progression Markers Initiative (PPMI)** | MRI, DAT imaging, clinical data, biomarkers, genetics, digital/sensor data | PD vs control, prodromal PD, longitudinal progression, multimodal modelling | Registration + data-use agreement | [PPMI Data Access](https://www.ppmi-info.org/access-data-specimens/download-data) |
| **NINDS Parkinson’s Disease Biomarkers Program (PDBP)** | MRI/DTI, clinical, genetic and biomarker data | Biomarker development, progression modelling, multimodal studies | Researcher account / controlled access | [PDBP Data Management Resource](https://pdbp.ninds.nih.gov/data-management-resource) |
| **OpenNeuro ds001907** | Anatomical MRI, resting/task fMRI, DTI | Public PD neuroimaging experiments, BIDS workflows, reproducible analysis | Public download | [OpenNeuro ds001907](https://openneuro.org/datasets/ds001907) |
| **ENIGMA-Parkinson’s Disease (ENIGMA-PD)** | Structural MRI, diffusion MRI, functional imaging and harmonized multicenter analyses | Large-scale multicenter neuroimaging, harmonization, disease staging, reproducibility | Consortium / collaborative access | [ENIGMA-PD](https://enigma.ini.usc.edu/ongoing/enigma-parkinsons/) |

> **Note:** Controlled-access resources are not redistributed in this repository. Users should obtain the data from the original provider and follow the corresponding data-use agreement.

### 🛠️ Open-source neuroimaging and computational tools

| Tool | Main purpose | Typical role in PD neuroimaging | Access link |
|---|---|---|---|
| **BIDS / BIDS Validator** | Data organization and standardization | Reproducible MRI/fMRI/DTI data structure | [BIDS](https://bids.neuroimaging.io/) |
| **NiBabel** | Neuroimaging file I/O | NIfTI loading, saving and manipulation | [NiBabel](https://nipy.org/nibabel/) |
| **ANTs / ANTsPy** | Registration and normalization | Within-subject and template registration | [ANTs](https://github.com/ANTsX/ANTs) |
| **FSL** | MRI/fMRI/diffusion processing | Brain extraction, registration, diffusion and functional analysis | [FSL](https://fsl.fmrib.ox.ac.uk/fsl/) |
| **fMRIPrep** | Standardized fMRI preprocessing | Reproducible resting/task fMRI pipelines | [fMRIPrep](https://fmriprep.org/) |
| **MRtrix3** | Diffusion MRI / tractography | DTI and white-matter connectivity analysis | [MRtrix3](https://www.mrtrix.org/) |
| **DIPY** | Diffusion MRI analysis | Diffusion modelling and tractography in Python | [DIPY](https://dipy.org/) |
| **Nilearn** | Statistical learning for neuroimaging | Functional connectivity and machine-learning analysis | [Nilearn](https://nilearn.github.io/stable/) |
| **PyRadiomics** | Quantitative radiomics | Engineered MRI/PET/SPECT feature extraction | [PyRadiomics](https://pyradiomics.readthedocs.io/) |
| **MONAI** | Medical-imaging deep learning | 3D CNN/Transformer pipelines and training utilities | [MONAI](https://monai.io/) |
| **TorchIO** | 3D medical-image preprocessing and augmentation | Patch sampling, augmentation and volumetric transforms | [TorchIO](https://torchio.readthedocs.io/) |
| **PyTorch Geometric** | Graph neural networks | Structural/functional/metabolic graph modelling | [PyG](https://pytorch-geometric.readthedocs.io/) |
| **neuroCombat** | Multi-site harmonization | Scanner/site harmonization for neuroimaging features | [neuroCombat](https://github.com/Jfortin1/neuroCombat) |
| **Captum** | Explainable AI for PyTorch | Integrated gradients, saliency and attribution | [Captum](https://captum.ai/) |
| **SHAP** | Feature attribution | Interpreting radiomics, clinical and multimodal features | [SHAP](https://shap.readthedocs.io/) |

### 📖 Representative computational PD neuroimaging studies

| Study | Year | Imaging / data | Computational contribution | Main task | Article link |
|---|---:|---|---|---|---|
| **Camacho et al.** | 2023 | Multicenter T1 MRI | Explainable 3D CNN on Jacobian maps | PD vs healthy control | [DOI](https://doi.org/10.1016/j.nicl.2023.103405) |
| **Camacho et al.** | 2024 | T1 + diffusion MRI | Macro-/microstructural multichannel 3D learning | PD vs healthy control | [DOI](https://doi.org/10.1038/s41531-024-00647-9) |
| **Dzialas et al.** | 2024 | Neuroimaging AI literature | Systematic quality analysis of validation, leakage and bias | Methodological assessment | [DOI](https://doi.org/10.1002/mds.30002) |
| **Suo et al.** | 2025 | Routine T1/T2/FLAIR MRI | Large self-supervised vision foundation model strategy | PD vs Parkinson-plus | [DOI](https://doi.org/10.1016/j.ebiom.2025.105773) |
| **Ling et al.** | 2025 | FDG-PET | Explainable GNN with metabolic similarity networks | PD/MSA/PSP differentiation | [DOI](https://doi.org/10.3389/fnagi.2025.1580910) |
| **Wu et al.** | 2025 | FDG-PET | CNN–Transformer with supervised contrastive learning | PD/MSA/PSP differentiation | [DOI](https://doi.org/10.1007/s12149-025-02081-0) |
| **Vaillancourt et al. (AIDP)** | 2025 | Multicenter diffusion MRI | Prospective multicenter machine-learning differential diagnosis | PD/MSA/PSP differentiation | [DOI](https://doi.org/10.1001/jamaneurol.2025.0112) |
| **Durand de Gevigney et al.** | 2026 | DAT-SPECT + quantitative features | Multimodal Transformer fusion, transfer learning and missing-input handling | Degenerative parkinsonism detection | [DOI](https://doi.org/10.1007/s10278-025-01831-w) |

### ✅ Validation, reproducibility and translation resources

| Resource | What it helps with | Repository / access link |
|---|---|---|
| **Subject-level split checking** | Detects train/validation/test leakage at participant level | [`scripts/check_subject_splits.py`](scripts/check_subject_splits.py) |
| **Classification metrics** | Accuracy, sensitivity, specificity, F1, ROC-AUC, PR-AUC, Brier score and confusion matrix | [`scripts/classification_metrics.py`](scripts/classification_metrics.py) |
| **Validation checklist** | Data splitting, harmonization, external testing, uncertainty and XAI checks | [`resources/validation-checklist.md`](resources/validation-checklist.md) |
| **Paper roadmap** | Maps the six research questions to the review sections | [`resources/paper-roadmap.md`](resources/paper-roadmap.md) |
| **Dataset catalogue** | Machine-readable summary of PD neuroimaging resources | [`data/dataset_catalog.csv`](data/dataset_catalog.csv) |
| **Representative-study catalogue** | Machine-readable study list organized by modality, method and task | [`data/representative_studies.csv`](data/representative_studies.csv) |

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

## 📑 Citation

If you use this repository or its curated resources, please cite the associated review article. Until the final bibliographic record is available, use the following temporary citation and update it after publication:

```bibtex
@article{zubair2026pdneuroimaging,
  title   = {Advances in Computational Neuroimaging for Parkinson's Disease: Models, Multimodal Learning, Validation, and Clinical Translation},
  author  = {Zubair, Muhammad and Bendechache, Malika},
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
