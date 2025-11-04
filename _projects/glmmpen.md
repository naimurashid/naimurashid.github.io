---
layout: page
title: glmmPen and high-dimensional mixed-model analytics
description: Enabling scalable inference for complex longitudinal cancer data
img: assets/img/7.jpg
importance: 5
category: work
related_publications: true
---

The `glmmPen` R package grew out of Rashid Lab collaborations with UNC Lineberger investigators who needed principled inference for clustered, high-dimensional datasets—ranging from bulk RNA-seq to clinic-based registries with missingness. The software implements penalized generalized linear mixed models with automated tuning and diagnostic utilities.

### Why it matters

- **Precision modeling.** Handles thousands of fixed and random effects simultaneously, empowering biomarker discovery and risk prediction studies with repeated measures.
- **Missing-data resilience.** Embeds likelihood-based approaches and imputation-aware penalties to mitigate non-ignorable missingness, a critical feature for real-world evidence and EHR applications.
- **Production ready.** Exposes user-friendly functions for simulation, cross-validation, and reporting, and underpins analyses in ARPA-H ADAPT, SPORE projects, and industry partnerships.

*Key reference:* {% cite heiling2021b %}
