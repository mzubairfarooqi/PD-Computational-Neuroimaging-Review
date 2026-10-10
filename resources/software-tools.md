# Software and open-source tools

These resources are organized around the computational pathway emphasized in the review.

## Data standards, I/O and reproducibility

| Tool | Main use | Link |
|---|---|---|
| BIDS Validator | Validate BIDS-formatted datasets | https://github.com/bids-standard/bids-validator |
| NiBabel | Read/write NIfTI and other neuroimaging formats | https://github.com/nipy/nibabel |
| DataLad | Dataset versioning and reproducible data access | https://github.com/datalad/datalad |

## Registration and preprocessing

| Tool | Main use | Link |
|---|---|---|
| ANTs / ANTsPy | Registration, normalization and image processing | https://github.com/ANTsX/ANTs |
| FSL | MRI/fMRI/diffusion preprocessing and analysis | https://fsl.fmrib.ox.ac.uk/fsl/ |
| fMRIPrep | Reproducible fMRI preprocessing | https://github.com/nipreps/fmriprep |

## Diffusion and functional neuroimaging

| Tool | Main use | Link |
|---|---|---|
| MRtrix3 | Diffusion MRI and tractography | https://github.com/MRtrix3/mrtrix3 |
| DIPY | Diffusion MRI analysis in Python | https://github.com/dipy/dipy |
| Nilearn | Statistical learning and visualization for neuroimaging | https://github.com/nilearn/nilearn |

## Radiomics, harmonization and machine learning

| Tool | Main use | Link |
|---|---|---|
| PyRadiomics | Quantitative radiomic feature extraction | https://github.com/AIM-Harvard/pyradiomics |
| neuroCombat | ComBat harmonization implementation | https://github.com/Jfortin1/neuroCombat |
| scikit-learn | Conventional ML, validation and metrics | https://github.com/scikit-learn/scikit-learn |

## Deep learning and graph learning

| Tool | Main use | Link |
|---|---|---|
| MONAI | Medical-imaging deep-learning framework | https://github.com/Project-MONAI/MONAI |
| TorchIO | 3D medical-image preprocessing and augmentation | https://github.com/TorchIO-project/torchio |
| PyTorch Geometric | Graph neural networks | https://github.com/pyg-team/pytorch_geometric |

## Explainability

| Tool | Main use | Link |
|---|---|---|
| Captum | PyTorch attribution methods including integrated gradients and occlusion | https://github.com/pytorch/captum |
| SHAP | Feature-attribution analysis | https://github.com/shap/shap |

## Important note

A tool's availability does not imply that a preprocessing or validation choice is appropriate for every PD dataset. Site harmonization, feature selection, normalization and augmentation should be fitted using training data only when those operations depend on population-level statistics.
