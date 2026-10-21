---
layout: page
title: TJBot
description: An open source DIY robot that teaches people how to program with AI, built by hundreds of thousands of students and makers worldwide.
img: assets/img/projects/tjbot.jpg
importance: 1
category: open source
github: https://github.com/tjbot-ce/tjbot
website: https://tjbot-ce.github.io
related_publications: true
---

[![Website](https://img.shields.io/badge/website-tjbot--ce.github.io-0b7a6e?logo=googlechrome&logoColor=white)](https://tjbot-ce.github.io) [![GitHub](https://img.shields.io/badge/GitHub-tjbot--ce-181717?logo=github&logoColor=white)](https://github.com/tjbot-ce)

TJBot is an open source, DIY cardboard robot that makes it easy and fun to learn how to program with AI {% cite DibiaACW17 abs-1805-10723 %}. Makers can laser cut or 3D print TJBot's body, add a Raspberry Pi and a few inexpensive components, and then write "recipes" that let TJBot listen, speak, see, shine its LED, and wave its arm.

TJBot has been **used by hundreds of thousands of students and makers** around the world to learn about AI, cloud services, and robotics. I was part of the original team at IBM Research that developed TJBot and maintained it for many years. I was also part of a separate team that developed classrom activities for Vietnam's Teacher's Day, for which I received an IBM Volunteer Excellence Award.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/tjbot-sxsw.jpg" title="TJBot" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    TJBot creator <a href="https://www.linkedin.com/in/mashoori">Maryam Ashoori</a> shows off a giant TJBot at SXSW 2017.
</div>

## TJBot Community Edition

**If you'd like to build a TJBot today, start with [TJBot Community Edition](https://tjbot-ce.github.io).** I created this fork of TJBot's software to keep it up to date with the evolving landscape of Raspberry Pi hardware, software, and cloud-based AI services. TJBot: Community Edition is built upon a modernized software stack:

- **Programming SDKs**: choose between TypeScript ([node-tjbotlib](https://github.com/tjbot-ce/node-tjbotlib)) and Python ([python-tjbotlib](https://github.com/tjbot-ce/python-tjbotlib)) for writing TJBot recipes.
- **On-device AI**: support for local speech-to-text, text-to-speech, and computer vision models.
- **Hardware**: supports Raspberry Pi 3B, 3B+, 4, and 5.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/tjbot-assembly.png" title="TJBot assembly" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    TJBot's cardboard body folds together around a Raspberry Pi and a handful of off-the-shelf components.
</div>
