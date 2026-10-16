---
layout: page
title: TJBot
description: An open source DIY robot that teaches people how to program with AI, built by hundreds of thousands of students and makers worldwide.
img: assets/img/projects/tjbot.jpg
importance: 1
category: open source
github: https://github.com/tjbot-ce/tjbot
related_publications: true
---

TJBot is an open source, DIY cardboard robot that we created at IBM Research to make it easy and fun to learn how to program with AI. Makers can laser cut or 3D print TJBot's body, add a Raspberry Pi and a few inexpensive components, and then write "recipes" that let TJBot listen, speak, see, shine its LED, and wave its arm.

TJBot has been **used by hundreds of thousands of students and makers** around the world. I was also recognized with an IBM Volunteer Excellence Award for TJBot classroom learning activities supporting Vietnam Teacher's Day.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/tjbot-sxsw.jpg" title="TJBot" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## TJBot Community Edition: the latest version

**If you're building a TJBot today, start with [TJBot Community Edition](https://tjbot-ce.github.io).** It keeps TJBot up to date with evolving Raspberry Pi hardware and software, and it modernizes the software stack:

- **New libraries** in TypeScript ([node-tjbotlib](https://github.com/tjbot-ce/node-tjbotlib)) and Python ([python-tjbotlib](https://github.com/tjbot-ce/python-tjbotlib)) for writing TJBot recipes.
- **On-device AI**: support for local speech-to-text, text-to-speech, and vision models, so TJBot no longer depends on cloud services.
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

## The original TJBot

The original IBM release used IBM Watson AI services and lives in [ibmtjbot/tjbot](https://github.com/ibmtjbot/tjbot) and [node-tjbotlib](https://github.com/ibmtjbot/node-tjbotlib). It is no longer actively developed. Other things I built for the original TJBot include the [TJBot Swift Playground](https://github.com/jweisz/tjbot-playground), [swifty-tj](https://github.com/jweisz/swifty-tj), and [tjbot-daemon](https://github.com/jweisz/tjbot-daemon).

{% cite DibiaACW17 abs-1805-10723 %}
