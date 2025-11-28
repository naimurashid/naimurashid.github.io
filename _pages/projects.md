---
layout: page
title: Projects
permalink: /projects/
description: Live build tracker for Rashid Lab software, analytics pipelines, and translational tooling.
nav: true
nav_order: 3

---

<section class="section-hero section-hero--projects">
  <div class="section-hero__content">
    <p class="section-hero__eyebrow">Build Tracker</p>
    <h1>Code-to-clinic projects</h1>
    <p class="section-hero__lede">
      Each card shows where a method sits on the journey from prototype to patient deployment. Readiness badges and links make it clear how collaborators or funders can plug into the next milestone.
    </p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="/repositories/">Browse repositories</a>
      <a class="btn btn-outline-primary" href="mailto:naim@unc.edu">Request a consultation</a>
    </div>
  </div>
  <div class="section-metrics">
    <div class="metric">
      <span class="metric__value">3</span>
      <span class="metric__label">development phases</span>
    </div>
    <div class="metric">
      <span class="metric__value">6</span>
      <span class="metric__label">pilot-ready methods</span>
    </div>
    <div class="metric">
      <span class="metric__value">10+</span>
      <span class="metric__label">community deployments</span>
    </div>
    <div class="metric">
      <span class="metric__value">24</span>
      <span class="metric__label">trainee-led builds</span>
    </div>
  </div>
</section>

<section class="page-section">
  <p class="page-intro__eyebrow">Stage 1</p>
  <h2 class="page-intro__title">In development</h2>
  <div class="focus-grid project-grid">
    <article class="project-card">
      <p class="project-card__badge project-card__badge--develop">Survival methodology</p>
      <h3>DeSurv Platform</h3>
      <p>Efficient survival estimators pairing de-biased gradients with flexible machine-learning bases for biomarker-rich trials.</p>
      <ul class="project-meta">
        <li><strong>Lead:</strong> <a href="{{ '/members/about_amber/' | relative_url }}">Amber Young</a></li>
        <li><strong>Milestone:</strong> Manuscript + CRAN submission · Fall 2025</li>
      </ul>
      <div class="project-card__links">
        <a href="https://github.com/naimurashid/DeSurv" target="_blank" rel="noopener" class="link-arrow">Preview code</a>
      </div>
    </article>

    <article class="project-card">
      <p class="project-card__badge project-card__badge--develop">Adaptive trial core</p>
      <h3>ADAPT Statistical Hub</h3>
      <p><code>evolveTrial</code> and <code>evolveBO</code> packages for adaptive monitoring and automated operating-characteristic tuning across EVOLVE_BDT and ARPA-H ADAPT reviews.</p>
      <ul class="project-meta">
        <li><strong>Leads:</strong> Naim Rashid, <a href="{{ '/members/about_amber/' | relative_url }}">Amber Young</a></li>
        <li><strong>Milestone:</strong> CRAN packages + interim review · Oct 2025</li>
      </ul>
      <div class="project-card__links">
        <a href="/funding/#tbcrc-evolvebdt" class="link-arrow">Protocol summary</a>
      </div>
    </article>

    <article class="project-card">
      <p class="project-card__badge project-card__badge--develop">Patient communication</p>
      <h3>TrialMatch LLM</h3>
      <p>Fine-tuned language model translating pancreatic cancer eligibility criteria into bilingual summaries with transparent inclusion/exclusion logic.</p>
      <ul class="project-meta">
        <li><strong>Lead:</strong> <a href="{{ '/members/about_tyler/' | relative_url }}">Tyler Humpherys</a></li>
        <li><strong>Milestone:</strong> Clinic pilot across GI clinics · Fall 2025</li>
      </ul>
      <div class="project-card__links">
        <a href="/news/" class="link-arrow">Read project brief</a>
      </div>
    </article>
  </div>
</section>

<section class="page-section page-section--alt">
  <p class="page-intro__eyebrow">Stage 2</p>
  <h2 class="page-intro__title">Pilot deployment</h2>
  <div class="focus-grid project-grid">
    <article class="project-card project-card--pilot">
      <p class="project-card__badge project-card__badge--pilot">Missing data</p>
      <h3>dlGLM Package</h3>
      <p>Deep-learning generalized linear models for non-ignorable missing data supporting ARPA-H ADAPT analytics and shared-resource consults.</p>
      <ul class="project-meta">
        <li><strong>Next:</strong> External validation manuscript</li>
      </ul>
    </article>

    <article class="project-card project-card--pilot">
      <p class="project-card__badge project-card__badge--pilot">Stromal genomics</p>
      <h3>DeCAF Classifier</h3>
      <p>Transcriptomic classifier of pancreatic tumor and stromal interaction states informing biomarker analyses for PDAC trials.</p>
      <ul class="project-meta">
        <li><strong>Next:</strong> Trial-readiness review</li>
      </ul>
    </article>

    <article class="project-card project-card--pilot">
      <p class="project-card__badge project-card__badge--pilot">Clinical registries</p>
      <h3>NIMIWAE Package</h3>
      <p>Deep-learning imputation methods for EHR labs and longitudinal clinical data supporting ARPA-H and Lineberger analytics.</p>
      <ul class="project-meta">
        <li><strong>Next:</strong> Bioconductor submission</li>
      </ul>
    </article>
  </div>
</section>

<section class="page-section">
  <p class="page-intro__eyebrow">Stage 3</p>
  <h2 class="page-intro__title">Community adoption</h2>
  <div class="focus-grid project-grid">
    <article class="project-card project-card--adopt">
      <p class="project-card__badge project-card__badge--adopt">Epigenomics</p>
      <h3>epigraHMM</h3>
      <p>Multi-condition epigenomic discovery pipeline with 5,014 Bioconductor downloads powering ATAC/ChIP analyses for UNC Lineberger and industry partners.</p>
      <ul class="project-meta">
        <li><strong>Maintainers:</strong> <a href="{{ '/members/about_pedro/' | relative_url }}">Pedro Baldoni</a>, Naim Rashid</li>
      </ul>
    </article>

    <article class="project-card project-card--adopt">
      <p class="project-card__badge project-card__badge--adopt">RNA-seq suite</p>
      <h3>FSCseq + CompDTUReg</h3>
      <p>Subtype discovery and differential transcript usage suite with reproducible vignettes, adopted by SPORE cores and industry partners.</p>
      <ul class="project-meta">
        <li><strong>Maintainers:</strong> <a href="{{ '/members/about_david/' | relative_url }}">David Lim</a>, <a href="{{ '/members/about_scott/' | relative_url }}">Scott Van Buren</a>, <a href="{{ '/members/about_amber/' | relative_url }}">Amber Young</a></li>
      </ul>
    </article>

    <article class="project-card project-card--adopt">
      <p class="project-card__badge project-card__badge--adopt">Clinical diagnostics</p>
      <h3>PurIST Clinical Pipeline</h3>
      <p>Single-sample PDAC classifier with CLIA reporting and API hooks supporting UNC Molecular Diagnostics and PANCREAS trial evaluations.</p>
      <ul class="project-meta">
        <li><strong>Status:</strong> Live in UNC Molecular Diagnostics · under review in PANCREAS trial</li>
      </ul>
    </article>
  </div>
</section>

<section class="page-section page-section--alt">
  <p class="page-intro__eyebrow">Journeys</p>
  <h2 class="page-intro__title">Code-to-clinic stories</h2>
  <div class="focus-grid project-grid">
    <article class="project-card project-card--story">
      <p class="project-card__badge project-card__badge--story">Diagnostics</p>
      <h3>PurIST → cooperative trials</h3>
      <p>Went from Nature Genetics prototype to CLIA-certified assay now informing UNC Molecular Diagnostics reports and PANCREAS trial subtyping.</p>
    </article>
    <article class="project-card project-card--story">
      <p class="project-card__badge project-card__badge--story">Epigenomics</p>
      <h3>epigraHMM → NIH consortia</h3>
      <p>Cited across Bioconductor workflows and used by UNC/TBCRC teams to harmonize ATAC/ChIP analyses for cell-state discovery.</p>
    </article>
    <article class="project-card project-card--story">
      <p class="project-card__badge project-card__badge--story">Missing data</p>
      <h3>dlGLM → ARPA-H analytics</h3>
      <p>Deployed in ADAPT analytics with containerized builds on Lineberger HPC; next milestone is external validation manuscript.</p>
    </article>
  </div>
</section>

<section class="page-section collaboration-callout">
  <h2>Collaboration &amp; access</h2>
  <p>Projects are co-developed with Gillings trainees, UNC Lineberger oncologists, Alliance cooperative groups, and partners such as GSK and ARPA-H. Every pilot runs through UNC IRB protocols, and documentation lives in GitHub repos plus lab wikis.</p>
  <ul class="project-meta">
    <li><strong>Request pilot access:</strong> <a href="mailto:naim@unc.edu">naim@unc.edu</a></li>
    <li><strong>Browse repositories:</strong> <a href="/repositories/">/repositories/</a></li>
    <li><strong>Join builds:</strong> Gillings BIOS 690 capstone + Lineberger internships</li>
  </ul>
</section>
