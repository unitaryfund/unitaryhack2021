---
layout: page
title: 🏆Results🏆
---

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:grey;border-style:none;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-sj11{!important;;font-size:medium; text-align:left;vertical-align:middle}
</style>
<table class="tg">
<tbody>
  <tr>
    <td class="tg-sj11"><a href="#new-projects">🆕 New projects</a></td>
    <td class="tg-sj11"><a href="#accepted-pulls">🎉 Hacks</a></td>
    <td class="tg-sj11"><a href="#completed-bounties">💸 Completed Bounties</a></td>
    <td class="tg-sj11"><a href="#pending-pull-requests">⌛ Pending Hacks</a></td>
  </tr>
</tbody>
</table>

> If you do not see your contribution, please ping @crazy4pi314 on the [Unitary Fund Discord](http://discord.unitary.fund) or send an email to [sarah@unitary.fund](mailto:sarah@unitary.fund).

---

<h2 id="new-projects">🆕 New projects/repos started 🆕</h2>

### [SciRate](https://github.com/scirate/scirate):
- **[infiniteregrets](https://github.com/infiniteregrets)** HACKED [Make a twitter/discord bot that posts the top papers each day](https://github.com/scirate/scirate/issues/430) by building [scirate-bots](https://github.com/scirate/scirate-bots/pull/1)

### [Yao.jl Website](https://github.com/QuantumBFS/QuantumBFS.github.io):
- **[VarLad](https://github.com/VarLad)** HACKED the docs [by fixing tutorials](https://github.com/QuantumBFS/QuantumBFS.github.io/pull/9) and [making them more consistent](https://github.com/QuantumBFS/QuantumBFS.github.io/pull/9)

### [Yao Ecosystem (QuantumBFS)](https://github.com/QuantumBFS):
- **[Sov-trotter](https://github.com/Sov-trotter)** HACKED two new libraries, YaoBlocks interfaces for the [IBMQClient](https://github.com/QuantumBFS/YaoBlocksQobj.jl) and [OpenQASM](https://github.com/QuantumBFS/YaoBlocksQASM.jl)

---
<h2 id="accepted-pulls">🎉 Accepted Pull Requests 🎉</h2>

{% for member in site.data.merged-prs %}
  <h3><a href="https://github.com/{{ member.name }}">
    {{ member.name }}:</a>
  </h3>
  <ul>
  {% for pr in member.data %}
    <li>
      <strong><a href="https://github.com/{{ pr.user }}"> {{ pr.user }}</a></strong> HACKED
      <a href="https://github.com/{{ member.name }}/issues/{{ pr.number }}"> {{ pr.title }}</a>
    </li>
    {% endfor %}
  </ul>
{% endfor %}

---
<h2 id="completed-bounties">💸 Completed Bounties 💸</h2>

{% for member in site.data.closed-bounties %}
  <h3><a href="https://github.com/{{ member.name }}">
    {{ member.name }}:</a>
  </h3>
  <ul>
  {% for pr in member.data %}
    <li>
      <a href="https://github.com/{{ member.name }}/issues/{{ pr.number }}"> {{ pr.title }}</a> was CASHED IN
    </li>
    {% endfor %}
  </ul>
{% endfor %}

---
<h2 id="pending-pull-requests">⌛ Pending Pull Requests ⌛</h2>

{% for member in site.data.open-prs %}
  <h3><a href="https://github.com/{{ member.name }}">
    {{ member.name }}:
  </a></h3>
  <ul>
  {% for pr in member.data %}
    <li>
      <strong><a href="https://github.com/{{ pr.user }}"> {{ pr.user }}</a></strong> is working on
      <a href="https://github.com/{{ member.name }}/issues/{{ pr.number }}"> {{ pr.title }}</a>
    </li>
    {% endfor %}
  </ul>
{% endfor %}

---


<!--
NB: Removing as the event is over
 ---
## 💲 Open Bounties 💲

{% for member in site.data.open-bounties %}
  <h3><a href="https://github.com/{{ member.name }}">
    {{ member.name }}:
  </a></h3>
  <ul>
  {% for issue in member.data %}
    <li>
      <a href="https://github.com/{{ member.name }}/issues/{{ issue.number }}"> {{ issue.title }}</a>
    </li>
  {% endfor %}
  </ul>
{% endfor %} -->
