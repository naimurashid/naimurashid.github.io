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


<div class="mt-5"></div>


<div class="research-themes">
  <div class="research-themes__grid">

    <div class="research-theme research-theme--primary">
      <div class="research-theme__icon">🎯</div>
      <h3>Cancer Precision Medicine</h3>
      <p class="research-theme__description">
        Developing statistical methods and clinical tools for biomarker-driven treatment selection, cancer subtyping, and patient stratification to enable personalized therapeutic decision-making.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>PurIST</strong>: CLIA-certified pancreatic cancer classifier (US Patent 12,000,003)</li>
          <li>Tumor-stroma deconvolution methods for PDAC subtyping</li>
          <li>High-dimensional inference from patient-derived xenograft (PDX) models</li>
          <li>Addressing between-study heterogeneity for reproducible biomarker discovery</li>
          <li>Penalized GLMMs for multi-omic outcome prediction across breast, pancreatic, and colorectal cancers</li>
        </ul>
        <h4>Representative Publications</h4>
        <ul>
          <li>Rashid et al. (2020). <em>Clinical Cancer Research</em> - PurIST classifier</li>
          <li>Rashid et al. (2020). <em>JASA</em> - Modeling heterogeneity for reproducibility</li>
          <li>Rashid et al. (2020). <em>JASA</em> - High-dimensional precision medicine from PDXs</li>
          <li>Heiling et al. (2024). <em>Biometrics</em> - Penalized GLMMs for biomarker discovery</li>
        </ul>
      </div>
      <a href="/publications/?filter=precision-medicine" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

    <div class="research-theme research-theme--secondary">
      <div class="research-theme__icon">🧬</div>
      <h3>Transcriptomic, Epigenomic, and Bioinformatics Tool Development</h3>
      <p class="research-theme__description">
        Creating computational methods and open-source software for analyzing RNA-seq, ChIP-seq, ATAC-seq, and multi-omic data to identify regulatory mechanisms and functional genomic elements in cancer.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>Differential transcript usage</strong>: CompDTUReg package incorporating quantification uncertainty</li>
          <li><strong>Epigenomic enrichment detection</strong>: epigraHMM, mixNBHMM, ZIMHMM, ZINBA</li>
          <li>Multi-sample consensus and differential enrichment pattern detection</li>
          <li>Allele-specific expression and isoform-level inference</li>
          <li>Feature selection and clustering for RNA-seq subtype discovery (FSCseq)</li>
        </ul>
        <h4>Representative Publications</h4>
        <ul>
          <li>Young et al. (2023). <em>Biostatistics</em> - CompDTUReg for differential transcript usage</li>
          <li>Baldoni et al. (2022). <em>Biometrics</em> - epigraHMM</li>
          <li>Baldoni et al. (2019). <em>Biometrics</em> - mixNBHMM</li>
          <li>Rashid et al. (2014). <em>JASA</em> - HMM-based enrichment with variable selection</li>
          <li>Rashid et al. (2011). <em>Genome Biology</em> - ZINBA</li>
          <li>Lim et al. (2021). <em>Ann Appl Stat</em> - FSCseq</li>
        </ul>
      </div>
      <a href="/publications/?filter=genomics" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

    <div class="research-theme research-theme--tertiary">
      <div class="research-theme__icon">🤖</div>
      <h3>Generative AI and Deep Learning</h3>
      <p class="research-theme__description">
        Developing deep learning architectures and generative AI methods for handling missing data, semi-supervised learning, and computational pathology to advance precision oncology applications.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>Deep learning with missing data</strong>: NIMIWAE and dlglm packages for non-ignorable missingness</li>
          <li>Importance-weighted autoencoders for EHR and clinical trial data</li>
          <li>Semi-supervised matrix factorization for cancer subtyping</li>
          <li>Generative AI for clinical trial matching and patient cohort identification</li>
          <li>Integration of deep learning with traditional GLM frameworks for robust inference</li>
        </ul>
        <h4>Representative Publications</h4>
        <ul>
          <li>Lim et al. (2024). <em>JCGS</em> - Deeply learned GLMs with missing data</li>
          <li>Lim et al. (2024). <em>Stat Biopharma Res</em> - NIMIWAE for non-ignorable missingness</li>
          <li>Young et al. (2025). <em>In Preparation</em> - Semi-supervised matrix factorization</li>
        </ul>
      </div>
      <a href="/publications/?filter=machine-learning" class="btn btn-sm btn-outline-primary">View Publications</a>
    </div>

    <div class="research-theme research-theme--quaternary">
      <div class="research-theme__icon">🏥</div>
      <h3>Adaptive Trial Design & Real-Time Biomarker Integration</h3>
      <p class="research-theme__description">
        Designing Bayesian adaptive platform trials for oncology that integrate biomarker-driven treatment allocation, real-time monitoring, and evolutionary trial frameworks to accelerate therapeutic discoveries.
      </p>
      <div class="research-theme__highlights">
        <h4>Key Contributions</h4>
        <ul>
          <li><strong>ARPA-H ADAPT</strong>: $28M platform trial for metastatic breast cancer with evolutionary design</li>
          <li>Bayesian adaptive randomization based on real-time efficacy and toxicity</li>
          <li>Serial biomarker assessment (tissue, ctDNA, imaging) integrated into trial design</li>
          <li>Master protocol frameworks for multi-arm cancer trials</li>
          <li>Cooperative group trials with Alliance and TBCRC</li>
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

  </div>
</div>


<div class="mt-5"></div>


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


<div class="mt-5"></div>


## Funding & Support

Our research is supported by:

- **ARPA-H** - ADAPT Platform Trial ($30M, 2025-2031)
- **NIH/NCI** - SPORE in Breast Cancer (P50-CA058223, Core B Co-Leader)
- **NIH/NCI** - SPORE in Pancreatic Cancer (P50-CA257911, Core C Co-Leader)
- **NIH/NCI** - Tumor-Stroma Integration (U01-CA199064, Co-PI)
- **DOD PCARP** - Clinical Trial Matching AI ($311K, 2024-2026)
- **Lineberger Comprehensive Cancer Center** - Biostatistics Core (P30-CA016086)

[View complete funding list →](/funding/)


<div class="mt-5"></div>


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


<div class="mt-5"></div>


## Join Us

We are always looking for motivated **PhD students**, **postdocs**, and **collaborators** interested in statistical methods for cancer research.

**Current Opportunities**:
- PhD positions in biostatistics with cancer genomics focus
- Collaborative projects with UNC Lineberger investigators
- Summer research internships for quantitative undergraduates

**Contact**: [naim@unc.edu](mailto:naim@unc.edu)

[View open positions →](/positions/)
