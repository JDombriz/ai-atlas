---
titulo: "The instruction: asking well and getting something usable"
etapa: 1
orden: 2
pregunta: What does an instruction have so that the answer can be used as it stands, and what is missing from one that cannot?
prerrequisitos: ["01-como-elegir-un-modelo.md"]
ultima_revision: 2026-10-22
estado: publicado
traduccion_de: 2026-10-22
---

# The instruction: asking well and getting something usable


<img src="../../assets/bandas/banda-e1-02-en.svg" alt="02" width="560">
> English translation of the Spanish original: [02-la-instruccion.md](02-la-instruccion.md). Spanish is the canonical text; this version follows the revision of 22 October 2026.

A team asks for forty supplier contracts to be summarised and for whatever binds them to be kept. The summary comes back impeccable: three paragraphs per contract, well written, with the parties, the subject and the amount. Nobody notices until the audit that the model has not written a single line about the late-delivery penalty clause, which is exactly what had to be found.

The model did not fail. The request failed: «a summary» was asked for and a summary was delivered. A summary puts in what seems important; to find a clause you have to ask about the clause, say where to look, demand the quotation and ask for a format that can be checked at a glance.

## What the model sees when it is asked for something

In an API call, the model remembers nothing from the previous one. It receives a text —the instruction, the documents, whatever history is passed to it— and returns a probable continuation of that text. Everything it is meant to take into account has to be in there. Anything that is not, does not exist.

Hence a practical consequence that saves arguments: the instruction **is** the programme. If one word changes and the result gets worse, it is not magic or randomness: the programme has been changed and it had to be tested again.

## The five parts of an instruction that works

**Context.** What this text is and what the answer is for. «You are the assistant of a purchasing department; the documents that follow are supplier contracts in force» orients more than any adjective about tone.

**Task.** One, in the imperative, with the precise verb. «Extract» is not «analyse»; «list» is not «summarise». If the task has two parts, they go in two calls: it is cheaper than one instruction doing two things badly.

**Output format.** How the answer is wanted: a table with these columns, one line per ticket with this separator, a JSON with these keys. It is the part most often forgotten and the one that saves most time, because it turns the answer into something that can be reviewed, sorted or fed into a process.

**One example.** Just one, the right size: an input and the output considered correct. It is worth more than three paragraphs describing the same thing, especially on format tasks. Two or three examples improve the result in classification; twenty usually make it worse, because they spend context and confuse.

**Acceptance criterion.** The sentence that allows a decision on whether the answer is good: «if the contract does not mention penalties, write ‹not stated›; do not infer it». Without a criterion, the model fills the gap with what sounds plausible, which is precisely what cannot be used.

## Order matters

Stable things first —the role the model plays, the rules, the format— and at the end what changes on each call: the document, the ticket, the question. For two reasons: attention concentrates on what is read last and, on models that bill for cache, an identical prefix is charged at a fraction. Ordering the instruction with the fixed part in front makes repeated use cheaper without touching the result.

## A before and an after

The same task, two requests. The first is the one written in a hurry and the one that produces the useless summary from the beginning.

> Summarise this contract and tell me what matters.

The second takes a minute longer to write and returns something reviewable.

> You are the assistant of a purchasing department. The text that follows is a supplier contract in force.
>
> Extract only three things: the committed delivery term, the penalty for late delivery (amount or percentage) and the renewal conditions. For each one, cite the clause and reproduce the sentence verbatim.
>
> Format: a table of three rows with the columns «Item | Clause | Verbatim sentence». If an item does not appear, write «not stated» in the clause column. Do not infer or fill in with what is usually the case.
>
> Example row: `Penalty for late delivery | Clause 7.2 | «...»`

What has changed is not the politeness: it is four decisions —a bounded task, a format, one worked example and a rule for the gap— and an explicit prohibition on inventing.

## What is fixed once and what is asked each time

Almost every vendor separates two messages: a system one, which defines the role and the rules and stays the same, and a user one, where what changes goes. The separation has three concrete advantages: the fixed prefix can be cached, the rules are not forgotten on the third turn, and the variable text stays clean to log.

What goes in the fixed part: role, limits —what it must not do—, default format and acceptance criterion. What goes in the variable part: the document, the question, the data for the case. And one hygiene rule: never paste into the variable message an instruction that contradicts the fixed one. When they contradict each other, the last one read wins, and that turns a system into a lottery.

## Length is not a virtue

A forty-line instruction is not maintained: nobody remembers why each sentence is there and it gets edited blind. Eight or twelve lines cover most office tasks, and if more are needed it is almost always a sign that two tasks are mixed together. A long instruction also carries a hidden cost: it is paid on every call and it takes up context needed for the document.

## The usual stumbles

- **Asking for a «professional tone» and believing that is an instruction.** It does not change the content, which is what is usually wrong.
- **Not specifying the format and then complaining about the format.** If the answer goes into a spreadsheet, ask for the spreadsheet, not for a correct paragraph.
- **Changing two things at once.** When it gets worse, there is no knowing which one did it. One variable per test.
- **Confusing detail with length.** One exact fact in the instruction is worth more than five adjectives.

## When it does not apply

- **If the fact is not in the text, the instruction does not create it.** Asking «find the penalty» in a contract that has none only produces a well-written invention. That is the ground of the limits of the model, which closes the stage with its page 5.
- **If the task is deterministic**, a rule or a query does the work with no cost per call and no variation between runs.
- **If the model is small and the instruction long**, it will not follow it: three-billion-parameter models answer well to short formats and examples, and badly to competing numbered rules.

## Definitions

- **System instruction**: the message that fixes role, rules and format, and stays the same between calls.
- **Output format**: the shape demanded of the answer —table, JSON, separated list— so it can be used without rewriting.
- **Acceptance criterion**: the condition that allows a decision on whether the answer serves; it includes what to do when a fact is missing.
- **Example (one or few shots)**: pair of input and correct output included in the instruction to fix format and criterion.

## References

- *Building effective agents* — Anthropic, 2024 — <https://www.anthropic.com/engineering/building-effective-agents> (consulted 2026-10-22). Cited for its criterion of starting with the simple; it is vendor documentation, not a neutral source.
- [Ministral 3 3B](../../catalogo/modelos/ministral-3-3b.md) — catalogue card, for the limit of small models facing long instructions.
- Own check — the two addresses on this page returned 200 on an HTTP request on 2026-10-22. The five-part method rests on no single source: it is craft practice, and what can be checked is the result, with the [bench of ten cases](../../recetas/banco-de-diez-casos.en.md).

## Continue

- Previous: [How to choose a model for a task](01-como-elegir-un-modelo.en.md)
- Next: [The context: what it is given and in what order](03-el-contexto.en.md)
- Stage index: [Stage 1 — Professional use](README.en.md)
- Subject index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Last reviewed: 2026-10-22.*
