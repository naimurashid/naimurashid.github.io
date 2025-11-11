---
layout: page
title: Projects
permalink: /projects/
description: Live build tracker for Rashid Lab software, analytics pipelines, and translational tooling.
nav: true
nav_order: 3
---

<section class="page-section page-intro">
  <p class="page-intro__eyebrow">Overview</p>
  <h2 class="page-intro__title">Bench-to-Bedside Pipeline</h2>
  <p class="page-intro__lede">
    Projects track the arc from statistical prototypes to clinical pilots and, ultimately, shared-tool adoption. Icons below highlight the stage so reviewers can see where each build sits on the path to patient impact.
  </p>
  <ul>
    <li>Methodology → pilot → community adoption pipeline</li>
    <li>Stage badges surface readiness for reviewers and funders</li>
    <li>Links to code, protocols, or news for every project</li>
  </ul>
</section>

<section class="page-section">
  <h2 class="mb-4">In Development</h2>
  <div class="row g-4">
    <div class="col-md-6 col-lg-4">
      <div class="card h-100 shadow-sm">
        <div class="card-body d-flex flex-column">
          <span class="badge bg-primary mb-2">Survival Methodology</span>
          <h3 class="h5">DeSurv Platform</h3>
          <p>New doubly-efficient survival estimators pairing de-biased gradients with flexible machine learning bases for high-dimensional biomarker trials.</p>
          <ul class="small text-muted project-list mb-4">
            <li>Lead: <a href="{{ '/members/about_amber/' | relative_url }}">Amber Young</a></li>
            <li>Milestone: Manuscript &amp; CRAN submission, Fall 2025</li>
          </ul>
          <a class="btn btn-outline-primary btn-sm mt-auto" href="https://github.com/naimurashid/DeSurv" target="_blank" rel="noopener">Preview Code</a>
        </div>
      </div>
    </div>
    <div class="col-md-6 col-lg-4">
      <div class="card h-100 shadow-sm">
        <div class="card-body d-flex flex-column">
          <span class="badge bg-warning text-dark mb-2">Adaptive Trial Core</span>
          <h3 class="h5">ADAPT Statistical Hub</h3>
          <p>Developing the <code>evolveTrial</code> R package for adaptive monitoring plus <code>evolveBO</code> for automated operating-characteristic tuning, supporting EVOLVE_BDT and ARPA-H ADAPT trial design reviews.</p>
          <ul class="small text-muted project-list mb-4">
            <li>Leads: Naim Rashid, <a href="{{ '/members/about_amber/' | relative_url }}">Amber Young</a></li>
            <li>Milestone: CRAN-ready packages &amp; first interim submission, Oct 2025</li>
          </ul>
          <a class="btn btn-outline-primary btn-sm mt-auto" href="/funding/#tbcrc-evolvebdt" target="_blank" rel="noopener">View Protocol Summary</a>
        </div>
      </div>
    </div>
    <div class="col-md-6 col-lg-4">
      <div class="card h-100 shadow-sm">
        <div class="card-body d-flex flex-column">
          <span class="badge bg-info text-dark mb-2">Patient Communication</span>
          <h3 class="h5">TrialMatch LLM</h3>
          <p>Fine-tuned language model translating pancreatic cancer eligibility criteria into bilingual patient summaries while surfacing inclusion/exclusion logic for GI oncologists.</p>
          <ul class="small text-muted project-list mb-4">
            <li>Lead: <a href="{{ '/members/about_tyler/' | relative_url }}">Tyler Humpherys</a></li>
            <li>Milestone: Pilot model finalized for GI clinics, Fall 2025</li>
          </ul>
          <a class="btn btn-outline-primary btn-sm mt-auto" href="/news/" target="_blank" rel="noopener">Read Project Brief</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="page-section page-section--alt">
  <h2 class="mb-4">Pilot Deployment</h2>
  <div class="row g-4">
    <div class="col-md-4">
      <div class="card h-100 border-0 bg-white shadow-sm">
        <div class="card-body">
          <h3 class="h5">dlGLM Toolkit</h3>
          <p class="mb-1">Deep-learning generalized linear models for non-ignorable missing data, now undergoing evaluation across the PSRC network and ARPA-H datasets.</p>
          <small class="text-muted">Dockerized for Lineberger HPC · Next: PSRC trial evaluation package</small>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card h-100 border-0 bg-white shadow-sm">
        <div class="card-body">
          <h3 class="h5">DeCAF Classifier</h3>
          <p class="mb-1">Digital histology/ctDNA fusion classifier stratifying triple negative breast cancer patients for pre-operative immunotherapy trials.</p>
          <small class="text-muted">Undergoing evaluation in the PSRC network · Next: trial-readiness review</small>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card h-100 border-0 bg-white shadow-sm">
        <div class="card-body">
      <h3 class="h5">NIMIWAE Toolkit</h3>
      <p class="mb-1">Deep-learning imputation toolkit for clinical lab data supporting PSRC lab networks and ARPA-H studies.</p>
      <small class="text-muted">Containerized for Lineberger HPC · Next: Bioconductor submission</small>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="page-section">
  <h2 class="mb-4">Community Adoption</h2>
  <div class="row g-4">
    <div class="col-md-6">
      <div class="card h-100 shadow-sm border-0">
        <div class="card-body">
          <h3 class="h5">epigraHMM</h3>
          <p>Multi-condition epigenomic discovery pipeline with 5,014 Bioconductor downloads (2024) supporting ChIP/ATAC signal integration.</p>
          <ul class="small text-muted project-list">
            <li>Maintainers: <a href="{{ '/members/about_pedro/' | relative_url }}">Pedro Baldoni</a>, Naim Rashid</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card h-100 shadow-sm border-0">
        <div class="card-body">
          <h3 class="h5">FSCseq + CompDTUReg</h3>
          <p>RNA-seq subtype discovery and differential transcript usage suite maintained with reproducible vignettes.</p>
          <ul class="small text-muted project-list">
            <li>Adopted by SPORE cores and industry partners</li>
            <li>Maintainers: <a href="{{ '/members/about_david/' | relative_url }}">David Lim</a>, <a href="{{ '/members/about_scott/' | relative_url }}">Scott Van Buren</a>, <a href="{{ '/members/about_amber/' | relative_url }}">Amber Young</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card h-100 shadow-sm border-0">
        <div class="card-body">
          <h3 class="h5">PurIST Clinical Pipeline</h3>
          <p>Single-sample PDAC classifier with CLIA reporting and API hooks supporting Alliance, SPORE, and industry trials.</p>
          <ul class="small text-muted project-list">
            <li>Implemented in UNC Molecular Diagnostics · scaling to cooperative groups</li>
            <li>Maintainers: Naim Rashid, Lineberger Molecular Pathology</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="page-section">
  <h2 class="mb-2">Bench-to-Bedside Stories</h2>
  <div class="row g-4">
    <div class="col-md-4">
      <div class="card h-100 border-0 shadow-sm">
        <div class="card-body">
          <h3 class="h5">PurIST → Cooperative Trials</h3>
          <p class="mb-3">PDAC classifier that moved from Nature Genetics prototype to CLIA-certified assay powering Alliance and ARPA-H stratification.</p>
          <ul class="small text-muted project-list">
            <li>Live in UNC Molecular Diagnostics</li>
            <li>Integrated into EVOLVE_BDT inclusion tiers</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card h-100 border-0 shadow-sm">
        <div class="card-body">
          <h3 class="h5">epigraHMM → NIH Consortia</h3>
          <p class="mb-3">Adopted by Cancer Moonshot labs to harmonize ATAC/ChIP workflows.</p>
          <ul class="small text-muted project-list">
            <li>18k+ Bioconductor downloads in 2024</li>
            <li>Supports TBCRC and GSK cell-state analyses</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card h-100 border-0 shadow-sm">
        <div class="card-body">
          <h3 class="h5">dlGLM → ARPA-H Analytics</h3>
          <p class="mb-3">Missing-data deep learning models embedded in ARPA-H ADAPT dashboards.</p>
          <ul class="small text-muted project-list">
            <li>Containerized on Lineberger HPC</li>
            <li>Next milestone: external validation manuscript</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="page-section">
  <h2 class="mb-3">Collaboration & Access</h2>
  <p>Projects are co-developed with Gillings biostatistics trainees, UNC Lineberger oncologists, Alliance cooperative groups, and partners such as GSK and ARPA-H. Code lives on GitHub, documentation sits in lab wikis and manuscripts, and every clinical pilot runs through UNC IRB protocols.</p>
  <ul class="small text-muted">
    <li>Request pilot access: <a href="mailto:naim@unc.edu">naim@unc.edu</a></li>
    <li>Browse repositories: <a href="/repositories/">/repositories/</a></li>
    <li>Join builds via the Gillings 690 capstone or Lineberger internships.</li>
  </ul>
</section>
