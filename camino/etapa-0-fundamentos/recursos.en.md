---
titulo: Stage 0 resources
etapa: 0
orden: 100
pregunta: Which external resources are worth reading to close out the fundamentals, and when is each of them not worth it?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de: 2026-10-10
---

# Stage 0 resources


<img src="../../assets/bandas/banda-recursos-en.svg" alt="Stage 0" width="560">
> English translation of the Spanish original: [recursos.md](recursos.md). Spanish is the canonical text; this version follows the revision of 10 October 2026.

## How this page is organised

None of these resources is compulsory for closing the stage: the exit criterion is demonstrated with the [exercise](practica.en.md), not with readings. This selection serves two purposes: knowing where what the pages state comes from —everything that can be checked has its source— and having somewhere to go on when a topic awakens curiosity.

Each entry carries the reason it is here and the case in which it is not worth reading. The latter is as useful as the former: there are admirable documents that at this stage waste your time.

> [!NOTE]
> **Delivery note (26 October 2026).** The twelve seed cards are now in the catalogue: the eight sources under «The sources that sustain the stage» and the four under «Evidence on the trade». Each title links to its card, and the link to the source is kept beside it. The six criteria readings are incorporated in a later delivery.

## The sources that sustain the stage

| Resource | Why it is here | When not to read it |
|:--|:--|:--|
| [*Computing Machinery and Intelligence*](../../catalogo/investigacion/turing-1950.md) — Turing, 1950 ([accessible copy](https://www.csee.umbc.edu/courses/471/papers/turing.pdf)) | The text where the problem is posed in a checkable way and where the idea of learning instead of programming knowledge appears | If you are looking for a technical introduction: it is a discussion article, with mathematical sections included |
| [Dartmouth workshop proposal](../../catalogo/investigacion/dartmouth-1955.md) — 1955 ([document](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf)) | The documentary origin of the term and of the expectation that sets the tone of the following two decades | If history does not interest you: it is understood far better told in [page 2](02-historia-hasta-2012.en.md) |
| [*Language and Machines*](../../catalogo/investigacion/alpac-1966.md) — ALPAC report, 1966 ([PDF](https://www.mt-archive.net/ALPAC-1966.pdf)) | It explains, with a concrete case, why funding follows demonstrable results | If you are looking for the current state of machine translation: it is a historical document |
| [Lighthill report](../../catalogo/investigacion/lighthill-1973.md) — 1973 ([original](https://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm)) | The documentary origin of the first winter: what the field was reproached with and on what grounds | Read in isolation it is taken for a definitive verdict on artificial intelligence; it is best accompanied by the context of [page 2](02-historia-hasta-2012.en.md) |
| [*Rule-Based Expert Systems: The MYCIN Experiments*](../../catalogo/investigacion/mycin-1984.md) — Buchanan and Shortliffe, 1984 ([full text](https://shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm)) | The best documented case of knowledge written by hand: what worked, what it cost to maintain and why it never reached daily use | It is a book: it is consulted by chapters, not read in full at this stage |
| [*R1: An Expert in the Computer Systems Domain*](../../catalogo/investigacion/r1-1980.md) — McDermott, 1980 ([archived PDF](https://web.archive.org/web/20171116060857/http:/aaai.org/Papers/AAAI/1980/AAAI80-076.pdf)) | The move of expert systems into industry, with the real problem they solved | If you are looking for a modern evaluation: it is a technical report of its time |
| [*Learning from Artificial Intelligence's Previous Awakenings*](../../catalogo/investigacion/brock-2018.md) — Brock, *AI Magazine*, 2018 ([article](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2809)) | A synthesis of the rise and decline of the expert-systems cycle, with its economics | It is a historical review, not a primary source: it orders things very well, but it is no use for citing the original datum |
| [*The Mathematics of Statistical Machine Translation*](../../catalogo/investigacion/brown-1993.md) — Brown and others, 1993 ([ACL Anthology](https://aclanthology.org/J93-2004/)) | The work that shows data displacing hand-written linguistic knowledge | It is dense in notation; the idea can be taken from [page 2](02-historia-hasta-2012.en.md) |

## Readings of judgement

| Resource | Why it is here | When not to read it |
|:--|:--|:--|
| *The Bitter Lesson* — Sutton, 2019 ([essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)) | The argument that explains why large-scale learning has been gaining ground over hand-written knowledge | It is a polemical essay, not an experimental result: it is read as a thesis, not as proof |
| *Rules of Machine Learning* — Google ([guide](https://developers.google.com/machine-learning/guides/rules-of-ml)) | Directly applicable negative criteria: why data engineering and evaluation weigh more than the model | It is written for classical machine learning; in language models, some rules read differently |
| *Hidden Technical Debt in Machine Learning Systems* — Sculley and others, 2015 ([NIPS](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)) | It documents that the model is the small part of the system and where the real cost accumulates | It is an engineering article, not an introduction: it presupposes some familiarity with systems in production |
| *Building effective agents* — Anthropic, 2024 ([guide](https://www.anthropic.com/engineering/building-effective-agents)) | Operational recommendation: start with the simple and add complexity only when it prevents a known failure | It is a vendor's documentation: useful for its criteria, not as a neutral source |
| [AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) — NIST, 2023 | The reference framework for talking about risk, evaluation and human oversight with a common vocabulary | It is not a technical document and does not go into architectures |
| [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | The framework that conditions what can be deployed and with what obligations, by phases | Reading it in full exceeds this stage: it is consulted by definitions and by risk classes |

## Evidence on the craft

| Resource | Why it is here | When not to read it |
|:--|:--|:--|
| [*The Impact of AI on Developer Productivity*](../../catalogo/investigacion/copilot-devprod-2023.md) — 2023 ([arXiv](https://arxiv.org/abs/2302.06590)) | An example of a controlled experiment on a closed task, with a clear improvement in time | It does not represent everyday work: the task is bounded and specified |
| [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](../../catalogo/investigacion/metr-2025.md) — METR, 2025 ([arXiv](https://arxiv.org/abs/2507.09089)) | The opposite case, in mature projects with expert developers: the result contradicts the expectation | Small sample and specific context: it is cited for what it measures, not as a general conclusion |
| [*SWE-bench*](../../catalogo/investigacion/swe-bench-2023.md) — 2023 ([arXiv](https://arxiv.org/abs/2310.06770)) | How a real capability is evaluated today: repository issues with their own tests | It measures resolution of issues, not the usefulness or the cost within a team |
| [DORA research](../../catalogo/investigacion/dora-research.md) — Google Cloud ([site](https://dora.dev/research/)) | An overall view of team practices and performance, by annual survey | They are surveys, not experiments: they serve to situate trends |

## If you lack the craft

The resources for covering what is taken for granted —Python, Git, terminal, JavaScript— are in the [starting point](../00-punto-de-partida.en.md), with their rough time. They are not part of this stage and are not reviewed here.

## How this selection is maintained

The links are checked automatically every week. When one goes down, the page is still valid: the reference is replaced and, if there is no substitute, it is withdrawn with the reason noted in [`CHANGELOG.md`](../../CHANGELOG.md). No address on this page requires registration or payment.

## The usual stumbling blocks

- **Reading the sources before the pages.** The natural order is the opposite: the pages situate the problem and say what to look for in each source. Read first, a good part of the historical material turns out incomprehensible.
- **Taking reviews for primary sources.** The *AI Magazine* article and the vendor guides order things very well, but they do not replace the original document when you want to cite a datum.
- **Reading the stage as a bibliography.** It is not a list of compulsory readings: it is a selection with a reason and with a limit.
- **Citing without a consultation date.** Every reference in this material carries the date on which it was checked; a reference without a date does not tell you whether it is current.

## When it does not apply

This selection covers the fundamentals and the general criteria. It is no use for choosing a model, a tool or an architecture: that belongs to the following stages. Nor does it include paid training material, courses or videos: the project's rule is that every reference be accessible without registration or payment and, where possible, primary.

## References

- Own verification — the addresses on this page were checked over HTTP on 2026-10-22. All returned 200 except two: the canonical edition of Turing's article in *Mind* (403, paywall; an open copy is linked) and the Dartmouth workshop proposal, whose host (`jmc.stanford.edu`) refused the connection that day —it returned 200 on 2026-10-10— and is accompanied by a copy in the Internet Archive. The European Regulation, among the criteria readings, returns 202 with an anti-automation challenge: it is verified in a browser
- The full references, with author, body and consultation date, appear at the end of each page of the stage

## Continue

- Previous: [Exercise — analysis of three processes of your own](practica.en.md)
- Stage index: [Stage 0 — Fundamentals](README.md)
- Next stage: Stage 1 (Professional use, in preparation)
- Thematic index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Last reviewed: 2026-10-10.*