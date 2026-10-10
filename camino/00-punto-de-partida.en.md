---
titulo: Starting point
orden: 0
pregunta: What is taken for granted before starting, and where to cover it if it is missing?
ultima_revision: 2026-10-10
estado: publicado
traduccion_de: 2026-10-10
---

# Starting point


<img src="../assets/bandas/banda-00-en.svg" alt="The path · starting point" width="560">
> English translation of the Spanish original: [00-punto-de-partida.md](00-punto-de-partida.md). Spanish is the canonical text; this version follows the revision of 10 October 2026.

## What it is for

It fixes where the «zero» of this material begins. The path starts from zero **in artificial intelligence**: it is not assumed that anything is known about the subject. The craft of programming is assumed, however, because from Stage 2 onwards programs are read and written, services are brought up and repositories are worked with.

This page exists so that nobody reaches Stage 0 without the rudiments and discovers it three pages later. If you already handle an editor, a terminal and Git, and you have written some code, you can go straight to [Stage 0 — Fundamentals](etapa-0-fundamentos/README.md). If not, here is the minimum to arrive in good shape, with rough timings and no ceremony.

## What is taken for granted

| Area | Sufficient level to start |
|:--|:--|
| Text editing | Being comfortable with an editor, finding and replacing across a project, working with several files open |
| Terminal | Moving around folders, copying and deleting files, reading a command's output, understanding environment variables and exit codes |
| Git | Initialising a repository, making commits, creating a branch, resolving a simple conflict |
| A programming language | Variables, conditionals, loops, functions, lists and dictionaries, reading and writing files, error handling. Python or JavaScript is enough |
| Consuming web services | Understanding what an HTTP request, an API key, a JSON and a 400 or 429 error are when seen in a response |
| Technical English | Reading documentation and articles in English. A good part of the path's primary sources are in English and are not translated |

None of this is examined: it is the starting assumption. What is checked, stage by stage, is the exit criterion of each one, and that is described in its own index.

## What is not taken for granted and is not taught either

- **Advanced mathematics.** The path explains what a model does and what it does not, and for that neither differential calculus nor linear algebra is needed. When a page uses a mathematical idea, it defines it in words and links the source for anyone who wants to go further. No stage requires proving anything.
- **Programming from scratch.** The path does not teach programming, does not teach how to use Git and does not teach systems administration. It takes the craft for granted, and when it needs a specific tool it names it and links its documentation.
- **Training models from scratch.** Stage 0 explains what training is; no stage asks you to train a large model. What it does ask, in Stage 5, is to assemble a complete piece with existing models.
- **Complete history and philosophy of mind.** [Page 2](etapa-0-fundamentos/02-historia-hasta-2012.en.md) and [page 3](etapa-0-fundamentos/03-historia-desde-2012.en.md) go through history by its technical consequences, not as a narrative.

## How to cover what is missing

> [!TIP]
> Public resources, in Spanish or with a Spanish version, accessible without registration. The timings are rough indications and correspond to sustained effort, not to quick reading.

| Missing | Resource | Rough time |
|:--|:--|:--|
| Python | The language's official tutorial, in Spanish — <https://docs.python.org/es/3/tutorial/> | 8–12 h |
| Git | The book *Pro Git*, in Spanish, chapters 2 and 3 — <https://git-scm.com/book/es/v2> | 4–6 h |
| Terminal and the tools of the craft | *The Missing Semester of Your CS Education*, from MIT — <https://missing.csail.mit.edu/> | 6–8 h |
| JavaScript and web development, if you prefer that language | MDN's learning pathway — <https://developer.mozilla.org/es/docs/Learn> | 10–15 h |

With those foundations, Stage 0 can be started with confidence. Without them, it can still be read: pages 1, 2, 3 and 5 do not require writing code.

## The usual stumbling blocks

- **Starting with the tool.** Installing an environment, an agent library and a framework before understanding what is being assembled. The opposite order —concept first, tool afterwards— is what this material proposes, and that is why Stage 0 does not ask you to install anything.
- **Mistaking the starting point for an exam.** Nobody is going to mark these foundations. The only consequence of not having them is that stages 2 to 5 become slower than necessary.
- **Jumping to Stage 3 out of interest in agents.** It is the most frequently consulted stage and the one that is worst used without the previous ones: almost all of its mistakes are decided earlier, when modelling the context and the state.

## When it does not apply

If the goal is to have an informed opinion about artificial intelligence without writing code, Stage 0 is just as useful and this starting point is not needed. If the goal is to develop systems, the craft assumption is real and it is best not to force it: stages 2 and 3 ask you to read someone else's code and run your own.

## Definitions

- **Starting point**: the set of knowledge that is assumed before Stage 0, limited to the craft of programming and not to the subject.
- **Craft**: handling of editor, terminal, Git, a programming language and the consumption of web services.

## References

- *The Python Tutorial* (Spanish) — Python Software Foundation — <https://docs.python.org/es/3/tutorial/> (consulted 2026-10-10)
- *Pro Git* (second edition, Spanish) — Scott Chacon and Ben Straub — <https://git-scm.com/book/es/v2> (consulted 2026-10-10)
- *The Missing Semester of Your CS Education* — MIT — <https://missing.csail.mit.edu/> (consulted 2026-10-10)
- *Learn web development* (Spanish) — MDN Web Docs, Mozilla — <https://developer.mozilla.org/es/docs/Learn> (consulted 2026-10-10)
- Own verification — the four addresses above returned code 200 on an HTTP request on 2026-10-10

## Continue

- Next: [Stage 0 — Fundamentals](etapa-0-fundamentos/README.md)
- Thematic index: [`../INDEX.md`](../INDEX.md)

---

*Pepe. Last reviewed: 2026-10-10.*