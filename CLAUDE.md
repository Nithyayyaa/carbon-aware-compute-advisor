# Project: Carbon-Aware Compute Advisor

## About me
I'm new to this stack (REST APIs like ENTSO-E, Postgres/TimescaleDB, FastAPI,
Docker/Docker Compose, GitHub Actions CI, time-series ML). I have a general
Python/ML/DS background (T5 fine-tuning, CNNs, sentiment pipelines) but not
hands-on experience with these specific tools in production-style use. My
goal for this project is deep understanding, not just a working result —
I should be able to explain every major decision in an interview afterward.

## How to work with me on this project
- Before writing any code for a new task, explain your plan in plain
  language first: what you're about to build, why this approach over
  alternatives, and what could realistically go wrong. Wait for me to
  confirm before proceeding.
- When you use a new tool, library, or pattern for the first time in this
  project, briefly explain what it is and why it's the right choice here —
  assume I don't already know it, even if it's "basic" in the field.
- After writing a non-trivial piece of code, briefly explain what it does
  and why it's structured that way, in a way I could repeat in an
  interview without notes.
- If there are two reasonable ways to do something, tell me both options
  and the tradeoff — don't just silently pick one and move on.
- Prefer smaller, incremental steps I can follow and approve over doing an
  entire multi-file task in one uninterrupted shot.
- If I ask "why" about something you already did, or ask you to slow down
  and re-explain, treat that as normal and expected, not a sign something
  went wrong.
- Flag anything that's a common interview talking point (tradeoffs,
  failure modes, "why not X instead") explicitly when it comes up
  naturally, rather than only if I ask.
- If I say I don't know where to start, or seem stuck: don't just hand me
  a finished solution. First break the task into 2-3 sub-problems, or walk
  through your thinking step by step, or give me a skeleton/pseudocode I
  can fill in myself — pick whichever fits, but default to helping me
  think rather than writing the full answer for me.
- For feature engineering and core model/data logic specifically: let me
  write a first attempt (even a rough one) and critique it, rather than
  writing it for me from scratch, unless I explicitly ask you to just
  write it.

## Project scope — what's IN (v1)
1. Ingest historical + live grid carbon intensity data for Germany via the
   ENTSO-E Transparency Platform API
2. Store it in Postgres/TimescaleDB (proper time-series table, not a CSV)
3. Forecast next 24-48h carbon intensity using LightGBM (or Prophet),
   with a real backtest (MAE against actual values)
4. Serve a recommendation ("best window in next 24h to run a job") via a
   FastAPI endpoint (/forecast, /recommend)
5. Show it in a small Streamlit dashboard: current intensity, forecast
   curve, recommended window
6. Package it with Docker Compose (API + DB + dashboard) and one basic
   GitHub Actions CI step (lint + test)
7. Prove it: run one real job (e.g. CNN or T5 training) and log actual
   CO2 via CodeCarbon, show before/after savings from better timing

## Explicitly OUT of scope (v1) — do not build these without asking first
- Multi-country / multi-region support — Germany only
- User accounts / auth
- Real-time streaming pipeline (Kafka etc.) — polling is fine
- Kubernetes — Docker Compose is enough
- Mobile/responsive frontend polish — Streamlit is fine as-is
- Any LLM component — that's a separate, later project

If a task seems to need something outside this list, stop and flag it to
me rather than expanding scope on your own.

## Definition of done (v1)
- Can pull last 30 days of real German grid carbon data
- Model has a documented backtest accuracy (MAE vs actual next-day values)
- `docker compose up` gives a working dashboard from a clean clone
- README explains the *why* for every major stack choice, not just the *what*
- At least one real before/after CO2 number from an actual run
