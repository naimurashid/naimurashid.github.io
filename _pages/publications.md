---
layout: page
permalink: /publications/
title: Publications
description: Peer-reviewed publications in biostatistics, clinical trials, machine learning, cancer genomics, and precision oncology. Research in AI, adaptive trial design, RNA-seq, and tumor subtyping.
nav: true
nav_order: 6
---

<!-- _pages/publications.md -->

Work spans clinical trials, genomics, machine learning, and epigenomics, with service on the *Nature Medicine* Statistical Advisory Panel (2023–) and as Associate Editor for *Annals of Applied Statistics* (2022–) and *Statistical Methods in Medical Research*.

<section class="page-section page-section--alt page-section--highlights">
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
  <a href="#clinical-trials" class="theme-filter">Clinical Trials</a>
  <a href="#mixed-models" class="theme-filter">Penalized Mixed Models</a>
  <a href="#genomics" class="theme-filter">Cancer Genomics</a>
  <a href="#machine-learning" class="theme-filter">Machine Learning</a>
  <a href="#epigenomics" class="theme-filter">Epigenomics</a>
  <a href="#all-publications" class="theme-filter theme-filter--active">All Publications</a>
</div>
</section>

<section class="page-section" markdown="1">
<details class="pub-section" open>
  <summary>Clinical Trials</summary>
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
