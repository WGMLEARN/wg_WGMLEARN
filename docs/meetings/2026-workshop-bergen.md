---
layout: group
title: "WGMLEARN 2026 Workshop Bergen"
heading: "WGMLEARN 2026 Workshop Bergen"
tagline: "November 9–13, 2026 · Bergen, Norway"
meeting_id: "2026-workshop-bergen"
permalink: /meetings/2026-workshop-bergen/
---

Workshop information and materials will be added here.

## Workshop posts

{% assign meeting_posts = site.posts | where: "meeting_id", page.meeting_id | sort: "section_order" %}
{% if meeting_posts.size > 0 %}
The following posts are generated from the workshop Google Doc. Each Heading 1 in the document creates one post.

<ul>
  {% for post in meeting_posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
{% else %}
Workshop posts will appear here after the meeting Google Doc is imported.
{% endif %}

[Back to meetings]({{ '/meetings/' | relative_url }})