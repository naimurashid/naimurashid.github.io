---
layout: about
title: About
page-title: About
permalink: /
subtitle:

profile:
  name: Naim U. Rashid, PhD
  position: >
    Associate Professor, Department of Biostatistics <br />
    Gillings School of Global Public Health &amp; Lineberger Comprehensive Cancer Center
  align: right
  image: prof.jpg
  image_circular: false # crops the image to make it circular
  address: >
    Lineberger 20-020 <br /> 450 West Drive <br /> University of North Carolina at Chapel Hill <br />Chapel Hill, NC, 27599
  website: https://naimurashid.github.io
  email: naim@unc.edu

news: true # includes a list of news items
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
social_feed: true
hero_profile: true
talks_intro: >
  Recent seminar topics include adaptive oncology statistics, biomarker-driven trial platforms, and AI-assisted decision tools. Talks are typically 45–60 minutes and can be tailored for biostatistics, oncology, or data science audiences. I am happy to meet with students and participate in chalk talks or lab meetings.
talks:
  - title: "Bayesian adaptive methods for metastatic breast cancer platforms"
    venue: "ARPA-H ADAPT Analytics Summit"
    location: "Washington, DC & virtual"
    date: "May 2025"
    description: "Presented reinforcement learning, platform-level borrowing, and LLM tools for the ADAPT network."
  - title: "Integrating tumor and stroma to guide precision oncology"
    venue: "James E. Grizzle Distinguished Alumnus Lecture, UNC Gillings"
    location: "Chapel Hill, NC"
    date: "October 2024"
    description: "Presented multi-omic models that pair PurIST and kinome readouts with stromal remodeling signals to prioritize translational studies."
  - title: "STATGEN keynote: multi-omic signatures for pancreatic cancer trials"
    venue: "STATGEN Conference, University of Pittsburgh"
    location: "Pittsburgh, PA"
    date: "June 2024"
    description: "Presented adaptive genomics pipelines—DeCAF, PurIST, and immune deconvolution—for basket trial applications."
---

<section class="hero-panel">
  <div class="hero-panel__grid">
    <div class="hero-panel__content">
      <h1 class="hero-panel__title">Statistical methods for cancer precision medicine</h1>
      <p class="hero-panel__lead">
        Dr. Rashid is an associate professor in Biostatistics at the Gillings School and Lineberger Comprehensive Cancer Center. He serves as associate director of the Biostatistics Shared Resource, co-director of the pancreatic and breast SPORE biostatistics cores, Co-PI and statistical lead for ARPA-H ADAPT, and statistical lead for the Translational Breast Cancer Research Consortium.
      </p>
      <div class="hero-panel__metrics metrics-condensed">
        <div class="metric">
          <span class="metric__label"><strong>Methods:</strong> glmmPen, dlGLM, PurIST</span>
        </div>
        <div class="metric">
          <span class="metric__label"><strong>Translation:</strong> CLIA-certified diagnostic, 2 US patents</span>
        </div>
        <div class="metric">
          <span class="metric__label"><strong>Trials:</strong> ARPA-H ADAPT (Co-PI), TBCRC, SPORE</span>
        </div>
        <div class="metric">
          <span class="metric__label"><strong>Leadership:</strong> Dual NCI SPORE core co-director</span>
        </div>
      </div>
      <div class="hero-panel__cta">
        <a class="btn btn-outline-primary btn-lg" href="{{ '/assets/pdf/Naim.Rashid.cv.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
        <p class="hero-panel__microcopy mb-3">
          Lineberger members can email <a href="mailto:LCCC_BIOS@med.unc.edu">LCCC_BIOS@med.unc.edu</a> for consultations or join the Wednesday Zoom office hours for trial support.
        </p>
        <a class="btn btn-primary btn-lg" href="mailto:LCCC_BIOS@med.unc.edu?subject=Consultation%20Request%20for%20Lineberger%20Biostatistics">Request a Lineberger consultation</a>
        <a class="btn btn-outline-secondary btn-lg" href="https://zoom.us/j/98595369470" target="_blank" rel="noopener">Join Wednesday drop-in (12–1 PM)</a>
      </div>
    </div>
    <aside class="hero-panel__aside">
      <figure class="hero-panel__portrait-wrapper">
        <img class="hero-panel__portrait" src="{{ '/assets/img/' | append: page.profile.image | relative_url }}" alt="{{ page.profile.image_alt | default: page.profile.name }}" loading="lazy" decoding="async" />
      </figure>
      <div class="hero-panel__contact">
        <p class="hero-panel__name">{{ page.profile.name }}</p>
        <div class="hero-panel__position">{{ page.profile.position | markdownify | replace: '<p>', '' | replace: '</p>', '' }}</div>
        {% if page.profile.address %}
          <div class="hero-panel__address">{{ page.profile.address | markdownify | replace: '<p>', '' | replace: '</p>', '' }}</div>
        {% endif %}
        <div class="hero-panel__links hero-panel__links--grid">
          {% if page.profile.email %}
            <a class="hero-panel__link" href="mailto:{{ page.profile.email }}" title="Email"><i class="ti ti-mail"></i><span>Email</span></a>
          {% endif %}
          <a class="hero-panel__link" href="https://sph.unc.edu/adv_profile/naim-rashid-phd/" target="_blank" rel="noopener" title="UNC SPH Profile"><i class="ti ti-briefcase"></i><span>UNC SPH</span></a>
          <a class="hero-panel__link" href="https://bsky.app/profile/naimurashid.bsky.social" target="_blank" rel="noopener" title="Bluesky"><i class="ti ti-brand-bluesky"></i><span>Bluesky</span></a>
          <a class="hero-panel__link" href="https://twitter.com/naimurashid" target="_blank" rel="noopener" title="X (Twitter)"><i class="ti ti-brand-twitter"></i><span>X</span></a>
          <a class="hero-panel__link" href="https://github.com/naimurashid" target="_blank" rel="noopener" title="GitHub"><i class="ti ti-brand-github"></i><span>GitHub</span></a>
          <a class="hero-panel__link" href="https://scholar.google.com/citations?user=3Cz_lcEAAAAJ" target="_blank" rel="noopener" title="Google Scholar"><i class="ti ti-brand-google"></i><span>Scholar</span></a>
        </div>
      </div>
    </aside>
  </div>
</section>

### Research Overview

<section class="mission-panel" aria-label="Research overview">
  <div class="mission-panel__intro">
    <p class="mission-panel__eyebrow">Purpose</p>
    <h3>We develop statistical methods and software that enable clinical translation of biomarker discoveries, from methodological innovation through CLIA-certified diagnostic tools.</h3>
    <p class="mission-panel__summary">Our lab collaborates with disease teams to develop methodology, software, and analytical frameworks for adaptive platforms, diagnostics, and clinical decision support tools. As associate director of the Lineberger Biostatistics Shared Resource, our team supports design and analysis for 40+ cancer center investigators and clinical trials annually.</p>
  </div>
  <div class="mission-panel__grid">
    <article class="mission-panel__card">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-function"></i>
        </span>
        <div>
          <p class="mission-panel__badge">AI &amp; Stat. Methods</p>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">CompDTUReg for isoform-level RNA testing</span>
        <span class="mission-chip">dlGLM deep-learning GLMs for missing omics</span>
        <span class="mission-chip">glmmPen penalties for correlated biomarkers</span>
      </div>
      <a class="mission-panel__link" href="/research/#methodology">Explore methodology →</a>
    </article>
    <article class="mission-panel__card">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-hospital"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Trial Applications</p>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">PurIST subtype classification for GI tumors</span>
        <span class="mission-chip">Kinome profiling for pancreatic cancer</span>
        <span class="mission-chip">HER2 residual-risk modeling for neoadjuvant trials</span>
      </div>
      <a class="mission-panel__link" href="/projects/">View translational projects →</a>
    </article>
    <article class="mission-panel__card">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-code"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Software</p>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">epigraHMM for multi-condition epigenomics</span>
        <span class="mission-chip">glmmPen + dlGLM Docker stacks for shared HPC</span>
        <span class="mission-chip">NIMIWAE imputation methods for registries</span>
      </div>
      <a class="mission-panel__link" href="/software/">Browse software packages →</a>
    </article>
    <article class="mission-panel__card mission-panel__card--alt">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-users-group"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Collaboration</p>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">Lineberger Biostatistics Shared Resource</span>
        <span class="mission-chip">ARPA-H ADAPT analytics for PSRC/NCI teams</span>
        <span class="mission-chip">TBCRC &amp; V Foundation cooperative groups</span>
      </div>
      <a class="mission-panel__link" href="/news/">View news updates →</a>
    </article>
  </div>
</section>

### Collaboration-Driven Methodology

<section class="page-section page-section--methodology">
  <h2>Embedded Clinical Partnerships</h2>
  <p class="section-lede">
    Our statistical methods emerge from embedded clinical partnerships rather than abstract theory. Working directly with UNC Lineberger oncologists, we identify unmet analytical needs in real trials and translate them into rigorous, reproducible software solutions.
  </p>
  <p>
    This approach ensures methodological innovations address practical challenges in precision oncology—from single-sample tumor subtyping to adaptive platform designs that integrate serial biomarker data. Close collaboration with disease teams allows us to develop tools that are both statistically principled and clinically actionable.
  </p>
</section>

### Clinical Impact & Translation

<section class="page-section">
  <div class="focus-grid">
    <article class="focus-card focus-card--featured">
      <p class="focus-card__badge">Clinical Translation</p>
      <h3>PurIST Diagnostic: From Statistical Method to Clinical Tool</h3>
      <p>The PurIST (Purity Independent Subtyping of Tumors) classifier represents a complete translational research arc—from methodological development to clinical deployment:</p>
      <ul>
        <li><strong>2020</strong> — Published classification method (<em>Clinical Cancer Research</em>)</li>
        <li><strong>2021-2024</strong> — Two US patents issued</li>
        <li><strong>2024</strong> — Analytical validation completed (<em>Journal of Molecular Diagnostics</em>)</li>
        <li><strong>2024</strong> — CLIA-certification achieved for clinical use</li>
        <li><strong>Present</strong> — Licensed to GeneCentric and Tempus Diagnostics; actively used in clinical trials</li>
      </ul>
      <p>PurIST is one of few single-sample, platform-independent tumor subtyping tools to achieve CLIA certification and clinical deployment.</p>
      <div class="focus-card__chips">
        <span class="focus-chip">2 US Patents (2021-2024)</span>
        <span class="focus-chip">CLIA certified (2024)</span>
        <span class="focus-chip">Licensed to GeneCentric & Tempus</span>
      </div>
    </article>
  </div>
</section>

### Recognition & Leadership

<section class="page-section">
  <div class="focus-grid">
    <article class="focus-card">
      <p class="focus-card__badge">Recent Honors</p>
      <h4>Awards & Recognition</h4>
      <ul>
        <li><strong>2025</strong> — Gillings Research Excellence Award</li>
        <li><strong>2024</strong> — James E. Grizzle Distinguished Alumnus Award</li>
        <li><strong>2023</strong> — Teaching Innovation Award, UNC Gillings</li>
      </ul>
    </article>
    <article class="focus-card">
      <p class="focus-card__badge">National Leadership</p>
      <h4>Collaborative Roles</h4>
      <ul>
        <li>Co-Director, Breast Cancer SPORE Biostatistics Core (2024-)</li>
        <li>Co-Director, Pancreatic Cancer SPORE Quantitative Sciences Core (2022-)</li>
        <li>Nature Medicine Statistical Advisory Panel (2024-)</li>
        <li>Associate Editor, Annals of Applied Statistics (2023-)</li>
        <li>V Foundation Scientific Advisory Board (2023-)</li>
        <li>TBCRC Statistical Working Group (2017-)</li>
      </ul>
    </article>
  </div>
</section>

### Recent Invited Talks

<section class="talks-section" aria-label="Recent invited talks">
  <div class="talks-section__intro">
    <p class="talks-section__eyebrow">Recent Seminar Topics</p>
    <p>{{ page.talks_intro }}</p>
    <a class="btn btn-outline-primary" href="mailto:naim@unc.edu?subject=Seminar%20Invitation%20for%20Naim%20Rashid">Invite Dr. Rashid to speak</a>
  </div>
  <div class="talks-section__list">
    {% for talk in page.talks %}
      <article class="talk-card">
        <div class="talk-card__meta">
          <span class="talk-card__date">{{ talk.date }}</span>
          <span class="talk-card__venue">{{ talk.venue }}</span>
          {% if talk.location %}
            <span class="talk-card__location">{{ talk.location }}</span>
          {% endif %}
        </div>
        <h4>{{ talk.title }}</h4>
        <p>{{ talk.description }}</p>
        {% if talk.slides %}
          <div class="talk-card__actions">
            <a class="btn btn-sm btn-outline-secondary" href="{{ talk.slides }}" target="_blank" rel="noopener">View slides</a>
          </div>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</section>

### Research Pillars

<div class="pillar-grid">
  <article class="pillar-card">
    <h4>Methodology</h4>
    <p>Robust subtyping, penalized GLMMs, and generative-AI methods for translational data.</p>
    <a href="/research/#methodology" class="link-arrow">Explore →</a>
  </article>
  <article class="pillar-card">
    <h4>Translation</h4>
    <p>Bayesian adaptive platforms integrating ctDNA, imaging, and microbiome data.</p>
    <a href="/research/#translation" class="link-arrow">Explore →</a>
  </article>
  <article class="pillar-card">
    <h4>Trial Leadership</h4>
    <p>Statistics lead for ARPA-H ADAPT, TBCRC, SPORE, and DOD initiatives.</p>
    <a href="/research/#trials" class="link-arrow">Explore →</a>
  </article>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Naim U. Rashid",
  "jobTitle": "Associate Professor of Biostatistics",
  "description": "Biostatistician developing methods for adaptive precision-oncology trials, ARPA-H ADAPT analytics, and CLIA-certified PurIST diagnostics.",
  "image": "{{ '/assets/img/prof.jpg' | relative_url | absolute_url }}",
  "url": "{{ '/' | absolute_url }}",
  "email": "mailto:naim@unc.edu",
  "telephone": "+1-919-966-8150",
  "affiliation": [
    {
      "@type": "CollegeOrUniversity",
      "name": "UNC Gillings School of Global Public Health",
      "url": "https://sph.unc.edu/"
    },
    {
      "@type": "ResearchOrganization",
      "name": "UNC Lineberger Comprehensive Cancer Center",
      "url": "https://unclineberger.org/"
    }
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "Rashid Lab",
    "url": "{{ '/' | absolute_url }}"
  },
  "sameAs": [
    "https://scholar.google.com/citations?user=3Cz_lcEAAAAJ",
    "https://www.linkedin.com/in/naim-rashid-a767aba/",
    "https://bsky.app/profile/naimurashid.bsky.social",
    "https://twitter.com/naimurashid",
    "https://github.com/naimurashid"
  ]
}
</script>

<!-- Default Statcounter code for Naimurashid.github.io
https://naimurashid.github.io/ -->
<script type="text/javascript">
var sc_project=12163716;  
var sc_invisible=1; 
var sc_security="51a4fa6c"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="Web Analytics
Made Easy - Statcounter" href="https://statcounter.com/"
target="_blank"><img class="statcounter"
src="https://c.statcounter.com/12163716/0/51a4fa6c/1/"
alt="Web Analytics Made Easy - Statcounter"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code -->
