---
layout: page
title: Software
permalink: /software/
description: Open-source R packages and AI tools for cancer genomics, biostatistics, and clinical trials. Includes glmmPen, PurIST, dlGLM, NIMIWAE, and epigraHMM for RNA-seq, machine learning, precision medicine, and clinical research.
nav: true
nav_order: 4
---

<section class="page-section page-intro">
  <p class="page-intro__eyebrow">Overview</p>
  <h2 class="page-intro__title">Software</h2>
  <p class="page-intro__lede">
    {{ page.description }}
  </p>
  <p class="mb-0">Clinical tools, R packages, and legacy utilities are grouped below so collaborators can jump straight to validated builds.</p>
  <ul>
    <li>PurIST CLIA assay + TrialMatch navigation stack</li>
    <li>Bioconductor / CRAN releases for GLMMs, DTU, and imputation</li>
    <li>Legacy research utilities archived with documentation</li>
  </ul>
</section>

<section class="page-section page-section--alt">
<h2>Decision Support Tools &amp; Patents</h2>
<div class="software-grid">
  <article class="software-card">
    <h3>PurIST Pancreatic Classifier</h3>
    <p>CLIA-ready, single-sample PDAC subtype assay embedded in cooperative trials.</p>
    <ul>
      <li><strong>Patents:</strong>
        <ul>
          <li><a href="https://patents.google.com/patent/US11053550B2" target="_blank" rel="noopener">US 11,053,550</a> (July 2021) – Gene-expression based subtyping of PDAC</li>
          <li><a href="https://patents.google.com/patent/US17336600" target="_blank" rel="noopener">US Patent App. 17/336,600</a> (April 2022) – Methods and compositions for prognostic/diagnostic subtyping</li>
          <li><a href="https://patents.google.com/patent/US12000003B2" target="_blank" rel="noopener">US 12,000,003</a> (June 2024) – Platform-independent single sample classifier</li>
        </ul>
      </li>
      <li><strong>Key papers:</strong> Rashid et al., <em>Clin Cancer Res</em> (2020); Li et al., <em>J Mol Diagnostics</em> (2024)</li>
      <li><strong>Code:</strong> <a href="https://github.com/naimurashid/PurIST">GitHub</a> · <a href="https://github.com/naimurashid/runPurIST">Shiny GUI</a></li>
    </ul>
  </article>
</div>
</section>

<section class="page-section">
<h2>R Packages</h2>
<div class="software-grid">
  <article class="software-card">
    <h3>dlglm</h3>
    <p>Deeply learned GLMs handling non-ignorable missingness. <strong>Deployed in ARPA-H ADAPT analytics.</strong></p>
    <ul>
      <li><a href="https://github.com/DavidKLim/dlglm">GitHub</a></li>
      <li>Lim et al., <em>JCGS</em> (2024)</li>
    </ul>
  </article>
  <article class="software-card">
    <h3>NIMIWAE</h3>
    <p>Variational autoencoder for non-ignorable missing data. <strong>Deployed in ARPA-H ADAPT analytics.</strong></p>
    <ul>
      <li><a href="https://github.com/DavidKLim/NIMIWAE">GitHub</a></li>
      <li>Lim et al., <em>Stat Biopharm Res</em> (2024)</li>
    </ul>
  </article>
  <article class="software-card">
    <h3>glmmPen</h3>
    <p>Penalized GLMM selection for biomarker discovery.</p>
    <ul>
      <li><a href="https://cran.r-project.org/package=glmmPen">CRAN</a> · <a href="https://github.com/hheiling/glmmPen">GitHub</a></li>
      <li>Heiling et al., <em>The R Journal</em> (2024)</li>
    </ul>
  </article>
  <article class="software-card">
    <h3>epigraHMM</h3>
    <p>Multi-sample enrichment detection for ChIP/ATAC.</p>
    <ul>
      <li><a href="http://bioconductor.org/packages/epigraHMM">Bioconductor</a> · <a href="https://github.com/plbaldoni/epigraHMM">GitHub</a></li>
      <li>Baldoni et al., <em>Biometrics</em> (2022)</li>
    </ul>
  </article>
  <article class="software-card">
    <h3>FSCseq</h3>
    <p>Model-based feature selection + clustering for RNA-seq.</p>
    <ul>
      <li><a href="https://github.com/DavidKLim/FSCseq">GitHub</a></li>
      <li>Lim et al., <em>Ann Appl Stat</em> (2021)</li>
    </ul>
  </article>
  <article class="software-card">
    <h3>CompDTUReg</h3>
    <p>Differential transcript usage with quantification uncertainty.</p>
    <ul>
      <li><a href="https://github.com/skvanburen/CompDTUReg">GitHub</a></li>
      <li>Young et al., <em>Biostatistics</em> (2023)</li>
    </ul>
  </article>
</div>
</section>

<section class="page-section page-section--alt">
<h3>Legacy &amp; Specialized Tools</h3>
<ul class="software-list">
  <li><strong>mixNBHMM</strong> – Differential peak calling for multi-condition epigenomic data. (<a href="https://github.com/plbaldoni/mixNBHMM">GitHub</a>)</li>
  <li><strong>ZIMHMM</strong> – Consensus enrichment calling across ChIP-seq replicates. (<a href="https://github.com/plbaldoni/ZIMHMM">GitHub</a>)</li>
  <li><strong>ZINBA</strong> – Zero-inflated negative binomial algorithm detecting NGS-enriched regions. (<a href="https://code.google.com/p/zinba">Project</a>)</li>
  <li><strong>hmmcov</strong> – HMM / AR-HMM procedures with variable selection for epigenetic enrichment. (<a href="https://code.google.com/p/hmmcov">Project</a>)</li>
  <li><strong>BASeG</strong> – Bivariate association studies linking expression and epigenetic marks with shared genetics. (Rashid et al., <em>Ann Appl Stat</em>, 2016)</li>
</ul>
</section>

<section class="page-section" markdown="1">
## Code Repositories

All software is actively maintained on GitHub. Contributions, issues, and feature requests are welcome, and the full repository + contributor stats live on the [Repositories page](/repositories/).

### Collaborative Development
Many packages are developed in close collaboration with lab members and trainees:
- **Hillary Heiling**: glmmPen lead developer
- **David Lim**: dlglm, NIMIWAE, FSCseq lead developer
- **Pedro Baldoni**: epigraHMM, mixNBHMM, ZIMHMM lead developer
- **Scott Van Buren**: CompDTUReg lead developer
- **Amber Young**: CompDTUReg co-developer; current PhD student working on semi-supervised matrix factorization for PDAC subtyping
</section>

<div class="page-cta page-cta--usage">
  <p><strong>Using these tools in your research?</strong> We'd love to hear about it. <a href="mailto:naim@unc.edu">Get in touch →</a></p>
</div>

<section class="page-section page-section--alt" markdown="1">
## Support & Contact

For technical support, please open an issue on the relevant GitHub repository. For collaboration inquiries, contact [naim@unc.edu](mailto:naim@unc.edu).
</section>
