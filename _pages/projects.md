---
title: "Projects"
permalink: /projects/
author_profile: true
output: 
  html_document:
    toc: true
---

# Pancreatic cancer subtyping 

# Developing statistical tools for high-throughput epigenomics

![](https://raw.githubusercontent.com/naimurashid/naimurashid.github.io/master/files/k36.png)

High throughput sequencing experiments such as ChIP-seq, ATAC-seq, and others are commonly utilized to characterize the human epigenome with scale and resolution not seen in prior microarray-based applications.  A common goal in such experiments is to detection regions of the genome containing that are "enriched" for a particular type of epigenomic activity of interest, for example specific protein-DNA interactions such as transcription factor binding or histone modifications.  As the cost of sequencing has dropped, the experimental design of such experiments have become more complex and diverse, posing problems to methods optimized for specific data types or questions.  We develop efficient and robust methods that aim to more accurately detect regions of enrichment, regardless of the of experiment performed (short or broad enrichment), experimental design (multi-replicate and/or multi condition), or research questions (consensus, differential, or combinatiorial enrichment detection). We are in the early stages of developing deep learning models for single-cell epigenome experiments, such as single-cell ChIP-seq.  

**Repos developed**

1.  [ZIMHMM](https://github.com/plbaldoni/ZIMHMM): Consensus peak detection from multiple replicates 

1.  [mixNBHMM](https://github.com/plbaldoni/mixNBHMM):  Flexible detection of differential regions of enrichment from multi-sample, multi-condition epigenomic experiments (ChIP-seq, ATAC-seq, DNase-seq, etc.).  Detection of combinational patterns of multiple types of epigenomic processes in the same sample or condition (chromatin state segmentation).

**Related publications:**

1.  P. L. Baldoni, **N.U. Rashid**, and J. G. Ibrahim. Improved detection of epigenomic marks with mixed effects hidden markov models. Biometrics, 2019 

1. Y.-Y. Chiou, Y. Yang, **N.U. Rashid**, R. Ye, C. P. Selby, and A. Sancar. Mammalian period represses and de-represses transcription by displacing clock-bmal1 from promoters in a cryptochrome-dependent manner. Proceedings of the National Academy of Sciences, 113(41):E6072-E6079, 2016

1.  **N.U. Rashid**, W. Sun, and J. G. Ibrahim. Some statistical strategies for dae-seq data analysis: variable selection and modeling dependencies among observations. Journal of the American Statistical Association, 109(505):78-94, 2014 

1. B. Bernstein, E. Birney, I. Dunham, E. Green, C. Gunter, M. Snyder, et al. An integrated encyclopedia of dna elements in the human genome. Nature, 489(7414):57, 2012

1.  **N.U. Rashid**, P. G. Giresi, J. G. Ibrahim, W. Sun, and J. D. Lieb. Zinba integrates local covariates with dna-seq data to identify broad and narrow regions of enrichment, even within amplified genomic regions. Genome biology, 12(7):R67, 2011

# Multi-study replicability of prediction models

# Unsupervised clustering of RNA-seq data

