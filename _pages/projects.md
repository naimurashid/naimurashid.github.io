---
title: "Projects"
permalink: /projects/
author_profile: true
---

* [Pancreatic cancer subtyping](#panc)
* [Statistical tools for high-throughput epigenomics](#epi)

<a name="panc"></a>

# Pancreatic cancer subtyping 
![](https://raw.githubusercontent.com/naimurashid/naimurashid.github.io/master/files/purist.png)

In 2015, the [Yeh lab](https://unclineberger.org/yehlab/) at UNC Lineberger proposed a novel [two subtype](https://www.nature.com/articles/ng.3398) gene expression-based molecular classification system, consisting of the "basal-like" and "classical" subtypes, faciliating “precision medicine” approaches in pancreatic cancer.  Multiple subtyping systems for pancreatic cancer have been also proposed, and therefore consensus regarding subtypes for clinical decision-making has been elusive. 

In a recent evaluation of existing subtyping systems in 7 clinical validation datasets, we found that the two-subtype system best explains survival outcomes and treatment response in a replicable manner across studies. We also show that basal-like patients are highly resistant to common first-line therapy FOLFIRINOX, suggesting alternative therapies for such patients up front.  

Building on these results, as well as concepts from [prior work](https://www.tandfonline.com/doi/abs/10.1080/01621459.2019.1671197), we have developed a robust classifier PurIST to predict pancreatic cancer subtype in new patients.  This method is robust to normalization method, gene expression platform (NanoSting, RNA-seq), and sample collection process used (FFPE, FNA), and is highly accurate across a range of conditions.  PurIST is currently undergoing CLIA certification for use in several upcoming clinical trials. 

**Github Repos**

1.  [PurIST](https://github.com/naimurashid/PurIST): A clinically robust, single-sample classifier for tumor subtyping in pancreatic cancer.  PurIST is for research purposes only and is NOT available for commercial use.  To access PurIST please contact us with your github ID.  

**Related publications:**

1.  **N.U. Rashid**, X. L. Peng, C. Jin, R. A. Moffitt, K. E. Volmar, B. A. Belt, R. Z. Panni, T. M. Nywening, S. G. Herrera1, K. J. Moore1, S. G. Hennessey, A. B. Morrison, R. Kawalerski, A. Nayyar, A. E. Chang, B. Schmidt, H. J. Kim, D. C. Linehan, and J. J. Yeh. Purity independent subtyping of tumors (PurIST), a clinically robust, single-sample classifier for tumor subtyping in pancreatic cancer. Clinical Cancer Research, In Press, 2019

1.  R. A. Moffitt,  J. J. Yeh, and **N.U. Rashid**. Methods and compositions for prognostic and/or diagnostic subtyping of pancreatic cancer. [US 20170233827A1](https://patentimages.storage.googleapis.com/3c/ff/58/788c66082b621b/US20170233827A1.pdf), United States Patent and Trademark Office, 17 August 2017.

1.  R. A. Moffitt, R. Marayati, E. L. Flate, K. E. Volmar, S. G. H. Loeza, K. A. Hoadley, **N.U. Rashid**, L. A. Williams, S. C. Eaton, A. H. Chung, et al. Virtual microdissection identifies distinct tumor-and stroma-specific subtypes of pancreatic ductal adenocarcinoma. Nature genetics, 47(10):1168, 2015



<a name="epi"></a>

# Developing statistical tools for high-throughput epigenomics

![](https://raw.githubusercontent.com/naimurashid/naimurashid.github.io/master/files/k36.png)

High throughput sequencing experiments such as ChIP-seq, ATAC-seq, and others are commonly utilized to characterize the human epigenome fine resolution.  A common goal in such experiments is to detect regions of the genome that are "enriched" for a particular type of epigenomic activity of interest, for example specific protein-DNA interactions such as transcription factor binding or histone modifications.  

As the cost of sequencing has dropped, the experimental design of such experiments has become more complex and diverse, posing problems to exiting methods optimized for specific data types or research questions.  We develop efficient and robust methods to accurately detect regions of enrichment, regardless of the of experiment performed (short or broad enrichment), experimental design (multi-replicate and/or multi condition), or research question (peak calling, consensus peak calling, differential peak calling, or combinatiorial enrichment pattern detection). 

We are in the early stages of developing deep learning models for single-cell epigenome experiments, such as single-cell ChIP-seq.  

**Github Repos**

1.  [ZIMHMM](https://github.com/plbaldoni/ZIMHMM): Consensus peak detection from multiple replicates 

1.  [mixNBHMM](https://github.com/plbaldoni/mixNBHMM):  Flexible detection of broa and short differential regions of enrichment from multi-sample, multi-condition epigenomic experiments (ChIP-seq, ATAC-seq, DNase-seq, etc.).  Detection of local combinational patterns of multiple epigenomic processes in the same sample or condition (chromatin state segmentation).

**Related publications:**

1.  P. L. Baldoni, **N.U. Rashid**, and J. G. Ibrahim. Improved detection of epigenomic marks with mixed effects hidden markov models. Biometrics, 2019 

1. Y.-Y. Chiou, Y. Yang, **N.U. Rashid**, R. Ye, C. P. Selby, and A. Sancar. Mammalian period represses and de-represses transcription by displacing clock-bmal1 from promoters in a cryptochrome-dependent manner. Proceedings of the National Academy of Sciences, 113(41):E6072-E6079, 2016

1.  **N.U. Rashid**, W. Sun, and J. G. Ibrahim. Some statistical strategies for dae-seq data analysis: variable selection and modeling dependencies among observations. Journal of the American Statistical Association, 109(505):78-94, 2014 

1. B. Bernstein, E. Birney, I. Dunham, E. Green, C. Gunter, M. Snyder, et al. An integrated encyclopedia of dna elements in the human genome. Nature, 489(7414):57, 2012

1.  **N.U. Rashid**, P. G. Giresi, J. G. Ibrahim, W. Sun, and J. D. Lieb. Zinba integrates local covariates with dna-seq data to identify broad and narrow regions of enrichment, even within amplified genomic regions. Genome biology, 12(7):R67, 2011

# Multi-study replicability of prediction models

# Unsupervised clustering of RNA-seq data

