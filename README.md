# BusinessMemBench

**A propagation-aware memory benchmark.** 149 deterministic questions across 7 categories testing what business operators actually need from memory layers — reassessment, contradiction, lineage, cross-stream consistency, historical fidelity, provenance, and forgetfulness — categories that LoCoMo and LongMemEval don't cover.

```
pip install businessmembench
```

## Why this exists

Existing memory benchmarks (LoCoMo, LongMemEval, MemoryArena) test retrieval. They ask: *given a long conversation, can the system find a fact?* Real business memory has a harder job — when a fact **changes**, the system has to re-evaluate every belief that depended on it. None of the existing benchmarks test that.

BusinessMemBench is the test set for **propagation-aware** memory. The headline category is **reassessment**: a price changes, and downstream margin claims that quoted the old price must update. A memory system that only retrieves stale beliefs scores 0.000 here. A system that merely flags affected beliefs scores partial credit. A system that re-evaluates them scores 1.000.

## What's in the box

- **Question generator** — deterministic seed=42 corpus generation across 7 categories
- **Scoring harness** — `score_answer()` for each category, returns 0.0–1.0
- **Adapter protocol** — `BenchmarkSystem` that any memory system can implement
- **Reference adapters** — vanilla (no-memory floor), graphiti, mem0, letta, memori, kumiho-stub
- **Gold-standard subset** — 200 human-authored questions for high-confidence scoring
- **Run JSON format** — reproducibility-first artifact every run produces

## Categories (149 questions × 7)

| Category | What it tests | Why it matters |
|---|---|---|
| `propagation` | A fact changes → downstream beliefs auto-update | Reassessment |
| `contradiction` | Two facts conflict → resolution traceable | Truth maintenance |
| `lineage` | "Why did I decide X?" → upstream chain | Decision audit |
| `cross_stream` | Same claim from screen + meeting + vault → consistency | Multi-source agreement |
| `historical` | "What did we believe on date Y?" | Bitemporal fidelity |
| `provenance` | Trace claim → source episode | Evidence chains |
| `forgetfulness` | Old beliefs invalidated → correctly pruned | Active set hygiene |

## Quickstart

```python
from businessmembench import BenchmarkRunner, load_questions, score_answer
from businessmembench.adapters import VanillaSystem  # the floor baseline

system = VanillaSystem()  # replace with your memory system
questions = load_questions(seed=42)
runner = BenchmarkRunner(system=system, questions=questions)
results = runner.run()
print(results.summary())
```

## Implementing your own adapter

Implement the `BenchmarkSystem` protocol — eight methods, one per category plus `ingest()`:

```python
from businessmembench.harness import BenchmarkSystem

class MyMemorySystem(BenchmarkSystem):
    def ingest(self, episodes): ...
    def query_propagation(self, q): ...
    def query_contradiction(self, q): ...
    def query_lineage(self, q): ...
    def query_cross_stream(self, q): ...
    def query_historical(self, q): ...
    def query_provenance(self, q): ...
    def query_forgetfulness(self, q): ...
```

Reference: see `businessmembench/adapters/graphiti_system.py` for a worked implementation against a real third-party memory system, or [Atlas](https://github.com/RichSchefren/atlas/blob/master/benchmarks/business_mem_bench/adapters/atlas_system.py) for the full propagation-aware reference.

## Reproducibility

```bash
pip install -e ".[dev]"
pytest tests/ -v
```

Every run JSON includes the seed, question hash, scoring version, and per-category breakdown. Two runs of the same system with the same seed must produce byte-identical results — drift means a bug.

## Honest disclaimer

This benchmark was authored by the team behind [Atlas](https://github.com/RichSchefren/atlas) — a propagation-aware memory system that scores 1.000 here by design. The benchmark categories were chosen to test what propagation-aware memory does well. **It is not a neutral benchmark.** Three categories (`historical`, `provenance`, basic `lineage`) can be scored well by any typed-graph system without propagation. Four categories (`propagation`, `contradiction`, `cross_stream`, `forgetfulness`) reward systems that re-evaluate downstream beliefs at ingestion time.

If you build a memory system that doesn't ship propagation, you'll score below Atlas on this benchmark. That's the design. The benchmark exists to **define the category** — not to claim Atlas is uniformly best at memory.

## Citation

If you use BusinessMemBench in a paper:

```bibtex
@misc{schefren2026bmb,
  title={BusinessMemBench: A Propagation-Aware Memory Benchmark},
  author={Schefren, Richard},
  year={2026},
  url={https://github.com/RichSchefren/businessmembench}
}
```

## License

MIT. Maximally permissive — adopt freely, run on your system, publish your numbers.

## Reference implementation

[Atlas](https://github.com/RichSchefren/atlas) — open-source local-first AGM-compliant memory layer that achieves the 1.000 reference score on BMB. Apache 2.0.
