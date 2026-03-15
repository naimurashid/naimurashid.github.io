---
layout: page
title: PurIST pancreatic subtyping diagnostic
description: Translating robust molecular subtyping into a clinically deployable test
img: assets/img/purist_figure4.jpg
importance: 4
category: work
related_publications: true
---

Purity Independent Subtyping of Tumors (PurIST) delivers the first clinically robust, single-sample classifier for pancreatic ductal adenocarcinoma. Developed with UNC Lineberger collaborators, the classifier is resilient to tumor purity, batch effects, and assay platforms, enabling prospective use in routine pathology workflows.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/purist_figure4.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Development and validation of the PurIST SSC classifier across multiple independent cohorts, demonstrating robust performance regardless of tumor purity or sequencing platform.
</div>

### From algorithm to diagnostic

- **Methodological foundation.** Rank-based scoring stabilizes gene-expression signatures in low-tumor-content samples, providing reproducible assignments across sequencing technologies.
- **Rigorous validation.** PurIST has been replicated across international cohorts, published in _Clinical Cancer Research_, and implemented in CLIA-certified laboratories supporting cooperative group trials.
- **Clinical deployment.** The test informs treatment selection in ongoing PDAC studies and is being evaluated as a stratification and enrichment tool for precision therapeutic trials.

### Software and data resources

- Open-source training and inference code with example datasets are available to academic collaborators.
- Trial sponsors can access QA documentation and integration guidance via the Lineberger Biostatistics Shared Resource.

*Key reference:* {% cite purity2020 %}
