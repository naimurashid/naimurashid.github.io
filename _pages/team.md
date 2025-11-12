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

<section class="section-hero section-hero--team">
  <div class="section-hero__content">
    <p class="section-hero__eyebrow">Lab Ecosystem</p>
    <h1>Biostatisticians embedded with oncologists</h1>
    <p class="section-hero__lede">
      We pair Gillings trainees with Lineberger disease-site teams to ship adaptive trials, biomarker pipelines, and patient-navigation AI. Alumni now lead analytics at Dana-Farber, GSK, UNC Molecular Diagnostics, and other cooperative groups.
    </p>
  </div>
  <div class="section-metrics">
    <div class="metric">
      <span class="metric__value">40+</span>
      <span class="metric__label">oncology collaborations</span>
    </div>
    <div class="metric">
      <span class="metric__value">12</span>
      <span class="metric__label">current trainees</span>
    </div>
    <div class="metric">
      <span class="metric__value">6</span>
      <span class="metric__label">disease-site partners</span>
    </div>
    <div class="metric">
      <span class="metric__value">20+</span>
      <span class="metric__label">alumni placements</span>
    </div>
  </div>
</section>

<section class="team-callout">
  <div class="team-callout__content">
    <p class="team-callout__eyebrow">Prospective PhD students</p>
    <h2>Fall 2026 cohort</h2>
    <p>We’re recruiting students excited about adaptive platforms, biomarker genomics, missing-data ML, and precision-oncology software.</p>
    <ul>
      <li><strong>Apply by Dec 10, 2025:</strong> Mention “Rashid Lab – adaptive oncology statistics.”</li>
      <li><strong>January 2026:</strong> Invite-only Q&amp;A with current trainees (travel support for visit weekend).</li>
      <li><strong>Funding:</strong> NIH SPORE, ARPA-H ADAPT, and Lineberger traineeships.</li>
    </ul>
    <p class="mb-0">Send a one-page research blurb, CV, and unofficial transcript to <a href="mailto:naim@unc.edu?subject=Prospective%20PhD%20-%20Rashid%20Lab">naim@unc.edu</a>.</p>
  </div>
</section>

<section class="page-section team-groups">
  <p class="page-intro__eyebrow">People</p>
  <h2 class="page-intro__title">Team roster</h2>
  <p class="page-intro__lede">
    Trainees, staff statisticians, and alumni are grouped below. Click any profile for bios, publications, and project links.
  </p>

  {% assign groups = site.members | sort: "group_rank" | map: "group" | uniq %}
  {% for group in groups %}
    <div class="team-group-block">
      <div class="team-group-block__header">
        <h3>{{ group }}</h3>
        <span class="badge badge-light">{{ site.members | where: "group", group | size }}</span>
      </div>
      <div class="team-group-block__grid">
        {% assign members = site.members | sort: "group_order" | where: "group", group %}
        {% for member in members %}
          {% assign image_alt = member.profile.image_alt | default: member.profile.name %}
          {% assign profile_link = nil %}
          {% if member.inline == false %}
            {% if member.external == true %}
              {% assign profile_link = member.profile.website %}
            {% else %}
              {% assign profile_link = member.url | relative_url %}
            {% endif %}
          {% endif %}
          {% assign team_label = member.profile["team-position"] %}
          {% assign badge_key = team_label | downcase %}
          {% assign badge_class = site.team_badges[badge_key] | default: site.team_badges.default %}
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

          {% assign card_classes = 'team-member-card' %}
          {% assign group_name = group | downcase %}
          {% if group_name contains 'faculty' %}
            {% assign card_classes = card_classes | append: ' team-member-card--faculty' %}
          {% endif %}
          <article class="{{ card_classes }}">
            <div class="team-member-card__media">
              {% if profile_link %}
                <a href="{{ profile_link }}" aria-label="View profile for {{ member.profile.name }}">
                  <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" alt="{{ image_alt }}" loading="lazy" decoding="async" />
                </a>
              {% else %}
                <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" alt="{{ image_alt }}" loading="lazy" decoding="async" />
              {% endif %}
            </div>
            <div class="team-member-card__body">
              <div class="team-member-card__title">
                <h4>
                  {% if profile_link %}
                    <a href="{{ profile_link }}">{{ member.profile.name }}</a>
                  {% else %}
                    {{ member.profile.name }}
                  {% endif %}
                </h4>
                {% if team_label %}
                  <span class="badge badge-pill {{ badge_class }}">{{ team_label }}</span>
                {% endif %}
              </div>
              {% if member.profile.position %}
                <p class="team-member-card__role">{{ member.profile.position }}</p>
              {% endif %}
              <p class="team-member-card__teaser">{{ member.teaser }}</p>

              {% if member.profile.linkedin or member.profile.website or member.profile.github %}
                <div class="team-member-card__badges">
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

              <div class="team-member-card__contact">
                {% if member.profile.email %}
                  <a href="mailto:{{ member.profile.email }}"><i class="fas fa-envelope"></i></a>
                {% endif %}
                {% if member.profile.orcid %}
                  <a href="https://orcid.org/{{ member.profile.orcid }}" target="_blank" rel="noopener"><i class="fab fa-orcid"></i></a>
                {% endif %}
                {% if member.profile.twitter %}
                  <a href="https://twitter.com/{{ member.profile.twitter }}" target="_blank" rel="noopener"><i class="fab fa-twitter"></i></a>
                {% endif %}
              </div>
            </div>
          </article>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</section>
