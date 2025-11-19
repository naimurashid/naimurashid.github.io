---
layout: page
permalink: /publications/
title: Publications
description: 75+ peer-reviewed publications in biostatistics, clinical trials, machine learning, cancer genomics, and precision oncology. h-index 28, 5000+ citations. Research in AI, adaptive trial design, RNA-seq, and tumor subtyping.
nav: true
nav_order: 6
---

<!-- _pages/publications.md -->

<section class="page-section page-intro">
  <p class="page-intro__eyebrow">Overview</p>
  <h2 class="page-intro__title">Publication Portfolio</h2>
  <p class="page-intro__lede">
    {{ page.description }}
  </p>
  <p>Our methodological contributions to adaptive trial design, cancer subtyping, and genomic inference support translational oncology research nationally. Editorial service includes the <em>Nature Medicine</em> Statistical Advisory Panel (2024–) and Associate Editor roles at <em>Annals of Applied Statistics</em> (2023–) and <em>Statistical Methods in Medical Research</em>, advancing methodological standards for reproducible cancer biomarker research.</p>
  <p class="mb-0">Publications span clinical trials methodology, genomics, machine learning, and epigenomics across top-tier journals:</p>
  <ul>
    <li>Methodological journals: <em>JASA</em>, <em>Biostatistics</em>, <em>Biometrics</em>, <em>Annals of Applied Statistics</em></li>
    <li>Clinical/translational journals: <em>Clinical Cancer Research</em>, <em>Nature Genetics</em>, <em>JCO</em>, <em>PNAS</em></li>
    <li>Areas: Adaptive trials, penalized regression, tumor subtyping, RNA-seq, deep learning</li>
  </ul>
</section>

<section class="page-section">
  <h2 class="mb-4">Impact Highlights</h2>
  <div class="row g-4">
    <div class="col-md-4">
      <div class="p-4 h-100 rounded shadow-sm bg-white">
        <p class="text-muted text-uppercase small mb-1">Peer-Reviewed Output</p>
        <p class="display-6 mb-2">75+</p>
        <p class="mb-0">Articles across JASA, Clin Cancer Res, Nature Genetics, and allied oncology journals.</p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="p-4 h-100 rounded shadow-sm bg-white">
        <p class="text-muted text-uppercase small mb-1">Citation Profile</p>
        <p class="display-6 mb-2">h-index 28</p>
        <p class="mb-0"><a href="https://scholar.google.com/citations?user=3Cz_lcEAAAAJ" target="_blank" rel="noopener">View on Google Scholar</a></p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="p-4 h-100 rounded shadow-sm bg-white">
        <p class="text-muted text-uppercase small mb-1">Mentored Scholarship</p>
        <p class="display-6 mb-2">25*</p>
        <p class="mb-0">Student or postdoc first-author papers spanning genomics, trials, and AI.</p>
      </div>
    </div>
  </div>
  <p class="small text-muted mt-3">*indicates student or postdoc lead author.</p>
</section>

<section class="page-section page-section--alt">
  <h2>Featured Publications</h2>
  {% include publication-highlights.liquid %}
</section>

<section class="page-section" markdown="1">
## Publications by Theme

Use the search box below to find publications by keyword, or browse by research theme.

<!-- Bibsearch Feature -->
{% include bib_search.liquid %}

### Research Themes

<div class="theme-filters">
  <a href="#clinical-trials" class="theme-filter">Clinical Trials Methodology</a>
  <a href="#mixed-models" class="theme-filter">Penalized Mixed Models</a>
  <a href="#genomics" class="theme-filter">Cancer Genomics</a>
  <a href="#machine-learning" class="theme-filter">Machine Learning</a>
  <a href="#epigenomics" class="theme-filter">Epigenomics</a>
  <a href="#all-publications" class="theme-filter theme-filter--active">All Publications</a>
</div>
</section>

<section class="page-section" markdown="1">
</section>

<section class="page-section" markdown="1">
<details class="pub-section" open>
  <summary>Clinical Trials Methodology</summary>
  <div class="publications">
    {% bibliography --query @*[keywords ~= trials] %}
  </div>
</details>

<details class="pub-section">
  <summary>Penalized Mixed Models &amp; High-Dimensional Inference</summary>
  <div class="publications">
    {% bibliography --query @*[keywords ~= mixed-models] %}
  </div>
</details>

<details class="pub-section">
  <summary>Cancer Genomics &amp; Multi-Omic Integration</summary>
  <div class="publications">
    {% bibliography --query @*[keywords ~= genomics] %}
  </div>
</details>

<details class="pub-section">
  <summary>Machine Learning for Precision Oncology</summary>
  <div class="publications">
    {% bibliography --query @*[keywords ~= machine-learning] %}
  </div>
</details>

<details class="pub-section">
  <summary>Epigenomics &amp; Regulatory Genomics</summary>
  <div class="publications">
    {% bibliography --query @*[keywords ~= epigenomics] %}
  </div>
</details>

<details class="pub-section">
  <summary>All Publications (Chronological)</summary>
  <div class="publications">
    {% bibliography %}
  </div>
</details>
</section>
