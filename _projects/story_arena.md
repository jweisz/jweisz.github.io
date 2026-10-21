---
layout: page
title: Story Arena
description: A multi-agent environment for crafting design fictions.
img: assets/img/projects/story-arena.jpg
importance: 4
category: open source
github: https://github.com/jweisz/story-arena
related_publications: true
---

Story Arena is a collaborative story-writing tool where multiple AI models write stories together in three phases:

1. **Ideation**: each agent proposes a story concept (genre, setting, characters, plot, and conflict) based on its own persona prompt and a shared story prompt.
2. **Consensus**: the agents converge on a single direction.
3. **Writing**: the agents write the story.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/story-arena.jpg" title="AI agents collaborating on a story" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    An AI-generated illustration of AI agents collaborating on a story.
</div>

I built Story Arena to explore speculative futures of software engineering and presented it at the workshop on _The End of Programming (as we know it)_ at the Aarhus 2025 Decennial Conference.

{% cite abs-2511-05410 %}
