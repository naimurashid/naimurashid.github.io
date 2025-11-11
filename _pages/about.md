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
---

<section class="hero-panel">
  <div class="hero-panel__grid">
    <div class="hero-panel__content">
      <h1 class="hero-panel__title">Statistical innovation powering cancer precision medicine</h1>
      <p class="hero-panel__lead">
        Dr. Rashid is an associate professor in Biostatistics and Lineberger, associate director of the Biostatistics Shared Resource, co-director of the pancreatic and breast SPORE cores, and statistical lead for programs such as ARPA-H ADAPT and the Translational Breast Cancer Research Consortium.
      </p>
      <div class="hero-panel__metrics metrics-condensed">
        <div class="metric">
          <span class="metric__icon">🔬</span>
          <span class="metric__label"><strong>Methods:</strong> glmmPen, dlGLM, kinome models</span>
        </div>
        <div class="metric">
          <span class="metric__icon">🤝</span>
          <span class="metric__label"><strong>Trials:</strong> ARPA-H ADAPT, TBCRC, SPORE</span>
        </div>
        <div class="metric">
          <span class="metric__icon">🧬</span>
          <span class="metric__label"><strong>Molecular Profiling:</strong> PurIST, DeCAF, kinome</span>
        </div>
        <div class="metric">
          <span class="metric__icon">🎓</span>
          <span class="metric__label"><strong>Mentorship:</strong> T32, SPORE, ARPA-H trainees</span>
        </div>
      </div>
      <div class="hero-panel__cta">
        <a class="btn btn-outline-primary btn-lg" href="{{ '/assets/pdf/Naim.Rashid.cv.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
        <p class="hero-panel__microcopy mb-3">
          Lineberger members can email <a href="mailto:LCCC_BIOS@med.unc.edu">LCCC_BIOS@med.unc.edu</a> for curated consults or drop into the Wednesday Zoom clinic for rapid trial support.
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

### Mission &amp; Impact

<section class="mission-panel" aria-label="Mission and impact">
  <div class="mission-panel__intro">
    <p class="mission-panel__eyebrow">Purpose</p>
    <h3>We ship statistical methodology plus reproducible software so Gillings and Lineberger discoveries reach patients faster.</h3>
    <p class="mission-panel__summary">We develop the statistical frameworks, software, and trial infrastructure needed to move Gillings and Lineberger discoveries into evaluated interventions. Rigor, transparent code, and embedded collaborations keep our methods grounded in the real clinical questions disease-site teams are facing.</p>
  </div>
  <div class="mission-panel__grid">
    <article class="mission-panel__card">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-function"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Method innovation</p>
          <h4>Foundational methods</h4>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">CompDTUReg · Biostatistics 2024</span>
        <span class="mission-chip">dlGLM missing-data engines · JCGS 2024</span>
        <span class="mission-chip">glmmPen · Biometrics 2024</span>
      </div>
      <a class="mission-panel__link" href="/research/#methodology">Explore methodology →</a>
    </article>
    <article class="mission-panel__card">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-hospital"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Trial impact</p>
          <h4>Clinical translation</h4>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">PurIST · Clin Cancer Res 2020</span>
        <span class="mission-chip">Innocenti et al. · JCO 2024</span>
        <span class="mission-chip">Tumor-intrinsic kinome · Cancer Discovery 2025</span>
      </div>
      <a class="mission-panel__link" href="/projects/">View translational builds →</a>
    </article>
    <article class="mission-panel__card">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-code"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Open science</p>
          <h4>Software implementation</h4>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">epigraHMM · Biometrics 2022</span>
        <span class="mission-chip">glmmPen &amp; dlGLM · containerized HPC builds</span>
        <span class="mission-chip">NIMIWAE · Stat Biopharm Res 2024</span>
      </div>
      <a class="mission-panel__link" href="/software/">Browse toolkits →</a>
    </article>
    <article class="mission-panel__card mission-panel__card--alt">
      <div class="mission-panel__header">
        <span class="mission-panel__icon">
          <i class="ti ti-users-group"></i>
        </span>
        <div>
          <p class="mission-panel__badge">Collaboration</p>
          <h4>Partnership &amp; amplification</h4>
        </div>
      </div>
      <div class="mission-panel__chips">
        <span class="mission-chip">Fernandez-Martinez et al. · JAMA Oncol 2023</span>
        <span class="mission-chip">Nature Genet 2015 · Cancer Cell 2018 consortiums</span>
        <span class="mission-chip">Lineberger consults · ARPA-H ADAPT briefs</span>
      </div>
      <a class="mission-panel__link" href="/news/">See partner updates →</a>
    </article>
  </div>
</section>

### Research Pillars

<div class="pillar-grid">
  <article class="pillar-card">
    <h4>Methodology</h4>
    <p>Robust subtyping, penalized GLMMs, and generative-AI engines for translational data.</p>
    <a href="/research/#methodology" class="link-arrow">Explore →</a>
  </article>
  <article class="pillar-card">
    <h4>Translation</h4>
    <p>Bayesian adaptive platforms that weave ctDNA, imaging, and microbiome signals into trials.</p>
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
  "description": "Biostatistician leading adaptive precision-oncology trials, ARPA-H ADAPT analytics, and CLIA-certified PurIST diagnostics.",
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
