---
layout: page
title: research
permalink: /research/
description: Statistical methods development for precision oncology and cancer genomics
nav: true
nav_order: 3
---

## Research Vision

The Rashid Lab develops **statistical methods and computational tools** that bridge genomics, clinical trials, and precision medicine. Our work spans **four interconnected research themes**, each addressing critical challenges in cancer biostatistics while maintaining strong ties to translational applications at UNC Lineberger Comprehensive Cancer Center.

---

<div class="research-themes">
  <div class="research-themes__grid">

    <div class="research-theme research-theme--primary">
      <div class="research-theme__icon">📊</div>
      <h3>Penalized Mixed Models & High-Dimensional Inference</h3>
      <p class="research-theme__description">
        Developing scalable variable selection methods for generalized linear mixed models (GLMMs) with applications to multi-omic biomarker discovery and patient subtyping.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>glmmPen</strong>: R package for simultaneous fixed and random effects selection in high-dimensional GLMMs</li>
          <li>Efficient computation via latent factor modeling of random effects</li>
          <li>Piecewise constant hazard models for survival outcomes</li>
          <li>Applications to cancer outcome prediction across breast, pancreatic, and colorectal cancers</li>
        </ul>
        <h4>Representative Publications</h4>
        <ul>
          <li>Heiling et al. (2024). <em>Biometrics</em> - Efficient computation of penalized GLMMs</li>
          <li>Heiling et al. (2024). <em>The R Journal</em> - glmmPen software</li>
          <li>Heiling et al. (2025). <em>Statistics in Medicine</em> - Penalized survival models</li>
        </ul>
      </div>
      <a href="/publications/?filter=mixed-models" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

    <div class="research-theme research-theme--secondary">
      <div class="research-theme__icon">🎯</div>
      <h3>Adaptive Clinical Trial Design</h3>
      <p class="research-theme__description">
        Designing Bayesian adaptive platform trials for oncology that integrate biomarker-driven treatment allocation, real-time monitoring, and evolutionary trial frameworks.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>ARPA-H ADAPT</strong>: $28M platform trial for metastatic breast cancer with evolutionary design</li>
          <li>Bayesian adaptive randomization based on real-time efficacy and toxicity</li>
          <li>Serial biomarker assessment (tissue, ctDNA, imaging)</li>
          <li>Master protocol frameworks for multi-arm cancer trials</li>
        </ul>
        <h4>Active Trials</h4>
        <ul>
          <li>TBCRC EvolveBDT (MBC, 2025-2031) - Statistical Lead</li>
          <li>NCI SPORE trials in breast and pancreatic cancer</li>
          <li>Alliance cooperative group trials (CALGB 80405, CALGB 40603)</li>
        </ul>
      </div>
      <a href="/publications/?filter=trials" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

    <div class="research-theme research-theme--tertiary">
      <div class="research-theme__icon">🧬</div>
      <h3>Multi-Omic Integration & Cancer Genomics</h3>
      <p class="research-theme__description">
        Integrating transcriptomic, epigenomic, proteomic, and phosphoproteomic data to identify cancer subtypes, therapeutic vulnerabilities, and mechanisms of resistance.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>PurIST</strong>: CLIA-certified pancreatic cancer classifier (US Patent 12,000,003)</li>
          <li>Tumor-stroma deconvolution methods for PDAC subtyping</li>
          <li>Differential transcript usage analysis (compositional measurement error)</li>
          <li>Epigenomic enrichment detection (epigraHMM, mixNBHMM, ZINBA)</li>
          <li>Allele-specific expression and isoform-level inference</li>
        </ul>
        <h4>Representative Publications</h4>
        <ul>
          <li>Rashid et al. (2020). <em>Clinical Cancer Research</em> - PurIST classifier</li>
          <li>Young et al. (2024). <em>Biostatistics</em> - Differential transcript usage</li>
          <li>Baldoni et al. (2022). <em>Biometrics</em> - epigraHMM</li>
          <li>Rashid et al. (2011). <em>Genome Biology</em> - ZINBA</li>
        </ul>
      </div>
      <a href="/publications/?filter=genomics" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

    <div class="research-theme research-theme--quaternary">
      <div class="research-theme__icon">🤖</div>
      <h3>Machine Learning for Precision Oncology</h3>
      <p class="research-theme__description">
        Developing deep learning and machine learning methods that address missing data, between-study heterogeneity, and patient-derived xenograft modeling for individualized treatment selection.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>Deep learning with missing data</strong>: NIMIWAE, dlglm packages for non-ignorable missingness</li>
          <li>Importance-weighted autoencoders for EHR data</li>
          <li>Addressing between-study heterogeneity for reproducible prediction models</li>
          <li>Patient-derived xenograft (PDX) models for precision medicine</li>
          <li>Feature selection and clustering for unsupervised subtype discovery (FSCseq)</li>
        </ul>
        <h4>Representative Publications</h4>
        <ul>
          <li>Lim et al. (2024). <em>JCGS</em> - Deeply learned GLMs with missing data</li>
          <li>Lim et al. (2024). <em>Stat Biopharma Res</em> - NIMIWAE</li>
          <li>Rashid et al. (2020). <em>JASA</em> - Modeling heterogeneity for reproducibility</li>
          <li>Rashid et al. (2020). <em>JASA</em> - High-dimensional precision medicine from PDXs</li>
          <li>Lim et al. (2021). <em>Ann Appl Stat</em> - FSCseq</li>
        </ul>
      </div>
      <a href="/publications/?filter=machine-learning" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

  </div>
</div>

---

## Cross-Cutting Methodological Innovations

Our research themes are united by several **core methodological principles**:

### 🔬 Rigor & Reproducibility
- Explicit modeling of measurement uncertainty (RNA-seq quantification, allele-specific expression)
- Between-study heterogeneity frameworks for gene signature selection
- Validated software with comprehensive documentation and vignettes

### 🏥 Clinical Translation
- Close collaboration with UNC Lineberger oncologists (Yeh, Carey, Perou, Vincent)
- Participation in cooperative group trials (Alliance, TBCRC)
- CLIA-certified clinical tools (PurIST)
- Real-time trial monitoring and adaptive designs

### 📦 Open-Source Software
- 10+ R packages on CRAN, Bioconductor, and GitHub
- Extensive documentation, tutorials, and reproducible examples
- Active maintenance and user support

### 🎓 Training & Mentorship
- 7 PhD students advised (5 graduated: GSK, Dana-Farber, Pitt, precision genomics firms)
- 2 current PhD students (Amber Young, Tyler Humpherys)
- Multiple awards: Grizzle Award (2024), Teaching Innovation (2023), Delta Omega Faculty (2021)

---

## Funding & Support

Our research is supported by:

- **ARPA-H** - ADAPT Platform Trial ($30M, 2025-2031)
- **NIH/NCI** - SPORE in Breast Cancer (P50-CA058223, Core B Co-Leader)
- **NIH/NCI** - SPORE in Pancreatic Cancer (P50-CA257911, Core C Co-Leader)
- **NIH/NCI** - Tumor-Stroma Integration (U01-CA199064, Co-PI)
- **DOD PCARP** - Clinical Trial Matching AI ($311K, 2024-2026)
- **Lineberger Comprehensive Cancer Center** - Biostatistics Core (P30-CA016086)

[View complete funding list →](/funding/)

---

## Collaborative Network

### UNC Lineberger Comprehensive Cancer Center
- **Jen Jen Yeh, MD PhD** - Pancreatic cancer biology and trials
- **Lisa Carey, MD** - Breast cancer adaptive trials
- **Chuck Perou, PhD** - Molecular subtyping and genomics
- **Ben Vincent, MD** - Immunotherapy and AML

### National Collaborators
- **Alliance for Clinical Trials in Oncology** - Cooperative group biostatistics
- **Translational Breast Cancer Research Consortium (TBCRC)** - Multi-institutional trials
- **PDAC Stromal Reprogramming Consortium** - Microenvironment analytics

### Methodological Collaborators
- **Joseph Ibrahim, PhD** (UNC) - High-dimensional inference
- **Michael Kosorok, PhD** (UNC) - Precision medicine and dynamic treatment regimes
- **Mike Love, PhD** (UNC) - RNA-seq and genomics
- **Katie Hoadley, PhD** (UNC) - Multi-platform cancer genomics

---

## Join Us

We are always looking for motivated **PhD students**, **postdocs**, and **collaborators** interested in statistical methods for cancer research.

**Current Opportunities**:
- PhD positions in biostatistics with cancer genomics focus
- Collaborative projects with UNC Lineberger investigators
- Summer research internships for quantitative undergraduates

**Contact**: [naim@unc.edu](mailto:naim@unc.edu)

[View open positions →](/positions/)
