---
layout: page
title: glmmPen and high-dimensional mixed-model analytics
description: Enabling scalable inference for complex longitudinal and survival data
img: assets/img/7.jpg
importance: 5
category: work
related_publications: true
---

The `glmmPen` R package grew out of Rashid Lab collaborations with UNC Lineberger investigators who needed principled inference for clustered, high-dimensional datasets—ranging from bulk RNA-seq to clinic-based registries and survival studies. The software implements penalized generalized linear mixed models and mixed-effects Cox models with automated tuning and diagnostic utilities.

<!-- TODO: Add Figure 1 from https://arxiv.org/pdf/2504.00755v1 showing survival model performance -->

### Why it matters

- **Precision modeling.** Handles thousands of fixed and random effects simultaneously, empowering biomarker discovery and risk prediction studies with repeated measures and time-to-event outcomes.
- **Survival analysis integration.** Extends penalized mixed models to Cox proportional hazards regression, enabling discovery of prognostic signatures in clustered cancer datasets with frailty terms.
- **Production ready.** Exposes user-friendly functions for simulation, cross-validation, and reporting, and underpins analyses in ARPA-H ADAPT, SPORE projects, and industry partnerships.

### Key publications

- *Penalized GLMMs:* {% cite heiling2021b %}
- *Survival extensions:* Variable selection in high-dimensional mixed effects survival models (_Biometrics_, 2024) - [arXiv:2504.00755](https://arxiv.org/abs/2504.00755)
