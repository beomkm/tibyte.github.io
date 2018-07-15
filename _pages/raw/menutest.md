<div style="position:relative">
<ul>
  {% for tag in site.tags %}
    <li>
        <a href="{{ site.baseurl}}/tag/{{ tag[0] | slugify }}">
        <strong>{{ tag[0] }}</strong> ({{ tag[1].size }})
      </a>
    </li>
  {% endfor %}
</ul>
</div>

