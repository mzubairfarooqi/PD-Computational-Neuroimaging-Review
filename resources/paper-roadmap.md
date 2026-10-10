# Paper roadmap

This companion repository follows the structure of the review manuscript.

| Section | Focus | Main question |
|---|---|---|
| I. Introduction | Clinical/computational motivation and review gap | Why is an integrated computational neuroimaging review needed? |
| II. Neuroimaging modalities and computational representations | MRI, dMRI, fMRI, nigral-sensitive MRI, DAT-SPECT, PET | What biological signal is available to the model and how is it represented? |
| III. Evolution of computational methods | ML → CNN/3D DL → GNNs → Transformers → self-supervised/foundation strategies | What has increasing model complexity actually added? |
| IV. Multimodal neuroimaging and computational fusion | Complementary imaging and interaction-aware representation learning | When does multimodal learning provide real value? |
| V. Datasets, validation, robustness and generalization | Leakage, site/scanner effects, harmonization, external testing | Can the reported performance be trusted outside the development data? |
| VI. Explainability and neurobiological plausibility | Spatial, feature, graph and attention-based explanations | What did the model learn, and does it make biological sense? |
| VII. Clinical translation | Differential diagnosis, uncertainty, prospective testing, workflow integration | Is the evidence sufficient for clinical decision support? |
| VIII. Challenges and future directions | Data scale, fairness, privacy, distributed learning, prospective impact | What prevents broader translation and what should research do next? |
| IX–X. Discussion and conclusion | Synthesis | What is the central message of the review? |

## Integrated review perspective

The review treats the computational pipeline as a connected chain:

`Modality → Preprocessing → Representation → Model → Fusion → Validation → Explanation → Clinical use`

The main message is that a higher reported accuracy is not, by itself, evidence of a better or more clinically useful PD neuroimaging model. The biological signal, representation, task definition, validation design and deployment context all matter.
