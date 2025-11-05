---
layout: page
permalink: /publications/
title: publications
description: Statistical methods and collaborative research in cancer genomics and precision oncology
nav: true
nav_order: 6
---

<!-- _pages/publications.md -->

## Publication Metrics

<div class="pub-metrics">
  <div class="pub-metric">
    <span class="pub-metric__value">75+</span>
    <span class="pub-metric__label">Peer-Reviewed Publications</span>
  </div>
  <div class="pub-metric">
    <span class="pub-metric__value">h-index: 28</span>
    <span class="pub-metric__label"><a href="https://scholar.google.com/citations?user=3Cz_lcEAAAAJ" target="_blank" rel="noopener">Google Scholar Profile</a></span>
  </div>
  <div class="pub-metric">
    <span class="pub-metric__value">5,000+</span>
    <span class="pub-metric__label">Total Citations</span>
  </div>
  <div class="pub-metric">
    <span class="pub-metric__value">20+</span>
    <span class="pub-metric__label">Methodology Papers</span>
  </div>
</div>

*indicates student or postdoc

---

## Featured Publications

{% include publication-highlights.liquid %}

---

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

---

<h3 id="clinical-trials">Clinical Trials Methodology</h3>

<div class="publications">

{% bibliography --query @*[keywords ~= trials] %}

</div>

---

<h3 id="mixed-models">Penalized Mixed Models & High-Dimensional Inference</h3>

<div class="publications">

{% bibliography --query @*[keywords ~= mixed-models] %}

</div>

---

<h3 id="genomics">Cancer Genomics & Multi-Omic Integration</h3>

<div class="publications">

{% bibliography --query @*[keywords ~= genomics] %}

</div>

---

<h3 id="machine-learning">Machine Learning for Precision Oncology</h3>

<div class="publications">

{% bibliography --query @*[keywords ~= machine-learning] %}

</div>

---

<h3 id="epigenomics">Epigenomics & Regulatory Genomics</h3>

<div class="publications">

{% bibliography --query @*[keywords ~= epigenomics] %}

</div>

---

<h3 id="all-publications">All Publications (Chronological)</h3>

<div class="publications">

{% bibliography %}

</div>
