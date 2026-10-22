---
layout: page
title: research
permalink: /research/
description: "My research focuses on three complementary themes: useful AI, safe AI, and personal AI."
nav: true
nav_order: 2
related_publications: true
_styles: >
  .post article hr { margin: 3.5rem 0 2.5rem; }
  .post article h2 { font-size: 2.25rem; margin-bottom: 0.75rem; }
  .post article h3 { font-size: 1.4rem; font-weight: 400; margin-top: 2.5rem; margin-bottom: 0.75rem; }
  .post article .theme-blurb { font-size: 1.1rem; margin-bottom: 0.5rem; }
  .post article .theme-blurb em { color: var(--global-text-color-light); }
  .post article .theme-tags { font-size: 0.875rem; margin-top: -0.5rem; }
  .post article .theme-tags em { color: var(--global-theme-color); }
  .post > h2 { margin-top: 3.5rem; }
---

AI systems don't need to be perfect to be useful {% cite WeiszMHRRMAT21 %}. But to be useful, they:

- Need to **fit into people's existing workflows**: the tools they already use and the context of the work they're doing.
- Need to **minimize their potential for harm**, both through explicit mitigations and by helping people critically evaluate their outputs.
- Need to **meet people where they're at**. People differ in how fluently they use AI and in how they prefer it to interact with them. People and AI both need new mechanisms for understanding each other.

These three points correspond to the three themes of my research: **useful AI**, **safe AI**, and **personal AI**. These themes overlap, and some of my projects sit in that overlap.

**Jump to:** [Useful AI](#useful-ai) · [Safe AI](#safe-ai) · [Personal AI](#personal-ai) · [Intersections](#intersections)

---

## Useful AI

_AI that fits into the way people already work and draws on the context of that work. My work here has focused on the professionals at the heart of building technology: software engineers, designers, and data scientists._
{: .theme-blurb}

### AI for software engineering

Software engineering was one of the first domains where generative AI became genuinely useful, and I've studied it since 2019, before large language models became mainstream.

We began by asking whether software engineers would find value in a generative model whose output was often wrong. In a design probe of AI-supported code translation, engineers were receptive to imperfect AI and treated its output with appropriate skepticism {% cite WeiszMHRRMAT21 %}. A follow-up experiment found net improvements in translation quality, along with a "scaffolding" effect for people unfamiliar with the target language. It also showed that the benefits were not evenly shared {% cite WeiszMRMHATR22 %}. Along the way, we studied how to explain generative models of code and how to estimate the quality of their output {% cite SunLMAHTW22 abs-2012-07581 abs-2110-05423 %}.

In 2022, interactions with code-fluent language models mostly took the form of "push button, get results." We built the **Programmer's Assistant**, a prototype that embedded a conversational LLM inside a code editor, to find out whether software engineers wanted richer, conversational interactions. They valued being able to ask both general programming questions and questions about their own code {% cite RossMHMW23 RossHMMW23 RossMMHW23 %}. ChatGPT was released while our paper was under review. Our work helped pave the way for the first generation of AI coding assistants, including IBM's [watsonx Code Assistant](https://www.ibm.com/docs/en/wx-code-assistant/5.1.x?topic=overview), and the demo received a Best Demo Honorable Mention at IUI 2023.

We later studied the use and impact of watsonx Code Assistant across the enterprise. Its most common use case was not generating code but _explaining_ it {% cite WeiszKMBGHB25 %}, which underscored the importance of our parallel work on [personalized code explanations](#personalized-code-explanations).

We have also used speculative design to think about where AI-assisted software engineering is headed. This includes a design fiction about the value tensions of pair programming with an AI {% cite MullerRHAMRTW22 MullerWHR24 %} and [Story Arena](/projects/story_arena/), a multi-agent environment in which AI agents write stories about the future of software engineering {% cite abs-2511-05410 %}.

### AI for designers and group ideation

Designers often run group ideation sessions, but these sessions can stall, or they can lack a particular expertise or viewpoint. We built two prototypes to explore how an LLM-based agent might participate:

- **Koala** is a Slack bot that joins group brainstorming discussions. It contributes ideas either reactively (when mentioned) or proactively (when it judges it has something valuable to add). All participants preferred having Koala in their groups, and most of the top ideas were shaped by both people and the AI {% cite MullerHGBRMW24 %}.
- **Collaborative Canvas** is a shared virtual canvas where people and an AI place digital stickies together. Design practitioners saw value in AI for filling expertise gaps and breaking through lulls, and they suggested that AI could act as a facilitator, not only as a participant {% cite HeHGMRMW24 GonzalezMHHRMKW24 %}.

From these experiences, we developed a framework for designing an AI agent's **participatory behaviors** in group conversations: when it should contribute, what and where, and who decides {% cite HoudeBMRMGKFW25 %}.

We have also developed frameworks for mixed-initiative generative AI interfaces and studied opportunities for generative AI in design and UX work {% cite MullerWG20iccc HoudeLMMPRWZ20 HoudeRMAMRTW22 MullerCW23 MullerHW25 %}. From 2021 to 2025, I co-organized the HAI-GEN workshop series on human-AI co-creation with generative models at IUI {% cite GeyerCWM21 WeiszMSCBG22 MaherWCGS23 GeyerMWBC24 MokrynSGMWBC25 %}.

### AI for data science

Automated machine learning (AutoML) promised to automate much of a data scientist's work. We interviewed data scientists about how they perceived automated AI {% cite WangWMRGDTSG19 %} and studied the information they need before they will trust an AutoML system {% cite DrozdalWWDYZMJS20 %}.

These findings shaped tools for **IBM AutoAI**, which automates the end-to-end AI lifecycle while keeping humans in the loop {% cite WangRW0MWVCTSA20 WangAWOKSCVTD20 %}. AutoAIViz visualizes the pipelines that AutoAI generates {% cite WeideleWOMAGW20 %}, Model LineUpper supports interactive comparison of the models it produces {% cite NarkarZLWW21 %}, and AutoDS explores human-centered automation of the broader data science workflow {% cite WangAWOD21 %}. We also built an AI system that generates documentation for code in computational notebooks, and studied how data scientists improve what it produces {% cite WangWDMPWLWD22 MullerWRWATHMRD21 %}. Finally, we reflected on where data science is headed and on how AI-assisted data science can cultivate human expertise rather than replace it {% cite WeiszM20 AndresWMWJSBDAP20 %}.

---

## Safe AI

_Identifying the risks that arise from using AI systems, and helping both developers and users recognize and mitigate them._
{: .theme-blurb}

### Mapping the risks of AI

The guidance we wrote on the risks of generative AI was adopted by IBM's AI Ethics Board, and we added new generative AI risks to the [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas). More recently, we interviewed people who build AI agents about how they perceive and prioritize the risks of agentic AI. I also co-organized the AgentCraft workshop on developing trustworthy agentic AI systems at IUI 2026 {% cite DinakarWLG26 %}.

### Factuality and transparency

LLMs can produce output that sounds confident but is wrong. We studied how visual factuality indicators and source attributions help people judge the reliability of LLM output {% cite DoOGMWW25 abs-2405-20434 %}.

### Privacy

New technologies, from drones to AI agents, can erode people's privacy in ways they don't expect. Earlier, we studied how drones affect people's privacy expectations and how technology can help preserve them {% cite UchidiunoMW18 %}. More recently, we turned to contextual privacy: people can overshare sensitive information with conversational agents, and agents can pass that information along in ways people don't anticipate. We developed methods that protect people from oversharing with conversational agents, and a way to evaluate contextual privacy across agentic workflows {% cite NgongK0MWDR25 abs-2603-04902 %}.

### Trust and alignment

We studied the factors that influence whether people find AI-infused decision-making processes trustworthy {% cite abs-1912-02675 %}, and more recently, the different scopes along which AI systems can be aligned {% cite abs-2501-12405 %}.

---

## Personal AI

_Giving AI systems models of their human users (their goals, knowledge, beliefs, and intentions) to improve how people and AI perform together, and making those models visible so people can form better mental models of the AI._
{: .theme-blurb}

### Mutual theory of mind

Many human-AI teaming studies show that AI doesn't always deliver the performance gains we expect. We hypothesized that teams would perform better if the human and the AI held a **mutual theory of mind**: an accurate model of each other's goals, knowledge, and reasoning. We proposed a way to operationalize it {% cite abs-2406-11946 %}, and we argued that current theory-of-mind benchmarks for LLMs are broken {% cite RiemerA0D0WC25 %}.

To study mutual theory of mind in practice, we built **Wavelength.AI**, a version of the cooperative party game _Wavelength_ in which people play alongside an LLM-based agent. The game rewards teammates who understand each other well. We tested two interventions: introductions with targeted questions before play, and retrospectives where players share their strategies and the reasoning behind their clues. Teams that had these interventions outperformed teams that did not {% cite MorrisonGARABW26 MorrisonABGW25tom4ai %}.

I co-organize workshops on theory of mind in human-AI interaction at CHI and CUI {% cite WangWSKW024 WangWPLWS25 %}.

### Helping people understand conversational agents

Before LLMs, I studied how to teach people effective strategies for interacting with chatbots {% cite WeiszJJJL19 %}, and which repair strategies people prefer when a conversation with a chatbot breaks down {% cite AshktorabJLW19 %}.

---

## Intersections

My three research themes reinforce each other. AI is rarely useful if people can't trust it, and it is rarely trustworthy if it ignores who is using it. Some of my projects address these themes together: design principles that weigh productivity, harm, and people's mental models of AI at the same time; explanations that make AI decisions both more useful and more accountable; attribution practices that let people benefit from AI while being transparent about its role; and code explanations that adapt to the individual developer.

### Design principles for generative AI

_Useful AI · Safe AI · Personal AI_
{: .theme-tags}

Generative AI applications pose new design challenges: their outputs vary, they can be wrong, and they can create harm. I led a cross-IBM effort to distill research on human-AI collaboration and co-creation into **design principles** and concrete strategies for designing generative AI applications. Together with a set of design thinking exercises, the principles trained over 3,000 IBM design practitioners to work with AI as a design material. We later extended them into a handbook chapter {% cite WeiszHMHMG24 WeiszMHH23 WeiszHM25handbook %}.

### Human-centered explainable AI

_Useful AI · Safe AI_
{: .theme-tags}

We showed that explanations of AI decisions should include _social_ context, such as who accepted or rejected a recommendation and why, alongside algorithmic explanations {% cite EhsanLMRW21 %}. This work helped launch the field of human-centered explainable AI (HCXAI), which we have grown through a workshop series at CHI {% cite EhsanWWMRWDRR23 EhsanWWMHSWR25 EhsanAHLRW26 %}.

### AI attribution

_Useful AI · Safe AI_
{: .theme-tags}

Who deserves credit when people create with generative AI? In a scenario-based study, we found that people feel AI deserves credit for its contributions, especially when it synthesizes information, contributes new ideas, or produces large amounts of material. _How_ AI was used matters, not only _whether_ it was used, yet many organizational AI-use policies only require disclosing use {% cite HeHW25 %}. We built the [AI Attribution Toolkit](https://aiattribution.github.io/) to give creators a more precise language for describing how AI contributed to their work. We then examined how the granularity of a disclosure, along with sociocultural enablers, affects the stigma people perceive around disclosing AI use {% cite HeADW26 %}.

### Personalized code explanations

_Useful AI · Personal AI_
{: .theme-tags}

Software engineers differ in how they process information, how they learn, and how confident they feel with technology, so a one-size-fits-all explanation of code won't serve all of them. We investigated how explanations could be tailored to these individual differences in problem-solving style, and we asked software engineers what they want explanations to contain {% cite AndersonPWBV26 abs-2503-11018 BrachmanG0HMW25 %}.

In parallel with the development of watsonx Code Assistant, we built the **Agentic Code Explorer (ACE)** and shared its ideas with the product team. ACE combines retrieval-augmented generation with user modeling to produce personalized code explanations and to support "co-investigation" of a codebase between a developer and an AI agent {% cite MoranBGHMBW25 %}. Our study of watsonx Code Assistant later reinforced the need for this work: explaining code was its most common use, yet many users felt its explanations were too verbose or poorly suited to their needs {% cite WeiszKMBGHB25 %}.
