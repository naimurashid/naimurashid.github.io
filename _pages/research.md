---
layout: page
title: Research
permalink: /research/
description: Statistical methods and machine learning for cancer genomics, clinical trials, and precision oncology. Expertise in adaptive trial design, AI, biostatistics, tumor subtyping, and translational research.
nav: true
nav_order: 3

---

## Research Overview

Our methodological work spans five areas, each motivated by problems arising in cancer genomics and clinical trials:

### Penalized Mixed Models & High-Dimensional Inference

Variable selection methods for correlated, high-dimensional biomarker data with complex correlation structures. The glmmPen framework handles longitudinal and clustered data through penalized generalized linear mixed models, with extensions to latent factor modeling and piecewise-constant hazard random-effects survival models. Published in [*The R Journal*](https://doi.org/10.32614/RJ-2024-006){:target="_blank"} (2024), [*Biometrics*](https://doi.org/10.1093/biomtc/ujae016){:target="_blank"} (2024), and [*Statistics in Medicine*](https://doi.org/10.1002/sim.10313){:target="_blank"} (2025); available on [CRAN](https://cran.r-project.org/package=glmmPen){:target="_blank"}.

### Deep Learning for Missing Data

NIMIWAE and dlGLM combine variational autoencoders with generalized linear models for principled inference when data are missing not at random. These methods address informative dropout in clinical registries and genomic studies where standard imputation approaches fail. Published in [*JCGS*](https://doi.org/10.1080/10618600.2023.2170607){:target="_blank"} (2024) and [*Statistics in Biopharmaceutical Research*](https://doi.org/10.1080/19466315.2024.2352613){:target="_blank"} (2024); deployed in ARPA-H ADAPT analytics.

### Genomic Subtyping & Clustering

Methods for discovering and validating molecular cancer subtypes, including PurIST (single-sample pancreatic cancer classification, CLIA-certified), FSCseq (model-based feature selection and clustering for RNA-seq), and semi-supervised nonnegative matrix factorization approaches that improve cross-cohort replicability. Published in [*Clinical Cancer Research*](https://doi.org/10.1158/1078-0432.CCR-19-1467){:target="_blank"} (2020), [*JASA*](https://doi.org/10.1080/01621459.2019.1671197){:target="_blank"} (2020), [*Annals of Applied Statistics*](https://doi.org/10.1214/20-AOAS1400){:target="_blank"} (2021), and [*Journal of Molecular Diagnostics*](https://doi.org/10.1016/j.jmoldx.2024.07.003){:target="_blank"} (2024).

### Epigenomics & Sequencing Methods

Statistical methods for ChIP-seq, ATAC-seq, and RNA-seq data, including epigraHMM (multi-condition differential peak detection), ZINBA (broad and narrow enrichment region identification), allele-specific expression modeling, isoform composition estimation, and CompDTUReg (differential transcript usage with quantification uncertainty). Published in [*Genome Biology*](https://doi.org/10.1186/gb-2011-12-7-R67){:target="_blank"} (2011), [*JASA*](https://doi.org/10.1080/01621459.2013.838899){:target="_blank"} (2014), [*Biometrics*](https://doi.org/10.1111/biom.13076){:target="_blank"} (2019), [*Biometrics*](https://doi.org/10.1111/biom.13617){:target="_blank"} (2022), [*Biometrics*](https://doi.org/10.1093/biometrics/ujad005){:target="_blank"} (2023), and [*Biostatistics*](https://doi.org/10.1093/biostatistics/kxad008){:target="_blank"} (2024).

### Adaptive Clinical Trial Design

Bayesian response-adaptive platform designs that integrate serial ctDNA, tissue, and imaging biomarkers arriving after enrollment. Includes reinforcement-learning-based allocation strategies and tools for automated operating-characteristic tuning. Core methodology for the ARPA-H ADAPT metastatic breast cancer platform. Published in [*Cancer Cell*](https://doi.org/10.1016/j.ccell.2025.11.017){:target="_blank"} (2026).

## New Directions

### LLM-Based Clinical Trial Matching

Pancreatic cancer patients face over 1,100 potentially relevant trials on ClinicalTrials.gov with complex eligibility criteria that are difficult for patients and community physicians to navigate, contributing to low enrollment rates and racial disparities in trial participation. We are fine-tuning a pre-trained LLM on expert-curated patient–trial matching data from UNC to generate personalized trial recommendations, delivered through an mHealth app that also provides general PDAC information and coaching on discussing trials with providers. The model is being prospectively evaluated with 100 PDAC patients at UNC, with attention to recommendation accuracy, patient–provider trial discussions, and equity across racial groups. Funded by DOD PCARP.

### Statistical Ensembling of Small Language Models

Most LLM-based clinical decision support systems rely on proprietary foundation models hosted externally, creating barriers in healthcare settings where HIPAA constraints require on-premises data handling and institutional compute budgets cannot support large models. We are developing statistical theory showing that ensembles of smaller, locally hostable LLMs (made diverse through prompt variation, fine-tuning divergence, and architectural heterogeneity) can match or exceed single large models for ranked clinical recommendations. The framework extends classical bias–variance theory to permutation-valued outputs, derives compute–risk frontiers characterizing when distributing compute across many small models outperforms a single large one, and provides distribution-free uncertainty quantification for ranked outputs via conformal prediction sets that exploit ensemble agreement. Smaller models can also be fine-tuned within institutional firewalls and combined across sites via federated learning without sharing patient data. Validated on pancreatic cancer trial matching using the open-source TrialGPT architecture.

### Liquid Biopsy Subtype Classification via Extracellular Vesicle RNA-seq

Existing PDAC subtype classifiers like PurIST require bulk tissue RNA-seq, but tissue biopsies are invasive and often infeasible for longitudinal monitoring. Plasma extracellular vesicle RNA-seq (evRNAseq) offers a non-invasive alternative, but presents severe statistical challenges: evRNAseq profiles are extremely sparse, with critical subtype-informative genes (e.g., *GATA6*, *KRT5*, *KRT6A*) exhibiting missing-not-at-random (MNAR) dropout where missingness depends on the latent expression intensity itself. We are developing a Bayesian semi-supervised transfer learning framework that learns subtype-specific transcriptional programs from ~800 bulk tumor samples via sparse latent factor models with horseshoe priors, then transfers this structure to the plasma domain through a learnable cross-domain alignment map. A logistic MNAR model explicitly accounts for expression-dependent dropout in EVs, and subtype classification operates on the transferred latent factors with fully Bayesian uncertainty quantification via credible intervals. This approach would enable non-invasive molecular subtyping from a blood draw, supporting longitudinal monitoring of subtype dynamics during treatment.

<section class="page-section page-section--alt diagram-wrapper">
  <h2>Research Portfolio Map (2011-2025)</h2>
  {% include research-diagram.html %}
</section>

## Collaborative Network

- **UNC Lineberger**: Jen Jen Yeh (tumor-stroma organoid models), Lisa Carey (TBCRC adaptive trials), Chuck Perou (breast subtype integration), Ben Vincent (immunotherapy biomarkers)
- **National consortia**: TBCRC Statistical Working Group, V Foundation Scientific Advisory Board, PDAC Stromal Reprogramming Consortium
- **Methodology partners**: Joseph Ibrahim, Michael Kosorok, Mike Love, Didong Li, Quefeng Li
