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

[![GitHub](https://img.shields.io/badge/GitHub-jweisz%2Fstory--arena-181717?logo=github&logoColor=white)](https://github.com/jweisz/story-arena)

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
    An AI-generated illustration of AI agents collaborating on a story. <a href="https://aiattribution.github.io/statements/AIA-EAI-Hin-R-?model=Gemini-v1.0">AIA EAI Hin R Gemini v1.0</a>.
</div>

I built Story Arena to explore speculative futures of software engineering and presented it at the workshop on [The End of Programming (as we know it)](https://glossy-twister-5ec.notion.site/Workshop-Invitation-1c7e06f235ea80b09717ce04663c448e) at the Aarhus 2025 Decennial Conference. Our story, "The Code of Trust," is about a software engineer who receives a large volume of AI-generated code that works flawlessly, but that they _can't fully understand_. This story raised questions about trust, ownership, and the fine line between augmentation and automation {% cite abs-2511-05410 %}.
