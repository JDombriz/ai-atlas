---
titulo: "The context: what it is given and in what order"
etapa: 1
orden: 3
pregunta: If the model does not remember, what is handed to it on each call, how much, and in what order?
prerrequisitos: ["02-la-instruccion.md"]
ultima_revision: 2026-10-22
estado: publicado
traduccion_de: 2026-10-22
---

# The context: what it is given and in what order


<img src="../../assets/bandas/banda-e1-03-en.svg" alt="03" width="560">
> English translation of the Spanish original: [03-el-contexto.md](03-el-contexto.md). Spanish is the canonical text; this version follows the revision of 22 October 2026.

There is a conversation everyone has had. Half an hour is spent explaining a matter to the assistant, with nuances, figures and a decision taken halfway through; coming back in the afternoon, the answer ignores half the conversation. The natural reaction is «it has forgotten». The real explanation is more uncomfortable and more useful: **it never knew it by heart**. On each call it is handed a text, and that text has a ceiling.

Understanding this changes how you work. It stops being a matter of trust and becomes a matter of arithmetic and order: what goes in, how much it takes up, and what is left out.

## What the model sees on each call

In an API call there is no memory. The model receives a composed text —system instruction, history, documents, question— and returns a continuation. The conversation seen on screen is a montage the application makes: it resends the previous turns on every call, whole or trimmed.

That is why two products with the same model behave differently on the same long conversation: one trims the oldest part, another summarises when it fills up, another does nothing and fails. The behaviour is not in the model; it is in what the application decides to put in the window.

## Context is a budget

The context window is declared in tokens and varies widely: 1.05 million in GPT-6.1 Sol, 1.05 in Gemini 4 Argon, 10 million in Llama 4 Scout. In Spanish, a million tokens is of the order of 600,000 to 700,000 words.

Three consequences that get forgotten:

- **It is paid for.** Everything sent is billed as input, used or not. Pasting the whole two-hundred-page contract to ask about a date costs the same as reading the whole contract, and sometimes more: above 272,000 input tokens, OpenAI's API bills double for the whole request.
- **It degrades.** That the window admits a million tokens does not mean the model uses the middle of a million tokens well. Information sitting in the middle of a very long text is used worse than what is at the beginning and at the end. The fact that matters should be kept close to the question.
- **It displaces.** Every paragraph pasted takes up room needed for something else. A context full of old history leaves today's document out.

## What goes in and what is left out

The priority order that works in practice, from what contributes most to what contributes least:

1. **The instruction and the rules.** Always, and always the same, so they can be cached.
2. **The data for the case.** The document, the record, the ticket, the specific fragment.
3. **What was decided earlier and still stands.** Two lines, not twenty: «the client accepted the 15 March deadline; the rest is still open».
4. **The format example.** One, short.
5. **The previous conversation.** Last and trimmed. It can almost always be replaced by item 3 written by hand, and it comes out better.

What is left out without remorse: the pleasantries, the model's answers that contributed nothing, the «could you repeat that?», the old versions of the document and everything already summarised in item 3.

## Order: stable in front, what changes at the end

An identical prefix on every call can be cached and is charged at a fraction —between 5 % and 10 % of input on OpenAI's models—. That imposes a discipline which also improves the result: **role, rules and format first; document and question afterwards**. The part that changes, at the end, where the model has it closest.

## Long documents: four ways, and what each costs

- **Paste it whole**, if it fits in the window. It is the simplest and the most expensive per call; it makes sense if the document is read once.
- **Cut it by sections** and make one call per chunk, joining afterwards. It costs several calls, each small, and requires an instruction that returns a fixed format so the results can be joined.
- **Find the fragment and cite it.** The paragraph is located —by keyword or by similarity search— and only that is passed, with its reference. This is what a retrieval system does, and it belongs to Stage 2; by hand, with two files and a search tool, it already solves half the cases.
- **Summarise in two passes.** A first pass that extracts what is relevant from each chunk and a second that works on those extracts. Cheap and faithful if the extraction is verbatim; dangerous if the first pass summarises from memory, because the error is carried forward and can no longer be checked against the original.

The choice between the four is not a matter of taste: it is calculated. Tokens of the document per call, multiplied by the input price, against the cost of cutting and joining.

## Why it «forgets» mid-conversation

Three different causes that get confused into one:

- **Trimming.** The application discards the oldest messages when the window fills. What was said at the beginning disappears without warning.
- **Automatic summarisation.** Some assistants compress the conversation when it fills. That summary is made by another model and loses exactly what it judged secondary: amounts, conditions, exceptions.
- **Dilution.** Even with everything fitting, information in the middle of a very long text is used worse.

All three are fought the same way: if something matters, it is not left to the conversation's memory. It is written in item 3 of the previous list, in two lines, and it is resent.

## When to start from scratch

Starting a new conversation and re-pasting what is needed is cheaper than carrying on, in three cases:

- **When the conversation has filled up** with failed attempts. Dragging them costs money and confuses: the model sees its own mistakes as context.
- **When the task changes.** A context that mixes two matters produces answers that mix the two.
- **When the result has turned odd for no apparent reason.** It is almost always a context saturated with old versions; a clean call confirms it in ten seconds.

What has to be carried into the new conversation is a paragraph: current state, decisions taken, data that still stands. Writing it by hand costs two minutes and saves an afternoon.

## The usual stumbles

- **Pasting everything «just in case».** It costs, it displaces and it worsens the focus. Context is not an archive: it is what is handed to someone who is going to read it once.
- **Trusting that the conversation remembers.** What is not resent does not exist; and what is resent trimmed exists by halves.
- **Ordering it backwards.** Putting the document in front and the rules behind is the most common and the worst working: besides losing the cache, it leaves the rules far from the question.
- **Fixing a context problem with a bigger model.** If the fact is missing, no window solves it.

## When it does not apply

- **If the task fits in a paragraph**, this page is surplus: paste the paragraph and ask.
- **If the problem is the instruction**, no ordering of context fixes it: see [The instruction](02-la-instruccion.en.md).
- **If remembering between sessions is needed** —preferences, histories, documents that change—, that is persistent memory and retrieval, and it is Stage 2 material.

## Definitions

- **Context**: all the text handed to the model on a call: instruction, history, documents and question.
- **Context budget**: the distribution of the available space among those parts, with its cost in tokens.
- **Prompt cache**: the discount a vendor applies when the prefix of the request is identical to the previous one's.
- **Trimming**: discarding the oldest messages when the conversation exceeds the window.
- **Retrieval**: locating the relevant fragment before calling the model, instead of sending it the whole document.

## References

- [GPT-6.1 Sol](../../catalogo/modelos/gpt-6-1-sol.md), [Gemini 4 Argon](../../catalogo/modelos/gemini-4-argon.md) and [Llama 4 Scout](../../catalogo/modelos/llama-4-scout.md) — catalogue cards with the context window declared by each vendor, verified on 2026-10-22.
- Rates and the 272,000-token rule: OpenAI pricing table — <https://developers.openai.com/api/docs/pricing> (consulted 2026-10-22).
- Own check — the addresses on this page returned 200 on an HTTP request on 2026-10-22. The window figures are those each vendor declares; the effective use of a very long context has not been measured on this page and is worth measuring on the task itself.

## Continue

- Previous: [The instruction: asking well and getting something usable](02-la-instruccion.en.md)
- Next: The cost of a repeated use — *in preparation*
- Stage index: [Stage 1 — Professional use](README.en.md)
- Subject index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Last reviewed: 2026-10-22.*
