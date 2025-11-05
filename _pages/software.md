---
layout: page
title: software
permalink: /software/
description: Open-source software packages and tools for statistical genomics and cancer research
nav: true
nav_order: 4
---

## R Packages

### glmmPen
[![CRAN](https://www.r-pkg.org/badges/version/glmmPen)](https://cran.r-project.org/package=glmmPen)
[![GitHub](https://img.shields.io/github/stars/hheiling/glmmPen?style=social)](https://github.com/hheiling/glmmPen)

**High dimensional penalized generalized linear mixed models**

Simultaneous fixed and random effects selection in high-dimensional generalized linear mixed models with applications to cancer outcome prediction and biomarker discovery.

- **Publication**: Heiling, Rashid, Li, Ibrahim (2024). *The R Journal* 15(4):106
- [CRAN Package](https://cran.r-project.org/package=glmmPen)
- [GitHub Repository](https://github.com/hheiling/glmmPen)
- [Documentation](https://cran.r-project.org/web/packages/glmmPen/glmmPen.pdf)

---

### epigraHMM
[![Bioconductor](https://img.shields.io/badge/Bioconductor-release-blue)](http://bioconductor.org/packages/release/bioc/html/epigraHMM.html)
[![GitHub](https://img.shields.io/github/stars/plbaldoni/epigraHMM?style=social)](https://github.com/plbaldoni/epigraHMM)

**Multi-sample consensus and differential enrichment pattern detection from epigenomic data**

Bioconductor package for multi-sample consensus and differential enrichment pattern detection from ChIP-seq, ATAC-seq, and related epigenomic data types using hidden Markov models.

- **Publication**: Baldoni, Rashid, Ibrahim (2022). *Biometrics* 78(3):1141-1154
- [Bioconductor Page](http://bioconductor.org/packages/release/bioc/html/epigraHMM.html)
- [GitHub Repository](https://github.com/plbaldoni/epigraHMM)
- [Vignette](http://bioconductor.org/packages/release/bioc/vignettes/epigraHMM/inst/doc/epigraHMM.html)

---

### dlglm
[![GitHub](https://img.shields.io/github/stars/DavidKLim/dlglm?style=social)](https://github.com/DavidKLim/dlglm)

**Deeply learned generalized linear models with missing data**

R package for flexible handling of non-ignorable missing data in deeply learned generalized linear models, combining deep learning with traditional GLM frameworks for robust inference.

- **Publication**: Lim, Rashid, Oliva, Ibrahim (2024). *J Computational & Graphical Statistics* 33(2):638-650
- [GitHub Repository](https://github.com/DavidKLim/dlglm)

---

### NIMIWAE
[![GitHub](https://img.shields.io/github/stars/DavidKLim/NIMIWAE?style=social)](https://github.com/DavidKLim/NIMIWAE)

**Non-ignorable missing data imputation using variational autoencoders**

R package for flexible handling and imputation of non-ignorable missing data patterns using deep learning variational autoencoders for high-dimensional biomedical data.

- **Publication**: Lim, Rashid, Oliva, Ibrahim (2024). *Statistics in Biopharmaceutical Research*, In Press
- [GitHub Repository](https://github.com/DavidKLim/NIMIWAE)

---

### FSCseq
[![GitHub](https://img.shields.io/github/stars/DavidKLim/FSCseq?style=social)](https://github.com/DavidKLim/FSCseq)

**Model-based feature selection and clustering of RNA-seq data**

Computational method to simultaneously detect latent clusters and cluster-discriminatory genes from RNA-seq data for unsupervised subtype discovery in cancer.

- **Publication**: Lim, Rashid, Ibrahim (2021). *Annals of Applied Statistics* 15(1):481
- [GitHub Repository](https://github.com/DavidKLim/FSCseq)

---

### mixNBHMM
[![GitHub](https://img.shields.io/github/stars/plbaldoni/mixNBHMM?style=social)](https://github.com/plbaldoni/mixNBHMM)

**Differential peak calling for multi-sample, multi-condition epigenomic data**

Highly efficient and flexible algorithm for calling differential peaks across multi-sample, multi-condition experimental settings for ChIP-seq, ATAC-seq, DNase-seq, and similar data. Can determine combinatorial patterns of interactions between different epigenomic processes across the genome.

- **Publication**: Baldoni, Rashid, Ibrahim (2019). *Biometrics* 75(4):1401-1413
- [GitHub Repository](https://github.com/plbaldoni/mixNBHMM)

---

### ZIMHMM
[![GitHub](https://img.shields.io/github/stars/plbaldoni/ZIMHMM?style=social)](https://github.com/plbaldoni/ZIMHMM)

**HMM-based consensus enrichment calling for ChIP-seq replicates**

HMM-based algorithm for calling broad consensus regions of enrichment across multiple technical ChIP-seq replicates with zero-inflated mixture modeling.

- [GitHub Repository](https://github.com/plbaldoni/ZIMHMM)

---

### ZINBA
[![Google Code](https://img.shields.io/badge/Google%20Code-archived-lightgrey)](https://code.google.com/p/zinba)

**Zero-inflated negative binomial algorithm for genomic enrichment**

Comprehensive R package for statistical detection of genomic regions enriched for NGS reads, applicable to a wide variety of NGS datasets including ChIP-seq, ATAC-seq, and DNase-seq.

- **Publication**: Rashid, Giresi, Ibrahim, Sun, Lieb (2011). *Genome Biology* 12(7):R67
- [Project Page](https://code.google.com/p/zinba)

---

### hmmcov
[![Google Code](https://img.shields.io/badge/Google%20Code-archived-lightgrey)](https://code.google.com/p/hmmcov)

**HMM-based analysis of DAE-seq data with variable selection**

R package implementing HMM and AR-HMM based procedures for enrichment detection in epigenetic datasets, including novel variable selection procedures for efficient detection of biological factors associated with correlated genomic features.

- **Publication**: Rashid, Sun, Ibrahim (2014). *JASA* 109(505):78-94
- [Project Page](https://code.google.com/p/hmmcov)

---

### BASeG
**Bivariate association studies using sequencing data with genetic effects**

R package for bivariate association studies using sequencing data while accounting for shared genetic effects. Implements bivariate Poisson-lognormal and bivariate logistic-normal regression to assess associations between gene expression and epigenetic marks from sequencing data, explicitly modeling DNA polymorphism effects in allele-specific or non-allele-specific manner.

- **Publication**: Rashid, Sun, Ibrahim (2016). *Annals of Applied Statistics* 10(4):2254

---

## Clinical Tools & Patents

### PurIST Pancreatic Cancer Classifier
**Clinically-validated single-sample subtype classifier for PDAC**

Platform and sample type independent single sample classifier for treatment decision making in pancreatic ductal adenocarcinoma (PDAC). CLIA-certified for clinical use.

- **Patent**: US Patent 12,000,003 (June 4, 2024)
- **Publications**:
  - Rashid et al. (2020). *Clinical Cancer Research* 26(1):82-92
  - Li et al. (2024). *J Molecular Diagnostics* 26(11):962-970
- **Application**: Now evaluated across cooperative group trials for precision oncology treatment selection

---

## Code Repositories

All software is actively maintained on GitHub. Contributions, issues, and feature requests are welcome.

### Rashid Lab GitHub Organization
- [naimurashid on GitHub](https://github.com/naimurashid)

### Collaborative Development
Many packages are developed in close collaboration with lab members and trainees:
- **Hillary Heiling**: glmmPen lead developer
- **David Lim**: dlglm, NIMIWAE, FSCseq lead developer
- **Pedro Baldoni**: epigraHMM, mixNBHMM, ZIMHMM lead developer
- **Amber Young**: Current PhD student working on semi-supervised matrix factorization for PDAC subtyping

---

## Citation

If you use our software in your research, please cite the appropriate publication listed with each package. For general citation of the Rashid Lab computational methods:

```
@misc{rashidlab2025,
  author = {Rashid, Naim U. and collaborators},
  title = {Rashid Lab Statistical Genomics Software},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/naimurashid}
}
```

---

## Support & Contact

For technical support, please open an issue on the relevant GitHub repository. For collaboration inquiries, contact [naim@unc.edu](mailto:naim@unc.edu).
