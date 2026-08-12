---
layout: page
title: Software
permalink: /software/
description: Open-source R packages and AI tools for cancer genomics, biostatistics, and clinical trials. Includes glmmPen, PurIST, dlGLM, NIMIWAE, and epigraHMM for RNA-seq, machine learning, precision medicine, and clinical research.
nav: true
nav_order: 4
---

<p class="software-page__lede">Clinical decision-support tools, R packages, and legacy utilities developed by the lab. Each card links to its repository, distribution, and the paper that describes it.</p>

<section class="page-section page-section--alt">
<h2>Decision Support Tools &amp; Patents</h2>
<div class="software-grid">

  <article class="software-card">
    <div class="software-card__head">
      <h3>PurIST Pancreatic Classifier</h3>
    </div>
    <p class="software-card__desc">Single-sample PDAC subtype assay used in cooperative trials.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="clinical">Clinical Tool</li>
      <li class="software-card__pill">3 patents</li>
      <li class="software-card__pill">Active</li>
    </ul>
    <ul class="software-card__patents">
      <li><strong><a href="https://patents.google.com/patent/US11053550B2" target="_blank" rel="noopener">US 11,053,550</a></strong> (Jul 2021) — Gene-expression based subtyping of PDAC</li>
      <li><strong><a href="https://patents.google.com/patent/US17336600" target="_blank" rel="noopener">US App. 17/336,600</a></strong> (Apr 2022) — Methods for prognostic / diagnostic subtyping</li>
      <li><strong><a href="https://patents.google.com/patent/US12000003B2" target="_blank" rel="noopener">US 12,000,003</a></strong> (Jun 2024) — Platform-independent single-sample classifier</li>
    </ul>
    <ul class="software-card__refs">
      <li>Rashid et al., Clin Cancer Res (2020)</li>
      <li>Li et al., J Mol Diagnostics (2024)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/naimurashid/PurIST">GitHub</a></li>
      <li><a href="https://github.com/naimurashid/runPurIST">Shiny GUI</a></li>
      <li><a class="software-card__download" href="{{ '/assets/img/hex/purist.svg' | relative_url }}" download>Hex sticker</a></li>
    </ul>
  </article>

</div>
</section>

<section class="page-section">
<h2>R Packages</h2>
<div class="software-grid">

  <article class="software-card">
    <div class="software-card__head">
      <h3>BATON</h3>
    </div>
    <p class="software-card__desc">Bayesian adaptive trial operating-characteristic tuning for platform trials.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="in-development">In Development</li>
      <li class="software-card__pill">2025</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/naimurashid/BATON">GitHub</a></li>
      <li><a class="software-card__download" href="{{ '/assets/img/hex/baton.svg' | relative_url }}" download>Hex sticker</a></li>
    </ul>
  </article>

  <article class="software-card">
    <div class="software-card__head">
      <h3>evolveTrial</h3>
    </div>
    <p class="software-card__desc">Adaptive monitoring and simulation tools for evolutionary clinical trial designs.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="in-development">In Development</li>
      <li class="software-card__pill">2025</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/naimurashid/evolveTrial">GitHub</a></li>
      <li><a class="software-card__download" href="{{ '/assets/img/hex/evolvetrial.svg' | relative_url }}" download>Hex sticker</a></li>
    </ul>
  </article>

  <article class="software-card">
    <div class="software-card__head">
      <h3>DeSurv</h3>
    </div>
    <p class="software-card__desc">Survival-guided nonnegative matrix factorization for discovering prognostic gene programs from bulk tumor expression.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="github">GitHub</li>
      <li class="software-card__pill">2026</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/rashidlab/DeSurv">GitHub</a></li>
      <li><a href="https://github.com/rashidlab/DeSurv-paper">Paper materials</a></li>
      <li><a class="software-card__download" href="{{ '/assets/img/hex/desurv.svg' | relative_url }}" download>Hex sticker</a></li>
    </ul>
  </article>

  <article class="software-card">
    <h3>dlglm</h3>
    <p class="software-card__desc">Deeply learned GLMs handling non-ignorable missingness.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="github">GitHub</li>
      <li class="software-card__pill">2024</li>
    </ul>
    <ul class="software-card__refs">
      <li>Lim et al., JCGS (2024)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/DavidKLim/dlglm">GitHub</a></li>
    </ul>
  </article>

  <article class="software-card">
    <h3>NIMIWAE</h3>
    <p class="software-card__desc">Variational autoencoder for non-ignorable missing data.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="github">GitHub</li>
      <li class="software-card__pill">2024</li>
    </ul>
    <ul class="software-card__refs">
      <li>Lim et al., Stat Biopharm Res (2024)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/DavidKLim/NIMIWAE">GitHub</a></li>
    </ul>
  </article>

  <article class="software-card">
    <h3>glmmPen</h3>
    <p class="software-card__desc">Penalized GLMM selection for biomarker discovery.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="cran">CRAN</li>
      <li class="software-card__pill">2024</li>
    </ul>
    <ul class="software-card__refs">
      <li>Heiling et al., The R Journal (2024)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://cran.r-project.org/package=glmmPen">CRAN</a></li>
      <li><a href="https://github.com/hheiling/glmmPen">GitHub</a></li>
    </ul>
  </article>

  <article class="software-card">
    <h3>CompDTUReg</h3>
    <p class="software-card__desc">Differential transcript usage with quantification uncertainty.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="github">GitHub</li>
      <li class="software-card__pill">2023</li>
    </ul>
    <ul class="software-card__refs">
      <li>Young et al., Biostatistics (2023)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/skvanburen/CompDTUReg">GitHub</a></li>
    </ul>
  </article>

  <article class="software-card">
    <h3>epigraHMM</h3>
    <p class="software-card__desc">Multi-sample enrichment detection for ChIP/ATAC.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="bioconductor">Bioconductor</li>
      <li class="software-card__pill">2022</li>
    </ul>
    <ul class="software-card__refs">
      <li>Baldoni et al., Biometrics (2022)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="http://bioconductor.org/packages/epigraHMM">Bioconductor</a></li>
      <li><a href="https://github.com/plbaldoni/epigraHMM">GitHub</a></li>
    </ul>
  </article>

  <article class="software-card">
    <h3>FSCseq</h3>
    <p class="software-card__desc">Model-based feature selection + clustering for RNA-seq.</p>
    <ul class="software-card__meta">
      <li class="software-card__pill software-card__pill--status" data-status="github">GitHub</li>
      <li class="software-card__pill">2021</li>
    </ul>
    <ul class="software-card__refs">
      <li>Lim et al., Ann Appl Stat (2021)</li>
    </ul>
    <ul class="software-card__links">
      <li><a href="https://github.com/DavidKLim/FSCseq">GitHub</a></li>
    </ul>
  </article>

</div>
</section>

<section class="page-section page-section--alt">
<h3>Legacy &amp; Specialized Tools</h3>
<ul class="software-list">
  <li><strong>mixNBHMM</strong> — Differential peak calling for multi-condition epigenomic data. (<a href="https://github.com/plbaldoni/mixNBHMM">GitHub</a>)</li>
  <li><strong>ZIMHMM</strong> — Consensus enrichment calling across ChIP-seq replicates. (<a href="https://github.com/plbaldoni/ZIMHMM">GitHub</a>)</li>
  <li><strong>ZINBA</strong> — Zero-inflated negative binomial algorithm detecting NGS-enriched regions. (Archived; formerly hosted on Google Code)</li>
  <li><strong>hmmcov</strong> — HMM / AR-HMM procedures with variable selection for epigenetic enrichment. (Archived; formerly hosted on Google Code)</li>
  <li><strong>BASeG</strong> — Bivariate association studies linking expression and epigenetic marks with shared genetics. (Rashid et al., <em>Ann Appl Stat</em>, 2016)</li>
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
- **Amber Young**: DeSurv lead developer, CompDTUReg co-developer (PhD 2026; now at Natera)
</section>

## Support & Contact

For technical support, please open an issue on the relevant GitHub repository. For collaboration inquiries, contact [naim@unc.edu](mailto:naim@unc.edu).
