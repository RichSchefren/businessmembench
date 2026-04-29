"""BenchmarkSystem adapters for BusinessMemBench.

Each module wires one system-under-test to the BenchmarkSystem protocol
the harness expects.

Reference adapters shipped in this package (some require their own
Python client to be installed):

  - vanilla   — no-memory baseline (returns canned None answers).
                Establishes the floor every memory system must beat.
  - graphiti  — Graphiti property-graph memory.
  - memori    — Memori 8-category taxonomy memory.
  - letta     — Letta block-based working memory.
  - mem0      — Mem0 vector-store memory.

External SDKs not yet wired (failing-loud stubs with install hints):

  - kumiho    — Kumiho commercial cloud SDK.
  - mempalace — MemPalace.

To benchmark your own memory system, implement the BenchmarkSystem
protocol from `businessmembench.harness` and pass an instance to
`BenchmarkRunner`. See `examples/` (or the Atlas reference adapter at
github.com/RichSchefren/atlas/tree/master/benchmarks/business_mem_bench)
for a worked implementation.
"""


from businessmembench.adapters.external_stubs import (
    KumihoSystem,
    MemPalaceSystem,
    MissingClientError,
)
from businessmembench.adapters.graphiti_system import (
    GraphitiSystem,
)
from businessmembench.adapters.letta_system import LettaSystem
from businessmembench.adapters.mem0_system import Mem0System
from businessmembench.adapters.memori_system import MemoriSystem
from businessmembench.adapters.vanilla import VanillaSystem

__all__ = [
    "GraphitiSystem",
    "KumihoSystem",
    "LettaSystem",
    "Mem0System",
    "MemoriSystem",
    "MemPalaceSystem",
    "MissingClientError",
    "VanillaSystem",
]
