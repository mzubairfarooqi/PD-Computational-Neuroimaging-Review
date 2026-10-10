# PD neuroimaging datasets and collaborative resources

This list is intentionally conservative. It distinguishes public datasets from controlled-access and consortium resources.

| Resource | What it contains | Access model | Link | Notes |
|---|---|---|---|---|
| **Parkinson's Progression Markers Initiative (PPMI)** | Longitudinal clinical, imaging, biomarker, genetics, sensor and related PD/prodromal data | Qualified-researcher registration, data-use agreement and application | https://www.ppmi-info.org/access-data-specimens/download-data | Major resource used across PD computational-neuroimaging studies. Imaging access is controlled; do not redistribute files. |
| **NINDS Parkinson's Disease Biomarkers Program (PDBP)** | Clinical, genetic, imaging and biomarker data for PD and related disorders | Research account / controlled access | https://pdbp.ninds.nih.gov/ | The Data Management Resource provides query and standardized-data infrastructure. |
| **OpenNeuro ds001907 – ANT: Healthy aging and Parkinson's disease** | 46 participants: 25 healthy-aging and 21 PD participants; two sessions; anatomical, resting-state, task fMRI and DTI | Public BIDS dataset | https://openneuro.org/datasets/ds001907/versions/3.2.0 | Useful for reproducible teaching/prototyping; verify the dataset README and associated publications before scientific analysis. |
| **ENIGMA-Parkinson's Disease Working Group** | Large international multicenter structural MRI, DTI, fMRI and harmonized collaborative analyses | Consortium / project collaboration rather than unrestricted raw-data download | https://enigma.ini.usc.edu/ongoing/enigma-parkinsons/ | Valuable for large-scale replication, harmonization and distributed analyses. |

## Access and ethics reminders

1. Always obtain data from the original provider.
2. Follow the provider's data-use agreement, publication policy and acknowledgement requirements.
3. Do not commit participant-level imaging, clinical tables or credentials to GitHub.
4. Use de-identified subject identifiers in code examples and split files.
5. Keep derived outputs compliant with the original dataset's sharing policy.
