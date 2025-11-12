---
layout: page
permalink: /team.html
title: Team
page-title: Team
description: Current and former group members
nav: true
nav_order: 2
nav_rank: 2
---

<section class="page-section page-intro">
  <p class="page-intro__eyebrow">Overview</p>
  <h2 class="page-intro__title">Lab Ecosystem</h2>
  <p class="page-intro__lede">
    Gillings biostatisticians and Lineberger clinicians partner here to ship adaptive trials, biomarker pipelines, and patient navigation AI. Alumni now lead analytics at Dana-Farber, GSK, and UNC, while current trainees drive liquid-biopsy transfer learning and microbiome multi-omics.
  </p>
  <ul>
    <li>40+ oncology collaborations across Lineberger disease groups</li>
    <li>NIH/ARPA-H trainees embedded with SPORE, TBCRC, and ADAPT</li>
    <li>Consulting, trial design, and software engineering under one team</li>
  </ul>
</section>

<section class="page-section">
  <h2 class="section-heading">Prospective PhD Students</h2>
  <p class="mb-2">Recruiting PhD students for Fall 2026 who want to build:</p>
  <p class="chips mb-3">Adaptive platforms · biomarker genomics · missing-data ML · precision oncology software</p>
  <ul>
    <li><strong>Apply by Dec 10, 2025:</strong> Mention “Rashid Lab – adaptive oncology statistics” in your statement.</li>
    <li><strong>January 2026:</strong> Invite-only Q&amp;A with current trainees (virtual, travel support for visit weekend).</li>
    <li><strong>Funding:</strong> NIH SPORE, ARPA-H ADAPT, and Lineberger traineeships with guaranteed summer support.</li>
  </ul>
  <p>Send a 1-page research blurb, CV, and unofficial transcript to <a href="mailto:naim@unc.edu?subject=Prospective%20PhD%20-%20Rashid%20Lab">naim@unc.edu</a>; note any clinical collaborations or large-scale data experience so we can match you to active projects quickly.</p>
  <p class="mb-0"><strong>Contact</strong>: <a href="mailto:naim@unc.edu">naim@unc.edu</a></p>
</section>

<section class="page-section page-section--alt">
{% assign groups = site.members | sort: "group_rank" | map: "group" | uniq %}
{% for group in groups %}
  <div class="team-group mb-5">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-center flex-wrap gap-2">
        <h3 class="team-group__title mb-0">{{ group }}</h3>
        <span class="badge badge-light team-group__count">{{ site.members | where: "group", group | size }} {{ group | downcase }}</span>
      </div>
      <div class="team-group__list mt-4">
        {% assign members = site.members | sort: "group_order" | where: "group", group %}
        {% for member in members %}
        <div class="card {% if member.inline == false %}hoverable{% endif %} mb-4 team-card">
          <div class="row no-gutters">
            <div class="col-sm-4 col-md-3">
              {% assign image_alt = member.profile.image_alt | default: member.profile.name %}
              {% if member.inline == false %}
                {% if member.external == true %}
                  <a class="team-card__image-link" href="{{ member.profile.website }}" aria-label="View profile for {{ member.profile.name }}">
                    <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ image_alt }}" loading="lazy" decoding="async" />
                  </a>
                {% else %}
                  <a class="team-card__image-link" href="{{ member.url | relative_url }}" aria-label="View profile for {{ member.profile.name }}">
                    <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ image_alt }}" loading="lazy" decoding="async" />
                  </a>
                {% endif %}
              {% else %}
                <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ image_alt }}" loading="lazy" decoding="async" />
              {% endif %}
            </div>
            <div class="team col-sm-8 col-md-9">
              <div class="card-body">
                <div class="team-card__title">
                  <h5 class="card-title mb-0">
                    {% if member.inline == false %}
                      {% if member.external == true %}
                        <a class="team-card__name-link" href="{{ member.profile.website }}" aria-label="View profile for {{ member.profile.name }}">{{ member.profile.name }}</a>
                      {% else %}
                        <a class="team-card__name-link" href="{{ member.url | relative_url }}" aria-label="View profile for {{ member.profile.name }}">{{ member.profile.name }}</a>
                      {% endif %}
                    {% else %}
                      {{ member.profile.name }}
                    {% endif %}
                  </h5>
                  {% assign team_label = member.profile["team-position"] %}
                  {% if team_label %}
                    {% assign badge_key = team_label | downcase %}
                    {% assign badge_class = site.team_badges[badge_key] | default: site.team_badges.default %}
                    <span class="badge badge-pill {{ badge_class }}">{{ team_label }}</span>
                  {% endif %}
                </div>
                {% if member.profile.position %}
                  <h6 class="card-subtitle mb-2 text-muted">{{ member.profile.position }}</h6>
                {% elsif team_label %}
                  <h6 class="card-subtitle mb-2 text-muted">{{ team_label }}</h6>
                {% endif %}
                <p class="card-text">{{ member.teaser }}</p>
                {% assign linkedin_url = member.profile.linkedin %}
                {% if linkedin_url %}
                  {% unless linkedin_url contains '://' %}
                    {% assign linkedin_url = 'https://www.linkedin.com/in/' | append: member.profile.linkedin | append: '/' %}
                  {% endunless %}
                {% endif %}
                {% assign github_url = member.profile.github %}
                {% if github_url %}
                  {% unless github_url contains '://' %}
                    {% assign github_url = 'https://github.com/' | append: member.profile.github | append: '/' %}
                  {% endunless %}
                {% endif %}
                {% if member.profile.linkedin or member.profile.website or member.profile.github %}
                  <div class="team-card__badges">
                    {% if member.profile.linkedin %}
                      <a href="{{ linkedin_url }}" class="badge badge-social badge-social--linkedin" target="_blank" rel="noopener">
                        <i class="fab fa-linkedin"></i> LinkedIn
                      </a>
                    {% endif %}
                    {% if member.profile.website %}
                      <a href="{{ member.profile.website }}" class="badge badge-social badge-social--website" target="_blank" rel="noopener">
                        <i class="ti ti-world"></i> Personal Site
                      </a>
                    {% endif %}
                    {% if member.profile.github %}
                      <a href="{{ github_url }}" class="badge badge-social badge-social--github" target="_blank" rel="noopener">
                        <i class="fab fa-github"></i> GitHub
                      </a>
                    {% endif %}
                  </div>
                {% endif %}
                {% if member.profile.email %}
                  <a href="mailto:{{ member.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                {% endif %}
                {% if member.profile.phone %}
                  <a href="tel:{{ member.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                {% endif %}
                {% if member.profile.orcid %}
                  <a href="https://orcid.org/{{ member.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                {% endif %}
                {% if member.profile.twitter %}
                  <a href="https://twitter.com/{{ member.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                {% endif %}
                {% if member.profile.website %}
                  <a href="{{ member.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                {% endif %}
                <p class="card-text"><small class="text-muted"><i class="fas fa-thumbtack"></i> {{ member.profile.address | replace: '<br />', ', ' }}</small></p>
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
{% endfor %}
</section>
