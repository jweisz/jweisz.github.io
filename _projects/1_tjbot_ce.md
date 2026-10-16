---
layout: page
title: TJBot Community Edition
description: A modernized software stack for TJBot, the open source DIY robot for makers, students, and educators.
img: assets/img/projects/tjbot-ce.jpg
importance: 1
category: open source
github: https://github.com/tjbot-ce/tjbot
github_stars: tjbot-ce/tjbot
related_publications: false
---

[TJBot Community Edition](https://tjbot-ce.github.io) keeps [TJBot](/projects/4_tjbot/) up to date with evolving Raspberry Pi hardware and software. It is a community fork of the original IBM TJBot repository.

TJBot is a small, open source DIY robot that you can 3D print or laser cut. Its body houses a Raspberry Pi, a speaker, an LED, a microphone, a camera, and a servo motor that lets it wave its arm. The Community Edition modernizes the software stack:

- **New libraries** in TypeScript ([node-tjbotlib](https://github.com/tjbot-ce/node-tjbotlib)) and Python ([python-tjbotlib](https://github.com/tjbot-ce/python-tjbotlib)) for writing TJBot recipes.
- **On-device AI**: support for local speech-to-text, text-to-speech, and vision models.
- **Current hardware**: works with the Raspberry Pi 3B, 3B+, 4, and 5.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/tjbot-assembly.png" title="TJBot assembly" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    TJBot's cardboard body folds together around a Raspberry Pi and a handful of off-the-shelf components.
</div>

**Links:** [Website](https://tjbot-ce.github.io) · [GitHub organization](https://github.com/tjbot-ce)
