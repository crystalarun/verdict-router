# Verdict Router

Labels a question before Verdict Desk spends any tokens.

| Route | When | Cost in v0.1 |
| --- | --- | --- |
| `extractive` | metric / policy / runbook lookup | $0 (Desk BM25) |
| `local_small` | short synthesis, still grounded | $0 (optional local model later) |
| `escalate` | forecast, live number, or multi-step analysis | **blocked** until a budget is set |
| `refuse` | jailbreak or out of corpus | $0 |

There is no OpenAI/Anthropic call in this repository. The interesting part is the **decision not to spend**.

```bash
python -m pip install -e .
python -m verdict_router "What is 30-day venue churn?"
python -m verdict_router "Forecast next month GMV for Riyadh"
```
