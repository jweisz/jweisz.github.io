---
layout: page
title: AI for Software Engineers
description: From AI-supported code translation to the Programmer's Assistant and the Agentic Code Explorer, how generative AI can help people build software.
importance: 1
category: research areas
related_publications: true
---

Software engineering was one of the first domains where generative AI became genuinely useful, and I've studied it since 2019, before large language models became mainstream. A lesson that runs through this work is that **AI doesn't have to be perfect to be useful**.

## Imperfect AI can still help

We began by asking whether software engineers would find value in a generative model whose output was often wrong. In a design probe of AI-supported code translation, engineers were receptive to imperfect AI and treated its output with appropriate skepticism. A follow-up experiment found net improvements in translation quality, along with a "scaffolding" effect for people unfamiliar with the target language. It also showed that the benefits were not evenly shared. Along the way, we studied how to explain generative models of code and how to estimate the quality of their output.

{% cite WeiszMHRRMAT21 WeiszMRMHATR22 SunLMAHTW22 abs-2012-07581 abs-2110-05423 %}

## The Programmer's Assistant

In 2022, interactions with code-fluent language models mostly took the form of "push button, get results." We wondered whether software engineers would want richer, **conversational interactions** with an AI that understood both their code and the context of their earlier exchanges.

We built the Programmer's Assistant, a prototype that embedded a conversational LLM inside a code editor. In a user study, software engineers valued being able to ask both general programming questions and questions about their own code. ChatGPT was released while our paper was under review. Our work helped pave the way for the first generation of AI coding assistants, including IBM's [watsonx Code Assistant](https://www.ibm.com/docs/en/wx-code-assistant/5.1.x?topic=overview). The demo received a Best Demo Honorable Mention at IUI 2023.

{% cite RossMHMW23 RossHMMW23 RossMMHW23 %}

## AI coding assistants at scale

We later studied the use and impact of an enterprise AI code assistant. Its most common use case was not generating code but **explaining** it. However, many users felt the explanations were too verbose or poorly suited to their needs.

{% cite WeiszKMBGHB25 %}

## The Agentic Code Explorer (ACE)

We investigated how code explanations could be tailored to individual differences in problem-solving style, such as how people process information, how they learn, and their confidence with technology. We also asked software engineers what they want code explanations to contain. Building on these findings, we developed the **Agentic Code Explorer (ACE)**. ACE combines retrieval-augmented generation with user modeling to produce personalized code explanations and to support "co-investigation" of a codebase between a developer and an AI agent.

{% cite MoranBGHMBW25 BrachmanG0HMW25 abs-2607-17022 abs-2503-11018 %}

## The future of programming

We have also used speculative design to think about where AI-assisted software engineering is headed, including a design fiction about the value tensions of pair programming with an AI, and [Story Arena](/projects/story_arena/), a multi-agent environment in which AI models write stories about the future of software engineering.

{% cite MullerRHAMRTW22 MullerWHR24 abs-2511-05410 %}
