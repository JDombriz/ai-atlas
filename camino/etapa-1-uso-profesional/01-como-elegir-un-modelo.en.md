---
titulo: How to choose a model for a task
etapa: 1
orden: 1
pregunta: How is the model that suits a specific task chosen, with judgement and with numbers?
prerrequisitos: ["../etapa-0-fundamentos/05-donde-no-hace-falta-ia.md"]
ultima_revision: 2026-10-22
estado: publicado
traduccion_de: 2026-10-22
---

# How to choose a model for a task


<img src="../../assets/bandas/banda-e1-01-en.svg" alt="01" width="560">
> English translation of the Spanish original: [01-como-elegir-un-modelo.md](01-como-elegir-un-modelo.md). Spanish is the canonical text; this version follows the revision of 22 October 2026.

A support team takes in four thousand tickets a month and wants them classified by type before anyone reads them. The question that arrives is always the same: «which model do we use?». The useful answer is not a name. It is a procedure that fits in an afternoon and that, done properly, also leaves the cost worked out.

The same task, with the same input text, costs a hundred times more today on the frontier model than on the cheapest in the catalogue —$10 per million input tokens against $0.10— and on most closed tasks the result does not improve in that proportion. Choosing by the list of the cleverest is the quickest way to multiply the bill without it showing in the result.

## The question asked first

Before looking at any model there is one that rules itself out: **can the text leave the building?** If the answer is no, the discussion is over and two paths remain: a model with open weights running on your own infrastructure, or not doing this with a model at all.

This is not an abstract compliance question. A contract, a medical record, the staff list or the draft of a penalty notice do not get pasted into the text box of a service that has not signed where that data ends up. And «it has a privacy policy» is not the same as «it does not use them for training», which is not the same as «it does not keep them for thirty days», which is not the same as «it is processed in the European Union». Each of those four sentences is a different box on a different contract.

When the answer is yes, or when the model has open weights and runs at home, you move on to the rest.

## Five things that decide

**One. Whether the model is capable of the task.** Not whether it is good in general: whether it gets this specific task right. A model that wins on public leaderboards can lose at classifying tickets for a lift company, because that company's vocabulary is in no public test. Capability is measured, not opined.

**Two. How much text has to fit.** The context window is how many tokens the model sees at once. A million tokens is of the order of 600,000 to 700,000 words in Spanish: far more than almost anything needs, and rather less than it seems when a two-day conversation with documents pasted into it is dragged along. A huge window does not mean the model uses the middle of a thousand-page document well: that is checked, not assumed.

**Three. How long whoever uses it can wait.** Latency is not reliably deduced from price or from size. It is measured in the test itself, with the real load, in the hours it will be used. An excellent model that takes twenty seconds is no use for classifying while somebody waits in front of a screen.

**Four. What each use costs.** Billing is per token, splitting input and output, and output is the expensive part. In the catalogue of October 2026, almost all of them charge five to ten times more for output than for input; the small ones, one to one. A calculation that counts only input falls short by a factor of three or four on long answers.

**Five. What happens when it fails.** Every model fails. The question is not whether, but who detects it and what it costs. A wrong classification in a billing system and another in a press archive have different prices, and that price —not the price of the token— is what decides in many cases.

## The method, in four questions

**First: what has to come out right?** It is worth writing it down before testing anything: «90 % of tickets with the correct category, and none marked urgent that is not». Without that number, any model looks good on the first test and none on the third.

**Second: which is the cheapest that might do?** You start at the bottom. In the catalogue, that means trying a small model first —Ministral 3 3B or GPT-6 Luna, both at $0.10 per million input tokens— rather than a frontier one. The reason is not the saving: it is that if the cheap one hits, the decision is made and the rest of the time is saved. Moving up a model is easy; moving down, after everything has been built around it, is not.

**Third: how is it checked?** With a bench of your own, small and fixed: ten real examples with their expected answer, run through each candidate with the same instruction. The [recipe for the bench of ten cases](../../recetas/banco-de-diez-casos.en.md) sets it up in an afternoon and leaves you, besides, the cost per case.

**Fourth: what happens if it fails?** If the failure is expensive, the model cannot be the only filter: human review is needed, and that review has to go into the account. A system that gets 92 % right and needs the remaining 8 % reviewed is cheaper than one that gets 96 % right and costs twice as much per call, almost always.

## What each one costs, in October 2026

Prices per million tokens, verified on each vendor's pages on 2026-10-22. The context column is the window the vendor declares.

| Model | Input | Output | Context | Licence |
|:--|--:|--:|--:|:--|
| [Claude Fable 5.1](../../catalogo/modelos/claude-fable-5-1.md) | $10 | $50 | 1M | proprietary |
| [Claude Opus 5.5](../../catalogo/modelos/claude-opus-5-5.md) | $4 | $20 | 1M | proprietary |
| [GPT-6.1 Sol](../../catalogo/modelos/gpt-6-1-sol.md) | $2 | $10 | 1.05M | proprietary |
| [Gemini 4 Argon](../../catalogo/modelos/gemini-4-argon.md) | $2 | $10 | 1.05M | proprietary |
| [Mistral Large 3](../../catalogo/modelos/mistral-large-3.md) | $0.50 | $1.50 | — | Apache 2.0 |
| [GPT-6 Luna](../../catalogo/modelos/gpt-6-luna.md) | $0.10 | $0.50 | 1.05M | proprietary |
| [Ministral 3 3B](../../catalogo/modelos/ministral-3-3b.md) | $0.10 | $0.10 | — | Apache 2.0 |
| [Llama 4 Scout](../../catalogo/modelos/llama-4-scout.md) | no API price | — | 10M | Llama 4 Community |

## The small print that doubles the bill

Four things that are not in the headline and that change a decision.

- **The long-context band is charged.** In OpenAI's API, a request with more than 272,000 input tokens is billed at double the rate for input and cache, with output 50 % dearer, across the whole request. A two-hundred-page contract goes through there.
- **A price can carry an expiry date.** Gemini 4 Argon costs $2 and $10 until 30 November 2026; from 1 December, $4 and $20. An estimate made today is good for six weeks.
- **Cache is the big lever.** If the prompt is the same on every call —and on a repeated use it almost always is—, the repeated part is charged at a fraction: between 5 % and 10 % of input on OpenAI's models. At high volume, neglecting this costs more than choosing the wrong model.
- **Names change.** A specific model identifier —`gpt-6.1-sol`, `claude-opus-5-5`— has a retirement date that the vendor announces months, not years, ahead. The integration has to be written so the model can be changed without redoing the code.

## The usual stumbles

- **Choosing by the leaderboard.** It measures tasks similar to your own, not your own. It serves to rule out, not to decide.
- **Comparing input prices and forgetting output.** The most common arithmetic error, and the one that shows most on long answers.
- **Fixing an instruction or context problem with another model.** If the instruction is ambiguous, the expensive model misreads it too; it only misreads it more confidently. Before changing models, [the instruction](02-la-instruccion.en.md) and [the context](03-el-contexto.en.md).
- **Measuring with three sentences and a feeling.** Any model hits with three cases; with ten, and the expected answer written down, the difference starts to show.

## When it does not apply

- **When the task is deterministic.** If the rule can be written, the rule wins: it is free, it is auditable and it does not change on Tuesday. The negative criterion is in [Where artificial intelligence is not needed](../etapa-0-fundamentos/05-donde-no-hace-falta-ia.en.md).
- **When there is no way to check the result.** If nobody can say whether the answer is right without redoing the work, the model saves nothing: it moves the work.
- **When the volume is huge and the task trivial.** Classifying two million rows by a keyword already sitting in a column is not a model problem.

## Definitions

- **Context window**: the maximum number of tokens the model can take into account in a single request; it includes instruction, documents and answer.
- **Token**: the unit of text by which usage is measured and billed. Rule of thumb: in Spanish, between 1.3 and 1.5 tokens per word.
- **Price per million tokens**: the billing unit of models served over an API, with different rates for input and output.
- **Open weights**: a model whose parameters are distributed under a licence that allows them to be downloaded and run on your own infrastructure.
- **Proprietary model**: a model reachable only through the vendor's API, under its terms.
- **Bench of cases**: a small, fixed set of examples with their expected answer, used to compare models by the same yardstick.

## References

- Catalogue cards: [Claude Fable 5.1](../../catalogo/modelos/claude-fable-5-1.md), [Claude Opus 5.5](../../catalogo/modelos/claude-opus-5-5.md), [GPT-6.1 Sol](../../catalogo/modelos/gpt-6-1-sol.md), [GPT-6 Luna](../../catalogo/modelos/gpt-6-luna.md), [Gemini 4 Argon](../../catalogo/modelos/gemini-4-argon.md), [Mistral Large 3](../../catalogo/modelos/mistral-large-3.md), [Ministral 3 3B](../../catalogo/modelos/ministral-3-3b.md), [Llama 4 Scout](../../catalogo/modelos/llama-4-scout.md) — each with its official URL and its verification date.
- Rates: the pricing pages of OpenAI, Anthropic, Google and Mistral — consulted on 2026-10-22. The figures on this page carry that date because they expire.
- Own check — the eight model pages and the four pricing pages returned 200 on an HTTP request on 2026-10-22. No API has been called and no latency measured: timings have to be measured case by case.

## Continue

- Previous: [The trade in 2026](../etapa-0-fundamentos/06-el-oficio-en-2026.en.md)
- Next: [The instruction: asking well and getting something usable](02-la-instruccion.en.md)
- Stage index: [Stage 1 — Professional use](README.en.md)
- Subject index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Last reviewed: 2026-10-22.*
