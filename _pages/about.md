---
layout: about
title: about
page-title: About
permalink: /
subtitle:

profile:
  name: Naim U. Rashid, PhD
  position:  Associate Professor <br />Department of Biostatistics<br />Gillings School of Global Public Health,<br /> Lineberger Comprehensive Cancer Center
  align: right
  image: prof.jpg
  image_circular: false # crops the image to make it circular
  address: >
    Lineberger 20-020 <br /> 450 West Drive <br /> University of North Carolina at Chapel Hill <br />Chapel Hill, NC, 27599

news: true # includes a list of news items
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
social_feed: true
hero_profile: true
---

<section class="hero-panel">
  <div class="hero-panel__grid">
    <div class="hero-panel__content">
      <p class="hero-panel__eyebrow">Gillings School of Global Public Health · Lineberger Comprehensive Cancer Center</p>
      <h1 class="hero-panel__title">Adaptive analytics powering UNC’s cancer breakthroughs</h1>
      <p class="hero-panel__lead">
        We design the statistical, AI, and trial infrastructures that move Gillings and Lineberger discoveries into patient-ready studies across breast, pancreatic, and precision oncology programs.
      </p>
      <div class="hero-panel__metrics">
        <div class="metric">
          <span class="metric__value">$28M</span>
          <span class="metric__label">ARPA-H ADAPT platform for metastatic breast cancer</span>
        </div>
        <div class="metric">
          <span class="metric__value">25</span>
          <span class="metric__label">NCI/NIH grants supported annually through the Lineberger Biostatistics Shared Resource</span>
        </div>
        <div class="metric">
          <span class="metric__value">50+</span>
          <span class="metric__label">peer-reviewed publications translating methods into oncology impact</span>
        </div>
      </div>
      <div class="hero-panel__cta">
        <a class="btn btn-primary btn-lg" href="mailto:LCCC_BIOS@med.unc.edu?subject=Consultation%20Request%20for%20Lineberger%20Biostatistics">Request a Lineberger consultation</a>
        <a class="btn btn-outline-secondary btn-lg" href="https://zoom.us/j/98595369470" target="_blank" rel="noopener">Join Wednesday drop-in (12–1 PM)</a>
      </div>
      <p class="hero-panel__note">
        Dr. Rashid is an <a href="https://sph.unc.edu/adv_profile/naim-rashid-phd/" target="_blank" rel="noopener">associate professor</a> with joint appointments in Biostatistics and Lineberger, Associate Director of the <a href="https://unclineberger.org/biostats/" target="_blank" rel="noopener">Biostatistics Shared Resource</a>, co-director of the pancreatic and breast cancer SPORE biostatistics cores, and statistical lead for national programs including ARPA-H ADAPT and the Translational Breast Cancer Research Consortium.
      </p>
    </div>
    <aside class="hero-panel__aside">
      <div class="hero-panel__logo-wrap">
        <img class="hero-panel__logo" src="{{ '/assets/img/RashidLabMainLogo2400x1800.jpeg' | relative_url }}" alt="Rashid Lab logo" />
      </div>
      <figure class="hero-panel__portrait-wrapper">
        <img class="hero-panel__portrait" src="{{ '/assets/img/' | append: page.profile.image | relative_url }}" alt="{{ page.profile.image_alt | default: page.profile.name }}" loading="lazy" decoding="async" />
      </figure>
      <div class="hero-panel__contact">
        <p class="hero-panel__name">{{ page.profile.name }}</p>
        <div class="hero-panel__position">{{ page.profile.position | markdownify | replace: '<p>', '' | replace: '</p>', '' }}</div>
        <div class="hero-panel__links">
          {% if page.profile.email %}
            <a href="mailto:{{ page.profile.email }}"><i class="fas fa-envelope"></i> {{ page.profile.email }}</a>
          {% endif %}
          {% if page.profile.phone %}
            <a href="tel:{{ page.profile.phone }}"><i class="fas fa-phone"></i> {{ page.profile.phone }}</a>
          {% endif %}
          {% if page.profile.website %}
            <a href="{{ page.profile.website }}" target="_blank" rel="noopener"><i class="fas fa-globe"></i> Website</a>
          {% endif %}
        </div>
        {% if page.profile.address %}
          <div class="hero-panel__address">{{ page.profile.address | markdownify | replace: '<p>', '' | replace: '</p>', '' }}</div>
        {% endif %}
      </div>
    </aside>
  </div>
</section>

### Gillings news spotlight

{% include gillings-news.liquid %}

### Research pillars

- **Methodological innovation.** Rashid’s lab advances robust subtyping, high-dimensional mixed models, and adaptive learning engines for genomics, epigenomics, and real-world data. Tools such as the PurIST pancreatic classifier and the `glmmPen` R package translate directly into diagnostic and trial workflows.
- **Translational partnerships.** Collaborations with UNC Lineberger clinicians and national consortia integrate longitudinal ctDNA, imaging, and microbiome assays into Bayesian adaptive trials, notably the $28M ARPA-H ADAPT platform and Department of Defense pancreatic cancer initiatives.
- **Clinical trial leadership.** Rashid serves as statistician of record or analytics lead for multi-institutional studies including HARMONY, InCITe, and SPORE projects, ensuring rigorous design, interim monitoring, and regulatory-aligned analysis plans.
- **Training and mentorship.** Through BIOS 735 and sustained one-on-one mentoring, Rashid prepares doctoral students and postdocs who now lead analytics teams at institutions such as Dana-Farber, GSK, and UNC Lineberger; lab alumni maintain active collaborations on methods, software, and trial design.

### Leadership & service

Rashid co-directs the biostatistics and bioinformatics cores for the UNC pancreatic and breast cancer SPOREs, sits on the Translational Breast Cancer Research Consortium Statistical Working Group, and serves on the V Foundation Scientific Advisory Committee. These roles position him to steward innovative methodology into NCI-funded programs and national cooperative group studies.

**Biostatistics Support for Lineberger Members**

Email [LCCC_BIOS@med.unc.edu](mailto:LCCC_BIOS@med.unc.edu) to schedule a consult with our statisticians. We also host a virtual drop-in clinic every Wednesday from 12–1 PM; join [via Zoom](https://zoom.us/j/98595369470). Additional details about the Lineberger Biostatistics Shared Resource are available [here](https://unclineberger.org/biostats/).

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
