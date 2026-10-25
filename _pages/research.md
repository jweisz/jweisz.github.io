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

_Useful AI fits into the way people already work and draws on their working context. My work in this space has focused on professionals at the heart of building technology, such as software engineers, designers, and data scientists._
{: .theme-blurb}

### AI for software engineering

Software engineering was one of the first domains where generative AI became genuinely useful. I've studied it with my colleagues since 2019, before large language models became mainstream.

We began by asking whether software engineers would find value in a generative model _whose output was often wrong_, because state-of-the-art model performance was much poorer than it is today. In a design probe of AI-supported code translation, we found that software engineers were receptive to AI despite its imperfections because they simply needed help {% cite WeiszMHRRMAT21 %}. In a follow-up experiment with 32 software engineers, we examined the utility of AI-produced code translations {% cite WeiszMRMHATR22 %}. We found that some, but not all, software engineers were able to work productively with imperfect translations by finding and fixing errors, and overall, participants produced code with fewer errors when aided by AI than when working alone. We also observed cases of a scaffolding effect, in which AI translations enabled developers less familiar with the programming language to complete a translation task that would otherwise have been too difficult for them. Along the way, we identified the kinds of explanations software engineers need from generative code models {% cite SunLMAHTW22 %}, developed a method for estimating the quality of AI-produced code translations {% cite abs-2012-07581 %}, and created a technique for building the datasets needed to train code translation models {% cite abs-2110-05423 %}.

In 2022, interactions with code-fluent language models primarily took the form of "push button, get results." We built the **Programmer's Assistant**, a tool that embedded a conversational LLM inside a code editor, to explore how software engineers felt about having conversational interactions around their code. In our evaluation, we found that developers valued the ability to ask both general programming questions and questions specific to their own code {% cite RossMHMW23 RossHMMW23 RossMMHW23 %}. While our paper was under review, ChatGPT was released in November 2022, demonstrating that our hypothesis was correct: LLMs reached a point where they could drive natural conversational interactions, and our work demonstrated that those interactions could be situated in a co-creative context: what we termed _artifact-grounded conversation_. Our work helped pave the way for the first generation of conversational AI coding assistants, including IBM's [watsonx Code Assistant](https://www.ibm.com/docs/en/wx-code-assistant/5.1.x?topic=overview), and our demo of the Programmer's Assistant received a Best Demo Honorable Mention award at IUI 2023.

In parallel with the development of watsonx Code Assistant (WCA), we built the **Agentic Code Explorer (ACE)**. ACE combined retrieval-augmented generation against a code repository with user modeling to produce personalized code explanations tailored to an individual programmer {% cite MoranBGHMBW25 %}.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/programmers-assistant.png" title="The Programmer's Assistant" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/ace-profile.png" title="A user profile in the Agentic Code Explorer" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Left: the Programmer's Assistant embeds a conversational assistant alongside a code editor {% cite RossMHMW23 %}. Right: the Agentic Code Explorer keeps a profile of each developer's roles and expertise, which it uses to tailor its explanations {% cite MoranBGHMBW25 %}.
</div>

During an internal deployment of an early version of WCA, we examined its use and impact on developer productivity. Counter to our expectations, we found that its most common use was not for generating code, but rather for _explaining_ it {% cite WeiszKMBGHB25 %}. Feedback from WCA's users also told us that its explanations were often verbose and not well-matched to their expertise. Together, these observations reinforced the ideas behind ACE and motivated new research into [personalized code explanations](#personalized-code-explanations).

Finally, we used speculative design methods to think about the future of AI-assisted software engineering. We wrote multiple design fictions, including one that probes the value tensions of pair programming with an AI {% cite MullerRHAMRTW22 MullerWHR24 %} and another that examines the role of the software engineer when they lose the ability to comprehend the code produced by AI {% cite abs-2511-05410 %}. This fiction was produced with [Story Arena](/projects/story_arena/), an environment I developed in which AI agents adopting various personas come together to collectively write design fictions.

### AI for designers

Generative AI opened new possibilities for creative and design work. In this space, we developed frameworks for mixed-initiative generative AI interfaces and studied opportunities for generative AI in design and UX work {% cite MullerWG20iccc HoudeLMMPRWZ20 HoudeRMAMRTW22 MullerCW23 MullerHW25 %}.

One example stems from our observation that designers spent a lot of time running group ideation sessions. Sometimes, these sessions would stall when people were quiet for uncomfortably long periods of time. Other times, people would make comments or suggestions that would have benefitted from having someone else in the room with a particular expertise or viewpoint. In response, we built two prototypes to explore how an LLM-based agent might participate in the group ideation process:

- **Koala** is a Slack bot that participates in group brainstorming discussions. It contributes ideas either _reactively_, when its name is mentioned, or _proactively_, when it judges that it has something valuable to add to the conversation. In an evaluation study, we found that participants preferred having Koala in their groups, and most of the top ideas that were generated in the brainstorm were shaped by both the participants and Koala {% cite MullerHGBRMW24 %}.
- **Collaborative Canvas** is a shared virtual canvas where people place digital stickies together, enhanced with the ability to generate & rewrite stickies using an LLM (like Mural, before they added AI features). Across multiple studies, design practitioners saw value in embedding AI into the canvas to fill in expertise gaps and break through lulls {% cite HeHGMRMW24 GonzalezMHHRMKW24 %}.

<div class="row justify-content-sm-center">
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/koala.png" title="Koala in a Slack brainstorming session" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/collaborative-canvas.png" title="The Collaborative Canvas" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Left: Koala contributes ideas to a brainstorming session in Slack {% cite MullerHGBRMW24 %}. Right: the Collaborative Canvas, where people and an LLM add sticky notes to a shared board {% cite HeHGMRMW24 %}.
</div>

These prototypes helped us develop a framework around how to design an AI agent's **participatory behaviors** in group conversations: when it should contribute, what and where, and who has control to change the agent's behavior {% cite HoudeBMRMGKFW25 %}.

### AI for data scientists

In 2018, automated machine learning (AutoML) tools were beginning to automate several portions of the data science lifecycle: feature engineering, model selection, and hyperparameter tuning. We were very keen to understand how data scientists would feel about these technologies: were they viewed as helpful or were they not to be trusted? We interviewed 20 data scientists about their perceptions of automated AI {% cite WangWMRGDTSG19 %}. Reactions were mixed: they worried about automation encroaching on their jobs and felt it was inevitable, yet they remained optimistic, because they saw the future of data science as a collaboration in which both automation and human expertise are indispensable. We then examined what information data scientists need to trust the models AutoML produces, which we measured as their willingness to deploy them. Adding transparency features to an AutoML tool increased both trust and understanding, and model performance metrics and visualizations mattered most {% cite DrozdalWWDYZMJS20 %}.

These findings shaped **IBM AutoAI**, a product that automates the end-to-end AI lifecycle while keeping humans in the loop {% cite WangRW0MWVCTSA20 WangAWOKSCVTD20 %}. We also developed AutoAIViz to visualize the pipelines that AutoAI generates {% cite WeideleWOMAGW20 %}, Model LineUpper to help data scientists interactively compare the models it produced {% cite NarkarZLWW21 %}, and AutoDS to explore human-centered automation of the broader data science workflow {% cite WangAWOD21 %}. We also built an AI system that generates documentation for data science code in computational notebooks and found that it helped data scientists document their code more quickly without sacrificing the quality of that documentation {% cite WangWDMPWLWD22 MullerWRWATHMRD21 %}. Finally, we reflected on how AI-assisted data science can cultivate human expertise rather than replace it {% cite WeiszM20 AndresWMWJSBDAP20 %}.

---

## Safe AI

_Developing AI that is safe requires identifying its risks and potential harms and helping both developers and users recognize and mitigate them._
{: .theme-blurb}

### Mapping the risks of AI

AI systems are probabilistic, so they make mistakes, and those mistakes can cause real harm when AI is used in high-stakes settings such as hiring, lending, and healthcare. A biased model can deny someone a loan; an inaccurate one can miss a diagnosis. Generative AI widened this risk landscape: alongside familiar risks such as bias, it introduced new ones, such as hallucination, harmful content, and the leakage of copyrighted or personal data. As generative AI entered the mainstream in 2023, I helped document its risks, their potential harms, and strategies for mitigating them. This material was incorporated into the [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas), which helps IBM's customers understand the AI risk landscape and make informed decisions about developing and deploying AI in their organizations.

### Factuality and transparency

Hallucination is one of the biggest risks of generative AI: LLMs can produce output that sounds confident but is wrong. Many groups, including IBM, developed quantitative methods for scoring the factuality of an LLM's output. But scores alone may be difficult to interpret; if a sentence scores "0.67 out of 1" for factuality, what does that really mean? We explored how to present factuality scores to people in ways that were easy to understand and interpret. Across two experiments, we found that people preferred and trusted a design that color-coded every phrase within an LLM's response by its factuality score, and they found this highlighting scheme the easiest to validate {% cite DoOGMWW25 abs-2405-20434 %}. Our results informed the design of evaluations in watsonx.governance.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/factuality-designs.png" title="Designs for displaying factuality scores" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Designs we tested for showing the factuality of an LLM's response, at the level of individual terms or whole phrases. Red marks content that is likely inaccurate and green marks content that is likely accurate {% cite DoOGMWW25 %}.
</div>

### Privacy

New technologies can erode people's privacy in ways they don't expect. When consumer drones took off in the mid-2010s, we conducted a large-scale survey of people's privacy expectations and fears regarding drones, along with how they felt about different privacy-preserving mitigations {% cite UchidiunoMW18 %}. Now, the rising popularity of AI agents is raising new privacy concerns, especially when people overshare sensitive information that isn't required to complete a task. With my colleagues at IBM, we examined ways to help people maintain _contextual privacy_: sharing sensitive information only within the contexts that require it, such as sharing medical information with your doctor but not your accountant. We developed methods that protect people from oversharing with conversational agents and a way to evaluate contextual privacy across agentic workflows {% cite NgongK0MWDR25 abs-2603-04902 %}.

### Trust

Why should someone trust an AI system to make a decision for them? Well before the popularity of generative AI, we set out to understand what made an AI-infused decision-making process trustworthy {% cite abs-1912-02675 %}. Trust is a complicated construct, and it can be examined _behaviorally_, by observing whether people act on an AI's recommendations, or _attitudinally_, by asking how willing people are to rely on it. We took the attitudinal view in our work and ran a crowdsourced study to examine people's willingness to trust AI across a variety of scenarios. People rated the trustworthiness of decision-making processes that ranged from a lower-stakes decision (planning meals) to a higher-stakes one (recommending a prison sentence). Across the scenarios, we varied factors such as the stakes of the decision, who had final authority over it, who trained the model, whether the model was interpretable, and how confident the model was in its recommendation. We found that people accepted AI more readily for lower-stakes decisions and for interpretable models. Information about how a model was trained and tested also increased their trust.

---

## Personal AI

_People construct mental models of AI systems that help them understand how to work with them effectively. Why can't AI systems do the same? Personal AI is about much more than personalization: it's about helping human-AI teams form a mutual understanding of each other to enable the team to accomplish goals that neither party could have accomplished alone._
{: .theme-blurb}

### Mutual theory of mind

Teams of people work well together when their members understand each other: they share common ground about what each person knows, and they can anticipate how their teammates will act. Yet, many human-AI teaming studies show that AI doesn't always deliver the performance gains we might expect. We hypothesized that human-AI teams would perform better if the human and the AI held a **mutual theory of mind**: when each party holds a model of the other's goals, knowledge, and reasoning, and uses it to predict how the other will behave. We used design fictions to envision both the promise and the pitfalls of an operationalized mutual theory of mind {% cite abs-2406-11946 %}. We also identified a difference between _literal_ theory of mind --- the ability to predict what another agent will do --- and _functional_ theory of mind --- the ability to adapt one's own behavior to that prediction --- and argued that many theory of mind LLM benchmarks were limited because they only focused on evaluating the former and not the latter {% cite RiemerA0D0WC25 %}.

To study mutual theory of mind in practice, we built **Wavelength.AI**, a version of the cooperative party game _Wavelength_ in which people play alongside an LLM-based agent. Wavelength's defining characteristic is that players must understand each other well to play well. We tested two interventions designed to help human-AI teams form a mutual theory of mind: introductions before play to establish common ground, and retrospectives in which players saw the reasoning behind each other's clues and guesses. In a preliminary study with 24 human-AI teams, teams that had both interventions tended to score higher than teams that did not, although the difference was not statistically significant. Players said that the introductions helped them give better clues and that the retrospectives helped them adjust their strategies {% cite MorrisonGARABW26 MorrisonABGW25tom4ai %}.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/wavelength.png" title="Wavelength.AI" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Wavelength.AI: a person and an LLM-based agent take turns giving clues and guessing where a target falls on a spectrum {% cite MorrisonGARABW26 %}.
</div>

---

## Intersections

The three themes of my research reinforce each other. AI is rarely useful if people can't trust it, and it is rarely trustworthy if it ignores who is using it. Some of my projects address these themes in tandem.

### Design principles for generative AI

_Useful AI · Safe AI · Personal AI_
{: .theme-tags}

Generative AI applications pose new design challenges stemming from their non-deterministic nature: their outputs can vary even given the same prompt, they can be confidently wrong, and when people overrely on incorrect outputs, the results can be harmful. I led a cross-IBM effort to distill research on human-AI collaboration and co-creation into a set of **design principles**, strategies, training materials, and exercises for designing generative AI applications {% cite WeiszHMHMG24 WeiszMHH23 WeiszHM25handbook %}. Our materials were used to train over 3,000 IBM design practitioners to work with AI as a design material.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/design-principles.png" title="Design principles for generative AI applications" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Six principles for designing generative AI applications. Three offer new interpretations of known issues in AI, and three address characteristics unique to generative AI {% cite WeiszHMHMG24 %}.
</div>

### Human-centered explainable AI

_Useful AI · Safe AI_
{: .theme-tags}

Explainable AI (XAI) research overwhelmingly treats AI as a black box to be opened: if only one could explain how the model operates (i.e. global explanations) and why the model made a specific prediction (i.e. local explanations), then explainability has been achieved and people can properly calibrate their trust in the model. But, models are increasingly becoming inscrutable (e.g. deep learning models, transformer-based LLMs), and explainability approaches such as training surrogate models (e.g. LIME) can only provide approximations of the model's actual behavior. Instead, we recognized that a wealth of information about a model's performance was present _outside_ of the black box, in the social and organizational contexts in which the model was being used. We introduced **social transparency** as a form of explainability in which information about whether a model's recommendations were followed or not, along with the reasons why, were captured and presented to other users to help them calibrate their trust {% cite EhsanLMRW21 %}. This work helped launch the field of human-centered explainable AI (HCXAI), which we have grown through a workshop series at CHI {% cite EhsanWWMRWDRR23 EhsanWWMHSWR25 EhsanAHLRW26 %}.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/social-transparency.png" title="Social transparency in an AI-mediated sales decision" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Social transparency in an AI pricing tool: alongside the AI's recommendation and its justification, salespeople see what their colleagues did with past recommendations, along with who acted, why, and when {% cite EhsanLMRW21 %}.
</div>

### AI attribution

_Useful AI · Safe AI_
{: .theme-tags}

When AI helps write source code or an essay, or creates an image, who should get credit for the work? Our norms for crediting human collaborators don't map neatly onto AI. In a scenario-based study, we found that people felt that AI does deserve credit for its contributions, although the amount of credit it deserves varies based on its contribution (e.g. synthesizing information or contributing new ideas deserves more credit than making grammatical changes). Thus, we learned that _how_ AI was used matters, not just _whether_ it was used. Yet, at the time, many organizational AI-use policies only required disclosing the fact of whether AI was used {% cite HeHW25 %}. In response, we built the [AI Attribution Toolkit](https://aiattribution.github.io/) to give content creators a more precise language for describing how AI contributed to their work. We then examined the social stigmas surrounding AI use and disclosure. Through a survey of workers who used AI, we found that disclosures stating one's compliance with AI policies, disclosures of how AI contributed, and disclosures that a human reviewed AI-generated content made people feel more comfortable disclosing their AI use. However, these disclosures were no more effective than a simple acknowledgment of AI use at changing whether people chose to disclose; shifting that decision may also require sociocultural enablers, such as messaging from leadership and the disclosure behaviors of peers {% cite HeADW26 %}.

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/attribution-statement-anatomy.png" title="Anatomy of an AI attribution statement" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Anatomy of an attribution statement from the <a href="https://aiattribution.github.io/">AI Attribution Toolkit</a>, which describes how much AI contributed, what it contributed, who initiated the work, whether a person reviewed the AI's content, and which AI application was used.
</div>

### Personalized code explanations

_Useful AI · Personal AI_
{: .theme-tags}

People differ in the ways they process information, how they learn, and how confident they feel with technology. Returning to the domain of software engineering, these observations imply that one-size-fits-all explanations of code won't be equally beneficial. We asked software engineers what kinds of information they wanted in their code explanations {% cite BrachmanG0HMW25 %} and found that there wasn't a single consistent answer: they wanted to configure the structure and level of detail of their explanations, and they wanted explanations that would personalize themselves automatically to their experience and goals. We then prompted an LLM to adapt its code explanations to five different problem-solving styles and found that explanations that matched a software engineer's style were more often beneficial, although not every matched adaptation helped {% cite abs-2503-11018 %}. Across 1,072 explanations from six LLMs, we uncovered 13 distinct ways in which the models adapted their language, forming a taxonomy of ways AI coding assistants could personalize their explanations to users as individuals {% cite AndersonPWBV26 %}.

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.liquid loading="lazy" path="assets/img/research/code-explanation-adaptation-ips.png" title="Code explanations adapted to information processing style" class="img-fluid rounded z-depth-1" zoomable=true avoid_scaling=true %}
    </div>
</div>
<div class="caption">
    Explanations of the same COBOL program from an LLM, both unadapted and prompted for selective or comprehensive information processing styles {% cite abs-2503-11018 %}.
</div>
