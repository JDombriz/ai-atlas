---
titulo: Building a bench of ten cases before choosing a model
cuando: A choice has to be made between two or more models, or the one already in use has to be checked
etapa_relacionada: 1
tiempo_estimado: 2-3 h
ultima_revision: 2026-10-22
estado: borrador
traduccion_de: 2026-10-22
---

# Recipe: building a bench of ten cases before choosing a model

> English translation of the Spanish original: [banco-de-diez-casos.md](banco-de-diez-casos.md). Spanish is the canonical text; this version follows the revision of 22 October 2026.

> **When to use it:** when a model has to be chosen for a repeated task, or when someone asks «can AI do this well?» and the conversation starts to rest on impressions.

## Assumptions

- There is a specific task that repeats: classifying tickets, extracting three fields from a contract, drafting the reply to a notice.
- At least ten real cases are available, with their correct result known. Ten is the minimum; twenty is better and thirty adds nothing.
- There is access to the API or the interface of at least two models, and a spreadsheet or twenty lines of Python.
- The task is not deterministic: if it can be solved with a rule, [neither this bench nor the model is needed](../camino/etapa-0-fundamentos/05-donde-no-hace-falta-ia.en.md).

## Steps

1. **Collect ten real cases, not invented ones.** Take them from the real queue, preferably the dull ones and the ones that caused trouble. A bench of easy cases measures what was already known.
2. **Write the correct answer for each one, by hand, before testing anything.** Whoever knows the task writes it; if there is argument over which answer is right, that case does not go into the bench yet. This is the step almost nobody takes, and it is the one that turns the exercise into a test.
3. **Fix the acceptance criterion per case, binary.** Right or wrong, not a score out of ten: with three models and ten cases, halfway marks only produce argument. If a case admits two valid answers, note which ones.
4. **Freeze the instruction and the format.** The same instruction, word for word, for every model, with its output format and its «not stated» rule. If the instruction changes between models, the test no longer compares models: it compares instructions. See [The instruction](../camino/etapa-1-uso-profesional/02-la-instruccion.en.md).
5. **Start with the cheapest.** Run the small model first —Ministral 3 3B or GPT-6 Luna, both at $0.10 per million input tokens— and then the others, in order of price. Keep the ten answers from each one exactly as they came, without correcting them.
6. **Record four columns per run:** hits out of ten, call time, input tokens and output tokens. Cost is calculated afterwards; tokens have to be written down because the provider charges for them whether anyone looks or not.
7. **Calculate the cost per case and per thousand cases.** Input at its price, output at its own —usually five to ten times dearer— and, if the case calls for it, the long-context band. The result goes in the same table as the hits, not in another sheet.
8. **Decide with the rule written in advance.** Ninety per cent or more hits on the cheap model: do not move up. Below eighty: move up. Between eighty and ninety: the cost of the error decides, not the average. The rule is written before seeing the results, because afterwards there is always a reason to adjust it.
9. **Note the date and the exact version of the model tested.** Identifiers change and versions are retired: a bench with no date is a bench that has to be repeated without knowing it.

## How to know it went well

The bench has done its job if it produces a table of two rows and three columns: model, hits out of ten, cost per thousand cases. And if that table allows the original question to be answered in one sentence, with a number in it: «the small model gets 90 % right and a thousand cases cost €2.40; the big one gets 93 % and costs €240».

If there is no number in the sentence, there is no decision: there is a preference.

## When not to do this

- **With fewer than ten real cases.** With three, any model hits; with ten the difference starts to show and with twenty it settles.
- **When nobody knows what the right answer is.** Without that step beforehand, the test measures which answer is liked best, which is a different thing.
- **When the task is done once a month.** The bench costs two hours; if the annual saving does not pay for them, it is not built.
- **To compare models by their public leaderboard.** There are tables for that; this recipe is for your own task, which is in none of them.

## Further reading

- [How to choose a model for a task](../camino/etapa-1-uso-profesional/01-como-elegir-un-modelo.en.md) — the five variables and the small print of the prices.
- [The context: what it is given and in what order](../camino/etapa-1-uso-profesional/03-el-contexto.en.md) — why the same test with more text changes the result.
- Cards of the models cited: [GPT-6 Luna](../catalogo/modelos/gpt-6-luna.md), [Ministral 3 3B](../catalogo/modelos/ministral-3-3b.md), [Claude Opus 5.5](../catalogo/modelos/claude-opus-5-5.md).

---

*Pepe. Last reviewed: 2026-10-22.*
