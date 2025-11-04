---
layout: page
permalink: /team.html
title: team
page-title: Team
description: Current and former group members
nav: true
nav_order: 2
nav_rank: 2
---

<p class="lead">
  The Rashid Lab pairs Gillings biostatisticians with Lineberger clinicians, fellows, and alumni who specialize in adaptive trials, multi-omic biomarker discovery, and patient-centered analytics. Alumni now lead analytics programs at institutions such as Dana-Farber Cancer Institute and GSK, while current trainees co-develop AI-driven trial navigation, transfer learning for liquid biopsies, and microbiome multi-omics. Explore the team advancing UNC’s cancer mission worldwide.
</p>

{% assign groups = site.members | sort: "group_rank" | map: "group" | uniq %}
{% for group in groups %}
## {{ group }}

{% assign members = site.members | sort: "group_order" | where: "group", group %}
{% for member in members %}
<div class="card {% if member.inline == false %}hoverable{% endif %} mb-4 team-card">
  <div class="row no-gutters">
    <div class="col-sm-4 col-md-3">
      {% assign image_alt = member.profile.image_alt | default: member.profile.name %}
      <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ image_alt }}" loading="lazy" decoding="async" />
    </div>
    <div class="team col-sm-8 col-md-9">
      <div class="card-body">
        {% if member.inline == false %}{% if member.external == true %}<a href="{{ member.profile.website }}" class="stretched-link">{% else %}<a href="{{ member.url | relative_url }}" class="stretched-link">{% endif %}{% endif %}
        <div class="team-card__title">
          <h5 class="card-title mb-0">{{ member.profile.name }}</h5>
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
        {% if member.inline == false %}</a>{% endif %}
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
        {% if member.profile.github %}
          <a href="https://github.com/{{ member.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
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
{% endfor %}
