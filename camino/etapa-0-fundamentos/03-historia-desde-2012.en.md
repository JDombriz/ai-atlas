---
titulo: From AlexNet to agents — the history since 2012
etapa: 0
orden: 3
pregunta: What changed from 2012 onwards, what each piece used today is, and what of all this the atlas covers?
prerrequisitos: [02-historia-hasta-2012.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de: 2026-10-10
---

# From AlexNet to agents: the history since 2012


<img src="../../assets/bandas/banda-03-en.svg" alt="Stage 0" width="560">
> English translation of the Spanish original: [03-historia-desde-2012.md](03-historia-desde-2012.md). Spanish is the canonical text; this version follows the revision of 10 October 2026.

From 2012 onwards the vocabulary fills up with words that are used without defining them: deep learning, transformer, pretraining, preference tuning, multimodal, reasoning model, agent. This stretch places each one in its moment and explains what made it possible for things to be done differently. It is, too, the part of the history that ages fastest, and that is why it carries a review date in the header. What came before 2012 no longer moves; what has happened in the last three years does.

## 2014 · Sequences stop having a fixed length

Two papers from the same year make it possible to translate a sequence of any length into another: the encoder–decoder architecture, and a few months later the attention mechanism, which lets the decoder look at each part of the input. In parallel, generative adversarial networks frame generative learning as a competition between two networks.

**What changed.** Text and audio no longer demand language-specific engineering. Attention, which in 2014 was a useful addition, would three years later become the entire architecture.

## 2015 · Depth stops being a problem

Residual connections make it possible to train networks of more than a hundred layers without the error degrading as it accumulates. In that year's image recognition competition, the resulting network drops below 4 % error, under the human performance estimated for that task in the competition's own report, around 5 %.

**What changed.** A perception task is solved in practical terms. Designing architectures by hand loses value next to stacking blocks and letting the data and the connections do the work.

## 2017 · Games and self-play

The system that beats the human Go champion combines neural networks with search and reinforcement learning over its own games. Its successor learns without human games, playing against itself.

**What changed.** It is demonstrated that reinforcement learning, with a well-defined environment and an unambiguous victory signal, produces superhuman performance. And its limit is demonstrated too: that environment has to be built, and in real problems it almost never exists that cleanly.

## 2017 · The transformer

*Attention Is All You Need* removes recurrence and builds the entire model on self-attention, so that all the elements of a sequence are processed in parallel. Training becomes far more efficient on matrix hardware, and the architecture becomes domain-independent.

**What changed.** It is the central piece of everything that comes after: text, image, audio and code. The idea that sustains the rest of the path is that a general architecture, trained at large scale, is then adapted to very different tasks.

## 2018 · Pretrain and fine-tune

BERT fixes the recipe that becomes widespread: train a general model on large volumes of unlabelled text and then fine-tune it, with little labelled data, for each specific task.

**What changed.** Knowledge is reused across tasks and the cost of a new system drops. The first clear division of the trade also appears: those who train models and those who adapt them.

## 2020 · From model to assistant

The work on scaling laws shows that error falls in a regular way as data, parameters and computation grow, and that the balance between them matters: a model that is too large for its data is wasted. In 2020, a model with 175,000 million parameters shows that a new task can be solved **without retraining anything**: it is enough to describe it in the input and give a few examples.

**What changed.** In-context learning separates two concepts that until then went together. A model is the trained artifact; an assistant is the system that wraps it and gives it instructions and context. Adapting stops being retraining and becomes writing an input. It is the frontier that explains why stages 1 and 2 of this material are different: using context well is one trade, and training is another.

## 2021 and 2022 · Image and speech follow the same path

A model that learns to relate images to text descriptions makes it possible to classify images without having been trained for the specific class. Diffusion becomes established as a method of image generation and, by 2022, the technique moves from the laboratory to tools of general use. In speech, a model trained on an enormous quantity of audio transcribes without prior fine-tuning for each domain.

**What changed.** The pattern repeats in every modality: a general model, trained with lots of unlabelled data, and later adaptation by instruction. Multimodality stops being an exotic capability and becomes the normal case.

## 2022 · Preference tuning and the conversational assistant

A 2022 paper shows that fine-tuning a model with human preferences makes it much more useful: it follows instructions, keeps to the format and refuses requests. At the end of that year, a product based on that technique puts a conversational assistant within everyone's reach, with no installation and no technical knowledge.

**What changed.** The audience changes before the technique does. Adoption stops depending on knowing how to program and conversation becomes the interface. Here begins the problem that this material addresses: many people using the system, and very few knowing what it does, what it costs and when it should not be used.

## 2022 · Reasoning out loud and using tools

Two papers from the same year close the stage. The first shows that asking the model to make its intermediate steps explicit improves its performance on multi-step problems. The second combines that reasoning with actions on external tools in a loop: think, act, observe and think again.

**What changed.** The pattern that underpins agentic systems appears, and with it the question answered by [page 4](04-que-es-y-que-no-es-un-agente.en.md). Stage 3 is built on this point.

## 2023 · Scale, openness and evaluation

A multimodal model reaches human-level results on professional reference tests. That same year, models with downloadable weights and an explicit licence are published, along with small models that compete with much larger ones thanks to efficiency decisions. In evaluation, a benchmark built from real issues in software repositories appears: the first credible measure of "solving a real problem" rather than "passing an exam".

**What changed.** Capability stops being the bottleneck, and evaluation takes its place. Open weights transfer control of cost and privacy to the user, not responsibility: the licence and the terms of use still belong to the maker. And the comparison between models starts to be made with tests that resemble real work.

## 2024 and more recently · Inference compute, standardised tools and agents

Two changes mark this stretch. The first is the deliberate use of computation at the moment of answering — models that generate long intermediate steps before giving the answer, trained by reinforcement learning to do so — so that quality depends on how much the system is allowed to think, and so does the cost. The second is the standardisation of access to tools and data through a common protocol, which separates the tool from the product and makes it possible to reuse it across different assistants.

**What changed.** The frontier shifts from "what the model knows" to "what the system can do, with which permissions and at what cost". It is exactly the ground of stages 2 to 4. And regulation comes into play: the European artificial intelligence regulation, in force since August 2024, applies its obligations in phases and affects above all those who deploy in sensitive domains.

> [!NOTE]
> No figures are asserted about the immediate present. There is no consolidated public figure that allows us to say how much team productivity has changed, and the available studies measure different things in different settings. The [study cited on page 6](06-el-oficio-en-2026.en.md) is the best example that these measures have to be read with care.

## What this material covers and what it leaves out

It covers, with the six stages of the path, what is needed to understand, use, design, operate and defend a system of this kind: the fundamentals, professional use, engineering, agentic patterns, production and specialisation.

It deliberately leaves out: original research and training models from scratch; the hardware and infrastructure of data centres; robotics and embedded systems; institutional history and the philosophy of mind; and the full treatment of ethics and policy, which appears only where it conditions engineering decisions. The reason is the same in every case: these are fronts that demand complete dedication and that this material would not cover with the depth it promises.

## Three things this stretch teaches

1. **It was not one idea, it was three things at once.** Data, computation and architecture. Any of them on its own would not have been enough, and that explains why the predictions of recent years fail in both directions.
2. **The bottleneck moves.** First it was the model's capability; then evaluation; now cost, permissions and reliability. Whoever optimises for the bottleneck of two years ago is solving a problem that no longer exists.
3. **The technique and the product do not advance at the same pace.** Mass adoption arrived with an interface, not with a leap in capability. It is worth looking at the two things separately.

## Definitions

- **Deep learning**: set of methods that train networks with several intermediate layers, so that representations are learned rather than designed.
- **Transformer**: architecture based on self-attention that processes the whole sequence in parallel; it underpins most current models.
- **Self-attention**: mechanism by which each element of a sequence is weighted against all the others to build its representation.
- **Pretraining**: general training on large volumes of unlabelled data, prior to any adaptation to a task.
- **Fine-tuning**: additional training of an already pretrained model for a specific task, domain or behaviour.
- **In-context learning**: the ability to solve a new task from examples and instructions included in the input itself, without modifying the parameters.
- **Fine-tuning with human feedback (RLHF)**: method that fine-tunes a model with human comparisons between answers, so that it is more useful and behaves as expected.
- **Diffusion model**: generative model that produces an image starting from noise and applying successive denoising steps.
- **Multimodal**: system capable of working with more than one type of content, for example text and image.
- **Scaling laws**: empirical relationships that describe how error falls as data, parameters and training computation increase.
- **Reasoning model**: model trained to produce extensive intermediate steps before answering, so that its quality depends on the computation it is allowed to spend.
- **Model Context Protocol (MCP)**: open specification for connecting a model with tools and data sources in a way that is reusable across products.
- **Context window**: maximum amount of text that a model can take into account in a single query.

## References

- *Sequence to Sequence Learning with Neural Networks* — I. Sutskever, O. Vinyals y Q. Le, 2014 — <https://arxiv.org/abs/1409.3215> (consulted 2026-10-10)
- *Neural Machine Translation by Jointly Learning to Align and Translate* — D. Bahdanau, K. Cho y Y. Bengio, 2014 — <https://arxiv.org/abs/1409.0473> (consulted 2026-10-10)
- *Generative Adversarial Networks* — I. Goodfellow et al., 2014 — <https://arxiv.org/abs/1406.2661> (consulted 2026-10-10)
- *Deep Residual Learning for Image Recognition* — K. He et al., 2015 — <https://arxiv.org/abs/1512.03385> (consulted 2026-10-10)
- *ImageNet Large Scale Visual Recognition Challenge* — O. Russakovsky et al., 2014 (includes the estimated human performance on the task) — <https://arxiv.org/abs/1409.0575> (consulted 2026-10-10)
- *AlphaGo Zero: starting from scratch* — DeepMind, 2017 (vendor note; the paper *Mastering the game of Go without human knowledge* is in *Nature*, behind a paywall) — <https://deepmind.google/discover/blog/alphago-zero-starting-from-scratch/> (consulted 2026-10-10)
- *Attention Is All You Need* — A. Vaswani et al., 2017 — <https://arxiv.org/abs/1706.03762> (consulted 2026-10-10)
- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* — J. Devlin et al., 2018 — <https://arxiv.org/abs/1810.04805> (consulted 2026-10-10)
- *Language Models are Unsupervised Multitask Learners* — A. Radford et al., 2019 — <https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf> (consulted 2026-10-10)
- *Scaling Laws for Neural Language Models* — J. Kaplan et al., 2020 — <https://arxiv.org/abs/2001.08361> (consulted 2026-10-10)
- *Training Compute-Optimal Large Language Models* — J. Hoffmann et al., 2022 — <https://arxiv.org/abs/2203.15556> (consulted 2026-10-10)
- *Language Models are Few-Shot Learners* — T. Brown et al., 2020 — <https://arxiv.org/abs/2005.14165> (consulted 2026-10-10)
- *Learning Transferable Visual Models From Natural Language Supervision* (CLIP) — A. Radford et al., 2021 — <https://arxiv.org/abs/2103.00020> (consulted 2026-10-10)
- *Denoising Diffusion Probabilistic Models* — J. Ho, A. Jain y P. Abbeel, 2020 — <https://arxiv.org/abs/2006.11239> (consulted 2026-10-10)
- *High-Resolution Image Synthesis with Latent Diffusion Models* — R. Rombach et al., 2021 — <https://arxiv.org/abs/2112.10752> (consulted 2026-10-10)
- *Robust Speech Recognition via Large-Scale Weak Supervision* — A. Radford et al., 2022 — <https://arxiv.org/abs/2212.04356> (consulted 2026-10-10)
- *Training language models to follow instructions with human feedback* — L. Ouyang et al., 2022 — <https://arxiv.org/abs/2203.02155> (consulted 2026-10-10)
- *Introducing ChatGPT* — OpenAI, 30 November 2022 (original vendor announcement; archived copy, because the address answers 403 to automated requests) — <https://web.archive.org/web/2023/https://openai.com/blog/chatgpt/> (consulted 2026-10-10)
- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* — J. Wei et al., 2022 — <https://arxiv.org/abs/2201.11903> (consulted 2026-10-10)
- *ReAct: Synergizing Reasoning and Acting in Language Models* — S. Yao et al., 2022 — <https://arxiv.org/abs/2210.03629> (consulted 2026-10-10)
- *GPT-4 Technical Report* — OpenAI, 2023 — <https://arxiv.org/abs/2303.08774> (consulted 2026-10-10)
- *Llama 2: Open Foundation and Fine-Tuned Chat Models* — H. Touvron et al., 2023 — <https://arxiv.org/abs/2307.09288> (consulted 2026-10-10)
- *Mistral 7B* — A. Jiang et al., 2023 — <https://arxiv.org/abs/2310.06825> (consulted 2026-10-10)
- *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* — C. Jimenez et al., 2023 — <https://arxiv.org/abs/2310.06770> (consulted 2026-10-10)
- *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning* — D. Guo et al., 2025 — <https://arxiv.org/abs/2501.12948> (consulted 2026-10-10)
- *Introducing the Model Context Protocol* — Anthropic, 2024, and the protocol specification — <https://www.anthropic.com/news/model-context-protocol> y <https://modelcontextprotocol.io/introduction> (consulted 2026-10-10)
- *Regulation (EU) 2024/1689* — Official Journal of the European Union — <https://eur-lex.europa.eu/eli/reg/2024/1689/oj> (consulted 2026-10-10)
- Own check — all the above addresses returned status code 200 on an HTTP request on 2026-10-10

## Continue

- Previous: [From Turing to AlexNet: the history up to 2012](02-historia-hasta-2012.en.md)
- Next: [What an agent is and what it is not](04-que-es-y-que-no-es-un-agente.en.md)
- Stage index: [Stage 0 — Fundamentals](README.md)
- Thematic index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe, assisted by AI. Last reviewed: 2026-10-10.*