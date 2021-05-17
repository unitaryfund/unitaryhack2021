---
layout: page
title: 🏆Results🏆
---

## Current closed PRs
<ul>
{% for member in site.data.closed-prs %}
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