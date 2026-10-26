# Prompt Testing Lab

**Focus:** systematic contract testing of AI prompts and candidate outputs under ambiguity, conflicting requirements, changes across turns, edge cases and strict formatting constraints.

## Executive summary
A model can produce fluent text while violating the exact task. This lab models prompt evaluation as a set of **explicit acceptance criteria**, then runs synthetic candidate responses through repeatable checks. It separates machine-checkable failures from issues that still require human review.

## Evaluation questions
1. Does the answer follow the latest valid constraint when user requirements change?
2. Are output formatting constraints satisfied exactly?
3. Can the evaluator expose unwanted assertions, missing content or verbosity?
4. Where would an automated lexical check be insufficient (semantic equivalence, safety, source grounding)?

## What is included
- `data/cases.json` — five annotated synthetic cases, with prompts, outputs and deterministic checks.
- `src/evaluator.py` — dependency-free validation engine.
- `tests/` — runnable unit tests.
- GitHub Actions workflow to run tests when code changes.

## Reproduce
Requires Python 3.11+ and **no third-party packages**.

```bash
python -m src.evaluator data/cases.json
python -m unittest discover -s tests -v
```

## Methodology
**Specify → Produce candidate response → Check explicit constraints → Record violations → Human adjudication.** The output records each rule and pass/fail result; checks never decide nuanced issues they cannot actually prove. A regex may confirm a string exists; it cannot establish that a claim is factually grounded. To extend the lab, add paired prompts, manual ratings for truthfulness and a versioned gold set.

## Suggested rubric (manual review)
| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Instruction adherence | Fails critical constraint | Partial | Meets all applicable instructions |
| Grounding | Unsupported | Mixed | Supported by cited source |
| Clarity | Confusing | Understandable | Precise and appropriate |
| Constraint change | Ignores update | Partly updates | Correctly applies latest constraint |

## Limitations and future research
No live API calls or model benchmark are included. Expand with a model adapter, per-model version logs, rater agreement and blind scoring. Explicitly separate violations of user requests from conflicts with higher-priority instructions.

## Skills demonstrated
Prompt engineering · Prompt testing · Edge-case design · Acceptance criteria · LLM QA · Reproducible evaluation · Python

# Scope and evidence

This is a **synthetic, independently developed demonstration**, not a reproduction of confidential employer data. All prompts, labels, examples, names and records are fabricated for demonstration. Sample counts and test outcomes are software demonstrations, **not historical workplace impact statistics**.

The repository demonstrates evaluation methodology and runnable code; it does not certify that the author achieved a specific result at a named client.

