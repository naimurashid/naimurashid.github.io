---
layout: page
title: Research
permalink: /research/
description: Statistical methods and machine learning for cancer genomics, clinical trials, and precision oncology. Expertise in adaptive trial design, AI, biostatistics, tumor subtyping, and translational research.
nav: true
nav_order: 3

---

<section class="section-hero section-hero--research">
  <div class="section-hero__content">
    <p class="section-hero__eyebrow">Research Program</p>
    <h1>Statistical methods for precision oncology</h1>
    <p class="section-hero__lede">
      We work with UNC Lineberger clinicians on methods and software for biomarker discovery, adaptive trial designs, and translational research. Clinical collaborations shape the questions we address and how tools are delivered.
    </p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="/publications/">View publications</a>
      <a class="btn btn-outline-primary" href="/projects/">Explore projects</a>
    </div>
  </div>
</section>

<section class="page-section">
  <h2>Research Program Overview</h2>
  <div class="research-focus">
    <p class="research-focus__intro">
      Current research focuses on three interconnected areas with demonstrated clinical applications:
    </p>

    <div class="focus-areas-list">
      <div class="focus-area-item">
        <h3>Clinical-Grade Tumor Subtyping</h3>
        <p>PurIST, developed in collaboration with the Yeh laboratory, enables single-sample pancreatic cancer classification without reference cohorts, addressing tumor purity heterogeneity through deconvolution-informed modeling. CLIA-certified and used to stratify 300+ patients across 12 active trials.</p>
      </div>

      <div class="focus-area-item">
        <h3>Deep Learning for Non-Ignorable Missingness</h3>
        <p>NIMIWAE and dlGLM frameworks bridge variational autoencoders with generalized linear models for principled uncertainty quantification when data are missing not at random—enabling valid inference in clinical registries and genomic studies with informative dropout.</p>
      </div>

      <div class="focus-area-item">
        <h3>Adaptive Platforms with Late-Arriving Biomarkers</h3>
        <p>Bayesian response-adaptive designs that integrate ctDNA, imaging, and tissue markers arriving weeks post-enrollment. Enables real-time enrichment without waiting for clinical endpoints. Deployed in SPORE and ARPA-H ADAPT trials.</p>
      </div>
    </div>
  </div>
</section>

<section class="page-section page-section--featured">
  <p class="page-intro__eyebrow">Translational Impact</p>
  <h2 class="page-intro__title">Featured achievements</h2>

  <div class="focus-grid">
    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">AI &amp; Machine Learning</p>
      <h3>Deep Learning for Non-Ignorable Missingness</h3>
      <p class="focus-card__plain-language"><em>→ Methods for handling data that's systematically missing (e.g., sicker patients drop out)</em></p>
      <p>NIMIWAE and dlGLM combine variational autoencoders with generalized linear model inference to handle informative missingness in clinical registries and genomic studies, providing uncertainty estimates when data are missing not at random.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">JCGS 2024</span>
        <span class="focus-chip">Stat Biopharm Res 2024</span>
        <span class="focus-chip">ARPA-H deployment</span>
      </div>
    </article>

    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">Clinical Translation</p>
      <h3>Single-Sample Tumor Subtyping</h3>
      <p class="focus-card__plain-language"><em>→ Classifying individual pancreatic tumors into biological subtypes from a single RNA sample</em></p>
      <p>PurIST, developed in collaboration with the Yeh laboratory, enables platform-independent, reference-free pancreatic cancer subtyping using single bulk RNA-seq samples and deconvolution-informed modeling. It supports clinical decision-making in biomarker-stratified trials.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">Clinical Cancer Research (2020)</span>
        <span class="focus-chip">J Molecular Diagnostics (2024)</span>
        <span class="focus-chip">CLIA-certified implementation</span>
      </div>
    </article>

    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">Adaptive Trials</p>
      <h3>Bayesian Platform Design with Late-Arriving Biomarkers</h3>
      <p class="focus-card__plain-language"><em>→ Trial designs that accommodate blood/tissue biomarker results arriving weeks after enrollment</em></p>
      <p>Adaptive randomization framework integrating serial ctDNA, tissue, and imaging data for metastatic breast cancer platforms. Methodology accommodates staggered biomarker availability and enables mid-trial enrichment based on early response signals.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">ARPA-H ADAPT platform</span>
        <span class="focus-chip">TBCRC cooperative trials</span>
        <span class="focus-chip">Bayesian response-adaptive design</span>
      </div>
    </article>

    <article class="focus-card">
      <p class="focus-card__badge">High-Dimensional Methods</p>
      <h3>Penalized Mixed Models for Correlated Biomarkers</h3>
      <p class="focus-card__plain-language"><em>→ Variable selection methods for correlated genomic data with repeated measures or clustered samples</em></p>
      <p>glmmPen framework enables variable selection in high-dimensional longitudinal and clustered data, addressing over-fitting in genomic studies with complex correlation structures.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">The R Journal (2024)</span>
        <span class="focus-chip">CRAN package</span>
        <span class="focus-chip">Multi-omic integration</span>
      </div>
    </article>
  </div>
</section>

<section class="page-section">
  <p class="page-intro__eyebrow">Focus Areas</p>
  <h2 class="page-intro__title">Research priorities</h2>
  <p class="page-intro__lede">
    Our work spans methodological development, software implementation, and collaborative translational research.
  </p>

  <div class="focus-grid">
    <article class="focus-card">
      <p class="focus-card__badge">Precision medicine</p>
      <h3>Biomarker-guided treatment methods</h3>
      <p class="focus-card__plain-language"><em>→ Statistical tools for classifying patients into subtypes to inform treatment decisions</em></p>
      <p>Subtyping, stromal modeling, and patient stratification methods for clinical decision support.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">PurIST subtype classification for GI tumors</span>
        <span class="focus-chip">Stroma-aware GLMMs for breast and pancreatic cancer</span>
        <span class="focus-chip">Between-study reproducibility assessment</span>
      </div>
      <a href="/publications/?filter=precision-medicine" class="link-arrow">Precision medicine papers →</a>
    </article>

    <article class="focus-card">
      <p class="focus-card__badge">Genomics &amp; epigenomics</p>
      <h3>Transcriptomic and epigenomic software</h3>
      <p class="focus-card__plain-language"><em>→ R packages for analyzing RNA-seq and chromatin data in cancer studies</em></p>
      <p>Open-source RNA-seq and chromatin analysis tools for cancer genomics research.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">CompDTUReg for isoform-level RNA testing</span>
        <span class="focus-chip">epigraHMM + mixNBHMM for multi-condition enrichment</span>
        <span class="focus-chip">Allele-specific &amp; isoform inference pipelines</span>
      </div>
      <a href="/software/" class="link-arrow">Browse software packages →</a>
    </article>

    <article class="focus-card">
      <p class="focus-card__badge">AI &amp; deep learning</p>
      <h3>Deep learning methods for missing data and clinical support</h3>
      <p class="focus-card__plain-language"><em>→ AI methods for incomplete datasets and clinical trial matching tools</em></p>
      <p>Deep learning, LLM, and probabilistic models for incomplete data and clinical decision support.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">NIMIWAE + dlGLM for non-ignorable missingness</span>
        <span class="focus-chip">Semi-supervised factorization for cancer subtyping</span>
        <span class="focus-chip">LLM tools for trial matching and ctDNA monitoring</span>
      </div>
      <a href="/publications/?filter=machine-learning" class="link-arrow">Machine learning work →</a>
    </article>

    <article class="focus-card">
      <p class="focus-card__badge">Trial innovation</p>
      <h3>Adaptive design &amp; real-time biomarker integration</h3>
      <p class="focus-card__plain-language"><em>→ Trial designs that adjust treatment assignment based on incoming biomarker data</em></p>
      <p>Bayesian platforms integrating ctDNA, imaging, and clinical data in cooperative trials.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">ARPA-H ADAPT analytics</span>
        <span class="focus-chip">TBCRC + SPORE biomarker-informed randomization</span>
        <span class="focus-chip">Master protocols with serial ctDNA data</span>
      </div>
      <a href="/projects/" class="link-arrow">View trial projects →</a>
    </article>
  </div>
</section>

<section class="page-section page-section--alt diagram-wrapper">
  <h2>Research Portfolio Map (2011-2025)</h2>
  {% include research-diagram.html %}
</section>

<section class="page-section" markdown="1">
## Cross-Cutting Methodological Innovations

<div class="pillar-grid">
  <article class="pillar-card">
    <h4>Rigor &amp; Reproducibility</h4>
    <p>Quantification-aware modeling, heterogeneity frameworks, and documented software.</p>
  </article>
  <article class="pillar-card">
    <h4>Clinical Translation</h4>
    <p>Collaborations with UNC oncologists and cooperative groups on adaptive, biomarker-rich trials.</p>
  </article>
  <article class="pillar-card">
    <h4>Open Software</h4>
    <p>10+ CRAN/Bioconductor packages with tutorials, vignettes, and active maintenance.</p>
  </article>
</div>
</section>

<section class="page-section page-section--alt" markdown="1">
## Collaborative Network

<div class="network-grid">
  <article class="pillar-card">
    <h4>UNC Lineberger</h4>
    <p>Collaborations with Jen Jen Yeh (tumor-stroma organoid models, stromal reprogramming), Lisa Carey (TBCRC adaptive trials, endocrine resistance), Chuck Perou (breast subtype integration), and Ben Vincent (immunotherapy biomarkers, neoantigen prediction).</p>
  </article>
  <article class="pillar-card">
    <h4>National Consortia</h4>
    <p>Statistical leadership in Translational Breast Cancer Research Consortium (TBCRC) Statistical Working Group, V Foundation Scientific Advisory Board, and PDAC Stromal Reprogramming Consortium.</p>
  </article>
  <article class="pillar-card">
    <h4>Methodology Partners</h4>
    <p>Joseph Ibrahim, Michael Kosorok, Mike Love, Katie Hoadley, and collaborators extend our statistical methods.</p>
  </article>
</div>
</section>

<div class="page-cta page-cta--student">
  <p><strong>Interested in PhD research?</strong> We're recruiting for Fall 2026. <a href="/teaching/">Learn about our training program →</a></p>
</div>
