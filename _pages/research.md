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

Variable selection methods for correlated, high-dimensional biomarker data with complex correlation structures. The glmmPen framework handles longitudinal and clustered data through penalized generalized linear mixed models, with extensions to latent factor modeling and piecewise-constant hazard random-effects survival models. Published in *The R Journal* (2024), *Biometrics* (2024), and *Statistics in Medicine* (2025); available on [CRAN](https://cran.r-project.org/package=glmmPen).

### Deep Learning for Missing Data

NIMIWAE and dlGLM combine variational autoencoders with generalized linear models for principled inference when data are missing not at random. These methods address informative dropout in clinical registries and genomic studies where standard imputation approaches fail. Published in *JCGS* (2024) and *Statistics in Biopharmaceutical Research* (2024); deployed in ARPA-H ADAPT analytics.

### Genomic Subtyping & Clustering

Methods for discovering and validating molecular cancer subtypes, including PurIST (single-sample pancreatic cancer classification, CLIA-certified), FSCseq (model-based feature selection and clustering for RNA-seq), and semi-supervised nonnegative matrix factorization approaches that improve cross-cohort replicability. Published in *Clinical Cancer Research* (2020), *JASA* (2020), *Annals of Applied Statistics* (2021), and *Journal of Molecular Diagnostics* (2024).

### Epigenomics & Sequencing Methods

Statistical methods for ChIP-seq, ATAC-seq, and RNA-seq data, including epigraHMM (multi-condition differential peak detection), ZINBA (broad and narrow enrichment region identification), allele-specific expression modeling, isoform composition estimation, and CompDTUReg (differential transcript usage with quantification uncertainty). Published in *Genome Biology* (2011), *JASA* (2014), *Biometrics* (2019, 2022, 2023), and *Biostatistics* (2024).

### Adaptive Clinical Trial Design

Bayesian response-adaptive platform designs that integrate serial ctDNA, tissue, and imaging biomarkers arriving after enrollment. Includes reinforcement-learning-based allocation strategies and tools for automated operating-characteristic tuning. Core methodology for the ARPA-H ADAPT metastatic breast cancer platform.

## New Directions

### LLM-Based Clinical Trial Matching

Fine-tuned large language models that translate complex eligibility criteria into patient-facing summaries and match prospective pancreatic cancer patients to appropriate trials. Funded by DOD PCARP.

### Statistical Ensembling of Small Language Models

Methods for ensembling smaller, domain-specific language models to achieve performance competitive with large foundation models in privacy-sensitive and resource-constrained clinical environments where large models cannot be deployed or trained on protected health data. Smaller models can be fine-tuned locally within institutional firewalls, combined via federated learning across sites without sharing patient data, and ensembled with formal uncertainty quantification for clinical recommendations.

### Liquid Biopsy Subtype Classification via Extracellular Vesicle RNA-seq

Extending tumor subtype classification to extracellular vesicle RNA-seq (evRNAseq) from blood samples, enabling non-invasive molecular subtyping without tissue biopsies. Key statistical challenges include domain adaptation between tissue and EV transcriptomic profiles, deconvolution of tumor-derived signal from background EV cargo, and calibrated uncertainty quantification for subtype calls made from lower-input material. If successful, this would enable longitudinal monitoring of subtype dynamics during treatment through serial blood draws.

<section class="page-section page-section--alt diagram-wrapper">
  <h2>Research Portfolio Map (2011-2025)</h2>
  {% include research-diagram.html %}
</section>

## Collaborative Network

- **UNC Lineberger**: Jen Jen Yeh (tumor-stroma organoid models), Lisa Carey (TBCRC adaptive trials), Chuck Perou (breast subtype integration), Ben Vincent (immunotherapy biomarkers)
- **National consortia**: TBCRC Statistical Working Group, V Foundation Scientific Advisory Board, PDAC Stromal Reprogramming Consortium
- **Methodology partners**: Joseph Ibrahim, Michael Kosorok, Mike Love, Didong Li, Quefeng Li
