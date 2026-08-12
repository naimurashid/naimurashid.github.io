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
talks:
  - title: "Adaptive Trial Design for the RAS-Inhibitor Era: Combinations, Resistance, and Biomarker-Guided Therapy"
    venue: "NCI GI SPORE Meeting"
    date: "June 2026"
    slides: "https://rashidlab.github.io/talks/2026-gispore-ras-trials-deck/ras-era-adaptive-trials.html"
    description: "Adaptive and biomarker-guided designs for RAS-inhibitor combination trials: dose optimization, resistance-aware randomization, and real-time biomarker integration in GI cancers."
  - title: "Staying in the Driver's Seat: Calibrating AI Use in Statistical Research, Training, and Practice"
    venue: "StatsUp.AI Webinar, American Statistical Association"
    date: "May 2026"
    slides: "https://rashidlab.github.io/talks/2026-04-25-statsupai-staying-in-drivers-seat-deck/staying-in-drivers-seat-v3.html"
    resources: "https://github.com/naimurashid/staying-in-drivers-seat-resources"
    description: "Practical guardrails and habits for using AI in statistical research while keeping scientific ownership. The companion repository includes templates, checklists, and the full lab guide, free to adapt and use."
  - title: "V Scholar Summit Biostatistics Panel"
    venue: "V Foundation for Cancer Research Summit"
    location: "Cary, NC"
    date: "2026"
    description: "Invited panelist on biostatistics and quantitative methods in translational cancer research for V Scholar awardees."
  - title: "When Biomarkers, Assays, and Protocols Co-evolve: Cross-platform Reproducibility, Validation, and Adaptive Design"
    venue: "FDA CDRH OSEL-wide AI Seminar (webinar)"
    date: "2026"
    description: "Cross-platform reproducibility and validation of biomarker assays, and adaptive design considerations when biomarkers, assays, and protocols evolve together during a trial."
  - title: "Uncertainty Quantification for Biomarker Prioritization: From Passive Monitoring to N-of-Some Pilot Trials"
    venue: "ARPA-H ADAPT Program Meeting"
    location: "Phoenix, AZ"
    date: "2026"
    description: "Quantifying uncertainty when prioritizing candidate biomarkers for the ADAPT platform, spanning passive monitoring through N-of-Some pilot trial designs."
  - title: "Leveraging Artificial Intelligence in Modern Biomarker-Driven Clinical Trial Design: the ARPA-H ADAPT Program"
    venue: "Lineberger Data Science Symposium, University of North Carolina"
    location: "Chapel Hill, NC"
    date: "2026"
    description: "How AI and adaptive statistical design come together in the ARPA-H ADAPT metastatic breast cancer platform."
  - title: "Leveraging Artificial Intelligence in Modern Biomarker-Driven Clinical Trial Design: the ARPA-H ADAPT Program"
    venue: "Division of Quantitative Sciences, Johns Hopkins Kimmel Cancer Center"
    location: "Baltimore, MD"
    date: "October 2025"
    description: "Bayesian borrowing, RL-based allocation, and real-time monitoring for the ARPA-H ADAPT metastatic breast cancer platform."
  - title: "Designing N-of-1 Trials for the ARPA-H ADAPT Program"
    venue: "ARPA-H ADAPT Program Meeting"
    location: "Washington, DC"
    date: "2025"
    description: "Design principles for N-of-1 trials within the ADAPT platform, including within-patient decision rules and biomarker-guided treatment switching."
  - title: "Replicability, semi-supervised learning and generative AI: recent statistical work in cancer biostatistics"
    venue: "James E. Grizzle Distinguished Alumnus Lecture, UNC Gillings"
    location: "Chapel Hill, NC"
    date: "October 2024"
    description: "Semi-supervised NMF for replicable pancreatic subtypes, plus generative-AI synthesis of clinical trial data preserving subgroup effects."
  - title: "Joint Nonnegative Matrix Factorization and Survival Modeling to Select Clinically-relevant Gene Signatures"
    venue: "STATGEN 2024 Conference (Invited Talk)"
    location: "Pittsburgh, PA"
    date: "June 2024"
    description: "A joint NMF–survival objective for selecting pancreatic cancer survival signatures, beating two-stage approaches on TCGA / ICGC."
---

<section class="hero-panel hero-panel--academic">
  <div class="hero-panel__grid">
    <div class="hero-panel__content">
      <p class="hero-panel__tagline">Statistical methods and software for precision oncology</p>
      <p class="hero-panel__lead">
        I am an associate professor in the <a href="https://sph.unc.edu/bios/biostatistics/">Department of Biostatistics</a> at the <a href="https://sph.unc.edu/">UNC Gillings School of Global Public Health</a>, with a joint appointment at the <a href="https://unclineberger.org/">Lineberger Comprehensive Cancer Center</a>.
      </p>

      <p class="hero-panel__lead">
        Our lab develops statistical and machine learning methods for precision oncology, including adaptive clinical trial designs that integrate real-time biomarker data, deep learning methods for tumor subtyping and missing data, and open-source R packages for cancer genomics.
      </p>
      <p class="hero-panel__interests">
        <strong>Research interests:</strong> adaptive trial design, Bayesian methods, nonnegative matrix factorization, deep learning, missing data, cancer genomics, precision oncology
      </p>
      <p class="hero-panel__education">
        <strong>Training:</strong> Postdoctoral fellow, Harvard School of Public Health &amp; Dana-Farber Cancer Institute (2014). PhD, Biostatistics, UNC Chapel Hill (2013). BS, Duke University (2006).
      </p>
      <p class="hero-panel__links-inline">
        <a href="/research/">Research</a> ·
        <a href="{{ '/assets/pdf/Naim.Rashid.cv.pdf' | relative_url }}" target="_blank" rel="noopener">CV (PDF)</a> ·
        <a href="/publications/">Publications</a>
      </p>
      <section class="hero-panel__recent" aria-label="Recent News">
        <p class="hero-panel__recent-label">Recent News</p>
        <ul class="hero-panel__recent-list">
          {% assign hp_recent = site.news | reverse %}
          {% assign hp_shown = 0 %}
          {% for hp_item in hp_recent %}
            {% if hp_shown >= 3 %}{% break %}{% endif %}
            {% if hp_item.inline %}{% continue %}{% endif %}
            <li class="hero-panel__recent-item">
              <span class="hero-panel__recent-date">{{ hp_item.date | date: '%m / %Y' }}</span>
              {% if hp_item.url %}
                <a class="hero-panel__recent-title" href="{{ hp_item.url | relative_url }}">{{ hp_item.title | truncate: 90 }}</a>
              {% else %}
                <span class="hero-panel__recent-title">{{ hp_item.title | truncate: 90 }}</span>
              {% endif %}
            </li>
            {% assign hp_shown = hp_shown | plus: 1 %}
          {% endfor %}
        </ul>
      </section>
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

## Representative Translational Work

Pancreatic oncologists at UNC Lineberger needed a way to classify individual tumors into molecular subtypes from a single biopsy, without requiring a reference cohort. We developed PurIST, a rank-based classifier that handles tumor purity variation, validated it across international cohorts, and worked with the Yeh laboratory to bring it through CLIA certification. It is currently being evaluated prospectively in several clinical trials and has been licensed to Tempus, making it available at hospitals nationwide. That cycle—clinical need, statistical method, validated software, deployed tool—is how most of our projects begin.

## Current Funding

- MPI, ARPA-H ADAPT program grant (metastatic breast cancer)
- MPI, NCI U01 (pancreatic cancer)
- PI, DOD-funded LLM clinical trial navigation tool

See [full funding portfolio](/funding/) for details.

## Selected Awards

<ul class="award-list">
  <li><span class="award-year">2025</span> Gillings Research Excellence Award</li>
  <li><span class="award-year">2024</span> James E. Grizzle Distinguished Alumnus Award</li>
  <li><span class="award-year">2023</span> Teaching Innovation Award, UNC Gillings</li>
  <li><span class="award-year">2021</span> Delta Omega Faculty Award, Gillings School of Global Public Health</li>
  <li><span class="award-year">2017</span> IBM and R.J. Reynolds Junior Faculty Development Award, UNC-CH</li>
  <li><span class="award-year">2013</span> Barry H. Margolin Dissertation Award for best doctoral dissertation</li>
</ul>

## Service & Leadership

- **Breast SPORE Core B Co-Director** (P50-CA058223, 2024–2029)
- **Pancreatic SPORE Core C Co-Director** (P50-CA257911, 2022–2027)
- **Lineberger LCCC Biostatistics Shared Resource Associate Director** (P30-CA016086)
- Nature Medicine Statistical Advisory Panel (2023–)
- Associate Editor, *Annals of Applied Statistics* (2022–)
- V Foundation Scientific Advisory Board (2023–)
- TBCRC Statistical Working Group (2017–)
- Faculty Executive Committee, Department of Biostatistics (2025–)
- Gillings Research Council (2023–)
- Chair, Applied Doctoral Exam Committee, Department of Biostatistics (2015–)

## Recent Invited Talks

<section class="talks-section" aria-label="Recent invited talks">
  <div class="talks-section__list">
    {% for talk in page.talks %}
      {% unless talk.slides %}{% continue %}{% endunless %}
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
        <div class="talk-card__actions">
          <a class="btn btn-sm btn-outline-secondary" href="{{ talk.slides }}" target="_blank" rel="noopener">View slides</a>
          {% if talk.resources %}
            <a class="btn btn-sm btn-outline-secondary" href="{{ talk.resources }}" target="_blank" rel="noopener">Companion resources</a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>

  <h4 class="talks-section__more-label">Other Recent Invited Talks</h4>
  <ul class="award-list">
    {% for talk in page.talks %}
      {% if talk.slides %}{% continue %}{% endif %}
      <li><span class="award-year">{{ talk.date | split: ' ' | last }}</span> {{ talk.title }} &middot; {{ talk.venue }}{% if talk.location %}, {{ talk.location }}{% endif %}</li>
    {% endfor %}
  </ul>
</section>


<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Naim U. Rashid",
  "givenName": "Naim",
  "familyName": "Rashid",
  "honorificSuffix": "PhD",
  "jobTitle": "Associate Professor of Biostatistics",
  "description": "Biostatistician developing methods for cancer genomics, machine learning, and adaptive clinical trials. Expertise in AI, precision oncology, clinical trial design, statistical computing, and translational research.",
  "image": "{{ '/assets/img/prof.jpg' | relative_url | absolute_url }}",
  "url": "{{ '/' | absolute_url }}",
  "email": "mailto:naim@unc.edu",
  "telephone": "+1-919-966-8150",
  "alumniOf": [
    {
      "@type": "CollegeOrUniversity",
      "name": "Harvard School of Public Health",
      "url": "https://www.hsph.harvard.edu/"
    },
    {
      "@type": "CollegeOrUniversity",
      "name": "University of North Carolina at Chapel Hill",
      "url": "https://www.unc.edu/"
    }
  ],
  "affiliation": [
    {
      "@type": "CollegeOrUniversity",
      "name": "UNC Gillings School of Global Public Health",
      "department": "Department of Biostatistics",
      "url": "https://sph.unc.edu/"
    },
    {
      "@type": "ResearchOrganization",
      "name": "UNC Lineberger Comprehensive Cancer Center",
      "url": "https://unclineberger.org/"
    }
  ],
  "memberOf": [
    {
      "@type": "Organization",
      "name": "Translational Breast Cancer Research Consortium",
      "url": "https://tbcrc.org/"
    },
    {
      "@type": "Organization",
      "name": "Nature Medicine Statistical Advisory Panel"
    }
  ],
  "knowsAbout": [
    "Biostatistics",
    "Cancer Genomics",
    "Machine Learning",
    "Artificial Intelligence",
    "Precision Medicine",
    "Clinical Trials",
    "Adaptive Clinical Trials",
    "Clinical Trial Design",
    "Bayesian Adaptive Trials",
    "Platform Trials",
    "Statistical Computing",
    "Deep Learning",
    "RNA-seq Analysis",
    "Epigenomics",
    "Tumor Subtyping",
    "Penalized Regression",
    "Missing Data Methods",
    "Bayesian Statistics"
  ],
  "award": [
    "Gillings Research Excellence Award (2025)",
    "James E. Grizzle Distinguished Alumnus Award (2024)",
    "Teaching Innovation Award, UNC Gillings (2023)"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "Rashid Lab",
    "url": "{{ '/' | absolute_url }}",
    "description": "Statistical methods research lab focused on cancer genomics, AI, and precision oncology"
  },
  "sameAs": [
    "https://scholar.google.com/citations?user=3Cz_lcEAAAAJ",
    "https://www.linkedin.com/in/naim-rashid-a767aba/",
    "https://orcid.org/0000-0001-5796-0836",
    "https://bsky.app/profile/naimurashid.bsky.social",
    "https://twitter.com/naimurashid",
    "https://github.com/naimurashid",
    "https://sph.unc.edu/adv_profile/naim-rashid-phd/"
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
