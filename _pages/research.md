---
layout: page
title: research
permalink: /research/
description: My research focuses on three complementary themes, useful AI, safe AI, and personal AI, studied with mixed methods.
nav: true
nav_order: 2
related_publications: true
---

AI systems don't need to be perfect to be useful {% cite WeiszMHRRMAT21 %}. To be useful, though:

1. AI needs to fit into people's existing workflows and be optimized for their specific use cases.
2. AI needs to minimize its potential for harm, both through explicit mitigations and by helping people critically evaluate what it produces.
3. People differ in how fluently they use AI and in how they prefer it to interact with them. Both people and AI need new mechanisms for understanding each other.

These three points correspond to the three themes of my research, and most of my projects touch more than one.

---

## Useful AI

_Specialized, domain-specific AI systems that integrate into existing workflows. My work here has focused on the roles at the heart of product development: software engineers, designers, and product managers._

**AI for software engineering.** Beginning in 2019, we studied whether imperfect generative models could still help software engineers. In a design probe of AI-supported code translation, engineers were receptive to imperfect AI and treated its output with appropriate skepticism {% cite WeiszMHRRMAT21 %}. A follow-up experiment found net improvements in translation quality, along with a "scaffolding" effect for people unfamiliar with the target language. It also showed that the benefits were not evenly shared {% cite WeiszMRMHATR22 %}. We then built the [Programmer's Assistant](/projects/ai_for_software_engineers/), one of the first empirical studies of conversational, LLM-based programming help inside a code editor {% cite RossMHMW23 %}. Later, a large-scale study of an enterprise coding assistant found that its top use case was explaining code, not generating it {% cite WeiszKMBGHB25 %}. That finding led to our work on the [Agentic Code Explorer](/projects/ai_for_software_engineers/).

**AI for group ideation.** With [Koala and Collaborative Canvas](/projects/ai_for_designers/), we explored how an LLM-based agent can join a brainstorming group, and we developed a framework for designing an agent's participatory behaviors {% cite MullerHGBRMW24 HeHGMRMW24 HoudeBMRMGKFW25 %}.

**Design principles for generative AI.** I led a cross-IBM effort to distill research on human-AI collaboration and co-creation into principles and strategies for designing generative AI applications. This work was used to train 3,000+ IBM design practitioners {% cite WeiszHMHMG24 %}.

**Human-centered explainable AI.** We showed that explanations of AI decisions should include _social_ context, such as who accepted or rejected a recommendation and why, alongside algorithmic explanations {% cite EhsanLMRW21 %}. This work helped launch the field of human-centered explainable AI (HCXAI), which we have grown through a workshop series at CHI {% cite EhsanWWMRWDRR23 EhsanWWMHSWR25 EhsanAHLRW26 %}. I also co-organized the HAI-GEN workshop series on human-AI co-creation with generative models at IUI from 2021 to 2025.

---

## Safe AI

_Identifying the risks that arise from using AI systems, and helping developers determine which risks and mitigations apply to their use cases._

**AI risk.** The guidance we wrote on the risks of generative AI was adopted by IBM's AI Ethics Board and became the first version of the [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas). More recently, we interviewed people who build AI agents about how they perceive and prioritize the risks of agentic AI.

**Factuality and transparency.** We studied how visual factuality indicators and source attributions help people judge the reliability of LLM output {% cite DoOGMWW25 abs-2405-20434 %}.

**Contextual privacy.** We developed methods that protect people from oversharing sensitive information with conversational agents and that evaluate contextual privacy across agentic workflows {% cite NgongK0MWDR25 abs-2603-04902 %}.

**Attribution and disclosure.** We studied how much credit people think AI deserves for its contributions to creative work {% cite HeHW25 %}. We then built the [AI Attribution Toolkit](/projects/ai_attribution/) and examined what makes people more comfortable disclosing their use of AI {% cite HeADW26 %}.

---

## Personal AI

_Giving AI systems models of their human users (their goals, knowledge, beliefs, and intentions) to improve how people and AI perform together, and making those models visible so people can form better mental models of the AI._

**Mutual theory of mind.** We proposed operationalizing [_mutual theory of mind_](/projects/mutual_theory_of_mind/) between people and AI {% cite abs-2406-11946 %}. Using the cooperative game Wavelength, we showed that human-AI teams with a stronger mutual understanding outperform teams without it {% cite MorrisonGARABW26 MorrisonABGW25tom4ai %}. We also argued that current theory-of-mind benchmarks for LLMs are broken {% cite RiemerA0D0WC25 %}. I co-organize workshops on theory of mind in human-AI interaction at CHI and CUI {% cite WangWSKW024 WangWPLWS25 %}.

**Adaptive code explanations.** Drawing on research into individual differences in problem-solving styles, we studied how LLMs adapt code explanations to different kinds of users and what developers want those explanations to contain {% cite abs-2607-17022 BrachmanG0HMW25 %}.

**Teaching people to work with AI.** Earlier, I developed ways to teach people effective strategies for interacting with conversational agents {% cite WeiszJJJL19 AshktorabJLW19 %}.

---

## Methods

I use a mixed-methods toolkit:

- **Qualitative** studies to understand a problem space
- **Prototyping** to create new tools and explore new forms of interaction
- **Quantitative** experiments to measure the effects of an intervention or design
- **Crowdsourcing** to gather feedback from larger groups
- **Speculative design** to reason about future trends and longer-term consequences {% cite MullerRHAMRTW22 abs-2511-05410 %}
