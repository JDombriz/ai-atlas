---
titulo: Exercise — analysis of three processes of your own
etapa: 0
orden: 99
pregunta: How do you decide, in writing, which of your own processes do not need artificial intelligence?
prerrequisitos: [05-donde-no-hace-falta-ia.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de: 2026-10-10
---

# Exercise — analysis of three processes of your own

> English translation of the Spanish original: [practica.md](practica.md). Spanish is the canonical text; this version follows the revision of 10 October 2026.

## What has to be delivered

Choose three real processes from your work and analyse them one by one, in writing. In **at least one of the three** the conclusion has to be that a model is not needed. If all three end in "yes", the analysis has not been done with judgement: almost every environment has processes that are solved with rules, with a query or with a person and a checklist.

A process works as a candidate if it repeats, has an identifiable owner and can be described in less than a page. Some common ones: preparing a periodic report, classifying incoming mail, reconciling two listings, reviewing applications against known criteria, extracting data from documents with a stable format.

Nothing has to be implemented. What is delivered is the analysis, not the system. And you do not need to be an engineer to do it: it is an exercise in judgement, and it is done better with someone who truly knows the process than with someone who knows the technology.

## How it is done

1. **Choose the three processes.** It is worth making one of them small and mechanical: it serves to check that the discard criterion is applied also where there is no merit in automating.
2. **Describe the current process** in five lines: what goes in, what comes out, who does it today, how much time it consumes and how often it repeats.
3. **Run the eight discard conditions** from [page 5](05-donde-no-hace-falta-ia.en.md), one by one, and note the result of each. The ones that hold are the basis of the verdict.
4. **Estimate roughly** the current cost —person-hours per month— and, if the conclusion is that a model is indeed needed, the expected cost per operation and that of reviewing its errors.
5. **Propose the alternative** for the discarded processes: rules, a query, a search, a classifier, a checklist or leaving it as it is.
6. **Write the verdict in one sentence**, in terms of what is done and why.

## Analysis template

| Section | Content |
|:--|:--|
| Process | Name and one line of description |
| What goes in and what comes out | Inputs, outputs and the format of each |
| Who does it today | Person or team, and with what tool |
| Volume | Cases per week or per month |
| Current cost | Hours per month, estimated from an explicit basis |
| Known and stable rule | Yes or no, and in what part of the process |
| Accuracy or determinism required | Yes or no, and what breaks if the output varies |
| Cost of the error | What happens if the output is incorrect and whether it can be undone |
| Available data | What examples exist, how many and with what usage restrictions |
| Admissible latency and cost per operation | Approximate figure for the environment |
| Verdict | Model, rules, query, person or leaving it as it is |
| Proposed alternative | What would be used instead and at what cost |
| Reason for the verdict | One sentence, with the criterion that decides it |

## A worked example

A simple case is included, from a racing workshop, to fix the level of detail expected. It is not a template to be copied: it is a sample of how an analysis is closed.

| Section | Content |
|:--|:--|
| Process | Reconciling the suppliers' parts delivery notes against the month's invoices |
| What goes in and what comes out | Delivery notes and invoices go in; the list of differences and the approved payment come out |
| Who does it today | The administration person, with the spreadsheet |
| Volume | Around 120 lines a month, from about fifteen suppliers |
| Current cost | Three hours a month, based on two sessions of an hour and a half |
| Known and stable rule | Yes: reference, quantity and price, with zero tolerance on the reference |
| Accuracy or determinism required | Yes, entirely: the amount paid has to be exact |
| Cost of the error | High in the sense of trust with the supplier, and reversible only with a claim |
| Available data | Those of the billing system; there are no labelled examples of discrepancies |
| Latency and cost per operation | No latency restriction; the volume does not justify a cost per use |
| Verdict | **Rules and a query.** No model at all |
| Proposed alternative | Comparison rules on the billing export and an exception alert for the lines that do not reconcile |
| Reason for the verdict | The rule is known, it is stable and the result has to be exact: it is exactly the case where a model is superfluous |

## How to know whether it is finished

The exercise is finished when you can answer yes to all of the following without reading the pages again:

- [ ] There are three processes described, with an owner and a volume.
- [ ] At least one of the three concludes that a model is **not** needed, with the discard condition that decides it.
- [ ] Each verdict names its alternative and, if it is another method, why it is preferable.
- [ ] The cost and volume figures have an explicit basis: if they are estimates, it says what they are estimated from.
- [ ] No section is left blank and no box is ticked without justification.

The review of the document itself is deliberately severe, and on purpose: in this area, the difference between an analysis and an opinion is that the analysis can be argued point by point.

## The usual stumbling blocks

- **Choosing three processes whose answer is already known.** The exercise is useful when one of the three admits an uncomfortable answer.
- **Filling in the template without figures.** "A lot of volume" is not a datum. If there is no measurement, you estimate and you say where the estimate comes from.
- **Mistaking the process for the tool.** "Automating mail" is not a process. The process starts at a concrete input and ends at a concrete output.
- **Skipping the cost of the error.** It is the section that changes the most decisions and the one that is most often omitted.
- **Turning the verdict into a personal preference.** The criterion is written before deciding; if the verdict forces you to change the criterion, the decision had been made in advance.

## When it does not apply

This exercise does not replace a business analysis or a formal risk assessment: it is an exercise in judgement with the information at hand. If the three processes chosen are irreversible or subject to regulation, the analysis is limited to documenting why in that context human oversight is needed, and it is worth adding at least one low-risk process in order to apply the discard conditions as normal.

## Definitions

- **Automation candidate**: a repetitive process, with an owner, identifiable inputs and outputs, suitable for comparing methods.
- **Basis of the estimate**: the datum from which a figure comes; if it does not come from any measurement, the estimate and its origin are declared.
- **Verdict**: a written decision about the method that corresponds to a process, with its reason in one sentence.

## References

- *Rules of Machine Learning: Best Practices for ML Engineering* — M. Zinkevich, Google — <https://developers.google.com/machine-learning/guides/rules-of-ml> (consulted 2026-10-10)
- *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* — NIST, 2023 — <https://doi.org/10.6028/NIST.AI.100-1> (consulted 2026-10-10)
- Own verification — the addresses above returned code 200 on an HTTP request on 2026-10-10

## Continue

- Previous: [The craft in 2026](06-el-oficio-en-2026.en.md)
- Stage resources: [Resources](recursos.en.md)
- Stage index: [Stage 0 — Fundamentals](README.md)
- Thematic index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe, assisted by AI. Last reviewed: 2026-10-10.*