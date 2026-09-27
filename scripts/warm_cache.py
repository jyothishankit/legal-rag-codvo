"""Pre-embed the benchmark corpus so later runs are fast and repeatable.

Embedding is the slow, rate-limited step. Warming the cache once up front
separates "waiting on OpenAI" from "evaluating a strategy", which keeps ablation
runs to a couple of minutes each.
"""

from __future__ import annotations

import asyncio
import sys

from tqdm import tqdm

from legalrag.chunking import chunk_corpus
from legalrag.config import get_settings
from legalrag.embeddings import OpenAIEmbedder
from legalrag.evaluation import load_tests, referenced_documents
from legalrag.ingest import load_corpus


async def main(chunkers: list[str], chunk_size: int, max_tests: int) -> None:
    settings = get_settings()
    tests, _ = load_tests(settings, None, max_tests)
    docs = load_corpus(settings.corpus_dir, referenced_documents(tests))
    embedder = OpenAIEmbedder(settings)

    for chunker in chunkers:
        chunks = chunk_corpus(docs, chunker, chunk_size)
        print(f"{chunker}: {len(chunks):,} chunks", flush=True)
        with tqdm(total=len(chunks), desc=chunker, unit="chunk") as bar:
            await embedder.embed([c.text for c in chunks], progress=bar.update)

    await embedder.embed([t.query for t in tests])
    print(f"queries: {len(tests)} embedded", flush=True)


if __name__ == "__main__":
    names = sys.argv[1].split(",") if len(sys.argv) > 1 else ["rcts"]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    tests_per_benchmark = int(sys.argv[3]) if len(sys.argv) > 3 else 194
    asyncio.run(main(names, size, tests_per_benchmark))
