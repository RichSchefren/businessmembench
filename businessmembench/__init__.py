"""BusinessMemBench — the benchmark Atlas authors.

Tests memory systems on what business operators actually need: implication
propagation, contradiction resolution, decision lineage, cross-stream
consistency, historical query fidelity, provenance accuracy, forgetfulness.

7 categories × ~143 questions = 1,000 question target. Atlas dominates
categories purpose-built for it (propagation, contradiction); baselines
(Mem0, Letta, Graphiti, Memori, Kumiho, vanilla GPT) compete on the rest.

Spec: 08 - BusinessMemBench Design.md (Phase 1 lock 2026-04-24)
License: MIT (max adoption — cited but never relicensed)
"""

from businessmembench.harness import (
    BenchmarkRunner,
    BenchmarkSystem,
    CategoryReport,
    EvalReport,
)
from businessmembench.questions import (
    CATEGORIES,
    Category,
    Question,
    load_questions,
)
from businessmembench.scoring import (
    SCORERS,
    score_answer,
)

__all__ = [
    "BenchmarkRunner",
    "BenchmarkSystem",
    "CategoryReport",
    "EvalReport",
    "CATEGORIES",
    "Category",
    "Question",
    "load_questions",
    "SCORERS",
    "score_answer",
]
