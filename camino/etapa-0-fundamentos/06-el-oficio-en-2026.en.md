---
titulo: The craft in 2026
etapa: 0
orden: 6
pregunta: What changes and what does not change for those who write software, according to the available evidence?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md, 04-que-es-y-que-no-es-un-agente.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de: 2026-10-10
---

# The craft in 2026


<img src="../../assets/bandas/banda-06-en.svg" alt="Stage 0" width="560">
> English translation of the Spanish original: [06-el-oficio-en-2026.md](06-el-oficio-en-2026.md). Spanish is the canonical text; this version follows the revision of 10 October 2026.

This stage closes by answering what those who already program ask most: what all this translates into in their daily work. The answer has three parts, and it is worth not mixing them: what changes in an observable way, what does not change and remains the responsibility of whoever deploys, and what the available evidence allows us to assert today — which is considerably less than the noise suggests.

The page also fixes the starting point for the following stages. If the craft consisted only of writing code, there would be nothing more to tell. What has shifted is where the bottleneck lies.

## What changes

**Writing the first version ceases to be the bottleneck in bounded tasks.** Drafting a function, transforming data, writing tests, translating code between languages: the time to the first draft shrinks clearly when the task has a checkable success criterion. It is a real saving, and an easy one to notice.

**The limit shifts to review and judgement.** Producing more code than can be reviewed is not productivity, it is inventory. The ability to read, understand and accept changes comes to determine the team's pace.

**The specification gains value.** The more precise the description of the expected result, the better any assistance works. Writing the problem well ceases to be a virtue and becomes the main lever.

**The work is shared between whoever builds and whoever evaluates.** Roles appear that previously did not have that name: designing the set of cases, measuring, instrumenting, watching the cost, and deciding what is automated and what is not.

**The debt changes place.** Besides the code, one must maintain instructions, contexts, permissions, connected tools and provider dependencies. None of that travels in the repository unless someone decides that it should.

**Cost enters the design.** A system that pays per operation has a constraint that traditional software did not have. It is managed from day one, or it is not managed at all.

## What does not change

A system is judged by what it does. The quality of the assistance does not alter the criterion: in production, what counts is observable behaviour.

Responsibility lies with whoever deploys. No tool signs, approves a deployment or answers for an incident. The allocation of permissions remains a human and explicit decision.

Security, access control and traceability remain prerequisites. That the system has more autonomy enlarges the problem; it does not replace it.

The fundamentals explain the failures. Data structures, networking, databases, concurrency, distributed systems: incidents in systems with models occur, for the most part, in the surrounding software.

Understanding is not delegated. Whoever accepts a change they do not understand is taking on a debt that they will pay at the next incident, with interest.

And professional judgement is not a configuration option. Deciding what is done, with what data and with what limits is the work, not a prior step to the work.

## What the evidence says, and with what limits

Here it is worth being more cautious than in the rest of the page, because the noise is enormous. Three useful references, each with its own scope:

| Study | What it measured | Result | Limit |
|:--|:--|:--|:--|
| Impact of assistance on productivity, 2023 | Controlled experiment: implementing an HTTP server in JavaScript, with and without assistance | The group with assistance finished the task 55.8 % faster | A small, isolated task with the specification closed; it does not represent everyday work |
| Productivity of experienced developers in mature projects, 2025 | Randomised trial with 16 open-source developers, 246 tasks in repositories they had known for about five years | Allowing assistance **increased** resolution time by 19 %, against the forecast of a 20 % improvement that the participants themselves had expressed | Small sample, mature projects with high standards and early-2025 tools |
| SWE-bench, since 2023 | Test bench with more than two thousand real issues from open-source repositories | It measures the proportion of issues genuinely resolved, verified by their own tests | It measures a specific capability, not usefulness in a team nor the cost of maintaining the result |

What can be asserted with this: performance depends greatly on the context; in closed and verifiable tasks the improvement is large; in mature projects with demanding standards and prior knowledge, assistance can slow things down.

> [!WARNING]
> What **cannot** be asserted: general figures for productivity improvement, comparisons between tools, or that the trend is stable.

Industry reports, such as those from the DORA programme, provide an overall view through surveys and serve to place trends, not to decide about a specific team.

## How to work with this

A simple criterion, applicable today and without new tools: **yes to assistance where the result can be checked cheaply and the action is reversible.**

| Situation | Reasonable assistance |
|:--|:--|
| Task with a clear automated test | Yes: writing, refactoring, extending tests |
| Documentation, examples, error messages | Yes, with review by whoever signs the text |
| Exploring an unfamiliar library or interface | Yes: it speeds up orientation, which must then be verified in the official documentation |
| Repetitive migrations with a clear pattern | Yes, in batches and with a check after each batch |
| Architecture or security decisions | Not as a decision: yes as a comparison of options, with expert review |
| Irreversible changes in production | Not without human review and a path back |
| Code that nobody is going to review | No: it is the case where the cost of error has no ceiling |
| Regulated domains or those with sensitive data | Requires prior analysis of the provider's conditions and the applicable framework |

In any case, sending code or data to an external service is a decision of the organisation, not of the user who has the tool installed. It is worth knowing this before trying it, and not afterwards.

## The usual stumbles

- **Measuring lines of code or number of changes.** Neither of the two measures value, and both can be inflated effortlessly.
- **Accepting changes that are not understood.** Today's saving is tomorrow's incident, and it is paid at the least opportune moment.
- **Generalising the result of a demonstration.** Studies with closed tasks and those of mature projects point in different directions: the difference is in the context, not in the tool.
- **Ignoring the terms of use.** What is sent, to whom, with what retention and with what licence over the result are questions that precede adoption.
- **Confusing speed of production with speed of delivery.** If review is the bottleneck, speeding up writing only moves the queue.
- **Failing to record what the system did.** Without a trace, it is impossible to reconstruct why something changed or to correct the process.

## When it does not apply

This page describes the craft, not the tools of the day. The choice of specific models, with their prices and limits, is a matter for Stage 1 (Professional use, in preparation); the design of stateful workflows, for Stage 2 (Engineering, in preparation); and operation, evaluation and control of spending, for Stage 4 (Production, in preparation).

Nor does it claim to predict the near future. Recent years discourage any extrapolation: almost all the quantitative forecasts of the last four years have fallen short or overshot in a very short time.

## Definitions

- **Code assistance**: use of a model that proposes changes which a person reviews before incorporating them.
- **Case-based evaluation**: a set of cases defined before knowing the result, with their acceptance criterion.
- **Configuration debt**: accumulated maintenance in the instructions, contexts, permissions and connected tools of a system with models.
- **Execution trace**: an ordered record of what the system did and with what result, necessary to reconstruct an incident.
- **Human review**: the step in which a person accepts, corrects or rejects the result of a system before it has consequences.
- **Review cost**: the time and effort of checking results; it adds to the cost of producing them and often exceeds it.

## References

- *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* — S. Peng, E. Kalliamvakou, P. Cihon and M. Demirer, 2023 — <https://arxiv.org/abs/2302.06590> (consulted 2026-10-10)
- *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* — J. Becker, N. Rush, E. Barnes and D. Rein (METR), 2025 — <https://arxiv.org/abs/2507.09089> (consulted 2026-10-10)
- *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* — C. Jimenez and others, 2023 — <https://arxiv.org/abs/2310.06770> (consulted 2026-10-10)
- *DORA — annual research on software delivery performance* — Google Cloud (survey-based reports; they do not amount to a controlled experiment) — <https://dora.dev/research/> (consulted 2026-10-10)
- *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* — NIST, 2023 — <https://doi.org/10.6028/NIST.AI.100-1> (consulted 2026-10-10)
- Own check — the above addresses returned status code 200 in an HTTP request on 2026-10-10

## Continue

- Previous: [Where artificial intelligence is not needed](05-donde-no-hace-falta-ia.en.md)
- Next: [Stage practice: analysis of three of your own processes](practica.en.md)
- Stage index: [Stage 0 — Fundamentals](README.md)
- Thematic index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe, assisted by AI. Last reviewed: 2026-10-10.*