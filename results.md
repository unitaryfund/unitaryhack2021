---
layout: page
title: 🏆Results🏆
---

## 📥 Hackathon Submissions 📥
### Accepted Pull Requests
<ul>
{% for member in site.data.merged-prs %}
  <li>
    <a href="https://github.com/{{ member.name}}">
      {{ member.name}}
    </a> :
    <ul>
    {% for issue in member.data %}
      <li>
        <a href="https://github.com/{{ member.name}}/issues/{{issue.number}}">
      {{ issue.title}} </a>
      </li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>

### Pending Pull Requests
<ul>
{% for member in site.data.open-prs %}
  <li>
    <a href="https://github.com/{{ member.name}}">
      {{ member.name}}
    </a> :
    <ul>
    {% for issue in member.data %}
      <li>
        <a href="https://github.com/{{ member.name}}/issues/{{issue.number}}">
      {{ issue.title}} </a>
      </li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>

## 💰 Bounties 💰
### Completed Bounties
<ul>
{% for member in site.data.closed-bounties %}
  <li>
    <a href="https://github.com/{{ member.name}}">
      {{ member.name}}
    </a> :
    <ul>
    {% for issue in member.data %}
      <li>
        <a href="https://github.com/{{ member.name}}/issues/{{issue.number}}">
      {{ issue.title}} </a>
      </li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>

### Open Bounties
<ul>
{% for member in site.data.open-bounties %}
  <li>
    <a href="https://github.com/{{ member.name}}">
      {{ member.name}}
    </a> :
    <ul>
    {% for issue in member.data %}
      <li>
        <a href="https://github.com/{{ member.name}}/issues/{{issue.number}}">
      {{ issue.title}} </a>
      </li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>