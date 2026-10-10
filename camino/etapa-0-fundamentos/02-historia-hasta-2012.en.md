---
titulo: From Turing to AlexNet — the history up to 2012
etapa: 0
orden: 2
pregunta: Where does artificial intelligence come from, and what technical consequence did each milestone before 2012 leave behind?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de: 2026-10-10
---

# From Turing to AlexNet: the history up to 2012

> English translation of the Spanish original: [02-historia-hasta-2012.md](02-historia-hasta-2012.md). Spanish is the canonical text; this version follows the revision of 10 October 2026.

The errors of today are explained by decisions that were made sixty years ago. Almost every debate that keeps repeating — whether knowledge should be written by hand or learned from data, whether more computation is enough or more structure is needed, why the money comes and why it goes — was already had back then, and was resolved in a concrete way for reasons worth knowing. Whoever does not know that the winters existed is surprised every time the next one appears.

This account proceeds by consequences: what changed in practice after each milestone and what ceased to be necessary. The winters count as much as the summers. The second half of the story — from 2012 to today — is on the [next page](03-historia-desde-2012.en.md).

## 1950 · Turing turns an impossible question into a test

In *Computing Machinery and Intelligence*, Turing replaces "can a machine think?" with a game: an interrogator converses in writing with two interlocutors and has to distinguish which of them is the machine. He does not propose a machine — he builds nothing — but an observable criterion and an orderly discussion of the objections that would be raised against it.

At the end of the paper he drops the idea that would have the longest reach: instead of trying to simulate the adult mind, it may be more practical to simulate a child's and educate it.

**What changed.** The problem becomes testable, and it is admitted for the first time that programming experience may be more viable than programming knowledge. It would take forty years to demonstrate.

## 1955 · Dartmouth: the name is born and so is the expectation

The proposal for the Dartmouth summer workshop, signed by McCarthy, Minsky, Rochester and Shannon, uses the expression *artificial intelligence* for the first time. And it formulates a very bold conjecture: that every aspect of learning can be described with such precision that a machine comes to simulate it. About ten people attended the workshop.

**What changed.** The term is coined — in a workshop proposal, not in a journal article — and with it an expectation that would take decades to correct: that this was a matter of one summer's work.

## 1958 · Rosenblatt and the perceptron

The perceptron learns to classify from examples, with a simple correction rule applied to a single layer of units. It even came to be built in hardware.

**What changed.** The alternative to written knowledge appears: instead of rules, examples and an adjustment procedure. It is the first operative formulation of machine learning, and the starting point of everything that follows.

## 1966 · The ALPAC report and the first withdrawal of the money

A United States committee evaluates the machine translation programs of the time and concludes that they match human translation neither in quality nor in cost. Funding for the field is cut.

**What changed.** It is demonstrated that money follows demonstrable results and not promises. And it leaves a prejudice that would take decades to undo: that machine translation does not work.

## 1969 · The critique that halted an entire line

*Perceptrons*, by Minsky and Papert, demonstrates the limits of single-layer networks: there are functions they cannot represent, and the classic example is exclusive disjunction. The book is accurate in what it asserts, but the reading made of it was much broader than what it said: it was concluded that adding layers was useless, when what was missing was a method to train them.

**What changed.** The connectionist line loses funding for almost two decades and the effort shifts to symbolic systems. The theorem was true; the conclusion drawn from it, false.

## 1972 · DENDRAL: knowledge, written by hand

At Stanford, the DENDRAL project encodes the constraints of mass spectrometry to propose chemical structures, and its continuation Meta-DENDRAL learns rules from data. It is the first expert system in the modern sense.

**What changed.** The thesis that dominates the following twenty years is established: the bottleneck is not reasoning, it is knowledge. And if it has to be written by hand, writing it is expensive.

## 1973 · The Lighthill report and the first winter

The report commissioned by the United Kingdom concludes that artificial intelligence had not delivered what it promised and that there was no basis for sustaining the spending. British funding is drastically reduced and a good part of the research is redirected.

**What changed.** The first winter arrives: between 1974 and 1980 funding contracts, groups dissolve and the expression becomes uncomfortable in budgets. The cause was not a lack of ideas, but the gap between what was promised and what was delivered.

## 1976 · MYCIN and the lesson that was not learned

MYCIN, also at Stanford, advises on antimicrobial therapy with several hundred rules that incorporate certainty factors. In the published evaluations its behaviour is comparable to that of specialists in the selected cases. It never reached routine clinical use.

**What changed.** Two lasting lessons. The first, that reasoning with uncertainty is tractable. The second, the uncomfortable one: a system that gets it right is not enough. Integration with the hospital's systems, a legal owner and, above all, a sustainable way of keeping the knowledge up to date were missing. Sixty years later we still call it evaluation and operation.

## 1980 · XCON: knowledge enters industry

At Digital Equipment Corporation, the R1 system — later XCON — configures orders for VAX systems: it checks compatibilities and produces the list of components. It was put into production and the company maintained its own knowledge engineering department to keep it going.

**What changed.** Expert knowledge goes from being an object of research to being a commercial asset, and the cycle of the 1980s begins: boom, expert-tool companies, oversized expectations. The cycle broke for an economic and not a technical reason: the rule bases grew to thousands of rules, each change forced a review of the whole set, and product lines changed faster than the knowledge could be maintained. The savings figures cited from that period come from testimony and from the company itself, not from auditable accounts.

## 1986 · Backpropagation brings learning back to the centre

Rumelhart, Hinton and Williams publish the method for adjusting the weights of networks with intermediate layers, calculating the contribution of each to the final error. The algorithm was known in other disciplines; what was missing was showing it working in useful networks.

**What changed.** The obstacle of 1969 disappears. Multilayer networks return to research on a sound footing, though without enough data or computation to compete with symbolic systems on real problems.

## 1998 · Convolutional networks and a solved task

The LeNet family recognises handwritten digits with an architecture that exploits the structure of the image — convolutions and downsampling — instead of treating each pixel separately. It came to be used in automatic cheque reading in the United States.

**What changed.** It is demonstrated that certain perception problems are solved better by learning from data than by writing rules. The method, however, does not scale with the volume of data and computation available then. The same architecture, with twenty years more data and with graphics processors, would be the one that won in 2012.

## 1993 · Statistical translation: data beats rules

IBM's translation models estimate, from parallel corpora, the probability that a sentence in one language corresponds to another. Without hand-written grammars and without explicit linguistic knowledge, they outperform rule-based systems.

**What changed.** The statistical turn becomes general in industry: search engines, mail filters and speech recognition come to be built on data. The lesson would repeat: when there is enough data, the method that exploits it displaces the one that encodes knowledge by hand.

## 1997 · Deep Blue: brute force, not learning

IBM's system beats Garry Kasparov by evaluating positions with a function written by experts and exploring millions of moves per second. There is no learning involved.

**What changed.** The victory showed the value of specific design and massive computation, and also its limit: the result did not transfer to any other problem. That pattern — spectacular milestone, zero transfer — repeats every decade, and it is worth remembering every time a new one appears.

## 2012 · ImageNet, graphics cards and the cut

The ImageNet dataset gathers millions of labelled images and, since 2010, an annual competition compares systems on the same task. In 2012, the network of Krizhevsky, Sutskever and Hinton reduces the error of the best previous system abruptly: 15.3% error against 26.2% for the second-placed entry. The work relied on graphics cards — two consumer units, adapted for matrix computation — and on architecture decisions such as the ReLU activation function and dropout.

**What changed.** Three things coincide for the first time: labelled data at scale, cheap and parallel computation, and an architecture trainable in depth. From then on, feature engineering ceases to be the main craft in computer vision: representations are learned. Here we cut the story, because since 2012 the discussion about what to encode by hand loses weight on almost all fronts.

## Three things this stretch teaches

1. **The winters have concrete causes.** They were not mysterious pauses: what was funded and what was researched changed. Lighthill's diagnosis of the gap between promise and delivery was reasonable; the error of the time was to promise ahead of the evidence.
2. **Every advance is a coincidence of three things.** The idea, the data and the machine. In 2012 convolutions and multilayer networks had been invented for decades; what arrived were the data and the processors.
3. **A milestone solves a bounded problem, not the problem.** Deep Blue taught nothing about language; digit recognition was no use for reading a contract. It is worth distrusting anyone who announces that the latest result changes everything.

## Definitions

- **Imitation game**: test proposed by Turing in which an interrogator must distinguish, in writing, between a machine and a person.
- **Expert system**: program that solves a bounded problem by reproducing the knowledge of specialists, written in the form of rules.
- **Perceptron**: single-layer classifier that learns its weights from examples.
- **Connectionism**: line of work that models learning with networks of simple connected units, as against the manipulation of symbols.
- **Backpropagation**: method for calculating how each weight of a multilayer network contributes to the final error, which allows them to be adjusted.
- **AI winter**: period of contraction in funding and institutional interest, with economic and expectation-related causes.
- **Feature engineering**: the craft of designing by hand the variables a system will use to decide, partly replaced by learned representations.
- **Knowledge acquisition bottleneck**: the difficulty of extracting knowledge from a specialist and writing it in a form usable by a program.
- **Convolutional network**: network that exploits the spatial structure of the input, applying the same filter at different positions.

## References

- *Computing Machinery and Intelligence* — A. M. Turing, *Mind*, vol. LIX, no. 236, 1950 — accessible copy at <https://www.csee.umbc.edu/courses/471/papers/turing.pdf> (accessed 2026-10-10)
- *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence* — J. McCarthy et al., 1955 — <http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf> (accessed 2026-10-10)
- *The perceptron: a probabilistic model for information storage and organization in the brain* — F. Rosenblatt, *Psychological Review*, 1958 — accessible copy at <https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf> (accessed 2026-10-10)
- *Perceptrons: An Introduction to Computational Geometry* — M. Minsky and S. Papert, MIT Press, 1969 — printed work; no open edition has been found (accessed 2026-10-10)
- *Language and Machines: Computers in Translation and Linguistics* (ALPAC report) — National Academy of Sciences, 1966 — <https://www.mt-archive.net/ALPAC-1966.pdf> (accessed 2026-10-10)
- *Artificial Intelligence: A General Survey* (Lighthill report) — J. Lighthill, 1973 — <https://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm> (accessed 2026-10-10)
- *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project* — B. Buchanan and E. Shortliffe (eds.), 1984 — <https://shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm> (accessed 2026-10-10)
- *R1: An Expert in the Computer Systems Domain* — J. McDermott, AAAI 1980 (archived copy of the original; technical report CMU-CS-80-119 is the extended version and has no stable open edition) — <https://web.archive.org/web/20171116060857/http:/aaai.org/Papers/AAAI/1980/AAAI80-076.pdf> (accessed 2026-10-10)
- *Learning from Artificial Intelligence's Previous Awakenings: The History of Expert Systems* — D. C. Brock, *AI Magazine*, 39(3), 2018 — <https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2809> (accessed 2026-10-10)
- *Learning representations by back-propagating errors* — D. Rumelhart, G. Hinton and R. Williams, *Nature*, vol. 323, 1986 — accessible copy at <https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf> (accessed 2026-10-10)
- *Gradient-Based Learning Applied to Document Recognition* — Y. LeCun, L. Bottou, Y. Bengio and P. Haffner, 1998 — <http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf> (accessed 2026-10-10)
- *The Mathematics of Statistical Machine Translation: Parameter Estimation* — P. Brown et al., *Computational Linguistics*, 19(2), 1993 — <https://aclanthology.org/J93-2004/> (accessed 2026-10-10)
- *Deep Blue* — IBM (manufacturer's historical page) — <https://www.ibm.com/history/deep-blue> (accessed 2026-10-10)
- *ImageNet Large Scale Visual Recognition Challenge* — O. Russakovsky et al., 2014 — <https://arxiv.org/abs/1409.0575> (accessed 2026-10-10)
- *ImageNet Classification with Deep Convolutional Neural Networks* — A. Krizhevsky, I. Sutskever and G. Hinton, 2012 — <https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html> (accessed 2026-10-10)
- Own check — all the above addresses returned status code 200 on an HTTP request on 2026-10-10, except the printed work of Minsky and Papert, for which no open edition has been found

## Continue

- Previous: [What artificial intelligence is](01-que-es-la-inteligencia-artificial.en.md)
- Next: [From AlexNet to agents: the history since 2012](03-historia-desde-2012.en.md)
- Stage index: [Stage 0 — Foundations](README.md)
- Thematic index: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe, assisted by AI. Last reviewed: 2026-10-10.*