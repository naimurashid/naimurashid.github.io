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
      We develop statistical methods and software in collaboration with UNC Lineberger clinicians to advance biomarker discovery, adaptive trial designs, and translational research. Our integrative approach bridges methodological innovation with embedded clinical partnerships.
    </p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="/publications/">View publications</a>
      <a class="btn btn-outline-primary" href="/projects/">Explore projects</a>
    </div>
  </div>
  <div class="section-metrics">
    <div class="metric">
      <span class="metric__value">{{ site.data.metrics.research.focus_areas }}</span>
      <span class="metric__label">{{ site.data.metrics.research.focus_areas_label }}</span>
    </div>
    <div class="metric">
      <span class="metric__value">{{ site.data.metrics.research.active_trials }}</span>
      <span class="metric__label">{{ site.data.metrics.research.active_trials_label }}</span>
    </div>
    <div class="metric">
      <span class="metric__value">{{ site.data.metrics.research.software_packages }}</span>
      <span class="metric__label">{{ site.data.metrics.research.software_packages_label }}</span>
    </div>
    <div class="metric">
      <span class="metric__value">{{ site.data.metrics.research.collaborative_network }}</span>
      <span class="metric__label">{{ site.data.metrics.research.collaborative_network_label }}</span>
    </div>
  </div>
</section>

<section class="page-section">
  <p class="page-intro__eyebrow">Program Overview</p>
  <h2 class="page-intro__title">Research program scope</h2>
  <p class="page-intro__lede">
    Our research program spans methodological innovation, software development, and embedded collaborative science across precision oncology applications. We develop adaptive trial designs, biomarker-driven stratification methods, and genomic analysis tools through partnerships with UNC Lineberger disease-site teams and national consortia. This integrative approach ensures statistical methods address real clinical needs while maintaining methodological rigor.
  </p>
</section>

<section class="page-section page-section--featured">
  <p class="page-intro__eyebrow">Translational Impact</p>
  <h2 class="page-intro__title">Featured achievements</h2>

  <div class="focus-grid">
    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">AI &amp; Machine Learning</p>
      <h3>Deep Learning for Non-Ignorable Missingness</h3>
      <p><strong>First framework bridging deep learning &amp; classical generalized linear model inference</strong> for principled uncertainty quantification. NIMIWAE and dlGLM methods use variational autoencoders to handle informative missingness in clinical registries and genomic studies—outperforming standard imputation when data are missing not at random.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">JCGS 2024</span>
        <span class="focus-chip">Stat Biopharm Res 2024</span>
        <span class="focus-chip">ARPA-H deployment</span>
      </div>
    </article>

    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">Clinical Translation</p>
      <h3>Single-Sample Tumor Subtyping</h3>
      <p><strong>PurIST classifier</strong> enables platform-independent, reference-free pancreatic cancer subtyping using single bulk RNA-seq samples—addressing the challenge of tumor purity heterogeneity through novel deconvolution-informed modeling. Methodology supports clinical decision-making in biomarker-stratified trials.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">Clinical Cancer Research (2020)</span>
        <span class="focus-chip">J Molecular Diagnostics (2024)</span>
        <span class="focus-chip">CLIA-certified implementation</span>
      </div>
    </article>

    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">Adaptive Trials</p>
      <h3>Bayesian Platform Design with Late-Arriving Biomarkers</h3>
      <p>Novel adaptive randomization framework integrating serial ctDNA, tissue, and imaging data for metastatic breast cancer platforms. Methodology accommodates staggered biomarker availability and enables mid-trial enrichment based on early response signals.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">ARPA-H ADAPT platform</span>
        <span class="focus-chip">TBCRC cooperative trials</span>
        <span class="focus-chip">Bayesian response-adaptive design</span>
      </div>
    </article>

    <article class="focus-card">
      <p class="focus-card__badge">High-Dimensional Methods</p>
      <h3>Penalized Mixed Models for Correlated Biomarkers</h3>
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
